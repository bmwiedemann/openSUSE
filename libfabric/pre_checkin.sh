#!/bin/bash
# This script has to be run prior to a check-in if changes were done
# to spec and/or changes
cp libfabric.changes fabtests.changes
GIT_VER=$(grep "%define git_ver" libfabric.spec)
VERSION=$(egrep "^Version:" libfabric.spec)
sed -i -e 's/^%define git_ver.*$/'"$GIT_VER/"  -e 's/^Version:.*$/'"$VERSION/" fabtests.spec
osc service localrun format_spec_file

