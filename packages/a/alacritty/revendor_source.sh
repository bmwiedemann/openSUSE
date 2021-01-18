#!/bin/sh
set -euo pipefail

# packaging helper to workaround:
# https://github.com/rust-lang/cargo/issues/7058

wd="$(mktemp -d /tmp/revendor.XXXXXXXXXX)"

# take what we need into the build
cp vendor*xz $wd

cd $wd

echo -n "Extracting vendor..."
tar xf vendor*xz
echo "done"

echo -n "Ejecting  winapi bloat... "
rm -fr vendor/winapi*gnu*/lib/*.a
echo "done"

# remake tarball
echo -n "Compressing archive... "
tar -cf - vendor/ |  xz -9 -c - > vendor-merged.tar.xz
echo "done"

cd -

echo -n "Replacing tarball... "
cp $wd/vendor-merged.tar.xz vendor.tar.xz
rm -fr $wd
echo "ok"
