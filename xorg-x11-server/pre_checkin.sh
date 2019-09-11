#!/bin/sh
# pre_checking.sh
# Licensed under the same condition as the xorg-server.
# This script updates the .spec file (based on .spec.in) and inject versioned ABI Symbols from the X-Server,
# stored in a template file xorg-server-provides. The content of this file is verified during build, as the
# same script runs then again, extracting ABI versions from the source to be built. This ensures we can't
# publish a package with wrong ABI Versions being provided as part of the RPM Metadata.
# Driver-, Input and extension-packages are supposed to use the provided macros to ensure correct Requires.

# extract ABI Versions... this function is copied from configure.ac
extract_abi() {
  grep ^.define.*${1}_VERSION ${xorg_src}/hw/xfree86/common/xf86Module.h | tr '(),' '  .' | awk '{ print $4$5 }'
}

if [ "$1" == "--tar" ]; then
	tmpdir=$(mktemp -d)
	tar xf "$2" -C ${tmpdir}
	xorg_src=${tmpdir}/*
elif [ "$1" == "--verify" ]; then
	xorg_src="$2"
	prv_ext=".build"
else
	echo "Wrong usage of this script"
	echo "$0 can be started in two ways:"
	echo "1: $0 --tar {xorg-server-xxxx.tar.bz2}"
	echo "2: $0 --verify {source-folder}"
	echo "Variant 1 creates the file xorg-server-provides to be included in the src rpm"
	echo "Variant 2 is being called during build to ensure the ABI provides match the expectations."
	echo ""
	echo ""
	echo "Trying to guess the right tarball"
	sh $0 --tar xorg-server-*.tar.bz2
	echo "... Please verify if the result makes sense"
	exit 2
fi

abi_ansic=`extract_abi ANSIC`
abi_videodrv=`extract_abi VIDEODRV`
abi_xinput=`extract_abi XINPUT`
abi_extension=`extract_abi EXTENSION`

A="Provides:       X11_ABI_XINPUT = ${abi_xinput}\nProvides:       X11_ABI_VIDEODRV = ${abi_videodrv}\nProvides:       X11_ABI_ANSIC = ${abi_ansic}\nProvides:       X11_ABI_EXTENSION = ${abi_extension}"

echo -e $A > xorg-server-provides${prv_ext}

if [ "$1" == "--tar" ]; then
	if [ -d ${tmpdir} ]; then
		rm -rf ${tmpdir}
	fi
elif [ "$1" == "--verify" ]; then
	diff "$3" xorg-server-provides${prv_ext}
        if [ $? -gt 0 ]; then
		echo "The ABI verification failed... please run $0 before checking in"
		exit 1
	fi
fi

