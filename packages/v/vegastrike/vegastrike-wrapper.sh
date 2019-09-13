#!/bin/sh

. /usr/share/opengl-games-utils/opengl-game-functions.sh

checkDriOK vegastrike

VSDATADIR=/usr/share/vegastrike
VERSION=`head -1 $VSDATADIR/Version.txt`

mkdir -p $HOME/$VERSION
cd $HOME/$VERSION
if [ \! -e ~/$VERSION/setup.config ]; then
  cp $VSDATADIR/setup.config .
fi
if [ \! -e ~/$VERSION/vegastrike.config ]; then
  cp $VSDATADIR/vegastrike.config .
  vssetup
fi
vegastrike "$@" || vssetup > /tmp/vslog 2>&1
