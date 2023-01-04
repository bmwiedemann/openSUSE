#!/bin/bash

LINUX_BRANCH=rpi-6.1.y

# this is a huge hunk of stuff, so reuse the local repo if possible
if [ -d linux/.git ]; then
	set -e
	cd linux
	git remote update
	# Check we are on the right branch, otherwise clone the right one
	git checkout origin/$LINUX_BRANCH || (cd .. && (echo "ERROR: Please remove the linux folder as we cannot switch to $LINUX_BRANCH branch"; exit 1) )
	cd ..
	set +e
else
	set -e
	git clone -b $LINUX_BRANCH --depth 1 --no-single-branch https://github.com/raspberrypi/linux.git
	set +e
fi

TOPDIR=$(pwd)

# Copy device tree files
SOURCES="COPYING arch/arm/boot/dts arch/arm64/boot/dts/broadcom/*bcm27* scripts/dtc/include-prefixes/ include"
cd linux
LINE=$(git log --format=format:"%h %ci" -- ${SOURCES}|head -n 1)
set -- $LINE
REV=$1
DATE=$2
VER=${DATE//-/.}
set -e
git archive --prefix=raspberrypi-firmware-dt-$VER/ -o $TOPDIR/raspberrypi-firmware-dt-${VER}.tar HEAD -- ${SOURCES}
cd ..
osc rm -f raspberrypi-firmware-dt-*.tar.xz || true
xz --force raspberrypi-firmware-dt-${VER}.tar
osc add raspberrypi-firmware-dt-${VER}.tar.xz

sed -i "s/^Version:.*/Version:        $VER/" raspberrypi-firmware-dt.spec
osc vc raspberrypi-firmware-dt -m "Update to $REV ($DATE)"
sh pre_checkin.sh
