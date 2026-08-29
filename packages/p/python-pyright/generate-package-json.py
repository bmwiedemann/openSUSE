#!/usr/bin/python3
"""Generate the npm manifest and lockfile used to vendor Pyright."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path


VERSION_RE = re.compile(r"^Version:\s*([^\s#]+)", re.MULTILINE)


def read_spec_version(spec_path: Path) -> str:
    match = VERSION_RE.search(spec_path.read_text(encoding="utf-8"))
    if match is None:
        raise SystemExit(f"could not find Version in {spec_path}")

    version = match.group(1)
    if "%" in version:
        raise SystemExit(f"Version in {spec_path} contains an RPM macro: {version}")
    return version


def make_manifest(version: str) -> dict[str, object]:
    return {
        "name": "python-pyright-vendor",
        "version": version,
        "private": True,
        "description": "NPM dependencies vendored for the openSUSE python-pyright package",
        "license": "MIT",
        "dependencies": {"pyright": version},
    }


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate package.json and package-lock.json for obs-service-node_modules"
    )
    parser.add_argument("--spec", type=Path, default=Path("python-pyright.spec"))
    parser.add_argument("--npm", type=Path, default=Path("/usr/bin/npm"))
    args = parser.parse_args()

    version = read_spec_version(args.spec)
    manifest = make_manifest(version)

    if not args.npm.is_file() or not os.access(args.npm, os.X_OK):
        raise SystemExit(f"system npm is not executable: {args.npm}")

    output_dir = args.spec.resolve().parent
    with tempfile.TemporaryDirectory(prefix="python-pyright-npm-") as temp_name:
        temp_dir = Path(temp_name)
        write_json(temp_dir / "package.json", manifest)
        subprocess.run(
            [
                str(args.npm),
                "install",
                "--package-lock-only",
                "--legacy-peer-deps",
                "--ignore-scripts",
                "--no-audit",
                "--no-fund",
                "--update-notifier=false",
            ],
            cwd=temp_dir,
            check=True,
        )

        lock_path = temp_dir / "package-lock.json"
        if not lock_path.is_file():
            raise SystemExit("npm did not create package-lock.json")

        lock = json.loads(lock_path.read_text(encoding="utf-8"))
        packages = lock.get("packages", {})
        fsevents = packages.get("node_modules/fsevents")
        if fsevents is not None:
            if not fsevents.get("optional") or fsevents.get("os") != ["darwin"]:
                raise SystemExit("refusing to prune an unexpected fsevents lock entry")
            # Pyright uses fsevents only on macOS. The OBS build passes
            # --omit=optional, so do not vendor its prebuilt Darwin binary.
            del packages["node_modules/fsevents"]

        write_json(output_dir / "package.json", manifest)
        write_json(output_dir / "package-lock.json", lock)

    print(f"generated package.json and package-lock.json for pyright {version}")


if __name__ == "__main__":
    main()
