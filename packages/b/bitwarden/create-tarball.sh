#!/bin/sh

# dnf install curl gzip jq npm patch tar wget

PKGDIR="$(pwd)"
TMPDIR="$(mktemp --tmpdir -d bitwarden-XXXXXXXX)"

version=2023.2.0
tag=desktop




cd $TMPDIR

curl -L https://github.com/bitwarden/clients/archive/${tag}-v${version}.tar.gz |tar --gzip -xvvf -



cd clients-${tag}-v${version}



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

cd ..
mv -v clients-${tag}-v${version} bitwarden

echo ">>>>>> Hardlink duplicate files to reduce extraction time"

/usr/lib/rpm/fdupes_wrapper bitwarden

echo ">>>>>> Create tarball"
ZSTD_CLEVEL=19 ZSTD_NBTHREADS=$(nproc) tar --zstd --sort=name -vvScf "${PKGDIR}/bitwarden-${version}.tar.zst" bitwarden
if [ $? -ne 0 ]; then
    echo "ERROR: tar cf failed"
    cleanup_and_exit 1
fi




#Run `osc service disabledrun` to regenerate vendor.tar.xz