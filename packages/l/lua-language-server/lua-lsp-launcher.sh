#!/bin/sh

cd /usr/share/lua-language-server/ || exit 1

TMPPATH=$(mktemp -d "/tmp/lua-language-server.XXXX")
DEFAULT_LOGPATH="${TMPPATH}/log"
DEFAULT_METAPATH="${TMPPATH}/meta"

exec @LIBEXECDIR@/lua-language-server/lua-language-server \
    -E ./main.lua \
    --logpath="${DEFAULT_LOGPATH}" \
    --metapath="${DEFAULT_METAPATH}" \
    "$@"
