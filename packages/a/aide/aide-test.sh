#!/bin/sh
export TESTDIR=`mktemp -d /tmp/aide.XXXXXX`
install -m 700 -d $TESTDIR/var/lib/aide
install -m 700 -d $TESTDIR/etc
install -m 600  /etc/aide.conf $TESTDIR/etc/aide.conf.new
sed -e "s#/var/lib/aide#$TESTDIR/var/lib/aide#g" <$TESTDIR/etc/aide.conf.new >$TESTDIR/etc/aide.conf
/usr/bin/aide -c $TESTDIR/etc/aide.conf --init || exit 1
mv $TESTDIR/var/lib/aide/aide.db.new $TESTDIR/var/lib/aide/aide.db
/usr/bin/aide -c $TESTDIR/etc/aide.conf --check --verbose || exit 1

rm -rf $TESTDIR
