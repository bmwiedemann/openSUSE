#!/bin/bash

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
    pnpm \
    go \
    webkitgtk4-devel \
    zstd \
    "${nodejs_package}" || exit 13

version="$( awk '/^Version:/ {print $2;exit;}' "${package_name}.spec" )"


echo "##########"
echo "Package version is $version"
basename="${package_name}-$version"

webassets_tarball="frontend-${version}.tar.zst"
obscpio="$basename.obscpio"
working_directory="$(pwd)"
tmpdir="$(mktemp -d -p /tmp)"
echo "Changing into tmpdir ${tmpdir}"
cd "${tmpdir}" || exit 15

echo "##########"
echo "Extracting obscpio archive"
cpio -id < "${working_directory}/${obscpio}" || exit 21
cd "$basename" || exit 23

echo "##########"
cd client/ui/frontend || exit 25
rm -rf node_modules || exit 27
WAILS_VERSION=$(go list -m -f '{{.Version}}' github.com/wailsapp/wails/v3)
go install github.com/wailsapp/wails/v3/cmd/wails3@$WAILS_VERSION
# ~/go/bin/ not in path by default, and pnpm run bindings calls wails3 to generate the bindings
mv /root/go/bin/wails3 /usr/local/bin/
pnpm install --frozen-lockfile --ignore-scripts
pnpm run bindings
pnpm run check
pnpm build
cd ../../.. || exit 29
echo "Creating web assets tarball"
tar -I "zstd -T0" -cvf "${working_directory}/${webassets_tarball}" client/ui/frontend

echo "##########"
echo "DONE preparing the webassets"
cd "${working_directory}" || exit 31
rm -rf "$tmpdir"
