#!/bin/bash

# this is a huge hunk of stuff, so reuse the local repo if possible
if [ -d firmware/.git ]; then
	cd firmware
	git pull
	cd ..
else
	set -e
	git clone --depth 1 https://github.com/raspberrypi/firmware.git
	set +e
fi

TOPDIR=$(pwd)
SOURCES="README.md boot/LICENCE.broadcom boot/*.elf boot/*.bin boot/*.dat"
cd firmware
LINE=$(git log --format=format:"%h %ai" -- ${SOURCES}|head -n 1)
set -- $LINE
REV=$1
DATE=$2
VER=${DATE//-/.}
set -e
git archive --prefix=raspberrypi-firmware-$VER/ -o $TOPDIR/raspberrypi-firmware-${VER}.tar master -- ${SOURCES}
cd $TOPDIR
osc rm -f raspberrypi-firmware-*.tar.bz2 || true
bzip2 --force raspberrypi-firmware-${VER}.tar
osc add raspberrypi-firmware-${VER}.tar.bz2
for f in raspberrypi-firmware.spec raspberrypi-firmware-config.spec; do
   sed -i "s/^Version:.*/Version:        $VER/" $f
done
osc vc raspberrypi-firmware -m "Update to $REV ($DATE)"
sh pre_checkin.sh
