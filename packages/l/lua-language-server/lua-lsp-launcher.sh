#!/bin/sh

cd /usr/share/lua-language-server/ || exit 1

TMPPATH=$(mktemp -d "/tmp/lua-language-server-$(id -u)")
INSTANCEPATH="${mktemp -d $TMPPATH/instance-.XXXXXX"}"
DEFAULT_LOGPATH="${INSTANCEPATH}/log"
DEFAULT_METAPATH="${INSTANCEPATH}/meta"

exec @LIBEXECDIR@/lua-language-server/lua-language-server \
    -E ./main.lua \
    --logpath="${DEFAULT_LOGPATH}" \
    --metapath="${DEFAULT_METAPATH}" \
    "$@"
