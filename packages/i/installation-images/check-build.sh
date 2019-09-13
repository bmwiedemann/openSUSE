#!/bin/bash
# Copyright (c) 2004 SuSE Linux AG Nuernberg, Germany. All rights reserved.
#

function error {
  echo
  echo "error: $1"
  echo
  echo "build does not work on `hostname` for this package"
  exit 1
}

mkdir -vp $BUILD_ROOT/looptest || exit 1
cd $BUILD_ROOT/looptest || exit 1
pwd
#
echo "Testing if this host is ok to build this package"

grep -q loop /proc/devices || error "no loop devices"

case `uname -m` in
  i?86)
    grep -q vfat /proc/filesystems || modprobe vfat
    grep -q vfat /proc/filesystems || error "no vfat filesystem"
    ;;
esac

echo "-------------- Testing loop mount capability -----------------"
dd if=/dev/zero of=tmpfile bs=1024 count=200
echo "--------------------------------------------------------------"
mke2fs -F tmpfile
echo "--------------------------------------------------------------"
mkdir tmpdir
mount -text2 -o loop tmpfile $PWD/tmpdir
exit_code=$?
umount $PWD/tmpdir
rmdir $PWD/tmpdir
rm tmpfile
if [ $exit_code != 0 ]; then
	echo "--------------------------------------------------------------"
	error "Could not mount an ext2 fs over a loop device"
fi
echo "------------------- Testing finished -------------------------"
# Need this because check-build.sh does not have 32-bit mount available
# before setting up the chroot. Can be done at the start of %prep, but it's
# ok to just turn off all emulation builds for s390x for now:
if [ -x /usr/bin/s390x ]; then
	CURRENT_ARCH=`arch`
	KERNELARCH=`/usr/bin/s390x arch`
	if [ "$CURRENT_ARCH" != "$KERNELARCH" ]; then
		error "31-bit emulation of loop ioctls is broken, see bug 15872."
	fi
fi
echo "ok"
exit 0
