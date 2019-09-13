#!/bin/bash

PATH=/sbin:/bin:/usr/sbin:/usr/bin
prog="oscap"

# Check config
test -f /etc/sysconfig/oscap-scan && . /etc/sysconfig/oscap-scan

RETVAL=0

test -f /etc/sysconfig/oscap-scan || exit 6

test x"$OPTIONS" != "x" || exit 6

$prog $OPTIONS

ERR=$?
if [ $ERR -eq 0 ] ; then
	logger "OpenSCAP security scan: PASS"
elif [ $ERR -eq 1 ] ; then
	logger "OpenSCAP security scan: ERROR. Run oscap scan from command line."
else
	logger "OpenSCAP security scan: FAILED. See results in /var/log/oscap-scan.xml.log"
fi

exit 0
