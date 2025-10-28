#!/bin/bash 

set -ex

version=$1
sed -i -e "s/^\(Version: *\)[^ ]*$/\1${version}/" element-web.spec

oldwd="$(pwd)"

# cleanup old stuff
(find -maxdepth 1 -type d -name 'element-web-*' | xargs rm -r) ||:

version=$(grep "Version:" element-web.spec | awk '{print $2}')
last_packaged_version=$(osc cat devel:languages:nodejs/element-web/element-web.spec | grep "^Version:" | awk '{print $NF}')

git rm --force element-web-*.tar.gz || :
#       https://github.com/element-hq/element-web/archive/refs/tags/v1.11.111.tar.gz
wget -c https://github.com/element-hq/element-web/archive/refs/tags/v${version}.tar.gz -O element-web-${version}.tar.gz
wget https://meet.element.io/libs/external_api.min.js -O jitsi_external_api.min.js
git add element-web-*.tar.gz

#zypper install yarn cargo gcc-c++ sqlcipher-devel libsecret-devel

rm -rf "element-web-${version}"
tar xzvf element-web-${version}.tar.gz
cd element-web-${version}
changes=$(grep "^Changes in \[$last_packaged_version\]" -B10000 CHANGELOG.md |  head -n -2 | sed -e '/^==*$/d' -e 's/Changes in \[\([^\[]*\)\].*/Version \1/' -e 's/^\([^-].*\)$/  \1/' -e 's/\[.*\](\(.*\))/\1/g' -e 's/^ *Version /Version /g')

tmpdir="$(mktemp -d)"
mkdir -pv "$tmpdir/home"
oldhome="$HOME"
export HOME="$tmpdir/home"

yarn cache clean
rm -rf node_modules/
#cp "$oldwd/yarn.lock" ./
yarn install  --frozen-lockfile --ignore-engines --ignore-platform  --ignore-scripts --link-duplicates || : # this will download the packages

#Remove non-free binaries, starting with a few common file extensions
find . -name '*.node' -print -delete
find . -name '*.jar' -print -delete
find . -name '*.dll' -print -delete
find . -name '*.exe' -print -delete
find . -name '*.dylib' -print -delete
find . -name '*.so' -print -delete
find . -name '*.o' -print -delete
find . -name '*.a' -print -delete

#now detect the rest. This should catch all ELFs that may be executed. We use sponge to avoid a race condition between find and rm
find . -type f| sponge |\
    xargs -P"$(nproc)" -- sh -c 'file -S "$@" | grep -v '\'': .*script'\'' | grep '\'': .*executable'\'' | tee /dev/stderr | sed '\''s/: .*//'\'' | xargs rm -fv'

rm -f "${oldwd}/vendor.tar.zst"
ZSTD_CLEVEL=19 ZSTD_NBTHREADS=$(nproc) tar --zstd --sort=name -Scf "${oldwd}/vendor.tar.zst" node_modules
export HOME="$oldhome"

cd "$oldwd"
rm -rf "$tmpdir"
echo -e "\n\nDONE creating npm offline dependencies archive 'vendor.tar.zst'"

read -p "Write changes?"
osc vc -m "${changes}" element-web.changes
dos2unix element-web.changes
