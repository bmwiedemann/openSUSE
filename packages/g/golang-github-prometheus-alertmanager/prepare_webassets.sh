#!/bin/bash

# do not use set -e, as the make step will abort the build due to warnings/errors
set -o pipefail

[[ "$#" == "0" ]] || {
        echo "Please call the script without arguments"
        exit 1
}

package_name=alertmanager
spec_file_name=golang-github-prometheus-alertmanager.spec

cd /data || exit 11

zypper -n install \
    gawk \
    git-core \
    npm || exit 13

version="$( awk '/^Version:/ {print $2;exit;}' "${spec_file_name}" )"

echo "##########"
echo "Package version is $version"
basename="${package_name}-$version"

webassets_tarball="ui-${version}.tar.gz"
tar="$basename.tar.gz"
working_directory="$(pwd)"
tmpdir="$(mktemp -d -p /tmp)"
cd "${tmpdir}" || exit 15

echo "##########"
echo "Extracting tar archive"
tar xf "$working_directory/$tar" || exit 21
ls -lah
cd "$basename" || exit 23
ls -lah

echo "##########"
pushd ui/app/ || exit 25
nvm install
npm ci
npm run build
popd || exit 29
echo "Creating web assets tarball"
tar -czf "${working_directory}/${webassets_tarball}" ui/app/dist/
echo "DONE preparing the webassets"

echo "##########"
echo "cleaning up"
cd "${working_directory}" || exit 41
rm -rf "$tmpdir" || exit 43
