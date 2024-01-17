#!/bin/sh
set -euo pipefail

# packaging helper to merge rusty_v8 in place,
# from source (i.e., avoid using the published crate).
#
# output is a single, merged vendor tarball

wd="$(mktemp -d /tmp/revendor.XXXXX)"

# take what we need into the build
cp rusty_v8*xz $wd
cp vendor*xz $wd

cd $wd

echo -n "Extracting vendor..."
tar xf vendor*xz
echo "done"

echo -n "Extracting rusty_v8 (v8)..."
tar xf rusty*xz \
    --exclude="Cargo.toml" \
    --exclude="Cargo.lock"
echo " done"

# take vendored Cargo toml and lock which
# can still be used
cp vendor/v8/{Cargo.*,.cargo*} .

# get rid of everything else
rm -fr vendor/v8

# drop version prefix
target=$(find  . -name "*_v8-*" -type d)
mv $target v8

# insert proper files
mv Cargo.* .cargo* v8
echo "Check final rusty_v8 root:"
ls -la v8
mv v8 vendor

# disregard rusty_v8 checks as we inject it directly from source
echo '{"files":{},"package":""}' > vendor/v8/.cargo-checksum.json

# extra: workaround winapi bloat
# by ejecting it from the build
# 
# https://github.com/rust-lang/cargo/issues/7058
echo -n "Pruning winapi bloat... "
rm -fr vendor/winapi*gnu*/lib/*.a
echo "done"

# remake tarball
echo -n "Compressing archive... "
tar -cf - vendor/ |  xz -9 -c - > vendor-merged.tar.xz
echo "done"

ls -lh "$wd/vendor-merged.tar.xz"

cd -
cp "$wd/vendor-merged.tar.xz" ./vendor.tar.xz
