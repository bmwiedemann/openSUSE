#!/bin/bash

NAME="fxload"
VERSION="2013_01_03"

wget -nv https://downloads.sourceforge.net/project/fx3load/fx3load.tgz
tar xf fx3load.tgz
pushd fx3load > /dev/null
  rm -rf CVS
  rm -f fxload
  rm -f *.o
popd > /dev/null
mv fx3load "$NAME-$VERSION"
tar -cf "$NAME-$VERSION.tar.xz" "$NAME-$VERSION"
rm -fr fx3load fx3load.tgz "$NAME-$VERSION"
