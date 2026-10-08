#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Generate git-bug's npm manifest and lock using only verified pnpm sources.

Maintainer-side tool, not an rpmbuild step. Requires Python/PyYAML, Node/npm,
local-npm-registry, and Linux unshare with unprivileged user namespaces enabled.
The npm resolver runs in a new network namespace with only loopback enabled.
"""
import argparse
import fcntl
import json
import os
from pathlib import Path
import re
import runpy
import socket
import struct
import subprocess
import sys
import tarfile
import tempfile
import time

import yaml

CONVERTER = runpy.run_path(str(Path(__file__).with_name("pnpm-to-obs.py")))
Error = CONVERTER["ConversionError"]


def build_manifest(package, lock):
    """Pin direct dependencies; leave transitive resolution to npm."""
    result = json.loads(json.dumps(package))
    if set(lock.get("importers", {})) != {"."}:
        raise Error("Expected a single root importer for the git-bug Web UI")
    importer = lock["importers"]["."]
    for kind in ("dependencies", "devDependencies", "optionalDependencies"):
        records = importer.get(kind, {})
        if set(result.get(kind, {})) != set(records):
            raise Error(f"package.json and pnpm importer disagree on {kind}")
        for name, record in records.items():
            if record["specifier"] != result[kind][name]:
                raise Error(f"package.json and pnpm importer disagree on {name}")
            version = record["version"].split("(", 1)[0]
            if not re.fullmatch(CONVERTER["VERSION"], version):
                raise Error(f"Unsupported direct dependency reference: {name}={version}")
            result[kind][name] = version
    overrides = lock.get("overrides", {})
    if overrides != {"js-yaml@4": "^4.3.2"}:
        raise Error("Upstream overrides changed; review their npm translation")
    result["overrides"] = overrides.copy()
    result["overrides"]["postcss-selector-parser"] = "7.1.6"
    result.pop("pnpm", None)
    result.pop("packageManager", None)
    return result


def validate_lock(lock, inventory, tarballs):
    """Validate source provenance, including dependencies bundled in tarballs.

    This does not assert identical npm and pnpm peer/dependency graphs.
    """
    if lock.get("lockfileVersion") != 3:
        raise Error("Expected an npm version-3 lock")
    selected = set()
    bundled_count = 0
    packages = lock["packages"]
    for path, entry in packages.items():
        if not path:
            continue
        name = entry.get("name", path.rsplit("node_modules/", 1)[-1])
        identity = f"{name}@{entry['version']}"
        if "resolved" in entry or entry.get("link"):
            raise Error(f"Non-portable URL or link in npm lock: {path}")
        if entry.get("inBundle"):
            parent = path.rsplit("/node_modules/", 1)[0]
            while packages.get(parent, {}).get("inBundle"):
                parent = parent.rsplit("/node_modules/", 1)[0]
            if parent == path or parent not in packages:
                raise Error(f"No source package for bundled entry: {path}")
            ancestor = packages[parent]
            parent_name = ancestor.get("name", parent.rsplit("node_modules/", 1)[-1])
            source = inventory.get(f"{parent_name}@{ancestor['version']}")
            if source is None:
                raise Error(f"Unknown bundle parent: {parent}")
            source_entry = next(iter(source["packages"].values()))
            filename = CONVERTER["service_filename"](source_entry["resolved"])
            relative = path[len(parent) + 1:]
            if ".." in relative.split("/"):
                raise Error(f"Invalid bundled path: {path}")
            with tarfile.open(tarballs / filename) as archive:
                member = archive.getmember(f"package/{relative}/package.json")
                if not member.isfile() or member.size > 1024 * 1024:
                    raise Error(f"Invalid bundled manifest: {path}")
                metadata = json.load(archive.extractfile(member))
            if metadata.get("name") != name or metadata.get("version") != entry["version"]:
                raise Error(f"Bundled manifest disagrees with npm: {path}")
            bundled_count += 1
            continue
        if identity not in inventory:
            raise Error(f"Npm selected a source absent from pnpm: {identity}")
        expected = next(iter(inventory[identity]["packages"].values()))
        if entry.get("integrity") != expected["integrity"]:
            raise Error(f"Npm integrity disagrees with pnpm: {identity}")
        selected.add(identity)
    return {"source_identities": len(selected), "installation_entries": len(packages) - 1,
            "bundled_entries": bundled_count,
            "not_selected_by_npm": sorted(set(inventory) - selected)}


def enable_loopback():
    # Executed only after unshare creates the private namespace.
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        flags = fcntl.ioctl(sock, 0x8913, struct.pack("16sH14x", b"lo", 0))
        value = struct.unpack("16sH14x", flags)[1]
        fcntl.ioctl(sock, 0x8914, struct.pack("16sH14x", b"lo", value | 1))


def resolve(manifest, tarballs, helper, timeout):
    with tempfile.TemporaryDirectory(prefix="git-bug-npm-lock-") as directory:
        work = Path(directory)
        (work / "package.json").write_text(json.dumps(manifest, indent=2) + "\n")
        # Do not inherit registry/cache settings or NODE_OPTIONS from the caller.
        env = {key: value for key, value in os.environ.items()
               if not key.lower().startswith("npm_config_") and key != "NODE_OPTIONS"}
        env.update(HOME=directory, npm_config_cache=str(work / "cache"),
                   npm_config_userconfig=str(work / "npmrc"),
                   npm_config_globalconfig=str(work / "global-npmrc"),
                   npm_config_update_notifier="false", NODE_OPTIONS="--max-old-space-size=1536")
        log_path = work / "registry.log"
        with log_path.open("w") as log:
            server = subprocess.Popen([*helper, str(tarballs), "--debug"],
                                      cwd=work, env=env, stdout=log, stderr=subprocess.STDOUT)
            try:
                deadline = time.monotonic() + timeout
                while time.monotonic() < deadline:
                    text = log_path.read_text()
                    match = re.search(r"port: (\d+)", text)
                    if match:
                        port = match[1]
                        break
                    if server.poll() is not None:
                        raise Error("Local registry exited:\n" + text[-4000:])
                    time.sleep(0.1)
                else:
                    raise Error("Local registry startup timed out")
                subprocess.run([
                    "npm", "install", "--package-lock-only", "--omit-lockfile-registry-resolved",
                    "--ignore-scripts", "--legacy-peer-deps", "--include=dev", "--no-audit",
                    "--no-fund", "--fetch-retries=0", "--maxsockets=2",
                    "--registry", f"http://localhost:{port}",
                ], cwd=work, env=env, check=True, timeout=timeout)
                return json.loads((work / "package-lock.json").read_text())
            finally:
                server.terminate()
                try:
                    server.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    server.kill()
                    server.wait()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--webui", type=Path, required=True)
    parser.add_argument("--tarballs", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--registry-helper", nargs="+", default=["local-npm-registry"],
                        help="helper command; defaults to local-npm-registry")
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--_in-namespace", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    try:
        if not args._in_namespace:
            result = subprocess.run(["unshare", "-Urn", sys.executable,
                                     str(Path(__file__).resolve()), *sys.argv[1:], "--_in-namespace"])
            return result.returncode
        enable_loopback()
        lock = yaml.load((args.webui / "pnpm-lock.yaml").read_text(),
                         Loader=CONVERTER["UniqueKeyLoader"])
        inventory = CONVERTER["convert"](lock)
        tarballs = args.tarballs.resolve()
        CONVERTER["verify_downloads"](inventory, tarballs)
        manifest = build_manifest(json.loads((args.webui / "package.json").read_text()), lock)
        npm_lock = resolve(manifest, tarballs, args.registry_helper, args.timeout)
        report = validate_lock(npm_lock, inventory, tarballs)
        args.output_dir.mkdir(parents=True, exist_ok=True)
        for name, value in (("webui-package.json", manifest), ("package-lock.json", npm_lock),
                            ("webui-lock-report.json", report)):
            (args.output_dir / name).write_text(json.dumps(value, indent=2) + "\n")
        print(f"Validated {report['source_identities']} tarball identities and "
              f"{report['bundled_entries']} bundled entries. Output: {args.output_dir}")
        return 0
    except (Error, OSError, ValueError, KeyError, tarfile.TarError,
            subprocess.SubprocessError, yaml.YAMLError) as exc:
        parser.exit(1, f"error: {exc}\n")


if __name__ == "__main__":
    sys.exit(main())
