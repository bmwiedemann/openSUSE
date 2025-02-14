#!/bin/sh
set -x
# The dependencies tarball is quite large, so we
# reduce it here by removing unecessary files for
# building (e.g, test files).

export SUBDIR="vendor/zig/"
export ZIG_GLOBAL_CACHE_DIR="${PWD}/${SUBDIR}"
export ZSTD_CLEVEL="9"

zig build --fetch
zig fetch git+https://github.com/zigimg/zigimg#3a667bdb3d7f0955a5a51c8468eac83210c1439e
zig fetch git+https://github.com/mitchellh/libxev#f6a672a78436d8efee1aa847a43a900ad773618b

find "${SUBDIR}" -type d -iname test -print0 | xargs -r0 rm -rv

tar --zstd -cvf ../vendor.tar.zst "${SUBDIR}"
