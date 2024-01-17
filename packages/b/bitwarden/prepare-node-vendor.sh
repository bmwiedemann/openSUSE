#!/bin/sh -eu

# dnf install curl gzip jq npm patch tar wget

PKGDIR="$(pwd)"






cd clients



#These patches touch NPM's files
patch --verbose -p1 -b < $PKGDIR/remove-unnecessary-deps.patch

#remove unnecessary / non-free source
rm -rf apps/browser apps/cli apps/web bitwarden_license

npm ci  --verbose --ignore-scripts

echo ">>>>>> Remove argon2 vendor"
rm -rf node_modules/argon2/argon2

echo ">>>>>> Remove non-free binaries"
find . -type f -name "*.wasm" -print -delete
find . -type f -name "*.jar" -print -delete
find . -type f -name "*.exe" -print -delete
find . -type f -name "*.node" -print -delete
find . -type f -name "*.dll" -print -delete
find . -type f -name "*.dylib" -print -delete
find . -type f -name "*.so" -print -delete
find . -type f -name "*.o" -print -delete
find . -type f -name "*.a" -print -delete

#We use sponge to avoid a race condition between find and rm
find -type f | sponge | xargs -P$(nproc) -- sh -c 'file -S "$@" | grep -v '\'' .*script'\'' | grep '\'' .*executable'\'' | tee /dev/stderr | sed '\''s/: .*//'\'' | xargs rm -fv'


# Remove empty directories
echo ">>>>>> Remove empty directories"
find . -type d -empty -print -delete


echo ">>>>>> Create tarball"
ZSTD_CLEVEL=19 ZSTD_NBTHREADS=$(nproc) tar --zstd --sort=name -vvScf "${PKGDIR}/node-vendor.tar.zst" node_modules

