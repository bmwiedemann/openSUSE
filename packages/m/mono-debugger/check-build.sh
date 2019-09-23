#!/bin/bash
# Copyright (c) 2003, 2004 SuSE Linux AG, Germany.  All rights reserved.

# Mono needs a 2.6.13 kernel on x86-64 machines, it definitly fails with 2.6.5.
# get kernel version
OFS="$IFS" ; IFS=".-" ; version=(`uname -r`) ; IFS="$OIFS"
if test ${version[0]} -gt 2 ; then
        : # okay
elif test ${version[0]} -lt 2 -o ${version[1]} -lt 6 -o ${version[2]} -lt 13 ; then
        echo "FATAL: kernel too old, need kernel >= 2.6.13 for this package" 1>&2
        exit 1                                                                   
fi                                                                               

exit 0

