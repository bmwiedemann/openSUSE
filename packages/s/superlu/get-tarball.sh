#!/bin/bash
set -e

VERSION=5.2.2
FILES="mc64ad.c sgsisx.c sldperm.c dgsisx.c dldperm.c cgsisx.c cldperm.c zgsisx.c zldperm.c"
URL="https://github.com/xiaoyeli/superlu/archive/v$VERSION/superlu-$VERSION.tar.gz"
TAR="superlu-$VERSION.tar.gz"

WORKDIR="$(mktemp -d superlu.XXXX)"

TODIR="$(pwd)"
cd "$WORKDIR"

wget $URL
tar xfz superlu-$VERSION.tar.gz

for file in $FILES; do
	rm superlu-$VERSION/SRC/$file
done

if [ -e "$TODIR/$TAR" ]; then
	echo "$TAR already exists."
else
	tar cfz "$TODIR/$TAR" superlu-$VERSION
fi

cd "$TODIR"
rm -r "$WORKDIR"

