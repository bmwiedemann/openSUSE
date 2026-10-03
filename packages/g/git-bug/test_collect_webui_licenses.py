# SPDX-License-Identifier: MIT
import contextlib
import io
import json
from pathlib import Path
import runpy
import tempfile
import unittest

COLLECT = runpy.run_path(str(Path(__file__).with_name("collect-webui-licenses.py")))["collect"]


class LicenseTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.webui = Path(self.tmp.name) / "webui"
        self.webui.mkdir()
        self.destination = Path(self.tmp.name) / "notices"
        self.packages = {"": {"name": "test"}}

    def package(self, name, license="MIT", **fields):
        path = "node_modules/" + name
        self.packages[path] = {"version": "1.0.0", "license": license, **fields}
        directory = self.webui / path
        directory.mkdir(parents=True)
        (directory / "package.json").write_text(json.dumps({"name": name, "license": license}))
        (directory / "LICENSE").write_text("test notice\n")
        return directory

    def collect(self):
        (self.webui / "package-lock.json").write_text(json.dumps({"packages": self.packages}))
        with contextlib.redirect_stdout(io.StringIO()):
            COLLECT(self.webui, self.destination)

    def test_copy_production_notices_without_npm_manifest_filename(self):
        self.package("@scope/runtime", license="OFL-1.1")
        self.package("build-tool", dev=True)
        self.collect()
        target = self.destination / "node_modules/@scope/runtime"
        self.assertEqual((target / "LICENSE").read_text(), "test notice\n")
        self.assertTrue((target / "package-metadata.json").is_file())
        self.assertFalse((target / "package.json").exists())
        self.assertFalse((self.destination / "node_modules/build-tool").exists())

    def test_undeclared_license_requires_review(self):
        self.package("changed-license", license="GPL-3.0-only")
        with self.assertRaisesRegex(ValueError, "Review the spec License"):
            self.collect()

    def test_missing_notice_is_reported(self):
        package = self.package("missing-notice")
        (package / "LICENSE").unlink()
        (package / "README.md").write_text("upstream README\n")
        with contextlib.redirect_stderr(io.StringIO()) as errors:
            self.collect()
        self.assertIn("missing-notice", errors.getvalue())
        self.assertTrue((self.destination / "node_modules/missing-notice/README.md").is_file())

    def test_reject_path_traversal(self):
        self.packages["node_modules/../../outside"] = {"license": "MIT", "version": "1.0.0"}
        with self.assertRaisesRegex(ValueError, "Invalid package path"):
            self.collect()


if __name__ == "__main__":
    unittest.main()
