#!/bin/sh

set -e

MIBS="LEXTUDIO-TEST-MIB CISCO-IPSEC-TC CISCO-SMI CISCO-TC CISCO-ENHANCED-IPSEC-FLOW-MIB"
URL_BASE="https://raw.githubusercontent.com/lextudio/mibs.pysnmp.com/refs/heads/master/asn1"

tmpdir=$(mktemp -d)
for mib in $MIBS; do
    curl -o $tmpdir/$mib $URL_BASE/$mib
done

tar -czvf mibs.tgz -C $tmpdir .
rm -rf $tmpdir
