#!/bin/bash -x

# get kernel version
OFS="$IFS" ; IFS=".-" ; version=(`uname -r`) ; IFS="$OIFS"
if test ${version[0]} -gt 2 ; then
        : # okay
elif test ${version[0]} -lt 2 -o ${version[1]} -lt 6 -o ${version[2]} -lt 15 ; then
        echo "FATAL: kernel too old, need kernel >= 2.6.15 for this package" 1>&2
        exit 1                                                                   
fi                                                                               

exit 0
