#!/bin/bash

URL=http://svn.unix-ag.uni-kl.de/vpnc/branches/vpnc-nortel
REL=0.5.3
if [ x$1 = x-h ]; then
	echo "usage: $0 <rev>"
	echo "	check out revision 'rev' of $URL"
	echo "	and pack it as vpnc-${REL}r<rev>.tar.bz2"
	echo
	exit 0
fi

REV=""
if [ $1 ]; then
	REV="$1"
else
	REV=$(LC_ALL=C svn info $URL| awk -F": " '/^Revision: / { print $2 }')
fi

DIR=$(mktemp -d ./vpnc-download-XXXXXX)
cd $DIR
echo "exporting revision $REV..."
svn export -r $REV $URL vpnc
if [ $? != 0 ]; then
	echo "export failed? please check and cleanup $DIR afterwards..."
	exit 1
fi
tar cpjf vpnc-${REL}r${REV}.tar.bz2 vpnc
mv -i vpnc-${REL}r${REV}.tar.bz2 ../
cd ..
rm -r $DIR
