#!/bin/bash

REMOVE_OBJECTS=(\
    extern_libs vid_enc_avi vid_enc_ffmpeg gap/gap_mpege.c gap/gap_mpege.h\
    libgapvidapi/gap_vid_api_ffmpeg.c libgapvidapi/gap_vid_api_mpeg3.c\
    libgapvidapi/gap_vid_api_mpeg3toc.c )

set -o errexit

CMDNAME=${0##*/}
SOURCEDIR=${0%$CMDNAME}

BASENAME=${1%.tar.bz2}

trap "rm -rf  \"$BASENAME-patched.tar\" \"$BASENAME-patched.tar.bz2\"" ERR

for (( N=0 ; N<${#REMOVE_OBJECTS[@]} ; N++ )) ; do
    REMOVE_OBJECTS[N]="$BASENAME/${REMOVE_OBJECTS[N]}"
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
tar --delete -f "$BASENAME-patched.tar" "${REMOVE_OBJECTS[@]}"
bzip2 "$BASENAME-patched.tar"
