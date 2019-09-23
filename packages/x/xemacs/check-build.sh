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

exit 0

