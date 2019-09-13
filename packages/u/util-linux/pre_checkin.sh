#!/bin/sh

if test util-linux.spec -ot python3-libmount.spec ; then
	echo "util-linux.spec is older than python3-libmount.spec. Please merge changes manually and call pre-checkin.sh again."
	exit 1
fi
if test util-linux.changes -ot python3-libmount.changes ; then
	echo "util-linux.changes is older than python3-libmount.changes. Please merge changes manually and call pre-checkin.sh again."
	exit 1
fi

if test util-linux.spec -ot util-linux-systemd.spec ; then
	echo "util-linux.spec is older than util-linux-systemd.spec. Please merge changes manually and call pre-checkin.sh again."
	exit 1
fi
if test util-linux.changes -ot util-linux-systemd.changes ; then
	echo "util-linux.changes is older than util-linux-systemd.changes. Please merge changes manually and call pre-checkin.sh again."
	exit 1
fi

sed '
	s/spec file for package util-linux/spec file for package python3-libmount/;
	/^Name:/s/util-linux/python3-libmount/;
	s/WARNING: After editing this file please/WARNING: Never edit this file!!! Edit util-linux.spec and/
' <util-linux.spec >python3-libmount.spec

sed '
	s/spec file for package util-linux/spec file for package util-linux-systemd/;
	/^Name:/s/util-linux/util-linux-systemd/;
	s/WARNING: After editing this file please/WARNING: Never edit this file!!! Edit util-linux.spec and/
' <util-linux.spec >util-linux-systemd.spec

cp -a util-linux.changes python3-libmount.changes

cp -a util-linux.changes util-linux-systemd.changes

touch util-linux.spec util-linux.changes
