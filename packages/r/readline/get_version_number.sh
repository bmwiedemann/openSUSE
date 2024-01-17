#!/bin/bash
# Note: this file is used in the spec file, do not remove it
# Print the highest version number of the patches from the archive
sourcedir=$1
test -n "${sourcedir}" || sourcedir=$PWD
test -e ${sourcedir}/readline.spec  || exit 1
version=$(sed -rn '/^%define[[:space:]]+rversion/{s/^%define[[:space:]]+rversion[[:space:]]+([0-9]+\.[0-9]+)(\.[^\.]+)?/\1/p}' ${sourcedir}/readline.spec) || exit 1
test -e ${sourcedir}/readline-${version}.tar.gz || exit 1
last=($(tar Oxf ${sourcedir}/readline-${version}.tar.gz readline-${version}/configure.ac | sed -rn '/^LIBVERSION/{s/LIBVERSION=//p}')) || exit 1
for p in ${sourcedir}/readline${last//\./}-*[0-9]
do
    level=${p##*-}
done
shopt -s extglob
echo ${level##+(0)}
