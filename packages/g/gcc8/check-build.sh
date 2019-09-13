#!/bin/bash
# Copyright (c) 2003,2005 SUSE Linux Products GmbH, Germany.  All rights reserved.
#
# Authors: Thorsten Kukuk <kukuk@suse.de>
#
# this script use the following variable(s):
# 
# - $BUILD_BASENAME
#

case $BUILD_BASENAME in
   *ppc*)
	# Our biarch 32-bit compiler needs to be build on a 64-bit machine,
	# otherwise some configure checks fail.
	# Note that we cannot use uname here since powerpc32 was invoked
	# already.
	grep 'series64\|ppc64' /proc/version > /dev/null
	if [ $? -ne 0 ] ; then
	  echo "build does not work on `hostname` for gcc"
	  exit 1
	fi
	;;
   *x86_64*)
	#if [ `ulimit -v` -le 740000 ] ; then
	#  echo "build does not work on ("`hostname`" for gcc)"
	#  exit 1
	#fi
	if [ `getconf _NPROCESSORS_CONF` -lt  2 ] ; then
	  echo "build does not work on `hostname` for gcc"
	  exit 1
	fi
   	;;
   *)
	;;
esac

exit 0

