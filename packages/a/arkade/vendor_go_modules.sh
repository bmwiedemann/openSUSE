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
    cpio \
    gawk \
    sed \
    git-core \
    "${golang_package}" || exit 13

version="$( awk '/^Version:/ {print $2;exit;}' "${package_name}.spec" )"

echo "##########"
echo "Package version is $version"
BASENAME="${package_name}-$version"

obscpio="$BASENAME.obscpio"
working_directory="$(pwd)"
tmpdir="$(mktemp -d -p /tmp)"
cd "${tmpdir}" || exit 15

echo "##########"
echo "Extracting obscpio archive"
cpio -id < "$working_directory/$obscpio" || exit 21
ls -lah
cd "${BASENAME}" || exit 23
ls -lah

echo "##########"
echo "Cloning gha-bump"
GHABUMP_COMMIT="$(awk '/^require github.com\/alexellis\/gha-bump/ {print $NF}' go.mod)"
git clone https://github.com/alexellis/gha-bump ../gha-bump || exit 25

echo "##########"
echo "Vendoring the go modules"
go mod tidy
go mod download || exit 33
go mod vendor || exit 35
echo "Verifying"
go mod verify || exit 37
echo "Creating the vendor tarball"
tar -czf "${working_directory}/vendor.tar.gz" vendor go.mod go.sum || exit 39
echo "DONE vendoring the go modules"

echo "##########"
echo "cleaning up"
cd "${working_directory}" || exit 41
rm -rf "$tmpdir" || exit 43
