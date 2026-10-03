# SPDX-License-Identifier: MIT
"""Offline tests: python3 -m unittest -v test_pnpm_to_obs.py."""
import base64
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import unittest

import yaml

SCRIPT = Path(__file__).with_name("pnpm-to-obs.py")
spec = importlib.util.spec_from_file_location("pnpm_to_obs", SCRIPT)
converter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(converter)
HASH = "sha512-" + base64.b64encode(bytes(64)).decode()
OTHER_HASH = "sha512-" + base64.b64encode(bytes([1]) * 64).decode()
SERVICE = Path("/usr/lib/obs/service/node_modules")


def record(**resolution):
    return {"resolution": {"integrity": HASH, **resolution}}


def fixture():
    return {
        "lockfileVersion": "9.0",
        "importers": {".": {"dependencies": {"react": {"version": "19.3.0"}}}},
        "packages": {
            "react@19.3.0": record(),
            "react@18.3.1": record(),
            "@scope/example@1.2.3": record(),
        },
    }


def package_entry(output, identity):
    return next(iter(output[identity]["packages"].values()))


class ConverterTests(unittest.TestCase):
    def test_names_versions_and_scopes(self):
        result = converter.convert(fixture())
        self.assertEqual(len(result), 3)
        self.assertEqual(package_entry(result, "@scope/example@1.2.3")["resolved"],
                         "https://registry.npmjs.org/@scope/example/-/example-1.2.3.tgz")
        self.assertEqual(package_entry(result, "react@19.3.0")["integrity"], HASH)

    def test_peer_contexts_share_source(self):
        lock = fixture()
        lock["packages"]["react@19.3.0(peer@1.0.0(other@2.0.0))"] = record()
        self.assertEqual(len(converter.convert(lock)), 3)

    def test_explicit_tarball(self):
        lock = fixture()
        url = "https://example.org/releases/react.tgz?download=1"
        lock["packages"]["react@19.3.0"] = record(tarball=url)
        self.assertEqual(package_entry(converter.convert(lock), "react@19.3.0")["resolved"], url)

    def test_optional_and_foreign_platforms_are_retained(self):
        lock = fixture()
        lock["packages"]["@scope/darwin-arm64@1.0.0"] = {
            **record(), "optional": True, "os": ["darwin"], "cpu": ["arm64"]}
        self.assertIn("@scope/darwin-arm64@1.0.0", converter.convert(lock))

    def test_deterministic(self):
        lock = fixture()
        reverse = copy.deepcopy(lock)
        reverse["packages"] = dict(reversed(list(reverse["packages"].items())))
        self.assertEqual(json.dumps(converter.convert(lock)), json.dumps(converter.convert(reverse)))

    def test_reject_bad_integrities(self):
        for value in (None, "", "sha512-AA==", "sha512-!", "unknown-AAAA", HASH + " " + OTHER_HASH):
            with self.subTest(value=value):
                lock = fixture()
                lock["packages"]["react@19.3.0"] = record(integrity=value)
                with self.assertRaises(converter.ConversionError):
                    converter.convert(lock)

    def test_reject_conflicting_peer_records(self):
        lock = fixture()
        lock["packages"]["react@19.3.0(peer@1.0.0)"] = record(integrity=OTHER_HASH)
        with self.assertRaisesRegex(converter.ConversionError, "Conflicting"):
            converter.convert(lock)

    def test_reject_conflicting_url(self):
        lock = fixture()
        lock["packages"]["react@19.3.0"] = record(tarball="https://example.org/a.tgz")
        lock["packages"]["react@18.3.1"] = record(tarball="https://example.org/a.tgz", integrity=OTHER_HASH)
        with self.assertRaisesRegex(converter.ConversionError, "Conflicting"):
            converter.convert(lock)

    def test_reject_service_filename_collision(self):
        lock = fixture()
        lock["packages"]["react@19.3.0"] = record(tarball="https://one.example/a.tgz")
        lock["packages"]["react@18.3.1"] = record(tarball="https://two.example/a.tgz")
        with self.assertRaisesRegex(converter.ConversionError, "filename collision"):
            converter.convert(lock)

    def test_reject_unsupported_resolutions(self):
        for resolution in ({"commit": "abc"}, {"directory": "../foo"},
                           {"tarball": "http://example.org/a.tgz"},
                           {"tarball": "https://user:password@example.org/a.tgz"},
                           {"tarball": "https://example.org/.."},
                           {"tarball": "https://example.org/"}):
            with self.subTest(resolution=resolution):
                lock = fixture()
                lock["packages"]["react@19.3.0"] = record(**resolution)
                with self.assertRaises(converter.ConversionError):
                    converter.convert(lock)

    def test_reject_nonregistry_importer_references(self):
        for version in ("workspace:*", "link:../foo", "file:../foo", "git+https://example.org/foo"):
            with self.subTest(version=version):
                lock = fixture()
                lock["importers"]["."]["dependencies"]["react"]["version"] = version
                with self.assertRaises(converter.ConversionError):
                    converter.convert(lock)

    def test_reject_patches_and_versions(self):
        for change in ({"patchedDependencies": {"react": "react.patch"}},
                       {"lockfileVersion": "6.0"}, {"packages": {}}):
            with self.subTest(change=change):
                with self.assertRaises(converter.ConversionError):
                    converter.convert({**fixture(), **change})

    def test_reject_duplicate_yaml_keys(self):
        with self.assertRaisesRegex(converter.ConversionError, "Duplicate YAML"):
            yaml.load("packages: {}\npackages: {}\n", Loader=converter.UniqueKeyLoader)

    def test_verify_downloads(self):
        content = b"test tarball contents"
        integrity = "sha512-" + base64.b64encode(hashlib.sha512(content).digest()).decode()
        lock = {"lockfileVersion": "9.0", "packages": {"example@1.0.0": record(integrity=integrity)}}
        inventory = converter.convert(lock)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            with self.assertRaisesRegex(converter.ConversionError, "verification failed"):
                converter.verify_downloads(inventory, path)
            tarball = path / "example-1.0.0.tgz"
            tarball.write_bytes(content)
            self.assertEqual(converter.verify_downloads(inventory, path), 1)
            tarball.write_bytes(b"damaged")
            with self.assertRaisesRegex(converter.ConversionError, "checksum mismatch"):
                converter.verify_downloads(inventory, path)

    def test_cli_does_not_overwrite_output_on_invalid_input(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "pnpm-lock.yaml"
            target = Path(directory) / "node-sources.json"
            source.write_text("lockfileVersion: '6.0'\n")
            target.write_text("keep me")
            result = subprocess.run([sys.executable, str(SCRIPT), "--input", str(source),
                                     "--output", str(target)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(target.read_text(), "keep me")

    def test_cli_refuses_npm_lock_filename(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run([sys.executable, str(SCRIPT), "--input", "unused.yaml",
                                     "--output", str(Path(directory) / "package-lock.json")],
                                    capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("NOT an npm install lock", result.stderr)

    @unittest.skipUnless(SERVICE.exists(), "obs-service-node_modules is not installed")
    def test_installed_service_parses_inventory_without_downloads(self):
        service = runpy.run_path(str(SERVICE), run_name="service_test")
        output = converter.convert(fixture())
        for lock in output.values():
            service["process_packagelock_file"](lock)
        modules = service["MODULE_MAP"]
        self.assertEqual(len(modules), 3)
        expected = {package_entry(output, key)["resolved"] for key in output}
        self.assertEqual({entry["url"] for entry in modules.values()}, expected)
        for filename, entry in modules.items():
            self.assertEqual(converter.service_filename(entry["url"]), filename)
            self.assertEqual(entry["algo"], "sha512")
            self.assertEqual(entry["chksum"], "00" * 64)


if __name__ == "__main__":
    unittest.main()
