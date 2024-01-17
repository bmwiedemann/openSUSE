#!/bin/bash

# Autobuild doesn't support package names with macros. This script will update versions in package names.

# Usage: Automatically called from spec file by:
# libwnck2_spec-update.sh DIR BASE_NAME libnames...

if ! test -f $1/$2.spec ; then
    exit
fi
BASE=$1/$2
shift 2

for PKGNAME in $@ ; do
    # Packages with name ending by number needs separator
    if test x`echo $PKGNAME | sed "s/.*[0-9]$//"` = x ; then
	SEPARATOR=-
    else
	SEPARATOR=
    fi
    sed -i "
	# Copy ${PKGNAME}_name to hold space
	/^%define ${PKGNAME}_name / {
	    h;
	    s/^%define ${PKGNAME}_name //;
	    x;
	};

	# Update ${PKGNAME}_name everywhere
	/$PKGNAME$SEPARATOR[0-9][-_0-9]*/ {
	    G;
	    s/$PKGNAME$SEPARATOR[0-9][-_0-9]*\(.*\)\n\(.*\)/$PKGNAME$SEPARATOR\2\1/;
	};" $BASE.spec
done
