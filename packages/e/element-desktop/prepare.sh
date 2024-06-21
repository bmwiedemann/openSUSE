#!/bin/bash

set -ex




version=$1
last_packaged_version=$(cat "element-desktop.spec" | grep "^Version:" | awk '{print $NF}')
sed -i -e "s/^\(Version: *\)[^ ]*$/\1${version}/" element-desktop.spec

oldwd="$(pwd)"
tmpdir="$(mktemp -d)"


#zypper install findutils file yarn cargo cargo-vendor-filterer moreutils jq

version=$(grep "Version:" element-desktop.spec | awk '{print $2}')
osc rm -f element-web-*.tar.gz ||:
osc rm -f element-desktop-*.tar.gz ||:
wget -c https://github.com/vector-im/element-desktop/archive/v${version}.tar.gz -O element-desktop-${version}.tar.gz
osc add -f element-desktop-*.tar.gz
cp element-desktop.spec "$tmpdir/"
cd "$tmpdir"

#dziobian: yarn has completely broken caching policy which first compiles the module and then caches the result.
#additionally, --ignore-scripts seems to be evaluated during caching, and not during install to node_modules.
#Mitigate this by resetting ~ to an empty directory
mkdir -pv "$tmpdir/home"
export HOME="$tmpdir/home"

tar -xzvvf "${oldwd}/element-desktop-${version}.tar.gz"
cd element-desktop-${version}

#These patches change results of things we want to execute below
patch -p1 --verbose < "${oldwd}/hak-remove-devdependencies.patch"

changes=$(grep "^Changes in \[$last_packaged_version\]" -B10000 CHANGELOG.md |  head -n -2 | sed -e '/^==*$/d' -e 's/Changes in \[\([^\[]*\)\].*/Version \1/' -e 's/^\([^-].*\)$/  \1/' -e 's/\[.*\](\(.*\))/\1/g' -e 's/^ *Version /Version /g')

# This will vendor the packages but not execute any build scripts (but see caveat about caching above)
yarn install --frozen-lockfile --ignore-engines --ignore-platform  --ignore-scripts --link-duplicates

export PATH="$PATH:node_modules/.bin"

#hak does not have version pinning, which is terrible.
#Therefore we manually pin the minimum versions specified in package.json
jq '.hakDependencies[]|= sub("^\\^";"";"i")' <package.json > package.json.new
diff --color=always -bup package.json{,.new} || true
mv package.json{.new,}



yarn run hak fetch

# prefetch cargo crates
pushd .hak/hakModules/matrix-seshat
mkdir -pv .cargo 
cargo vendor-filterer --platform='*-unknown-linux-gnu' --platform='*-unknown-linux-gnueabihf' --all-features > .cargo/config
#remove vendored libraries
rm -rvf vendor/openssl-src/openssl
popd

#fetch node-addon-api for keytar. Unfortunately there is no package lock, therefore we use lowest supported version (for reproducility)
#we need to install it manuall in a separate directory wiithout a package.json. good that node-addon-api has no dependencies.
pushd .hak/hakModules/keytar
naa_version=$(jq -cj '.dependencies["node-addon-api"]' <package.json | sed 's/^\^//')
mkdir -pv "$tmpdir/naa"
pushd "$tmpdir/naa"
npm install --verbose --ignore-scripts --no-save node-addon-api@"${naa_version}"
popd
mv -v "$tmpdir/naa/node_modules" -t .
popd

#Remove non-free binaries, starting with a few common file extensions
find . -name '*.node' -print -delete
find . -name '*.jar' -print -delete
find . -name '*.dll' -print -delete
find . -name '*.exe' -print -delete
find . -name '*.dylib' -print -delete
find . -name '*.so' -print -delete
find . -name '*.o' -print -delete
find . -name '*.a' -print -delete
find . -name '*.wasm' -print -delete

#now detect the rest. This should catch all ELFs that may be executed. We use sponge to avoid a race condition between find and rm
find . -type f| sponge |\
    xargs -P"$(nproc)" -- sh -c 'file -S "$@" | grep -v '\'': .*script'\'' | grep '\'': .*executable'\'' | tee /dev/stderr | sed '\''s/: .*//'\'' | xargs rm -fv'


rm -f "${oldwd}/vendor.tar.zst"
ZSTD_CLEVEL=19 ZSTD_NBTHREADS=$(nproc) tar --zstd --sort=name -vvScf "${oldwd}/vendor.tar.zst" .hak node_modules


cd "$oldwd"
echo rm -rf "$tmpdir"
echo -e "\n\nDONE creating npm offline dependencies archive 'vendor.tar.zst'"


read -p "Write changes?"
osc vc -m "${changes}" element-desktop.changes
dos2unix element-desktop.changes
