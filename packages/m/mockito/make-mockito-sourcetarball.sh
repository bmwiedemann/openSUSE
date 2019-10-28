#!/bin/bash -ex

VERSION=1.10.19
SRCDIR=mockito-${VERSION}

git clone https://github.com/mockito/mockito.git ${SRCDIR}
pushd $SRCDIR
git archive --format=tar --prefix=${SRCDIR}/ v${VERSION} > ../${SRCDIR}.tar
popd

rm -rf ${SRCDIR}

tar -xf ${SRCDIR}.tar
rm ${SRCDIR}.tar
pushd ${SRCDIR}
rm -rf `find -name *.jar` build.gradle cglib-and-asm doc gradle gradlew gradlew.bat javadoc
dos2unix `find -name *.java`
popd

tar -cvJf mockito-${VERSION}.tar.xz ${SRCDIR}
