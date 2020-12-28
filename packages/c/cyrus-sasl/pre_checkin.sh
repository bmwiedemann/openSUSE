#!/bin/bash

echo -n "Generating cyrus-sasl-saslauthd "

cp cyrus-sasl.changes cyrus-sasl-saslauthd.changes
cp cyrus-sasl.changes cyrus-sasl-saslauthd.changes
cp cyrus-sasl.changes cyrus-sasl-bdb.changes
cp cyrus-sasl.changes cyrus-sasl-saslauthd-bdb.changes
SASLVERSION=$(awk '/^Version/ {print $2; exit;} {next;};' < cyrus-sasl.spec)
perl -pi -e "s/^Version:.*/Version: $SASLVERSION/" cyrus-sasl-saslauthd.spec
perl -pi -e "s/^Version:.*/Version: $SASLVERSION/" cyrus-sasl-bdb.spec
perl -pi -e "s/^Version:.*/Version: $SASLVERSION/" cyrus-sasl-saslauthd-bdb.spec
echo "Done."
