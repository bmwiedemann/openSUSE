#!/bin/bash

# do not use set -e, as the make step will abort the build due to warnings/errors
set -o pipefail

[[ "$#" == "2" ]] || {
        echo "Please use the package name and the nodejs version as the only arguments"
        exit 1
}

package_name="${1}"
pnpm_package="${2}"

cd /data || exit 11

zypper -n install \
    cpio \
    gawk \
    make \
    git-core \
    npm \
    "${pnpm_package}" || exit 13

version="$( awk '/^Version:/ {print $2;exit;}' "${package_name}.spec" )"


echo "##########"
echo "Package version is ${version}"
basename="${package_name}-$version"

idp_tarball="idp-${version}.tar.gz"
obscpio="${basename}.obscpio"
working_directory="$(pwd)"
tmpdir="$(mktemp -d -p /tmp)"
echo "Changing into tmpdir"
cd "${tmpdir}" || exit 15

echo "##########"
echo "Extracting obscpio archive"
cpio -id < "${working_directory}/${obscpio}" || exit 21
ls -lah

echo "##########"
echo "Changing into the services/idp/ subdirectory"
cd "${basename}/services/idp/" || exit 23
ls -lah
echo "Starting pnpm install"
pnpm install --frozen-lockfile

echo "##########"
echo "Starting tarball creation"
tar -czf "${working_directory}/${idp_tarball}" ./node_modules/
echo "Tarball creation finished, cleaning up"

echo "##########"
echo "DONE preparing the webassets"
cd "${working_directory}" || exit 31
rm -rf "${tmpdir}"
