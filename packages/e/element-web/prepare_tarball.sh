#!/bin/bash

set -ex

oldwd="$(pwd)"
tmpdir="$(mktemp -d)"

version=$(grep "Version:" element-web.spec | awk '{print $2}')
wget -c https://github.com/vector-im/element-web/archive/v${version}.tar.gz -O element-web-${version}.tar.gz
cp element-web.spec "$tmpdir/"
cd "$tmpdir"

#zypper install yarn cargo gcc-c++ sqlcipher-devel libsecret-devel


rm -rf "element-web-${version}"
wget -c https://github.com/vector-im/element-web/archive/v${version}.tar.gz -O element-web-${version}.tar.gz
tar xzvf element-web-${version}.tar.gz
cd element-web-${version}

yarn install || :
DIST_VERSION=$version ./scripts/package.sh

cp "dist/element-${version}.tar.gz" "$oldwd/"
cd "$oldwd"
rm -rf "$tmpdir"
echo -e "\n\nDONE creating output file 'element-${version}.tar.gz'"
