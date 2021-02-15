#!/bin/sh

commit=6ac62d2e888cabb138c8427e6173c04e07bb60e0
# See: mozc/src/data/version/mozc_version_template.bzl
# REVISION is always 102 for Linux
version=2.26.4276.102

set -e

if [ ! -e mozc ]; then
    git clone --depth=1 https://github.com/google/mozc.git
fi

cd mozc
git checkout $commit

git archive --prefix=mozc-$version/ $commit | tar xC ../
cd ..
rm -r mozc-$version/src/third_party/*
rm -r mozc-$version/docker
tar --owner=0 --group=0 -cvJf mozc-$version.tar.xz mozc-$version
