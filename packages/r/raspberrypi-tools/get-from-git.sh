#!/bin/bash

# this is a huge hunk of stuff, so reuse the local repo if possible
if [ -d tools/.git ]; then
	cd tools
	git pull -r
	cd ..
else
	set -e
	git clone --depth 1 https://github.com/raspberrypi/tools.git
	set +e
fi

TOPDIR=$(pwd)
SOURCES="armstubs/armstub8.S armstubs/Makefile"
cd tools
LINE=$(git log --format=format:"%h %ai" -- ${SOURCES}|head -n 1)
set -- $LINE
REV=$1
DATE=$2
VER=${DATE//-/.}
set -e
git archive --prefix=raspberrypi-tools-$VER/ -o $TOPDIR/raspberrypi-tools-${VER}.tar master -- ${SOURCES}
cd $TOPDIR
osc rm -f raspberrypi-tools-*.tar.bz2 || true
bzip2 --force raspberrypi-tools-${VER}.tar
osc add raspberrypi-tools-${VER}.tar.bz2
sed -i "s/^Version:.*/Version:        $VER/" raspberrypi-tools.spec;
osc vc raspberrypi-tools -m "Update to $REV ($DATE)"
osc service localrun format_spec_file
