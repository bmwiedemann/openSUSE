#!/bin/bash

REMOVE_DIRS=( 
admin
appl
etc
kadmin
kcm
kpasswd
kuser
packages
po
tests
tools
windows
)

set -o errexit

CMDNAME=${0##*/}
SOURCEDIR=${0%$CMDNAME}

BASENAME=${1%.tar.gz}

trap "rm -rf \"$BASENAME-patched.tar\" \"$BASENAME-patched.tar.bz2\"" ERR

for (( N=0; N<${#REMOVE_DIRS[@]}; N++ )) ; do
    REMOVE_DIRS[N]="*/${REMOVE_DIRS[N]}"
done

cd "$SOURCEDIR" > /dev/null

if [ ! -f "$BASENAME.tar.gz" ]; then
    exit 0
fi

if [ -f "$BASENAME-patched.tar.bz2" ] && [ "$BASENAME.tar.gz" -ot "$BASENAME-patched.tar.bz2" ]; then
    if [ $CMDNAME -ot "$BASENAME-patched.tar.bz2" ]; then
        exit 0
    fi
fi

gzip -d "$BASENAME.tar.gz"
mv -f "$BASENAME.tar" "$BASENAME-patched.tar"
tar --wildcards --delete -f "$BASENAME-patched.tar" "${REMOVE_DIRS[@]}"
bzip2 "$BASENAME-patched.tar"
