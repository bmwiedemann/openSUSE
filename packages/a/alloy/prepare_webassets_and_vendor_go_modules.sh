#!/bin/bash

# do not use set -e, as the make step will abort the build due to warnings/errors
set -o pipefail

[[ "$#" == "2" ]] || {
        echo "Please use the package name and the golang package as the only arguments"
        exit 1
}

package_name="${1}"
golang_package="${2}"

cd /data || exit 11

zypper -n install \
    gawk \
    git-core \
    npm \
    patch \
    "${golang_package}" || exit 13

echo "Installing nvm"
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
export NVM_DIR="$HOME/.nvm"
source $NVM_DIR/nvm.sh

version="$( awk '/^Version:/ {print $2;exit;}' "${package_name}.spec" )"

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
pushd internal/web/ui/ || exit 25
nvm install
npm install
npm run build
popd || exit 29
echo "Creating web assets tarball"
tar -czf "${working_directory}/${webassets_tarball}" internal/web/ui/dist/
echo "DONE preparing the webassets"

echo "##########"
echo "Vendoring the go modules"
pushd collector/ || exit 31
go mod download || exit 33
go mod vendor || exit 35
echo "Verifying"
go mod verify || exit 37
echo "Creating the vendor tarball"
tar -czf "${working_directory}/vendor.tar.gz" vendor || exit 39
echo "DONE vendoring the go modules"

echo "##########"
echo "cleaning up"
cd "${working_directory}" || exit 41
rm -rf "$tmpdir" || exit 43
