#!/bin/bash

set -o pipefail

[[ "$#" == "2" ]] || {
        echo "Please use the package name and the nodejs version as the only arguments"
        exit 1
}

spec_file_name="${1}"
nodejs_package="${2}"

package_name=prometheus

cd /data || exit 11

zypper -n install \
    cpio \
    gawk \
    make \
    git-core \
    npm \
    "${nodejs_package}" || exit 13

version="$( awk '/^Version:/ {print $2;exit;}' "${spec_file_name}" )"

[[ -z "${version}" ]] && {
        echo "version variable is empty..."
        exit 14
}

echo "##########"
echo "Preparing the webui dependencies"
echo "Package version is ${version}"
basename="${package_name}-${version}"
obscpio="${basename}.obscpio"
working_directory="$(pwd)"
tmpdir="$(mktemp -d -p /tmp)"
echo "Changing into tmpdir ${tmpdir}"
cd "${tmpdir}" || exit 15

echo "##########"
echo "Extracting obscpio archive"
cpio -id < "${working_directory}/${obscpio}" || exit 21

echo "##########"
cd "${basename}/web/ui/" || exit 23

echo "Removing package-lock.json"
rm -vf package-lock.json || exit 25
echo "Starting npm install"
npm install --package-lock-only || exit 27
echo "Copy package-lock.json"
cp -vf package-lock.json "${working_directory}" || exit 29

echo "##########"
echo "Cleaning up..."
cd "${working_directory}" || exit 31
rm -rf "$tmpdir"

echo "##########"
echo "DONE creating the package-lock.json file"

exit 0
