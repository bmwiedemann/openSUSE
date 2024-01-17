#!/bin/bash
#
# Copyright (c) 2006 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# This script use the following variable(s):
# 
# - $BUILD_BASENAME
#

case $BUILD_BASENAME in
   *ia64)
	read -t 10 name dummy version rest < /proc/version
	if test -z "$version" ; then
	    echo "FATAL: can not read /proc/version" 1>&2
	    exit 1
	fi
	OIFS="$IFS"
	IFS='.-'
	version=($version)
	IFS="$OIFS"
	if test ${version[0]} -lt 2 -o ${version[1]} -lt 6 -o ${version[2]} -lt 16 ; then
	    echo "FATAL: kernel too old, need kernel >= 2.6.16 for this package" 1>&2
	    exit 1
	fi
	;;
   *)
	;;
esac

#
# XEN kernel may use different stack addresse range
#
if test -e /proc/xen; then 
     echo "FATAL: kernel contains xen support!" 1>&2
     exit 1
fi

#
# Success
#
exit 0
