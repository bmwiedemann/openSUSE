#!/bin/sh
# Generate the bundled Zig package cache (Source2, zig-deps.tar.zst) for
# herdr-core. Run from the unpacked source tree, next to the spec's sources:
#
#   cd herdr-core-<version>
#   sh ../vendor-zig.sh
#   mv zig-deps.tar.zst ../            # commit the result as Source2
#
# herdr-core builds the vendored ghostty-vt C ABI library with the system Zig
# (zig0.16). That library pulls Zig packages over the network at build time,
# which OBS build roots do not have, so the packages are cached here and
# exposed to the build through ZIG_GLOBAL_CACHE_DIR.
#
# The set is what `zig build -Demit-lib-vt` needs today: translate-c (plus its
# arocc dependency), uucode for UTF-8 decoding, wuffs, zlib, pixels and highway
# for image decoding, and the iterm2 themes archive. The themes are wanted by
# this step although nothing reads them: drop them and the build stops at
# "error: unable to connect to server" on that manifest entry, even though the
# entry says lazy and the archive contributes no object to the library. The
# rest of the vendored tree (gtk4, harfbuzz, freetype, NDK/SDK wrappers, the
# nerd fonts) is marked lazy and really is not asked for, so it stays out.
# Dependencies are
# listed by name so a version bump only needs new URLs; if upstream adds or
# renames one, the offline check below fails with "unable to find package"
# and this list needs updating.
set -eu

PATTERN='translate-c|vancluever/arocc|jacobsandlund/uucode|ghostty-themes-|/highway-|/pixels-|/wuffs-|/zlib-'

root=$PWD
cache=$root/zig-deps
rm -rf "$cache"
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

# "zig fetch" writes downloaded packages to the global cache, which is the only
# thing an offline "zig build" reads from.
export ZIG_GLOBAL_CACHE_DIR=$cache
unset http_proxy https_proxy all_proxy HTTP_PROXY HTTPS_PROXY ALL_PROXY

cd "$root/vendor/ghostty"

{
    cat build.zig.zon.txt
    grep -hoE 'https?://[^"]+' pkg/*/build.zig.zon
} | sort -u | grep -E "$PATTERN" | while read -r url; do
    echo "fetching $url"
    tries=0
    until zig fetch "$url" > /dev/null; do
        tries=$((tries + 1))
        [ "$tries" -ge 3 ] || { echo "  retrying after a failed download" >&2; sleep 10; continue; }
        echo "  cannot fetch $url" >&2
        exit 1
    done
done

# Sanity check first: the library must build from this cache alone, with no
# network. It compiles into the cache too, which is why the pruning below runs
# afterwards. Skip with SKIP_OFFLINE_CHECK=1 when the host has no network
# namespace tools.
if [ -z "${SKIP_OFFLINE_CHECK:-}" ] && command -v unshare > /dev/null; then
    echo "checking that the build works offline"
    # ZIG_LOCAL_CACHE_DIR goes to the temp tree as well: without it Zig also
    # looks in the project's own .zig-cache, where an earlier run may have left
    # a package, and the check then passes with a cache that is missing one.
    unshare -rn env ZIG_LOCAL_CACHE_DIR="$tmp/zig-local" \
        zig build -Demit-lib-vt -Doptimize=ReleaseFast -Dcpu=baseline \
        --prefix "$tmp/out" --cache-dir "$tmp/zig-cache"
fi

# Ship only the downloaded package archives: the compilation cache the check
# added next to p/ is rebuildable, machine specific and ten times the size.
find "$cache" -mindepth 1 -maxdepth 1 -not -name p -exec rm -rf {} +
count=$(find "$cache/p" \( -name '*.tar.gz' -o -name '*.tgz' \) | wc -l)
[ "$count" -ge 8 ] || {
    echo "only $count packages in the cache - the dependency list changed" >&2
    exit 1
}

tar --sort=name --owner=0 --group=0 --numeric-owner --mtime=@0 \
    --zstd -cf "$root/zig-deps.tar.zst" -C "$root" zig-deps
rm -rf "$cache"

echo "wrote $root/zig-deps.tar.zst ($count packages)"
