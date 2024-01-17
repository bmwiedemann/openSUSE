#!/bin/bash
# Note: this file is used in the spec file, do not remove it
sourcedir=$1
test -n "${sourcedir}" || sourcedir=$PWD
test -e ${sourcedir}/ncurses.spec  || exit 1
version=$(sed -rn '/^Version:[[:space:]]+/{s/^Version:[[:space:]]+([0-9]+\.[0-9]+)(\.[^\.]+)?/\1/p}' ${sourcedir}/ncurses.spec) || exit 1
test -e ${sourcedir}/ncurses-${version}.tar.gz || exit 1
last=($(tar Oxf ${sourcedir}/ncurses-${version}.tar.gz ncurses-${version}/VERSION)) || exit 1
test -e ${sourcedir}/ncurses-${version}-patches.tar.bz2 || echo ${last[2]}
tar --wildcards -tf ${sourcedir}/ncurses-${version}-patches.tar.bz2 '*/*.patch' &> /dev/null || echo ${last[2]}
OFS="$IFS"
IFS=-
last=($(tar -tf ${sourcedir}/ncurses-${version}-patches.tar.bz2 | grep -v 'gz.asc' | sed -r 's@\.patch$@@'| sort -t '-' -k 3,3 -n | tail -n 1))
IFS="$OFS"
echo ${last[2]}
