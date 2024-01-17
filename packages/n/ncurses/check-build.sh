#!/bin/bash -e
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# This script use the following variable(s):
# 
# - $BUILD_BASENAME
#

: ${BUILD_BASENAME:=$(uname -m)}

kernel_version()
{
    echo $((($1<<16)+($2<<8)+($3)))
}
kernel_string()
{
    echo $((($1>>16)&0xff)).$((($1>>8)&0xff)).$(($1&0xff))
}

typeset -i major minor level version required
IFS=' .-' read -t 10 name dummy major minor level rest < /proc/version || exit 1
let version=$(((major<<16)+(minor<<8)+(level)))
unset name dummy major minor level rest

case "$BUILD_BASENAME" in
   *x86_64*) let required=$(kernel_version 2 6 32) ;;	# gcc exception 32
   *)	     let required=$(kernel_version 2 6 16) ;;
esac

if ((version<required)) ; then
    echo "FATAL: kernel too old, need kernel >= $(kernel_string required) for this package" 1>&2
    exit 1
fi

#
# Success
#
exit 0
