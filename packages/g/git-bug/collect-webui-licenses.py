#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Collect available notices for installed non-dev npm dependencies.

This deliberately includes more packages than Vite may retain after tree
shaking. Missing upstream license files are reported, not invented.
"""
import argparse
import json
from pathlib import Path
import shutil
import sys


def collect(webui, destination):
    lock = json.loads((webui / "package-lock.json").read_text())
    index = []
    # Keep this in sync with the conservative License expression in the spec.
    declared = {"0BSD", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "BlueOak-1.0.0",
                "CC-BY-4.0", "ISC", "MIT", "OFL-1.1", "Python-2.0", "Unlicense"}
    for path, package in sorted(lock["packages"].items()):
        if not path or package.get("dev"):
            continue
        relative = Path(path)
        if relative.is_absolute() or ".." in relative.parts or relative.parts[0] != "node_modules":
            raise ValueError(f"Invalid package path: {path}")
        source = webui / relative
        if not source.is_dir():
            # Optional packages for other platforms are not installed.
            if package.get("optional"):
                continue
            raise ValueError(f"Missing installed package: {path}")
        if package.get("license") not in declared:
            raise ValueError(f"Review the spec License expression for {path}: {package.get('license')}")
        target = destination / relative
        target.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source / "package.json", target / "package-metadata.json")
        notices = []
        for item in sorted(source.iterdir()):
            if item.is_file() and item.name.lower().startswith(
                    ("license", "licence", "copying", "notice", "copyright", "ofl")):
                shutil.copyfile(item, target / item.name)
                notices.append(item.name)
        if not notices:
            print(f"warning: no top-level license text supplied by {path}", file=sys.stderr)
            for item in source.glob("README*"):
                if item.is_file():
                    shutil.copyfile(item, target / item.name)
        index.append({"path": path, "version": package["version"],
                      "license": package.get("license", "UNKNOWN"), "notices": notices})
    (destination / "index.json").write_text(json.dumps(index, indent=2) + "\n")
    print(f"Collected available notices for {len(index)} installed production dependencies")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("webui", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    collect(args.webui, args.destination)
