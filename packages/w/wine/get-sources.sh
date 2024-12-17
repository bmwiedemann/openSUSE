#!/usr/bin/sh

set -e

if [[ -z "$1" ]]; then
echo "Please enter the version you want to update to";
exit 1;
fi

VERSION="$1"
# for the rc1 releases we translate 10.0-rc1 to 10.0~rc1 , as 10.0~x is < 10.0
REALVERSION=`echo $1|sed -e's/-/~/';`

echo "++++++++++++++++++++++++++++++++++++++++++++++"
echo "patching spec file and downloading the tarball"
echo "++++++++++++++++++++++++++++++++++++++++++++++"

sed -i -e 's|Version: .*|Version:        '${REALVERSION}'|g' wine.spec
sed -i -e 's|downloadver .*|downloadver  '${VERSION}'|g' wine.spec
osc service mr download_files
sed -i -e "s|tags/v.*<|tags/v${VERSION}<|g" _service
osc service dr

echo "++++++++++++++++++++++++++++++++++++++++++++++"
echo "Done! Have fun building and testing"
echo "++++++++++++++++++++++++++++++++++++++++++++++"
