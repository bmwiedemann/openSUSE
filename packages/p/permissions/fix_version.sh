#!/bin/sh

version=`date '+%Y%m%d'`

echo "setting version to ${version}"
sed -E -i -e "s/^%define VERSION_DATE [0-9]+/%define VERSION_DATE ${version}/" permissions.spec
