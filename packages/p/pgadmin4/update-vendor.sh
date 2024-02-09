#!/bin/bash
#
# This script updates the vendor source package.
# It should be run in the developer system in each pgadmin version update
#
# -- Antonio Larrosa <alarrosa@suse.com>
#

version=`grep ^Version: *.spec | sed -e "s/^Version: *//"`
if [ -d pgadmin4-$version ]; then
	echo "The directory pgadmin4-$version already exists. Please remove it in order to recreate it from scratch by running"
	echo "rm -Rf pgadmin4-$version"
	exit 1
fi

quilt setup pgadmin4.spec
pushd pgadmin4-$version/web
quilt push -a
# remove the last, which is fixups
quilt pop

echo "Generating new package-lock.json ..."
npm i --package-lock-only --legacy-peer-deps
mv package-lock.json ../..
popd

echo "Fetching updated dependencies ..."
osc service mr

echo "Removed old deps:"
find -maxdepth 1 -name \*.tgz -print -delete

