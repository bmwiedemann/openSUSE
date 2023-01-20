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

rpmspec -P velociraptor.spec --define "_sourcedir $PWD" | \
awk '
BEGIN { go=0; };
/^%build/ { go=0; };
{ if (go) print };
/^%setup/ { go=1 }' > ${dir}/setup.sh

echo "Expanding archive..."
cpio -D "${dir}" -id < velociraptor-${version}.obscpio

echo "Running %prep"
cd "${dir}/velociraptor-${version}"
tar Jxf ${topdir}/vmlinux.h-5.14.21150400.22-150400-default.tar.xz
sh ${dir}/setup.sh

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
