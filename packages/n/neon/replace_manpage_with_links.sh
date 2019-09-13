#!/bin/bash

# Is this just a linked manpage?
echo "Processing $1"
grep '^\.so man\([0-7]\?\)/.*\1$' "$1" || exit 0

# extract target name
TARGET=`sed -e 's/^\.so man\([0-7]\?\)\///' "$1"`
MANDIR=`dirname "$1"`

# verify that target exists
[ -e "$MANDIR"/"$TARGET" ] || exit 1

# replace manpage reload with symlink
echo "    -> $TARGET"
rm "$1"
ln -s $TARGET "$1"

