#!/bin/sh
set -x

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

# zig 0.17 keeps fetched packages compressed as p/<hash>.tar.gz, but
# `zig build --system` only finds them unpacked as p/<hash>/
for f in "${SUBDIR}"p/*.tar.gz; do
  tar -xzf "$f" -C "${SUBDIR}p" && rm "$f"
done

# Drop the prebuilt binaries some dependencies carry (Windows and macOS
# tools, test fixtures, Java build wrappers); the build uses none of them
find "${SUBDIR}p" -type f \( -name '*.[ao]' -o -name '*.so' -o -name '*.class' \
  -o -name '*.jar' -o -name '*.exe' -o -name '*.dll' -o -name '*.lib' \
  -o -name crashInMain -o -name crashduringload -o -name dump_syms_dwarf_data \
  -o -name sentry_example \) -print -delete

tar --zstd -cvf ../vendor.tar.zst "${SUBDIR}"
