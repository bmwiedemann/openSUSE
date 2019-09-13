#!/bin/sh
sed -e 's/Name:.*/Name:           e2fsprogs-mini/' \
    -e 's/spec file for package.*/&-mini/' \
    -e 's/%define.*build_mini.*/%define build_mini 1/' e2fsprogs.spec > e2fsprogs-mini.spec
cp e2fsprogs.changes e2fsprogs-mini.changes

