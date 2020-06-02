#!/bin/sh

version=2.23.2815.102
commit=afb03ddf

set -e

# git clone --depth=1 https://github.com/google/mozc.git
cd mozc
git archive --prefix=mozc-$version/ $commit | tar xC ../
cd ..
rm -r mozc-$version/src/third_party/*
rm -r mozc-$version/docker
tar --owner=0 --group=0 -cvJf mozc-$version.tar.xz mozc-$version