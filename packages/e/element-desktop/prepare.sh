#!/bin/bash

set -ex

oldwd="$(pwd)"
tmpdir="$(mktemp -d)"

#zypper install yarn cargo gcc-c++ sqlcipher-devel libsecret-devel

version=$(grep "Version:" element-desktop.spec | awk '{print $2}')
osc rm element-web-*.tar.gz
osc rm element-desktop-*.tar.gz
wget -c https://github.com/vector-im/element-desktop/archive/v${version}.tar.gz -O element-desktop-${version}.tar.gz
wget -c https://github.com/vector-im/element-web/archive/v${version}.tar.gz -O element-web-${version}.tar.gz
osc add element-web-*.tar.gz
osc add element-desktop-*.tar.gz
cp element-desktop.spec "$tmpdir/"
cd "$tmpdir"

rm -rf "element-desktop-${version}"
wget -c https://github.com/vector-im/element-desktop/archive/v${version}.tar.gz -O element-desktop-${version}.tar.gz
tar xzvf element-desktop-${version}.tar.gz
cd element-desktop-${version}

#sed -i 's@"electronVersion": "11.2.3"@"electronVersion": "13.1.2"@g' package.json
#sed -i 's@"https://packages.riot.im/desktop/update/"@null@g' element.io/release/config.json

echo 'yarn-offline-mirror "./npm-packages-offline-cache"' > .yarnrc
yarn cache clean
rm -rf node_modules/
yarn install --pure-lockfile || : # this will download tha packages into the offline cache

#mkdir -p electron-builder-offline-cache
#export ELECTRON_BUILDER_CACHE="$(pwd)/electron-builder-offline-cache/"
#export PATH="$PATH:node_modules/.bin"
#yarn run build

tar czf npm-packages-offline-cache.tar.gz ./npm-packages-offline-cache
cp -v npm-packages-offline-cache.tar.gz "$oldwd/"

#tar czf electron-builder-offline-cache.tar.gz ./electron-builder-offline-cache/
#cp electron-builder-offline-cache.tar.gz "$oldwd/"
cd "$oldwd"
echo rm -rf "$tmpdir"
echo -e "\n\nDONE creating npm dependency offline cache file 'npm-packages-offline-cache.tar.gz'"





#yarn install
#export PATH="$PATH:node_modules/.bin"
#yarn run build:native
#yarn run build
#tar czvf ../dist.tar.gz dist/linux-unpacked/resources/
#cd ..
#cp dist.tar.gz "$oldwd/"
#cd "$oldwd"
#rm -rf "$tmpdir"
#rm -rf "element-desktop-${version}"
#echo -e "\n\nDONE creating output file 'dist.tar.gz'"
