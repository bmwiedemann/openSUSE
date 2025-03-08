#!/bin/sh

cd /usr/share/lua-language-server/ || exit 1

TMPPATH="/tmp/lua-language-server-$(id -u)"
install -dm0700 "${TMPPATH}"
INSTANCEPATH="$(mktemp -d "${TMPPATH}/instance-XXXXXX")"
DEFAULT_LOGPATH="${INSTANCEPATH}/log"
DEFAULT_METAPATH="${INSTANCEPATH}/meta"

exec @LIBEXECDIR@/lua-language-server/lua-language-server \
    -E ./main.lua \
    --logpath="${DEFAULT_LOGPATH}" \
    --metapath="${DEFAULT_METAPATH}" \
    "$@"
