#!/bin/bash
#
# Script to build VirtualBox guest kernel modules
# Copyright C 2017 by Larry Finger
#
# This script is part of the openSUSE VirtualBox package
#
SOURCE="/usr/src/kernel-modules/"
LOGFILE="/var/log/virtualbox.log"
INCLUDE="/lib/modules/`uname -r`/build/include"
#
# Test if vboxguest module loaded. If it is, skip everything else
loaded=$(lsmod | grep vboxguest)
if [ -n "$loaded" ] ; then
	echo "Kernel modules available. but we will continue..."
fi
#
# Check if virtualbox-guest-source is installed, quit if not
if ! rpm -qf "$SOURCE/additions/guest_src.tar.bz2" &>/dev/null ; then
	echo "Sources for building guest modules are not present,"
	echo "Use 'sudo zypper install virtualbox-guest-source' to install them. Quitting .."
	exit 1
fi
# unpack source
pushd $SOURCE > /dev/null 2>&1
tar jxf additions/guest_src.tar.bz2 > /dev/null 2>&1
popd > /dev/null 2>&1
#
# Check if virtualbox-guest-source version matches virtualbox version
if [ "$(rpm -q virtualbox virtualbox-guest-source --queryformat='%{version}-%{release}\n' 2>/dev/null | sort -u | wc -l)" -ne "1" ] ; then
	echo "virtualbox-guest-source package version doesn't match the version of virtualbox package."
	echo "This situation is probably not fatal, thus we will try to continue .."
fi
# Prerequisites are available, start build
pushd $SOURCE/additions/src > /dev/null 2>&1
echo "Building kernel modules..."
make > $LOGFILE 2>&1
if [ "$?" -ne 0 ] ; then
	echo ""
	echo "Build of VirtualBox guest kernel modules failed."
	echo "Look at $LOGFILE to find reasons."
	popd > /dev/null 2>&1
	exit 1
else
echo "Kernel modules built correctly. They will now be installed."
fi
make install >> $LOGFILE 2>&1
if [ "$?" -ne 0 ] ; then
	echo ""
	echo "Installation of VirtualBox guest kernel modules failed."
	echo "Look at $LOGFILE to find reasons."
	popd > /dev/null 2>&1
	exit 1
fi
depmod -a
modprobe -av vboxsf vboxguest vboxvideo
cd ../..
rm -rf additions
popd > /dev/null 2>&1
echo "Kernel modules are installed and loaded."
exit 0

