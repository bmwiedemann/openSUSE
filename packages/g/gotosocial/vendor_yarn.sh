#!/bin/bash
set -eux

PKG_NAME=gotosocial
PKG_VERSION="$1"
PKG_TARBALL="${PKG_NAME}-${PKG_VERSION}.tar.gz"
PKG_DIR="$PWD"
PKG_TMPDIR=$(mktemp --tmpdir -d "${PKG_NAME}-XXXXXXXX")
PKG_PATH="$PKG_TMPDIR"

echo "TARBALL: $PKG_TARBALL"
echo "NAME:    $PKG_NAME"
echo "VERSION: $PKG_VERSION"
echo "PATH:    $PKG_PATH"

if ! which pixz yarn; then
  echo "This script requires yarn and pixz to run"
  exit 1
fi

cleanup_tmpdir() {
    rm -rf "$PKG_TMPDIR"
    rm -rf /tmp/yarn--*
}
trap cleanup_tmpdir SIGINT

cleanup_and_exit() {
    cleanup_tmpdir
    if test "$1" = 0 -o -z "$1" ; then
        exit 0
    else
        exit "$1"
    fi
}

mkdir -p "$PKG_TMPDIR"
tar -xf "$PKG_TARBALL" -C "$PKG_TMPDIR"

cd "$PKG_PATH"

export YARN_CACHE_FOLDER="$PWD/.package-cache"
echo ">>>>>> Install npm modules"
if ! yarn --cwd ./web/source install || ! yarn --cwd ./web/source ts-patch install
then
    echo "ERROR: yarn install failed"
    cleanup_and_exit 1
fi

echo ">>>>>> Package vendor files"
rm -f "$PKG_DIR/${PKG_NAME}-${PKG_VERSION}-vendor.tar.xz"

if ! XZ_OPT="-9e -T$(nproc)" tar -I pixz -cf "$PKG_DIR/${PKG_NAME}-${PKG_VERSION}-vendor.tar.xz" .package-cache
then
    cleanup_and_exit 1
fi

cd -

cleanup_and_exit 0
