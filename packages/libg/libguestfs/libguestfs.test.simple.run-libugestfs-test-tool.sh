#!/bin/bash
# libguestfs-test-tool starts its temporary guest using a dummy disk image
# It creates a partition, a filesystem, mounts it and touches a file
# Once it is done the dummy image is removed again
# Per default it runs in --verbose mode, and our version trace the API calls
#
# Expected runtime: ca. 10 seconds
#
# Expected output:
# guest should start
# no "obvious" errors should be shown during the disk operation
# Somewhere at the end of the verbose output lines like this are expected:
# ...
# libguestfs: trace: touch "/hello"
# ...
# libguestfs: trace: touch = 0
#
#
set -x
set -e
unset LANG
unset ${!LC_*}
cpus=`grep -Ec 'cpu[0-9]' /proc/stat || echo 1`

libguestfs-test-tool -V
time libguestfs-test-tool
