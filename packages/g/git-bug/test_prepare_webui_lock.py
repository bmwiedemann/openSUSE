# SPDX-License-Identifier: MIT
"""Unit tests for npm preparation. No Node processes or network access."""
import base64
import copy
import io
import json
from pathlib import Path
import runpy
import tarfile
import tempfile
import unittest

HELPER = runpy.run_path(str(Path(__file__).with_name("prepare-webui-lock.py")))
HASH = "sha512-" + base64.b64encode(bytes(64)).decode()


class PreparationTests(unittest.TestCase):
    def fixture(self):
        package = {"dependencies": {"react": "^19.3.0"}, "packageManager": "pnpm@10.33.0",
                   "pnpm": {"overrides": {"js-yaml@4": "^4.3.2"}}}
        lock = {"importers": {".": {"dependencies": {
            "react": {"specifier": "^19.3.0", "version": "19.3.0(peer@1.0.0)"}}}},
                "overrides": {"js-yaml@4": "^4.3.2"}}
        return package, lock

    def test_pin_and_translate_without_mutating_input(self):
        package, lock = self.fixture()
        before = copy.deepcopy(package)
        result = HELPER["build_manifest"](package, lock)
        self.assertEqual(package, before)
        self.assertEqual(result["dependencies"]["react"], "19.3.0")
        self.assertEqual(result["overrides"], {"js-yaml@4": "^4.3.2", "postcss-selector-parser": "7.1.6"})
        self.assertNotIn("packageManager", result)
        self.assertNotIn("pnpm", result)

    def test_reject_manifest_mismatch(self):
        package, lock = self.fixture()
        package["dependencies"]["react"] = "^18.0.0"
        with self.assertRaisesRegex(ValueError, "disagree"):
            HELPER["build_manifest"](package, lock)

    def test_reject_unreviewed_overrides(self):
        package, lock = self.fixture()
        lock["overrides"] = {"parent>child": "1.0.0"}
        with self.assertRaisesRegex(ValueError, "overrides changed"):
            HELPER["build_manifest"](package, lock)

    def test_reject_workspace_importers(self):
        package, lock = self.fixture()
        lock["importers"]["another"] = {}
        with self.assertRaisesRegex(ValueError, "single root importer"):
            HELPER["build_manifest"](package, lock)

    def inventory(self):
        return {"example@1.0.0": {"packages": {"node_modules/example": {
            "resolved": "https://registry.npmjs.org/example/-/example-1.0.0.tgz",
            "version": "1.0.0", "integrity": HASH}}}}

    def npm_lock(self):
        return {"lockfileVersion": 3, "packages": {
            "": {"name": "test"}, "node_modules/example": {"version": "1.0.0", "integrity": HASH}}}

    def test_source_identity_and_integrity(self):
        lock = self.npm_lock()
        result = HELPER["validate_lock"](lock, self.inventory(), Path("unused"))
        self.assertEqual(result["source_identities"], 1)
        for field, value in (("version", "2.0.0"), ("integrity", "invalid"),
                             ("resolved", "http://localhost:1234/a.tgz"), ("link", True)):
            with self.subTest(field=field):
                changed = copy.deepcopy(lock)
                changed["packages"]["node_modules/example"][field] = value
                with self.assertRaises(ValueError):
                    HELPER["validate_lock"](changed, self.inventory(), Path("unused"))

    def test_bundled_dependencies_are_checked_against_parent_archive(self):
        lock = self.npm_lock()
        lock["packages"]["node_modules/example/node_modules/child"] = {
            "version": "2.0.0", "inBundle": True}
        with tempfile.TemporaryDirectory() as directory:
            content = json.dumps({"name": "child", "version": "2.0.0"}).encode()
            path = Path(directory)
            with tarfile.open(path / "example-1.0.0.tgz", "w:gz") as archive:
                entry = tarfile.TarInfo("package/node_modules/child/package.json")
                entry.size = len(content)
                archive.addfile(entry, io.BytesIO(content))
            result = HELPER["validate_lock"](lock, self.inventory(), path)
            self.assertEqual(result["bundled_entries"], 1)
            lock["packages"]["node_modules/example/node_modules/child"]["version"] = "3.0.0"
            with self.assertRaisesRegex(ValueError, "Bundled manifest disagrees"):
                HELPER["validate_lock"](lock, self.inventory(), path)
    def test_build_inventory_drops_only_optional_platform_packages(self):
        inventory = {f"{name}@1.0.0": {"name": name} for name in (
            "binding-linux", "systeminformation", "plain", "dev-required", "unused")}
        lock = {"packages": {
            "": {"name": "test"},
            "node_modules/binding-linux": {"version": "1.0.0", "optional": True,
                                            "dev": True, "os": ["linux"], "cpu": ["x64"]},
            # Required pure-JS packages may still declare supported platforms.
            "node_modules/systeminformation": {"version": "1.0.0", "os": ["linux"]},
            # devOptional is required for a development install.
            "node_modules/dev-required": {"version": "1.0.0", "devOptional": True,
                                           "cpu": ["x64"]},
            "node_modules/plain": {"version": "1.0.0"},
            "node_modules/plain/node_modules/inner": {"version": "9.0.0", "inBundle": True}}}
        sources, excluded = HELPER["build_inventory"](lock, inventory)
        self.assertEqual(set(sources), {"systeminformation@1.0.0", "plain@1.0.0",
                                        "dev-required@1.0.0"})
        self.assertEqual(excluded, ["binding-linux@1.0.0"])

    def test_build_inventory_keeps_identity_required_elsewhere(self):
        inventory = {"shared@1.0.0": {}}
        lock = {"packages": {
            "node_modules/a/node_modules/shared": {"version": "1.0.0", "optional": True,
                                                    "os": ["linux"]},
            "node_modules/shared": {"version": "1.0.0"}}}
        sources, excluded = HELPER["build_inventory"](lock, inventory)
        self.assertEqual((list(sources), excluded), (["shared@1.0.0"], []))

    def test_build_inventory_rejects_unknown_source(self):
        lock = {"packages": {"node_modules/x": {"version": "1.0.0"}}}
        with self.assertRaisesRegex(ValueError, "absent from the inventory"):
            HELPER["build_inventory"](lock, {})

    def test_native_overrides_pick_highest_version(self):
        lock = {"packages": {
            "node_modules/lightningcss": {"version": "1.32.0"},
            "node_modules/vite/node_modules/lightningcss": {"version": "1.33.0"},
            "node_modules/x/node_modules/lightningcss": {"version": "1.9.10"},
            "node_modules/rolldown": {"version": "1.2.8"}}}
        self.assertEqual(HELPER["native_overrides"](lock), {"lightningcss": "1.33.0"})
        del lock["packages"]["node_modules/vite/node_modules/lightningcss"]
        del lock["packages"]["node_modules/x/node_modules/lightningcss"]
        self.assertEqual(HELPER["native_overrides"](lock), {})


if __name__ == "__main__":
    unittest.main()
