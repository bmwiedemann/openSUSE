#!/usr/bin/sh

set -e

if [[ -z "$1" ]]; then
echo "Please enter the version you want to update to";
exit 1;
fi

VERSION="$1"

echo "++++++++++++++++++++++++++++++++++++++++++++++"
echo "patching spec file and downloading the tarball"
echo "++++++++++++++++++++++++++++++++++++++++++++++"

sed -i -e 's|Version: .*|Version:        '${VERSION}'|g' forgejo.spec
osc service ra download_files

echo "++++++++++++++++++++++++++++++++++++++++++++++"
echo "extracting package-lock.json"
echo "++++++++++++++++++++++++++++++++++++++++++++++"

tar xf forgejo-src-${VERSION}.tar.gz forgejo-src-${VERSION}/package-lock.json
cp forgejo-src-${VERSION}/package-lock.json .

echo "++++++++++++++++++++++++++++++++++++++++++++++"
echo "Downloading node_modules"
echo "++++++++++++++++++++++++++++++++++++++++++++++"

osc service ra node_modules

echo "++++++++++++++++++++++++++++++++++++++++++++++"
echo "Cleanup Step"
echo "++++++++++++++++++++++++++++++++++++++++++++++"

rm -r forgejo-src-${VERSION}
rm node_modules.sums

echo "++++++++++++++++++++++++++++++++++++++++++++++"
echo "Done! Have fun building and testing"
echo "++++++++++++++++++++++++++++++++++++++++++++++"
