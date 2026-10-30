#!/bin/sh
# Regenerate zig-deps.tar.zst, a Zig global cache holding the package archives
# (p/<hash>.tar.*), which lets zig build run offline, for the vendored
# libghostty-vt that herdr's crates/ghostty-vt/build.rs compiles with
# "zig build -Demit-lib-vt" (see %build in herdr.spec).
#
# Usage, from the root of an unpacked herdr source tree, with zig 0.16 in PATH:
#   sh /path/to/vendor-zig.sh
# then commit the resulting zig-deps.tar.zst next to the spec.
#
# Only the packages the library build graph reaches are fetched (zig builds
# lazily, and "zig fetch" does not follow transitive dependencies, see
# https://github.com/ziglang/zig/issues/20976). If a version bump needs
# another one, the build stops with "unable to find dependency": add it to
# PATTERN below.
set -eu

PATTERN='/translate-c/|/vancluever/arocc/|/uucode-|/wuffs-|/pixels-|/highway-|/zlib-|/ghostty-themes-'

root=$PWD
cache=$root/zig-deps
export ZIG_GLOBAL_CACHE_DIR=$cache
rm -rf "$cache"
mkdir -p "$cache"

# "zig fetch" needs a build.zig in the working directory
cd "$root/vendor/libghostty-vt"
urls=$(grep -E "$PATTERN" build.zig.zon.txt)
for url in $urls; do
	echo "Fetching: $url"
	zig fetch "$url" >/dev/null
done
cd "$root"

tar --sort=name --owner=0 --group=0 --numeric-owner --mtime=@0 \
	--zstd -cf "$root/zig-deps.tar.zst" -C "$root" zig-deps
rm -rf "$cache"
