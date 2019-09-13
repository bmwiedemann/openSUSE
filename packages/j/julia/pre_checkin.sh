#!/bin/sh
cp -f julia.changes julia-compat.changes
cp -f julia.spec julia-compat.spec
sed -i 's/%define compat_mode  0/%define compat_mode  1/' julia-compat.spec
