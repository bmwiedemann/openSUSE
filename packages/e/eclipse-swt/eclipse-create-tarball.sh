#!/bin/bash

ECLIPSE_DATE=20180906
ECLIPSE_TIME=0745
VERSION=4.9
NAME="eclipse-platform-sources"

tmp_dir=$(mktemp -d)

echo ${tmp_dir}

pushd ${tmp_dir}

wget http://archive.eclipse.org/eclipse/downloads/drops4/R-${VERSION}-${ECLIPSE_DATE}${ECLIPSE_TIME}/${NAME}-${VERSION}.tar.xz
tar -xf ${NAME}-${VERSION}.tar.xz
rm ${NAME}-${VERSION}.tar.xz

pushd ${NAME}-I${ECLIPSE_DATE}-${ECLIPSE_TIME}

# Delete pre-built binary artifacts except some test data that cannot be generated
find . ! -path "*/JCL/*" ! -name "rtstubs*.jar" ! -name "java10api.jar" ! -name "j9stubs.jar" \
   -type f -name *.jar -delete
find . -type f -name *.class -delete
find . -type f -name *.so -delete
find . -type f -name *.dll -delete
find . -type f -name *.jnilib -delete

# Remove pre-compiled native launchers
rm -rf rt.equinox.binaries/org.eclipse.equinox.executable/{bin,contributed}/

popd

tar cJf ${NAME}-${VERSION}-clean.tar.xz ${NAME}-I${ECLIPSE_DATE}-${ECLIPSE_TIME}

popd

mv ${tmp_dir}/${NAME}-${VERSION}-clean.tar.xz .

rm -rf ${tmp_dir}
