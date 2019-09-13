#!/bin/bash
# This script has to be run prior to a check-in if changes were done
# to spec and/or changes
sed -e "s,^\(Name:.*dapl\),\1-debug," dapl.spec > dapl-debug.spec
cp dapl.changes dapl-debug.changes

osc service localrun format_spec_file

