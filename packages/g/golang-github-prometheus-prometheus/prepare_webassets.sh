#!/bin/bash

set -o pipefail

[[ "$#" == "0" ]] || {
        echo "This script accepts no arguments"
        exit 1
}

spec_file_name=golang-github-prometheus-prometheus.spec
package_name=prometheus

cd /data || exit 11

zypper -n install \
    cpio \
    gawk \
    make \
    git-core \
    patch \
    pnpm || exit 13

version="$( awk '/^Version:/ {print $2;exit;}' "${spec_file_name}" )"

[[ -z "${version}" ]] && {
        echo "version variable is empty..."
        exit 14
}

echo "##########"
echo "Package version is ${version}"
basename="${package_name}-${version}"
obscpio="${basename}.obscpio"
webassets_tarball="web-${version}.tar.gz"
working_directory="$(pwd)"
tmpdir="$(mktemp -d -p /tmp)"
echo "Changing into tmpdir ${tmpdir}"
cd "${tmpdir}" || exit 15

echo "##########"
echo "Extracting obscpio archive"
cpio -id < "${working_directory}/${obscpio}" || exit 21
cd "${basename}" || exit 23

patch -p1 < 0003-Remove-build-react-app.patch

echo "##########"
cd web/ui/ || exit 25
rm -rf node_modules || exit 27
pnpm install --frozen-lockfile

# cd react-app || exit 25
# rm -rf node_modules || exit 27
# pnpm install --frozen-lockfile
# cd .. || exit 25

CI="true" pnpm run build:mantine-ui

cd ../../ || exit 29
echo "Creating web assets tarball"
tar -czf "${working_directory}/${webassets_tarball}" web/ui/

echo "##########"
echo "Cleaning up..."
cd "${working_directory}" || exit 31
rm -rf "$tmpdir"

echo "DONE preparing the webassets"

exit 0
