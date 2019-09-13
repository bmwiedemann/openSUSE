#!/bin/sh

MODULE=$(basename $(pwd))

if [ ! -x /usr/bin/svn ]; then
  echo "subversion is missing - aborting"
  exit 1
fi

if [ ! -d $MODULE ]; then
  echo "Base directory of $MODULE checkout is missing - aborting"
  exit 2
fi

pushd $MODULE
svn update
VERSION=$(grep "version" $MODULE/CMakeLists.txt | awk -F'(' '{print $2}' | awk '{print $1+0"."$2+0"."$3+0}')
SVNREV=$(svn info | awk '/Revision:/ { print $2 }')
popd

# Adjust the version information and svn rev in the spec file to what we get from the svn checkout.
sed -i "s/Version:.*/Version:        ${VERSION}.svn.$SVNREV/" $MODULE.spec

tar cjf $MODULE.tar.bz2 $MODULE

[ -f pre_checkin.sh ] && sh pre_checkin.sh

osc ci -m "Update to ${VERSION/git/svn.$SVNREV}" --skip-validation
