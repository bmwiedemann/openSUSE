#!/bin/bash

# Autobuild doesn't support package names with macros. This script will update versions in package names.

ORIG_SPEC=${2%-utils}
# Never update -utils fíle when it is already opened. It will break advanced build scripts:
if test "$2" != "$ORIG_SPEC" ; then
    exit
fi

if ! test -f $1/$ORIG_SPEC.spec ; then
    exit
fi

# Edit file to fit -utils build needs:
sed '
    s/BUILD_UTILS\ 0/BUILD_UTILS 1/;
    s/BUILD_CORE\ 1/BUILD_CORE 0/;
    s/^.ame:.*/&-utils/;
    # No more needed.
    #s/^..hangelog.*/& utils/;
    s/^\(# WARNING:\).*After editing.*/\1 Do not edit this auto generated file./
' <$1/$ORIG_SPEC.spec >$1/$ORIG_SPEC-utils.spec

cp -a $1/$ORIG_SPEC.changes $1/$ORIG_SPEC-utils.changes
