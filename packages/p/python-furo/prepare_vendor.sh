#!/bin/bash
set -eux

PKG_URL="$(awk '
/^Source0?:/ {url = $2}
/^Version:/  {version = $2}
END { sub(/%{version}/, version, url); print url}' *.spec)"
PKG_TARBALL=$(basename $PKG_URL)
PKG_NAME=$(rpmspec -q --queryformat="%{NAME}" *.spec --srpm | sed 's/^python-//')
PKG_VERSION=$(rpmspec -q --queryformat="%{VERSION}" *.spec --srpm)
PKG_SRCDIR="${PKG_NAME}-${PKG_VERSION}"
PKG_DIR="$PWD"
PKG_TMPDIR=$(mktemp --tmpdir -d ${PKG_NAME}-XXXXXXXX)
PKG_PATH="$PKG_TMPDIR/$PKG_SRCDIR/"

echo "URL:     $PKG_URL"
echo "TARBALL: $PKG_TARBALL"
echo "NAME:    $PKG_NAME"
echo "VERSION: $PKG_VERSION"
echo "PATH:    $PKG_PATH"

cleanup_tmpdir() {
    popd 2>/dev/null
    rm -rf $PKG_TMPDIR
    rm -rf /tmp/yarn--*
}
trap cleanup_tmpdir SIGINT

cleanup_and_exit() {
    cleanup_tmpdir
    if test "$1" = 0 -o -z "$1" ; then
        exit 0
    else
        exit $1
    fi
}

if [ ! -w "$PKG_TARBALL" ]; then
    wget "$PKG_URL"
fi


mkdir -p $PKG_TMPDIR
tar -xf $PKG_TARBALL -C $PKG_TMPDIR

cd $PKG_PATH

export YARN_CACHE_FOLDER="$PWD/.package-cache"
echo ">>>>>> Install npm modules"
rm package-lock.json
yarn install
if [ $? -ne 0 ]; then
    echo "ERROR: yarn install failed"
    cleanup_and_exit 1
fi

echo ">>>>>> Package vendor files"
rm -f $PKG_DIR/${PKG_NAME}-${PKG_VERSION}-vendor.tar.xz
XZ_OPT="-9e -T$(nproc)" tar cJf $PKG_DIR/${PKG_NAME}-${PKG_VERSION}-vendor.tar.xz .package-cache
if [ $? -ne 0 ]; then
    cleanup_and_exit 1
fi

yarn add license-checker
yarn license-checker --summary | sed "s#$PKG_PATH#/tmp/#g" > $PKG_DIR/${PKG_NAME}-${PKG_VERSION}-vendor-licenses.txt

cd -

rm -rf .package-cache node_modules
cleanup_and_exit 0
