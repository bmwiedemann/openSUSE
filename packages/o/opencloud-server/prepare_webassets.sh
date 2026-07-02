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
    patch \
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
cd "${tmpdir}/${basename}/services/idp/" || exit 23
ls -lah

mkdir -p assets/identifier/static/
cp src/images/favicon.svg assets/identifier/static/favicon.svg
rm -f assets/identifier/static/favicon.ico
cp src/images/icon-lilac.svg assets/identifier/static/icon-lilac.svg

# change pnpm version to match ours
PNPM_VERSION="$(rpm -q pnpm | awk -F '-' '{print $2}')"
sed -i "/packageManager/ s/\"pnpm@.*\"/\"pnpm@${PNPM_VERSION}\"/g" package.json
grep packageManager package.json

echo "Starting pnpm install"
pnpm install --frozen-lockfile
pnpm build

echo "##########"
echo "Starting tarball creation"
tar -czf "${working_directory}/${idp_tarball}" .
echo "Tarball creation finished, cleaning up"

echo "##########"
echo "DONE preparing the webassets"
cd "${working_directory}" || exit 31
rm -rf "${tmpdir}"
