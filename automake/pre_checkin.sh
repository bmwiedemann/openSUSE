#!/bin/bash
# This script has to be run prior to a check-in if changes were done
# to spec and/or changes
sed -e "s,^\(Name:.*automake\),\1-testsuite," automake.spec > automake-testsuite.spec
cp automake.changes automake-testsuite.changes

osc service localrun format_spec_file

