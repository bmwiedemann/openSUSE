#!/bin/bash

# This program searches for all active translations in the distro and
# does dumb guesses of project - domain relations.
#
# It needs access to distro RPMs.
#
set -o errexit

source ${0%create-tlst-step1-list-all-po-projects.sh}create-tlst.conf

for i in $BINARY_REPO/{$BINARY_ARCH,noarch}/*.rpm ; do rpm -q --queryformat=%{name} -p $i ; echo : ; rpm -qlp $i | grep LC_MESSAGES || : ; done |
	sed "s~^$BINARY_REPO/($BINARY_ARCH|noarch)~~" >create-tlst-temp-all-po-files.lst

cat create-tlst-temp-all-po-files.lst |
sed '
/:$/ {
    h
    d
}
/LC_MESSAGES$/d
s:.*/LC_MESSAGES/::
/.*/ {
    G
    s/\(.*\)\.mo\n\(.*\):/\2 \1/
}
/kde3-i18n/d
' |
uniq |
LC_COLLATE=C LC_ALL= sort -u >create-tlst-temp-all-po-projects.lst

rm create-tlst-temp-all-po-files.lst
