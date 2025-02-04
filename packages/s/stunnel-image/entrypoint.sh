#!/bin/bash

set -eo pipefail

STUNNEL_CERT="${STUNNEL_CERT:-/etc/stunnel/stunnel.pem}"
STUNNEL_KEY="${STUNNEL_KEY:-/etc/stunnel/stunnel.key}"

if [[ -n ${STUNNEL_DEBUG} ]]; then
    echo "debug = ${STUNNEL_DEBUG}" > /etc/stunnel/conf.d/000debug.conf
fi

conf="/etc/stunnel/conf.d/container-ssl.conf"
echo "cert = ${STUNNEL_CERT}" > $conf
echo "key = ${STUNNEL_KEY}" >> $conf


if [[ -n "${STUNNEL_SERVICE_NAME}" ]] && [[ -n "${STUNNEL_ACCEPT}" ]] && [[ -n "${STUNNEL_CONNECT}" ]]; then
    conf="/etc/stunnel/conf.d/container.conf"
    echo "[${STUNNEL_SERVICE_NAME}]" > $conf
    echo "accept = ${STUNNEL_ACCEPT}" >> $conf
    echo "connect = ${STUNNEL_CONNECT}" >> $conf
fi

exec "$@"
