#!/bin/bash
# This script has to be run prior to a check-in if changes were done
# to spec and/or changes
sed -e "s,^\(Name:.*coreutils\),\1-testsuite," coreutils.spec > coreutils-testsuite.spec
cp coreutils.changes coreutils-testsuite.changes

osc service localrun format_spec_file

