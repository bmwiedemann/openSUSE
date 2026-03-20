#!/bin/bash

# do not use set -e, as the make step will abort the build due to warnings/errors
set -o pipefail

cd /data

[[ "$#" == "2" ]] || {
        echo "Please use the package name and the nodejs version as the only arguments"
        exit 1
}

package_name="${1}"
nodejs_package="${2}"

zypper -n install \
    cpio \
    gawk \
    make \
    git-core \
    yarn \
    npm \
    "${nodejs_package}"

version="$( awk '/^Version:/ {print $2;exit;}' "${package_name}.spec" )"

echo "##########"
echo "Package version is $version"
basename="${package_name}-$version"
obscpio="$basename.obscpio"
wd="$(pwd)"
tmpdir="$(mktemp -d -p /tmp)"
cd "$tmpdir"

echo "##########"
echo "Extracting obscpio archive"
cpio -id < "$wd/$obscpio"
ls -lah
cd "$basename" || exit 13
ls -lah

echo "##########"
make install-ui-dependencies ember-dist

tar -czf "${wd}/ui-${version}.tar.gz" ui http/

echo "##########"
echo "DONE preparing the webassets"
rm -rf "$tmpdir"
