#!/bin/bash -eux

ASAR_PKGDIR="$(pwd)"
ASAR_PKGVERSION=$(<./*.spec grep ^Version | sed -e 's/Version:[ ]*//g')
ASAR_URL="https://github.com/electron/asar/archive/refs/tags/v${ASAR_PKGVERSION}.tar.gz"
ASAR_TARBALL=v${ASAR_PKGVERSION}.tar.gz
ASAR_TMPDIR=$(mktemp --tmpdir -d asar-XXXXXXXX)
ASAR_PATH="$ASAR_TMPDIR/asar-$ASAR_PKGVERSION"



echo "VERSION: $ASAR_PKGVERSION"
echo "PATH:    $ASAR_PATH"

cleanup_tmpdir()
{
    popd 2> /dev/null || exit 1
    rm -rf "$ASAR_TMPDIR"
}
trap cleanup_tmpdir SIGINT

cleanup_and_exit()
{
    cleanup_tmpdir
    if test "$1" = 0 -o -z "$1"; then
        exit 0
    else
        exit "$1"
    fi
}

if [ ! -w "$ASAR_TARBALL" ]; then
    wget "$ASAR_URL"
fi

tar -xf "$ASAR_TARBALL" -C "$ASAR_TMPDIR"

pushd "$ASAR_PATH" || cleanup_and_exit 1



echo ">>>>>> Install npm modules"
yarn install --frozen-lockfile --ignore-engines --ignore-platform  --ignore-scripts --link-duplicates
ret=$?
if [ $ret -ne 0 ]; then
    echo "ERROR: yarn install failed"
    cleanup_and_exit 1
fi

echo ">>>>>> Cleanup object files"
find node_modules/ -name "*.node" -print -delete
find node_modules/ -name "*.wasm" -print -delete
find node_modules/ -name "*.jar" -print -delete
find node_modules/ -name "*.dll" -print -delete
find node_modules/ -name "*.exe" -print -delete
find node_modules/ -name "*.dylib" -print -delete
find node_modules/ -name "*.so" -print -delete
find node_modules/ -name "*.o" -print -delete
find node_modules/ -name "*.a" -print -delete



echo '>>>>>> Remove vendored binaries'
#We use sponge to avoid a race condition between find and rm
find . -type f| sponge |\
    xargs -P"$(nproc)" -- sh -c 'file "$@" | grep -v '\'': .*script'\'' | grep '\'': .*executable'\'' | tee /dev/stderr | sed '\''s/: .*//'\'' | xargs rm -fv'

echo ">>>>>> Remove empty directories"
find . -type d -empty -print -delete

echo ">>>>>> Package vendor files"
rm -f "${ASAR_PKGDIR}/vendor.tar.zst"
ZSTD_CLEVEL=19 ZSTD_NBTHREADS=$(nproc) tar --zstd --sort=name -vvScf "${ASAR_PKGDIR}/vendor.tar.zst" node_modules
if [ $? -ne 0 ]; then
    cleanup_and_exit 1
fi
echo "vendor $(du -sh "${ASAR_PKGDIR}/vendor.tar.zst")"
