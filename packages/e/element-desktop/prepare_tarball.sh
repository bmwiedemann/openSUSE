#!/bin/bash

set -ex

oldwd="$(pwd)"
tmpdir="$(mktemp -d)"

#zypper install yarn cargo gcc-c++ sqlcipher-devel libsecret-devel

version=$(grep "Version:" element-desktop.spec | awk '{print $2}')
wget -c https://github.com/vector-im/element-desktop/archive/v${version}.tar.gz -O element-desktop-${version}.tar.gz
wget -c https://github.com/vector-im/element-web/archive/v${version}.tar.gz -O element-web-${version}.tar.gz
cp element-desktop.spec "$tmpdir/"
cd "$tmpdir"

rm -rf "element-desktop-${version}"
wget -c https://github.com/vector-im/element-desktop/archive/v${version}.tar.gz -O element-desktop-${version}.tar.gz
tar xzvf element-desktop-${version}.tar.gz
cd element-desktop-${version}

sed -i 's@"electronVersion": "11.2.3"@"electronVersion": "13.1.2"@g' package.json
sed -i 's@"https://packages.riot.im/desktop/update/"@null@g' element.io/release/config.json

yarn install
export PATH="$PATH:node_modules/.bin"
yarn run build:native
yarn run build
tar czvf ../dist.tar.gz dist/linux-unpacked/resources/
cd ..
cp dist.tar.gz "$oldwd/"
cd "$oldwd"
rm -rf "$tmpdir"
#rm -rf "element-desktop-${version}"
echo -e "\n\nDONE creating output file 'dist.tar.gz'"
