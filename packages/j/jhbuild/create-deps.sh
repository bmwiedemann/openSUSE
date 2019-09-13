#!/bin/bash

TARBALL=$1
MODULE=$2

tar -Oxf "$1" --wildcards */modulesets/gnome-sysdeps-${2}.modules | \
	grep -o  "<pkg-config>\(.*\)</pkg-config>" | \
	sed -e "s|</\?pkg-config>||g" \
	    -e "s|\.pc\$|)|g" \
	    -e "s|^|Requires:       pkgconfig(|g" | sort -u | \
	grep -v -e "pkgconfig(bdw-gc-threaded)" -e "pkgconfig(lttng-ust)" -e "pkgconfig(fwup)"
