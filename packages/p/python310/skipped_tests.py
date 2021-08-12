#!/usr/bin/python3
"""
Simple regexp-based skipped test checker.
It lists tests that are mentioned (presumably for exclusion)
in BASE, and in MAIN (presumably for inclusion)
and reports discrepancies.

This will have a number of 
"""

MAIN = "python39.spec"

import glob
import re
from os.path import basename

alltests = set()
qemu_exclusions = set()

for item in glob.glob("Python-*/Lib/test/test_*"):
    testname = basename(item)
    if testname.endswith(".py"):
        testname = testname[:-3]
    alltests.add(testname)

testre = re.compile(r'[\s"](test_\w+)\b')

def find_tests_in_spec(specname):
    global qemu_exclusions

    found_tests = set()
    with open(specname) as spec:
        in_qemu = False
        for line in spec:
            line = line.strip()
            if "#" in line:
                line = line[:line.index("#")]
            tests = set(testre.findall(line))
            found_tests |= tests
            if line == "%if 0%{?qemu_user_space_build} > 0":
                in_qemu = True
            if in_qemu:
                if line == "%endif":
                    in_qemu = False
                qemu_exclusions |= tests
    return found_tests

excluded = find_tests_in_spec(MAIN)

#print("--- excluded tests:", " ".join(sorted(excluded)))
#print("--- included tests:", " ".join(sorted(included)))

mentioned = excluded
nonexistent = mentioned - alltests
missing = excluded - qemu_exclusions

print("--- the following tests are excluded for QEMU and not tested in python")
print("--- (that probably means we don't need to worry about them)")
for test in sorted(qemu_exclusions - excluded):
    print(test)

print("--- the following tests might be excluded in python:")
for test in sorted(missing):
    print(test)

if nonexistent:
    print("--- the following tests don't exist:")
    for test in sorted(nonexistent):
        print(test)
