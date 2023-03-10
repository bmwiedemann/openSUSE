#!/bin/bash
# Script based on the fedora package
# https://src.fedoraproject.org/rpms/python-pydata-sphinx-theme/blob/rawhide/f/prepare_vendor.sh

PKG_DIR="$(pwd)"
PKG_PATH=pydata-sphinx-theme
PKG_NAME=python-pydata-sphinx-theme
PKG_VERSION=0.13.1

cleanup_tmpdir() {
    popd 2>/dev/null
    rm -rf /tmp/yarn--*
    rm /tmp/core-js-banners
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

cd $PKG_PATH
export YARN_CACHE_FOLDER=".package-cache"
echo ">>>>>> Install npm modules"
yarn install --frozen-lockfile
if [ $? -ne 0 ]; then
    echo "ERROR: yarn install failed"
    cleanup_and_exit 1
fi

echo ">>>>>> Cleanup object dirs"
find node_modules/ -type d -name "*.o.d" -execdir rm {} +
find node_modules/ -type d -name "__pycache__" -execdir rm {} +

echo ">>>>>> Cleanup object files"
find node_modules/ -name "*.node" -execdir rm {} +

find node_modules/ -name "*.dll" | grep -v signal-client | xargs rm -f
find node_modules/ -name "*.dylib" -delete
find node_modules/ -name "*.so" -delete
find node_modules/ -name "*.o" -delete
find node_modules/ -name "*.a" -delete
find node_modules/ -name "*.snyk-*.flag" -delete

echo ">>>>>> Cleanup build info"
find node_modules/ -name "builderror.log" -delete
find node_modules/ -name "yarn-error.log" -delete
find node_modules/ -name "yarn.lock" -delete
find node_modules/ -name ".deps" -type d -execdir rm {} +
find node_modules/ -name "Makefile" -delete
find node_modules/ -name "*.target.mk" -delete
find node_modules/ -name "config.gypi" -delete
find node_modules/ -name "package.json" -exec sed -i "s#$PKG_PATH#/tmp#g" {} \;

echo ">>>>>> Cleanup yarn tarballs"
find node_modules/ -name ".yarn-tarball.tgz" -delete

echo ">>>>>> Cleanup source maps"
find node_modules/ -name "*.js.map" -delete
find node_modules/ -name "*.ts.map" -delete
find node_modules/ -name "*.mjs.map" -delete
find node_modules/ -name "*.cjs.map" -delete
find node_modules/ -name "*.css.map" -delete
find node_modules/ -name "*.min.map" -delete

echo ">>>>>> Package vendor files"
rm -f ${PKG_NAME}-${PKG_VERSION}-vendor.tar.xz
XZ_OPT="-9e -T$(nproc)" tar cJf $PKG_DIR/${PKG_NAME}-${PKG_VERSION}-vendor.tar.xz .package-cache

yarn add license-checker
yarn license-checker --summary | sed "s#$PKG_PATH#/tmp#g" > $PKG_DIR/${PKG_NAME}-${PKG_VERSION}-vendor-licenses.txt

rm -rf .package-cache
cd -

cleanup_and_exit 0
