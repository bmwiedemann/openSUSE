#!/bin/sh -x

#This script is used to create netpbm-$VER-nohpcdtoppm-nojbig.tar.bz2
#from upstream svn, http://sourceforge.net/projects/netpbm/


rm -rf REMOVE
mkdir REMOVE
cd REMOVE
svn checkout https://svn.code.sf.net/p/netpbm/code/advanced/ netpbm
VER=`echo \`cut -f2 -d= netpbm*/version.mk \`|sed -e "s| |.|g"`
mv netpbm* netpbm-$VER

find . -name ".svn" -exec rm -rf {} \;

cd netpbm*/converter/ppm/hpcdtoppm || exit 1
rm -rf *
echo all: >> Makefile
echo install.bin: >> Makefile
echo install.man: >> Makefile
echo install.data: >> Makefile
echo clean: >> Makefile
cd ../../../..

cd netpbm*/converter/ppm/ppmtompeg || exit 1
rm -rf *
echo all: >> Makefile
echo install.bin: >> Makefile
echo install.man: >> Makefile
echo install.data: >> Makefile
echo clean: >> Makefile
cd ../../../..

tar cjf ../netpbm-$VER-nohpcdtoppm-noppmtompeg.tar.bz2 *

wget -m netpbm.sourceforge.net
tar cjf ../netpbm-$VER-documentation.tar.bz2 netpbm.sourceforge.net

