#!/usr/bin/python3

import os
import pathlib
import pytest

os.chdir(pathlib.Path.cwd() / "tests")
pytest.main(["-v", "-n", "auto"])
