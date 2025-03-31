#!/bin/bash

set -euo pipefail

if [ $# -gt 0 ]; then
    # launched via entrypoint.sh foo bar => execute the args
    exec "$@"
else
    # mimic what named.service does
    /usr/local/lib/bind/named.prep

    exec /usr/sbin/named -u named -fg -c "${NAMED_CONF}" ${NAMED_ARGS:+ "$NAMED_ARGS"}
fi
