#!/bin/bash

# do not use set -e, as the make step will abort the build due to warnings/errors
set -o pipefail

[[ "$#" == "2" ]] || {
        echo "Please use the package name and the nodejs version as the only arguments"
        exit 1
}

package_name="${1}"
nodejs_package="${2}"

cd /data || exit 11

zypper -n install \
    cpio \
    gawk \
    make \
    git-core \
    npm \
    "${nodejs_package}" || exit 13

version="$( awk '/^Version:/ {print $2;exit;}' "${package_name}.spec" )"


echo "##########"
echo "Package version is $version"
basename="${package_name}-$version"

webassets_tarball="web-${version}.tar.gz"
obscpio="$basename.obscpio"
working_directory="$(pwd)"
tmpdir="$(mktemp -d -p /tmp)"
cd "${tmpdir}" || exit 15

echo "##########"
echo "Extracting obscpio archive"
cpio -id < "$working_directory/$obscpio" || exit 21
ls -lah
cd "$basename" || exit 23
ls -lah

echo "##########"
cd web/ || exit 25
mkdir -p dist/ || exit 27
npm install
npm run build
cd .. || exit 29
echo "Creating web assets tarball"
tar -czf "${working_directory}/${webassets_tarball}" web/ api/

echo "##########"
echo "DONE preparing the webassets"
cd "${working_directory}" || exit 31
rm -rf "$tmpdir"
