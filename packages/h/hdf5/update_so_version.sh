#!/bin/bash

exit_error()
{
	echo "$0: $@" >&2
	exit 1
}

cleanup()
{
    rm -f ${spectmp}
    rm -f ${shtmp}
}

## We are going to parse these variables from tarball:
# LT_VERS_INTERFACE
# LT_CXX_VERS_INTERFACE
# LT_F_VERS_INTERFACE
# LT_HL_VERS_INTERFACE
# LT_HL_CXX_VERS_INTERFACE
# LT_HL_F_VERS_INTERFACE

cleanup

spectmp=$(mktemp hdf-XXXX.spec)
shtmp=$(mktemp lt-XXXX.sh)
outtmp=$(mktemp so-XXXX)
sed -e "s/@BUILD_FLAVOR@/standard/" hdf5.spec > ${spectmp}
VER="$(rpmspec --define "_sourcedir $(pwd)" -P ${spectmp} | grep -m1 "^Version:")" || \
    exit_error "can't grep version"
read x VER <<<$VER

SRC="$(rpmspec --define "_sourcedir $(pwd)" -P ${spectmp} | grep -m1 "^Source0:")" || \
    exit_error "can't grep source"
read x SRC <<<$SRC
SRC=$(basename "$SRC" | sed "s/%{version}/$VER/")

test -f "$SRC" || exit_error "tarball '$SRC' does not exist"

tar --wildcards -x -O -f "$SRC" "*/config/lt_vers.am" \
	| tr -d ' \t' \
	| grep -E "^LT_.*INTERFACE=|^LT_.*AGE=" \
	> ${shtmp} \
	|| exit_error "can't grep interface versions"

source ./${shtmp} || exit_error "can't source ${shtmp}"

for infix in "" _CXX _F _HL _HL_CXX _HL_F; do
	current="LT${infix}_VERS_INTERFACE"
	age="LT${infix}_VERS_AGE"
	currv=$(eval "echo \$$current")
	agev=$(eval "echo \$$age")
	if [ -n "$currv" -a -n "$agev" ]; then
	    echo %define sonum${infix} $((currv - agev)) >> ${outtmp}
	else
	    rm -f ${outtmp}
	    cleanup
	    exit 1
	fi
done

[ -e ${outtmp} ] && mv ${outtmp} so_versions
  
cleanup
