#!/bin/bash

#dnf install cargo-vendor-filterer curl git-core moreutils npm zstd

set -euxo pipefail


PKGDIR="$(pwd)"
TMPDIR="$(mktemp --tmpdir -d bitwarden-XXXXXXXX)"


# Upstream does not offer any tarballs. We need to get the commit info from npm and download it manually.
VERSION="$(rpmspec -P ./*.spec | grep ^\s*Version | sed -e 's/Version:[ ]*//g' | sed 's/~/-/g' )"


pushd "$TMPDIR"
curl -L https://registry.npmjs.org/@bitwarden/sdk-internal/-/sdk-internal-"$VERSION".tgz | tar -zxvv package/VERSION
git_tag=$(<package/VERSION)
mkdir sdk-internal
cd sdk-internal
git init
git remote add origin https://github.com/bitwarden/sdk-internal
git fetch origin $git_tag --depth=1 --filter=tree:0
git checkout $git_tag
mv -v ../package/VERSION -t crates/bitwarden-wasm-internal/npm/

patch -p1 --verbose --no-backup-if-mismatch < "$PKGDIR/wasm-bindgen-cli.patch"



cargo vendor-filterer --platform='*-unknown-linux-gnu' --platform='*-unknown-linux-gnueabihf' --platform=wasm32-unknown-unknown --all-features > .cargo/config

pushd crates/bitwarden-wasm-internal/npm/
NODE_ENV=production npm ci --ignore-scripts --verbose --omit dev
popd

#Remove non-free code
rm -rf bitwarden_license

echo '>>>>>> Remove git directories'
find . -name .git -print0 | xargs -0 rm -rf

echo '>>>>>> Remove vendored binaries'
find . -type f -name "*.wasm" -print -delete
find . -name "*.jar" -print -delete
find . -name "*.exe" -print -delete
find . -name "*.node" -print -delete
find . -name "*.dll" -print -delete
find . -name "*.dylib" -print -delete
find . -name "*.so" -print -delete
find . -name "*.o" -print -delete
find . -name "*.a" -print -delete

find -type f | sponge | xargs -P$(nproc) -- sh -c 'file -S "$@" | grep -v '\'' .*script'\'' | grep '\'' .*executable'\'' | tee /dev/stderr | sed '\''s/: .*//'\'' | xargs rm -fv'

cd ..

ZSTD_CLEVEL=19 ZSTD_NBTHREADS=$(nproc) tar --zstd --sort=name -vvScf "${PKGDIR}/sdk-internal-${VERSION}.tar.zst"  sdk-internal

popd

rm -rf "$TMPDIR"