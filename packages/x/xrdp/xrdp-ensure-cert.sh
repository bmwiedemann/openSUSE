#!/bin/sh

set -eu

CERT=/etc/xrdp/cert.pem
KEY=/etc/xrdp/key.pem

if [ -s "$CERT" ] && [ -s "$KEY" ]; then
    exit 0
fi

install -d -m 0755 /etc/xrdp

HOSTNAME_FQDN=$(hostname -f 2>/dev/null || hostname)

openssl req \
    -x509 \
    -newkey rsa:2048 \
    -nodes \
    -subj "/CN=${HOSTNAME_FQDN}" \
    -keyout "$KEY" \
    -out "$CERT" \
    -days 3650

chmod 0600 "$KEY"
chmod 0644 "$CERT"

exit 0
