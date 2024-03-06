#!/bin/sh
# Prepare go and node languages used for packaging
# Author: jweberhofer@weberhofer.at
#

echo "Preparing sources for packaging"

if  [ -z `which osc` ] ; then
	echo 'osc must be installed!'
	exit 1;
fi
if  [ -z `which yarn` ] ; then
	echo 'yarn must be installed!'
	exit 1;
fi
if  [ -z `which npm` ] ; then
	echo 'npm must be installed!'
	exit 1;
fi

# download sources from github, package and create the vendor-package
osc service runall download_files
if [ "$?" -ne 0 ] ; then
	exit 1
fi

# create package-lock for packaging offline node_modules
VERSION=`grep '^Version:[\t ]*' traefik.spec | sed -e 's/^[^0-9]*// ; s/[ \t]*$//'`
tar -xzf "traefik-$VERSION.tar.gz"
pushd "traefik-$VERSION/webui"
if [ "$?" -ne 0 ] ; then
	exit 1
fi
npm install --package-lock-only --legacy-peer-deps --ignore-scripts
if [ "$?" -ne 0 ] ; then
	exit 1
fi
mv package-lock.json ../../
popd

# create the offline packages
osc service manualrun

# remove unnecessary file
if [ -e 'node_modules.sums' ] ; then
	rm 'node_modules.sums'
fi
