#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: ./create-tarball VERSION"
    exit 1
fi

VERSION=${1}
NAME="kxml"

wget https://downloads.sourceforge.net/sourceforge/${NAME}/${NAME}2-src-${VERSION}.zip
unzip -d ${NAME}-${VERSION} ${NAME}2-src-${VERSION}.zip
rm ${NAME}2-src-${VERSION}.zip

( cd ${NAME}-${VERSION}
  find . -name "*.jar" -delete
  rm -Rf bin/ dist/* www/ samples_midp/ samples/ contrib/
)

tar cJvf ${NAME}-${VERSION}-clean.tar.xz ./${NAME}-${VERSION}

