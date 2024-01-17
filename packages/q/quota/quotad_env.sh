#!/bin/sh

. /etc/sysconfig/nfs

if [ -n "${RQUOTAD_PORT}" ]; then
   RQUOTAD_PORT="-p ${RQUOTAD_PORT}"
fi

mkdir -p /run/sysconfig
echo "RQUOTAD_ARGS=\"${RQUOTAD_PORT}\"" > /run/sysconfig/quotad

