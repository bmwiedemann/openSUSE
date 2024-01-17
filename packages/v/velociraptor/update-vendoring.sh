#!/bin/bash

cleanup() {
	test -n "${dir}" && rm -rf "${dir}"
	if test -n "${gopathdir}"; then
		chmod -R u+w "${gopathdir}"
		rm -rf "${gopathdir}"
	fi
}

error() {
	echo "An error occurred.  Exiting." >&2
}

trap error ERR SIGINT
trap cleanup EXIT
set -e

version=$(rpmspec -q --queryformat="%{VERSION}\n" velociraptor.spec|head -1)

dir="$(realpath "$(mktemp -d vendoring.XXXXXX)")"
topdir="$(realpath "$(dirname "$0")")"

# Pull the %prep section out of the spec file and replace the tarball with the obscpio
awk '
BEGIN { go=1; };
/^%build/ { go=0; };
{ if (go) print };' < velociraptor.spec > ${dir}/velociraptor.spec

rpmspec -P ${dir}/velociraptor.spec --define "_sourcedir $PWD" --define "_builddir ${dir}"| \
awk '
BEGIN { go=0; };
/^%build/ { go=0; };
{ if (go) print };
/^%prep/ { go=1 }' | sed -e "/rpmuncompress.*velociraptor-.*.tar.xz/s#.*#cpio -D . -id < $PWD/velociraptor-${version}.obscpio#" > ${dir}/setup.sh

echo "Running %prep"
cd ${dir}
sh -e ${dir}/setup.sh
cd "${dir}/velociraptor-${version}"

echo "Re-vendoring Go code..."
gopathdir="$(mktemp -d /tmp/gopath.XXXXXXX)"
rm -rf vendor
export GOPATH="$gopathdir"


# Vendoring doesn't get along with replaced modules, so symlink to those
go mod vendor
replace_module() {
	local mod=$1
	local path=$2
	rm -rf "vendor/${mod}"
	rel="$(echo $mod|tr A-Za-z0-9_- .|sed -e 's/\.\.\.*/../g')"
	ln -s "${rel}/${path}" "vendor/${mod}"
	set -x
	ls -la vendor/${mod}/
	set +x
}

replace_module github.com/aquasecurity/libbpfgo third_party/libbpfgo

tar Jcf ${dir}/vendor-golang-${version}.tar.xz vendor
cd "${dir}"
mv vendor-golang-*${version}.tar.xz ${topdir}

cd "${dir}/velociraptor-${version}/contrib/kafka-humio-gateway"
rm -rf vendor
go mod vendor
cd "${dir}/velociraptor-${version}"
tar Jcf "${dir}/vendor-golang-kafka-humio-gateway-${version}.tar.xz" "contrib/kafka-humio-gateway/vendor"

echo "Re-vendoring nodejs code..."
cd "${dir}/velociraptor-${version}/gui/velociraptor"
rm -rf node_modules
npm install
cd ../..
tar Jcf ${dir}/vendor-nodejs-${version}.tar.xz gui/velociraptor/node_modules

cd "${dir}"
mv vendor-golang-*${version}.tar.xz vendor-nodejs-${version}.tar.xz ${topdir}

for spec in ${topdir}/*.spec; do
    sed -i "s/^%define vendor_version.*/%define vendor_version ${version}/" ${spec}
done

echo "Done"
