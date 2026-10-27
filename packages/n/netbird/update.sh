#!/bin/bash
#
QUILT_PATCHES=".quilt-patches"
set -x
set -e
VERSION="${1:?please give me a version}"

if ! test -d netbird ; then
  git clone https://github.com/netbirdio/netbird.git
fi

pushd netbird
git fetch --tags
git checkout ${VERSION}
ln -s .. ${QUILT_PATCHES}
quilt push -a
rm -rv client/ui
go mod vendor
tar --zstd -cvf ../vendor.tar.zst vendor/ go.sum
rm -rv vendor/ .pc/ ${QUILT_PATCHES}
git reset --hard
popd

rm *cpio
perl -p -i -e "s|refs/tags/[^<]+|refs/tags/${VERSION}|g" _service
osc service mr
osc ar
