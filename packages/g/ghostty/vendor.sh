#!/bin/sh
set -x
# The dependencies tarball is quite large, so we
# reduce it here by removing unecessary files for
# building (e.g, test files).

export SUBDIR="vendor/zig/"
export ZIG_GLOBAL_CACHE_DIR="${PWD}/${SUBDIR}"

# NOTE THIS IS A TEMPORARY SCRIPT TO SUPPORT PACKAGE MAINTAINERS.
#
# A future Zig version will hopefully fix the issue where
# `zig build --fetch` doesn't fetch transitive dependencies[1]. When that
# is resolved, we won't need any special machinery for the general use case
# at all and packagers can just use `zig build --fetch`.
#
# [1]: https://github.com/ziglang/zig/issues/20976

if [ -z ${ZIG_GLOBAL_CACHE_DIR+x} ]
then
  echo "must set ZIG_GLOBAL_CACHE_DIR!"
  exit 1
fi

ZON_TXT_FILE="build.zig.zon.txt"
while IFS= read -r url; do
  echo "Fetching: $url"
  zig fetch "$url" >/dev/null 2>&1 || {
    echo "Failed to fetch: $url" >&2
    exit 1
  }
done < "$ZON_TXT_FILE"


find "${SUBDIR}" -type d -iname test -print0 | xargs -r0 rm -rv

tar --zstd -cvf ../vendor.tar.zst "${SUBDIR}"
