#!/bin/bash

exit_error()
{
	echo "$0: $@" >&2
	exit 1
}

dbg()
{
	echo "dbg: $@" >&2
}

cleanup()
{
	rm -f lt_vers.sh sonum_spec.sed
	rm -f hdf5.spec.tmp
}

## We are going to parse these variables from tarball:
# LT_VERS_INTERFACE
# LT_CXX_VERS_INTERFACE
# LT_F_VERS_INTERFACE
# LT_HL_VERS_INTERFACE
# LT_HL_CXX_VERS_INTERFACE
# LT_HL_F_VERS_INTERFACE
# LT_TOOLS_VERS_INTERFACE

cleanup

VER="$(grep -m1 "^Version:" hdf5.spec)" || exit_error "can't grep version"
read x VER <<<$VER

SRC="$(grep -m1 "^Source0:" hdf5.spec)" || exit_error "can't grep source"
read x SRC <<<$SRC
SRC=$(basename "$SRC" | sed "s/%{version}/$VER/")

test -f "$SRC" || exit_error "tarball '$SRC' does not exist"
dbg "inspecting $SRC"

tar --wildcards -x -O -f "$SRC" "*/config/lt_vers.am" \
	| tr -d ' \t' \
	| grep "^LT_.*INTERFACE=" \
	> lt_vers.sh \
	|| exit_error "can't grep interface versions"

# we expect exactly 7 variables
. lt_vers.sh || exit_error "can't source lt_vers.sh"
test $(wc -l < lt_vers.sh) -le "7" \
	|| exit_error "more than 7 vars found, update this script!"

for infix in "" _CXX _F _HL _HL_CXX _HL_F _TOOLS; do
	var="LT${infix}_VERS_INTERFACE"
	test "${!var}" -gt 0 || exit_error "$var='${!var}' bad or undefined"
	dbg "update $var=${!var}"
	def_sonum="sonum${infix}"
	# create sed scripts for spec file
	echo "s/^%define $def_sonum .*/%define $def_sonum ${!var}/" >> sonum_spec.sed
done

# update spec file if needed
sed -f sonum_spec.sed hdf5.spec > hdf5.spec.tmp
if diff -q hdf5.spec.tmp hdf5.spec &>/dev/null; then
	dbg "hdf5.spec was up-to-date"
else
	mv hdf5.spec.tmp hdf5.spec
	echo "hdf5.spec updated" >&2
fi

cleanup
