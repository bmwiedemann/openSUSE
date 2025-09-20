#!/bin/bash -eux

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

# Since version 2024.8.0 (August 2024), obs-service-cargo_vendor does not work anymore:
# ERROR obs_service_cargo::audit: cargo_lock_err=Parse("parse error: couldn't resolve dependency: bytes\n")
# ERROR obs_service_cargo::utils: Unable to complete cargo audit rustsec_err=Error { kind: BadParam, msg: "parse error: parse error: couldn't resolve dependency: bytes\n", source: None }
pushd apps/desktop/desktop_native
mkdir -pv .cargo
cargo vendor-filterer --platform='*-unknown-linux-gnu' --platform='*-unknown-linux-gnueabihf' --all-features > .cargo/config
popd

echo ">>>>>> Remove sqlite vendor"
rm -v  apps/desktop/desktop_native/vendor/libsqlite3-sys/sqlite3/sqlite3*
rm -v  apps/desktop/desktop_native/vendor/libsqlite3-sys/sqlcipher/sqlite3*



echo ">>>>>> Remove non-free binaries"
find . -type f -name "*.wasm" -print -delete
find . -type f -name "*.wasm.js" -print -delete
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
ZSTD_CLEVEL=19 ZSTD_NBTHREADS=$(nproc) tar --zstd --sort=name -vvScf "${PKGDIR}/vendor.tar.zst" node_modules apps/desktop/desktop_native/{.cargo/config,vendor}

