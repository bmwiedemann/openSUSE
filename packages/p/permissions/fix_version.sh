#!/bin/sh

version=`date '+%Y%m%d'`

echo "setting version to ${version}"
sed -E -i -e "s/^%define VERSION [0-9]+/%define VERSION ${version}/" permissions.spec
