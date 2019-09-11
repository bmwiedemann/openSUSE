#! /bin/bash

NAME=tesseract
svn co svn://svn.tuxfamily.org/svnroot/tesseract/main ${NAME}_
osc rm $NAME-*.tar.bz2
pushd ${NAME}_
svn export . ../$NAME
ver=`date -u +%Y_%m_%d`
ARC=$NAME-$ver.tar.xz
popd
echo "New version $ver"
sed -i "s/\(Version: \+\).\+/\1$ver/;" ${NAME}.spec
tar -cJf $ARC $NAME
rm -rf ${NAME}_ $NAME
osc add $ARC
