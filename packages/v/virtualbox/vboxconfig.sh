#!/bin/bash
#
# Script to build VirtualBox host kernel modules
# Copyright C 2017 by Larry Finger
#
# This script is part of the openSUSE VirtualBox package
#
SOURCE="/usr/src/kernel-modules/virtualbox/src"
LOGFILE="/var/log/virtualbox.log"
INCLUDE="/lib/modules/`uname -r`/build/include"
#
# Test if vboxpci module loaded. If it is, skip everything else
loaded=$(lsmod | grep vboxpci)
if [ -n "$loaded" ] ; then
	echo "Kernel modules are loaded, unload them via"
	echo "systemctl stop vboxdrv.service if you wish to rebuild them."
	echo "Quitting .."
	exit 1
fi
#
# Check if virtualbox-host-source is installed, quit if not
if ! rpm -qf "$SOURCE/Makefile" &>/dev/null ; then
	echo "Sources for building host modules are not present,"
	echo "Use 'sudo zypper install virtualbox-host-source kernel-devel kernel-default-devel' to install them. Quitting .."
	exit 1
fi
#
# Check if virtualbox-host-source version matches virtualbox version
if [ "$(rpm -q virtualbox virtualbox-host-source --queryformat='%{version}-%{release}\n' 2>/dev/null | sort -u | wc -l)" -ne "1" ] ; then
	echo "virtualbox-host-source package version doesn't match the version of virtualbox package."
	echo "This situation is probably not fatal, thus we will try to continue .."
fi
# Prerequisites are available, start build
pushd $SOURCE > /dev/null 2>&1
echo "Building kernel modules..."
make clean &>/dev/null
make > $LOGFILE 2>&1
if [ "$?" -ne 0 ] ; then
	echo ""
	echo "Build of VirtualBox host kernel modules failed."
	echo "Look at $LOGFILE to find reasons."
	popd > /dev/null 2>&1
	exit 1
else
echo "Kernel modules built correctly. They will now be installed."
fi
make install >> $LOGFILE 2>&1
if [ "$?" -ne 0 ] ; then
	echo ""
	echo "Installation of VirtualBox host kernel modules failed."
	echo "Look at $LOGFILE to find reasons."
	popd > /dev/null 2>&1
	exit 1
fi
depmod -a
modprobe -av vboxnetflt vboxnetadp vboxpci
popd > /dev/null 2>&1
echo "Kernel modules are installed and loaded."
exit 0

