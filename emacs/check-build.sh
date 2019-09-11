#!/bin/bash
case $BUILD_BASENAME in
   *ppc*)
        if test $(getconf PAGESIZE) -ne 65536; then
            echo "Error: wrong build host, PAGESIZE must be 65536"
	    exit 1
        fi
	;;
   *ia64*)
        if test $(getconf PAGESIZE) -ne 65536; then
            echo "Error: wrong build host, PAGESIZE must be 65536"
	    exit 1
        fi
	;;
   *)
	;;
esac

exec_shield=0
if test -e /proc/sys/kernel/exec-shield; then
	read -t 1 exec_shield < /proc/sys/kernel/exec-shield
fi
if test $exec_shield -ne 0 ; then
	echo Sorry, Execution Shield exists and is enabled 1>&2
	exit 1
fi
exit 0

