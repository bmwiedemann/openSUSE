#!/bin/sh
set -x
# The dependencies tarball is quite large, so we
# reduce it here by removing unecessary files for
# building (e.g, test files).

export SUBDIR="vendor/zig/"
export ZIG_GLOBAL_CACHE_DIR="${PWD}/${SUBDIR}"
export ZSTD_CLEVEL="9"

./nix/build-support/fetch-zig-cache.sh

find "${SUBDIR}" -type d -iname test -print0 | xargs -r0 rm -rv

tar --zstd -cvf ../vendor.tar.zst "${SUBDIR}"
