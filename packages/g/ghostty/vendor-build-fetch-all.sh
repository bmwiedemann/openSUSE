#!/bin/sh
set -eux

version=$(awk '$1 == "Version:" { print $2; exit }' ghostty.spec)
if [ ! -d "ghostty-$version" ]; then
  tar -xzf "ghostty-$version.tar.gz"
fi

tmp=$(mktemp -d "${PWD}/.vendor.XXXXXXXX")

export ZIG_GLOBAL_CACHE_DIR="$tmp/cache"
export ZIG_LOCAL_PKG_DIR="$tmp/vendor/zig/p"

(
  cd "ghostty-$version"
  # Include lazy dependencies for offline builds.
  zig build --fetch=all
)

if [ ! -d "$ZIG_LOCAL_PKG_DIR" ]; then
  printf '%s\n' 'Zig did not populate the local package directory' >&2
  exit 1
fi

tar --zstd -cf "$tmp/vendor.tar.zst" -C "$tmp" vendor/zig/p
mv -f "$tmp/vendor.tar.zst" vendor.tar.zst
rm -r -- "$tmp"
