#!/bin/sh
# This expects to be run from the package dir
# and will build a single package
set -x
project=${project:-`cat ../.project 2>/dev/null`}
project=${project:-openSUSE:Factory}
set -e
pkg=$(basename $(pwd))
mkdir -p .osc
echo "$project" > .osc/_project
echo "$pkg" > .osc/_package
osc build --noservice "$@"
