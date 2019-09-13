#!/bin/bash
set -ex

API="1.2"
HEADERS="opencl.h cl_platform.h cl.h cl_ext.h cl_dx9_media_sharing.h cl_d3d10.h cl_d3d11.h cl_gl.h cl_gl_ext.h cl.hpp"
URL="http://www.khronos.org/registry/cl/api/$API/"

WORKDIR="$(mktemp -d opengl.XXXX)"

TODIR="$(pwd)"
cd "$WORKDIR"

mkdir headers
cd headers

DATE=0
for file in $HEADERS; do
	wget "$URL/$file"
	FILEDATE="$(date -ud "@$(stat -c%Y "$file")" +%Y%m%d)"
	[ $FILEDATE -gt $DATE ] && DATE=$FILEDATE
done

cd ..

TARNAME="opencl-headers-`echo $API | tr . _`-"$API"_$DATE"
TAR="$TARNAME.tar.bz2"
mv headers "$TARNAME"

if [ -e "$TODIR/$TAR" ]; then
	echo "$TAR already exists."
else
	tar -cjf "$TODIR/$TAR" "$TARNAME"
fi
cd "$TODIR"
rm -r "$WORKDIR"
