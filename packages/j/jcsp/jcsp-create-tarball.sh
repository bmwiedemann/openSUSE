#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: ./create-sources VERSION"
    exit 1
fi

VERSION=${1}
NAME="jcsp"

wget https://github.com/codehaus/${NAME}/archive/${VERSION}.tar.gz
tar -xf ${VERSION}.tar.gz
rm ${VERSION}.tar.gz
find ./${NAME}-${VERSION} -name "*.jar" -delete
find ./${NAME}-${VERSION} -name "*.class" -delete
# Remove unused files
rm -Rf ./${NAME}-${VERSION}/*gradle*
rm -Rf ./${NAME}-${VERSION}/wrapper
rm -Rf ./${NAME}-${VERSION}/.gitignore
rm -Rf ./${NAME}-${VERSION}/src/jcsp-demos 
rm -Rf ./${NAME}-${VERSION}/src/org/jcsp/win32/Installing\ NT\ Services.txt
rm -Rf ./${NAME}-${VERSION}/src/org/jcsp/win32/*.c*
rm -Rf ./${NAME}-${VERSION}/src/org/jcsp/win32/*.h*
rm -Rf ./${NAME}-${VERSION}/JCSP\ Networking.pdf

tar cJf ${NAME}-${VERSION}-clean.tar.xz ./${NAME}-${VERSION}