#!/bin/sh

#
# repack source -- delete libX11-*.noarch.rpm from there; see bug #926061
#

VERSION=$1

if [ -z $VERSION ]; then
  echo "usage: $0 date_version"
  echo "example: $0 20150330"
  exit 1
fi

wget "https://github.com/fontforge/fontforge/archive/$VERSION.tar.gz"
tar xf $VERSION.tar.gz
pushd fontforge-$VERSION
# do not depend on git
git clone https://github.com/troydhanson/uthash
git clone --depth 1 https://github.com/coreutils/gnulib.git gnulib
# remove not shippable files (bug 926061)
rm win/gold/libX11-*.noarch.rpm
./bootstrap --copy --force
popd
tar cJf fontforge-$VERSION-repacked.tar.xz fontforge-$VERSION
rm -rf fontforge-$VERSION
rm $VERSION.tar.gz

