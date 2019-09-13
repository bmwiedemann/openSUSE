#!/bin/sh

LANG_xaos=${LANG%.UTF-8}

if [ "x$LANG" = "x$LANG_xaos" ]; then
    exec /usr/bin/xaos.bin "$@"
else
    export LANG="$LANG_xaos"
    eval `locale -k charmap`
    /usr/bin/xaos.bin "$@" | iconv -f "$charmap" -t UTF-8
fi
