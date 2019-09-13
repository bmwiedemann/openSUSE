#!/bin/bash

CERTIFICATE_PATH=/etc/sfcb/clist.pem

# Fetch certificate path from the config file.
CONFIG_PATH=`grep '^sslCertificateFilePath:' /etc/sfcb/sfcb.cfg | sed -e 's,sslCertificateFilePath:\\s*,,'`

if [ 'x'$CONFIG_PATH != 'x' ]; then
    CERTIFICATE_PATH=$CONFIG_PATH
fi

# Exit early if server certificate exists
if [ -e $CERTIFICATE_PATH ]; then
    exit 0
fi

# Generate server certificates
D=`dirname $CERTIFICATE_PATH`
exec /usr/share/sfcb/genSslCert.sh $D

