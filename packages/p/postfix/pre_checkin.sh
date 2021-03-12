#!/bin/bash

echo -n "Generating postfix-bdb "

cp postfix.changes postfix-bdb.changes
VERSION=$(awk '/^Version/ {print $2; exit;} {next;};' < postfix.spec)
perl -pi -e "s/^Version:.*/Version: $VERSION/" postfix-bdb.spec
echo "Done."
