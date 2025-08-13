#!/bin/bash
# Note: this file is used in the spec file, do not remove it
# Print the highest version number of the patches from the archive
sourcedir=$1
test -n "${sourcedir}" || sourcedir=$PWD
test -e ${sourcedir}/bash.spec  || exit 1
version=$(sed -rn '/^%define[[:space:]]+bversion/{s/^%define[[:space:]]+bversion[[:space:]]+([0-9]+\.[0-9]+)(\.[^\.]+)?/\1/p}' ${sourcedir}/bash.spec) || exit 1
beta=$(sed -rn '/^%define[[:space:]]+bextend/{s/^%define[[:space:]]+bextend[[:space:]]+([^[:space:]])?/\1/p}' ${sourcedir}/bash.spec) || exit 1
test "$beta" = "%{nil}" && beta="" || version=${version}${beta}
test -e ${sourcedir}/bash-${version}.tar.gz || exit 1
last=($(tar Oxf ${sourcedir}/bash-${version}.tar.gz bash-${version}/configure.ac | sed -rn '/^define.bashvers/{s/^define\(bashvers,[[:space:]]([0-9\.]+)\)/\1/p}')) || exit 1
tar --wildcards -tf ${sourcedir}/bash-${version}-patches.tar.bz2 '*/bash[0-9][0-9]-*[0-9]' &> /dev/null || { echo 0 ; exit; }
OFS="$IFS"
IFS=-
last=($(tar --wildcards -tf ${sourcedir}/bash-${version}-patches.tar.bz2 '*/bash[0-9][0-9]-*[0-9]' | sed -r 's@\.patch$@@'| sort -t '-' -k 3,3 -n | tail -n 1))
IFS="$OFS"
shopt -s extglob
echo ${last[3]##+(0)}
