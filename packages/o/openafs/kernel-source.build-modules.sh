#!/bin/bash

if [ $# != 1 ]; then
    echo building a openafs-kernel module for the running kernel
    echo Need one of: build build_debug install
    exit 1
fi

rootdir=`cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd`

if [ -z "$rootdir" ]; then
    echo "failed to determine the dirname of this script"
    exit 1
fi

cd "$rootdir"

LOGFILE=libafs_tree/build.log
kernel_flavour=`uname -r | awk -F- '{print $NF}'`
kernel_version=`uname -r | sed "s/-$kernel_flavour//"`
arch=`uname -m`

suse_flavour=`cat /etc/os-release | grep PRETTY_NAME | awk -F '=' '{print $2}'`
suse_version=`cat /etc/os-release | grep VERSION_ID | awk -F '=' '{print $2}'`

echo This SUSE is version $suse_version of flavour $suse_flavour
echo you are running the kernel \"$kernel_version\" of flavour \"$kernel_flavour\" on \"$arch\"
echo all output is saved into $LOGFILE

if [ $1 == "build_debug" ]; then
   DEBUG_OPT="--enable-debug-kernel"
fi

if [ $1 == "build" -o $1 == "build_debug" ]; then
   cd libafs_tree
   echo calling configure...
   ./configure --with-linux-kernel-headers=/usr/src/linux/ --with-linux-kernel-build=/usr/src/linux-obj/$arch/$kernel_flavour $DEBUG_OPT > build.log 2>&1
   if [ $? != 0 ]; then
       echo configure failed! See $LOGFILE for details
       exit $?
   fi
   echo calling make
   make >> build.log 2>&1
   if [ $? != 0 ]; then
       echo make failed! See $LOGFILE for details
       exit $?
   fi
   echo
   echo build sucessfull!
   echo Now run $0 install to install the kernel-modules
   exit 0
fi


if [ $1 == "install" ]; then
   module_files="afspag.ko libafs.ko"
   build_dir=libafs_tree/src/libafs/MODLOAD-$kernel_version-$kernel_flavour-MP/
   install_dir=/lib/modules/$kernel_version-$kernel_flavour
   echo installing kernel-modules into
   for mod in $module_files; do
      cp -v $build_dir/$mod $install_dir/$mod
   done
   /sbin/depmod -a
fi
