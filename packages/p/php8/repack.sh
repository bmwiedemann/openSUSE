#!/bin/sh
version=$(grep '^Version:' php8.spec | sed 's/Version:\s*\([0-9\.]\+\).*/\1/')
if [ -d php-$version ]; then
  echo "php-$version exists, please remove it"
  exit 1
fi
echo
echo Verifying archive
wget https://secure.php.net/distributions/php-$version.tar.xz.asc
gpg --verify php-$version.tar.xz.asc php-$version.tar.xz
rm php-$version.tar.xz.asc
echo
echo Extracting original archive
tar -xf php-$version.tar.xz
echo
echo Patching unicode files
pushd php-*/
# will fail as the issue is fixed
patch -p1 < ../php-unicode-allow-redistribution.patch
popd
echo
echo Creating repacked archive
tar -cJf php-$version.tar.xz php-$version
echo
echo Done
