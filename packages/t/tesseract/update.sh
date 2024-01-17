#! /bin/bash
tput setaf 9
echo This script downloads source code via unencrypted svn://.
echo Unfortunately upstream does not provide a secure download as of today.
echo Please check if this has changed, and switch to https:// if possible.
echo
tput sgr0
echo Press enter to proceed.
read

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
