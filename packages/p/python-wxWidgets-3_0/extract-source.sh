#!/bin/bash

# Upstream wxPython-src contain complete wxWidgets sources plus several
# legally questionable files.  That is why we repackage it here.

set -x

REMOVE_DIRS=(contrib/samples/applet/monitors.c "wxPython/distrib/msw/*.DLL"
	"wxPython/distrib/msw/*.dll")

set -o errexit

CMDNAME="${0##*/}"
SOURCEDIR="${0%$CMDNAME}"
if [ -z "$SOURCEDIR" -o "$SOURCEDIR" = "$0" ]; then
	SOURCEDIR="$PWD"
fi

BASENAME="${1%.tar.bz2}"
NEWNAME="${BASENAME/-src/}.tar.xz"

if ! test -f "$1"; then
	exit 0
fi
if test -f "$NEWNAME"; then
	if test "$1" -ot "$NEWNAME"; then
		if test "$CMDNAME" -ot "$NEWNAME"; then
			exit 0
		fi
	fi
fi

cd "$SOURCEDIR"
trap 'cd ..; rm -Rf "$PWD/tmp$$.python-wxWidgets-extract-source"' ERR
rm -rf "tmp$$.python-wxWidgets-extract-source"
mkdir "tmp$$.python-wxWidgets-extract-source"
pushd "tmp$$.python-wxWidgets-extract-source/"
tar -xf "../$1"
pushd "$BASENAME/"

eval rm -Rf "${REMOVE_DIRS[@]}"

# wxpython now requires private headers that are not installed in the wxWidgets installation:
mv include/wx/* wxPython/include/wx/
if ! rmdir include/wx; then
	ls -l include/wx/
fi
if ! rmdir include; then
	ls -l include/
fi
rm -Rf include

for ITEM in *; do
	case "$ITEM" in
	wxPython|docs) continue;;
	*) rm -Rf "$ITEM";;
	esac
done

popd
tar -Jcf "../$NEWNAME" "$BASENAME"
popd
rm -Rf "tmp$$.python-wxWidgets-extract-source"
