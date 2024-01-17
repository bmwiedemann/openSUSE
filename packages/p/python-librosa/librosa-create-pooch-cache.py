""" librosa-create-pooch-cache.py

Create the pooch cache tarball for testing the package.

Copyright (c) 2021 SUSE LLC
Copyright (c) 2021 Ben Greiner <code@bnavigator.de>

All modifications and additions to the file contributed by third parties
remain the property of their copyright owners, unless otherwise agreed
upon. The license for this file, and modifications and additions to the
file, is the same license as for the pristine package itself (unless the
license for the pristine package is not an Open Source License, in which
case the license is the MIT License). An "Open Source License" is a
license that conforms to the Open Source Definition (Version 1.9)
published by the Open Source Initiative.

Please submit bugfixes or comments via https://bugs.opensuse.org/
"""

import os
import subprocess
import sys

import pooch

data_name = "librosa-pooch-cache"
registry_file = "librosa/util/example_data/registry.txt"

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <librosa-srcdir>")
    print(f"Download test data into $PWD/{data_name} and compress the directory into $PWD/{data_name}.tar.gz")
    sys.exit(1)

srcdir = os.path.abspath(sys.argv[1])
data_path = os.path.abspath(os.getcwd() + "/" + data_name)


pc = pooch.create(
    data_path, base_url="https://librosa.org/data/audio/", registry=None
)
pc.load_registry(srcdir + "/" + registry_file)
with open(srcdir + "/" + registry_file) as fh:
    for line in fh:
        filename, hsum = line.split(" ")
        pc.fetch(filename)

subprocess.run(["tar", "czf", f"{data_name}.tar.gz", data_name], check=True)
