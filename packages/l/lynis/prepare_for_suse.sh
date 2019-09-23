#!/bin/bash 

umask 0077

OSVERS=$(grep VERSION /etc/SuSE-release |  sed "s/VERSION = //")
OS=$(head -n 1 /etc/SuSE-release | sed "s/[()]//g" | sed "s/ /_/g")

fileperms()
{
	PERMS=$(grep -E "^PERMISSION_SECURITY=" /etc/sysconfig/security | awk -F'=' '{print $2}' | sed s/\"//g)
	echo $PERMS
	for p in $PERMS
	do
		echo $p
		grep -E "^/\w.*" "/etc/permissions."$p | awk -F' ' '{print "file:"$1":"$3":"$2":Linux:"}' >> $TMPDIR/fileperms.lst
	done

	if ! [ -f db/fileperms.db.orig ]; then
		cp -v db/fileperms.db db/fileperms.db.orig
	fi

	rm -f db/fileperms.db
	cp $TMPDIR/fileperms.lst db/fileperms.db.$OS
	ln -s fileperms.db.$OS db/fileperms.db
}

dbussystem()
{
	for i in $(ls -1 /usr/share/dbus-*/system-services/*.service /etc/dbus-*/system.d/*.conf 2>/dev/null)
	do     
		basename $i >> $TMPDIR/dbus-whitelist.db.$OS
	done

	rm -f db/dbus-whitelist.db
	cp -v $TMPDIR/dbus-whitelist.db.$OS db/
	ln -s dbus-whitelist.db.$OS db/dbus-whitelist.db
}

TMPDIR=$(mktemp -d /tmp/lynis.XXXXXX)

echo "prepare lynis config for your suse systems"
echo "1. lookup file permission level"
fileperms
echo "2. lookup dbus system serices in /etc/dbus-1/system.d/"
dbussystem

rm -rf $TMPDIR
