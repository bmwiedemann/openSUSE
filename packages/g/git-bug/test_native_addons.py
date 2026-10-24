# SPDX-License-Identifier: MIT
"""Unit tests for native-addons.py. No network access."""
from pathlib import Path
import runpy
import tempfile
import unittest

NATIVE = runpy.run_path(str(Path(__file__).with_name("native-addons.py")))

SERVICE = """<services>
    <service name="go_modules" mode="manual"/>
</services>
"""


def lock(**overrides):
    packages = {"": {"name": "webui"},
                "node_modules/rolldown": {"version": "1.2.8"},
                "node_modules/@tailwindcss/oxide": {"version": "4.3.3"},
                "node_modules/lightningcss": {"version": "1.33.0"},
                "node_modules/lightningcss-linux-x64-gnu": {"version": "1.33.0",
                                                           "optional": True}}
    packages.update(overrides)
    return {"lockfileVersion": 3, "packages": packages}


class NativeAddonTests(unittest.TestCase):
    def test_versions_from_lock(self):
        self.assertEqual(NATIVE["addon_versions"](lock()),
                         {"rolldown": "1.2.8", "tailwindcss": "4.3.3", "lightningcss": "1.33.0"})

    def test_reject_duplicate_or_nested_installation(self):
        nested = {"node_modules/vite/node_modules/lightningcss": {"version": "1.32.0"}}
        cases = {"duplicate": lock(**nested),
                 "missing": lock(**{"node_modules/rolldown": None}),
                 "bundled": lock(**{"node_modules/rolldown": {"version": "1.2.8",
                                                              "inBundle": True}}),
                 "prerelease": lock(**{"node_modules/rolldown": {"version": "1.2.8-rc.1"}})}
        cases["missing"]["packages"].pop("node_modules/rolldown")
        for name, value in cases.items():
            with self.subTest(name), self.assertRaises(ValueError):
                NATIVE["addon_versions"](value)

    def test_service_region_insert_and_replace(self):
        versions = NATIVE["addon_versions"](lock())
        first = NATIVE["update_service"](SERVICE, versions)
        self.assertIn("go_modules", first)
        self.assertIn("<param name=\"revision\">v1.2.8</param>", first)
        self.assertIn("<param name=\"src\">lightningcss-1.33.0.tar.zst</param>", first)
        self.assertIn("keeps update=false on purpose", first)
        self.assertNotIn("--", first.replace("<!--", "").replace("-->", ""))
        self.assertTrue(first.rstrip().endswith("</services>"))
        self.assertEqual(NATIVE["update_service"](first, versions), first)
        newer = NATIVE["update_service"](first, dict(versions, rolldown="1.3.0"))
        self.assertIn("v1.3.0", newer)
        self.assertNotIn("v1.2.8", newer)
        self.assertEqual(newer.count(NATIVE["BEGIN"]), 1)

    def test_reject_damaged_region(self):
        versions = NATIVE["addon_versions"](lock())
        damaged = SERVICE.replace("</services>", f"    {NATIVE['BEGIN']}\n</services>")
        with self.assertRaisesRegex(ValueError, "incomplete"):
            NATIVE["update_service"](damaged, versions)

    def test_spec_include(self):
        text = NATIVE["spec_include"](NATIVE["addon_versions"](lock()))
        self.assertIn("rolldown,1.2.8,rolldown_binding,librolldown_binding.so,"
                      "node_modules/rolldown/dist/rolldown-binding,"
                      "packages/rolldown/package.json,rolldown", text)
        self.assertIn("Source20000:   rolldown-1.2.8.tar.zst\n", text)
        self.assertIn("Source20005:   vendor-lightningcss.tar.zst\n", text)
        self.assertEqual(text.count("%global"), 1)

    def test_stale_files(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            for name in ("rolldown-1.2.7.tar.zst", "rolldown-1.2.8.tar.zst", "other-1.tar.zst"):
                (path / name).touch()
            self.assertEqual(NATIVE["stale_files"](path, {"rolldown": "1.2.8"}),
                             ["rolldown-1.2.7.tar.zst"])


if __name__ == "__main__":
    unittest.main()
