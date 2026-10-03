#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Convert a pnpm v9 lock to an obs-service-node_modules download inventory.

Requires Python 3 and PyYAML. No network access, dependency resolution, or
installation is performed. The output is NOT an npm installation lockfile.
"""

import argparse
import base64
import binascii
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote, urlsplit

import yaml


class ConversionError(ValueError):
    """Input cannot be represented safely as a service download inventory."""


class UniqueKeyLoader(yaml.SafeLoader):
    """Do not silently overwrite conflicting YAML keys."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            if key in result:
                raise ConversionError(f"Duplicate YAML key: {key!r}")
            result[key] = loader.construct_object(value_node, deep=deep)
        except TypeError as exc:
            raise ConversionError("YAML mapping keys must be scalar values") from exc
    return result


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)
NAME = r"(?:@[a-z0-9_~][a-z0-9._~-]*/)?[a-z0-9_~][a-z0-9._~-]*"
NUMBER = r"(?:0|[1-9][0-9]*)"
VERSION = rf"{NUMBER}\.{NUMBER}\.{NUMBER}(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?"
PACKAGE = re.compile(rf"^(?P<name>{NAME})@(?P<version>{VERSION})(?P<peers>\(.*\))?$")
DIGEST_SIZES = {"sha1": 20, "sha256": 32, "sha384": 48, "sha512": 64}
UNSUPPORTED = ("link:", "workspace:", "file:", "git:", "git+", "github:", "http:", "https:")


def mapping(value, context):
    if not isinstance(value, dict):
        raise ConversionError(f"{context}: expected a mapping")
    return value


def integrity_value(value, context):
    if not isinstance(value, str) or not value.split():
        raise ConversionError(f"{context}: missing integrity hash")
    algorithms = {}
    for token in value.split():
        algorithm, separator, encoded = token.partition("-")
        if not separator or algorithm not in DIGEST_SIZES:
            raise ConversionError(f"{context}: unsupported integrity algorithm")
        try:
            digest = base64.b64decode(encoded, validate=True)
        except (ValueError, binascii.Error) as exc:
            raise ConversionError(f"{context}: malformed integrity hash") from exc
        if len(digest) != DIGEST_SIZES[algorithm]:
            raise ConversionError(f"{context}: incorrect {algorithm} digest length")
        if algorithm in algorithms and algorithms[algorithm] != digest:
            raise ConversionError(f"{context}: conflicting {algorithm} integrity hashes")
        algorithms[algorithm] = digest
    return " ".join(sorted(set(value.split())))


def https_url(value, context):
    if not isinstance(value, str) or any(c.isspace() for c in value):
        raise ConversionError(f"{context}: expected an HTTPS tarball URL")
    try:
        url = urlsplit(value)
        valid = (url.scheme == "https" and url.hostname
                 and url.path.rsplit("/", 1)[-1] not in {"", ".", ".."}
                 and not url.username and not url.password and not url.fragment)
        _ = url.port
    except ValueError as exc:
        raise ConversionError(f"{context}: malformed URL") from exc
    if not valid:
        raise ConversionError(f"{context}: expected HTTPS without credentials or fragment")
    return value


def service_filename(url):
    """Match obs-service-node_modules' make_unique_fn_from_path convention."""
    parts = urlsplit(url).path.split("/")
    basename = parts[-1]
    prefix = [part for part in parts[1:-1]
              if part != "-" and not basename.startswith(part)]
    return "-".join([*prefix, basename])


def check_references(lock):
    # Local/workspace dependencies may occur only in importers, with no package
    # record. Refuse these instead of producing an apparently complete inventory.
    for section in ("importers", "snapshots"):
        for key, record in mapping(lock.get(section, {}), section).items():
            record = mapping(record, f"{section}.{key}")
            for kind in ("dependencies", "devDependencies", "optionalDependencies"):
                for name, reference in mapping(record.get(kind, {}), f"{key}.{kind}").items():
                    if isinstance(reference, dict):
                        reference = reference.get("version")
                    if not isinstance(reference, str):
                        raise ConversionError(f"{key}: invalid reference for {name}")
                    if reference.startswith(UNSUPPORTED) or "patch_hash=" in reference:
                        raise ConversionError(f"{key}: unsupported dependency {name}: {reference}")


def convert(lock):
    lock = mapping(lock, "lockfile")
    if str(lock.get("lockfileVersion")) != "9.0":
        raise ConversionError("Only pnpm lockfileVersion 9.0 is supported")
    if lock.get("patchedDependencies"):
        raise ConversionError("patchedDependencies require explicit patch handling")
    check_references(lock)
    packages = mapping(lock.get("packages"), "packages")
    if not packages:
        raise ConversionError("The package inventory is empty")
    output = {}
    by_url = {}
    by_filename = {}
    for key, metadata in packages.items():
        match = PACKAGE.fullmatch(key) if isinstance(key, str) else None
        if not match:
            raise ConversionError(f"Unsupported registry package identity: {key!r}")
        name, version, peers = match.group("name", "version", "peers")
        if peers:
            depth = 0
            for char in peers:
                depth += (char == "(") - (char == ")")
                if depth < 0:
                    break
            if depth != 0 or "patch_hash=" in peers:
                raise ConversionError(f"Unsupported peer/patch suffix: {key}")
        metadata = mapping(metadata, key)
        if metadata.get("patched"):
            raise ConversionError(f"{key}: patched package is unsupported")
        resolution = mapping(metadata.get("resolution"), f"{key}.resolution")
        unknown = set(resolution) - {"integrity", "tarball"}
        if unknown:
            raise ConversionError(f"{key}: unsupported resolution fields: {sorted(unknown)}")
        integrity = integrity_value(resolution.get("integrity"), key)
        url = resolution.get("tarball")
        if url is None:
            basename = name.rsplit("/", 1)[-1]
            url = (f"https://registry.npmjs.org/{quote(name, safe='@/')}/-/"
                   f"{quote(basename, safe='')}-{quote(version, safe='')}.tgz")
        url = https_url(url, key)
        identity = f"{name}@{version}"
        entry = {
            "lockfileVersion": 3,
            "packages": {
                f"node_modules/{name}": {
                    "version": version, "resolved": url, "integrity": integrity
                }
            },
        }
        if identity in output and output[identity] != entry:
            raise ConversionError(f"Conflicting sources for {identity}")
        if url in by_url and by_url[url] != integrity:
            raise ConversionError(f"Conflicting integrity hashes for {url}")
        filename = service_filename(url)
        if filename in by_filename and by_filename[filename] != (url, integrity):
            raise ConversionError(f"Service tarball filename collision: {filename}")
        by_filename[filename] = (url, integrity)
        by_url[url] = integrity
        output[identity] = entry
    return dict(sorted(output.items()))


def verify_downloads(inventory, directory):
    """The service may log download errors without failing; check every file."""
    errors = []
    seen = set()
    for lock in inventory.values():
        entry = next(iter(lock["packages"].values()))
        filename = service_filename(entry["resolved"])
        if filename in seen:
            continue
        seen.add(filename)
        expected = dict(token.split("-", 1) for token in entry["integrity"].split())
        hashes = {algorithm: hashlib.new(algorithm) for algorithm in expected}
        try:
            with (directory / filename).open("rb") as stream:
                while chunk := stream.read(1024 * 1024):
                    for digest in hashes.values():
                        digest.update(chunk)
        except OSError as exc:
            errors.append(f"{filename}: {exc.strerror}")
            continue
        for algorithm, digest in hashes.items():
            if base64.b64encode(digest.digest()).decode("ascii") != expected[algorithm]:
                errors.append(f"{filename}: {algorithm} checksum mismatch")
    if errors:
        raise ConversionError("Download verification failed:\n" + "\n".join(errors))
    return len(seen)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="pnpm-lock.yaml")
    parser.add_argument("--output", type=Path, required=True, help="service-only JSON inventory")
    parser.add_argument("--verify-dir", type=Path,
                        help="also verify every downloaded tarball in this directory")
    args = parser.parse_args()
    try:
        if args.input.resolve() == args.output.resolve():
            raise ConversionError("Input and output paths must differ")
        if args.output.name in {"package-lock.json", "npm-shrinkwrap.json"}:
            raise ConversionError("Use node-sources.json: output is NOT an npm install lock")
        lock = yaml.load(args.input.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
        result = convert(lock)
        if args.verify_dir is not None:
            count = verify_downloads(result, args.verify_dir)
            print(f"Verified {count} tarballs.", file=sys.stderr)
        content = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
        args.output.write_text(content, encoding="utf-8")
    except (ConversionError, OSError, yaml.YAMLError) as exc:
        parser.exit(1, f"error: {exc}\n")
    print(f"Wrote {len(result)} package identities to {args.output}; service input only.", file=sys.stderr)


if __name__ == "__main__":
    main()
