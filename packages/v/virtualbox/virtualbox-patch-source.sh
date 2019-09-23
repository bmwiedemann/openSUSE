#!/bin/bash

REMOVE_DIRS=( 
src/VBox/Additions/WINNT 
src/VBox/Additions/os2 
kBuild/bin
kBuild/msgstyles
kBuild/tools
kBuild/sdks
tools/darwin.x86
tools/darwin.amd64
tools/freebsd.x86
tools/os2.x86
tools/solaris.x86
tools/solaris.amd64
tools/win.amd64
tools/win.x86
tools/linux.x86
tools/linux.amd64
)

set -o errexit

CMDNAME=${0##*/}
SOURCEDIR=${0%$CMDNAME}

BASENAME=${1%.tar.bz2}

trap "rm -rf  \"$BASENAME-patched.tar\" \"$BASENAME-patched.tar.bz2\"" ERR

for (( N=0 ; N<${#REMOVE_DIRS[@]} ; N++ )) ; do
    #REMOVE_DIRS[N]="$BASENAME/${REMOVE_DIRS[N]}"
    # use a wildcard because VirtualBox-1.6.0-OSE != VirtualBox-1.6.0_OSE
    REMOVE_DIRS[N]="*/${REMOVE_DIRS[N]}"
done

cd "$SOURCEDIR" >/dev/null

if ! test -f "$BASENAME.tar.bz2" ; then
    exit 0
fi

if test -f "$BASENAME-patched.tar.bz2" ; then
    if test "$BASENAME.tar.bz2" -ot "$BASENAME-patched.tar.bz2" ; then
	if test $CMDNAME -ot "$BASENAME-patched.tar.bz2" ; then
	    exit 0
	fi
    fi
fi

cp -a "$BASENAME.tar.bz2" "$BASENAME-patched.tar.bz2"
bunzip2 "$BASENAME-patched.tar.bz2"
tar --wildcards --delete -f "$BASENAME-patched.tar" "${REMOVE_DIRS[@]}"
bzip2 "$BASENAME-patched.tar"
