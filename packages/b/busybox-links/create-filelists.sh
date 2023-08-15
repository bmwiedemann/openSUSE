#!/bin/bash

set -euxo pipefail

mkdir {apps,used,missing}

dnf --refresh install -y busybox
busybox_links=$(rpm -ql busybox|grep busybox.links)
for i in $(cat $busybox_links); do touch apps/$(basename $i); done

# No rpm/rpm2cpio, will break build service
rm -f apps/rpm apps/rpm2cpio; \
# No /linuxrc
rm -f apps/linuxrc; \
# Does not really fit
rm apps/[[

for package in coreutils diffutils findutils grep util-linux util-linux-systemd iputils iproute2 gzip sed cpio procps xz bzip2 psmisc kbd sharutils hexedit hostname net-tools net-tools-deprecated traceroute ncurses-utils kmod tar gawk patch attr which bind-utils man sendmail sha3sum shadow less whois unzip vim wget ed bc netcat-openbsd dos2unix telnet tftp time tunctl vlan sysvinit-tools selinux-tools policycoreutils; do
    for i in $(dnf rq -l $package |grep "bin/") ; do
	prog=$(basename $i)
	if [ -f apps/$prog ]; then
	    touch used/$prog;
	    echo $i >> filelist-$package.txt
	else
	    touch missing/$prog
	fi
    done
done

BINDIR=$(rpm -E %_bindir)
SBINDIR=$(rpm -E %{_sbindir})
DATADIR=$(rpm -E %{_datadir})

# Merge net-tools sub-packages
cat filelist-net-tools-deprecated.txt >> filelist-net-tools.txt
rm filelist-net-tools-deprecated.txt
# Create some extra sub-packages
echo -e "$BINDIR/ash" > filelist-sh.txt
touch used/ash
echo -e "$BINDIR/hush" >> filelist-sh.txt
touch used/hush
echo -e "$BINDIR/sh" >> filelist-sh.txt
touch used/sh
echo -e "$SBINDIR/loadfont" >> filelist-kbd.txt
touch used/loadkmap used/loadfont

echo -e "/usr/sbin/addgroup\n/usr/sbin/adduser\n/usr/sbin/delgroup\n/usr/sbin/deluser" >> filelist-shadow.txt
touch used/addgroup used/adduser used/delgroup used/deluser

echo -e "/usr/sbin/syslogd" > filelist-syslogd.txt
touch used/syslogd

# Some iproute2 commands are named sligthly different
echo -e "/usr/sbin/ifdown\n/usr/sbin/ifenslave\n/usr/sbin/ifup\n/usr/sbin/ipaddr\n/usr/sbin/iplink\n/usr/sbin/ipneigh\n/usr/sbin/iproute\n/usr/sbin/iprule\n/usr/sbin/brctl" >> filelist-iproute2.txt
touch used/ifdown used/ifenslave used/ifup used/ipaddr used/iplink used/ipneigh used/iproute used/iprule used/brctl

for i in $(/bin/ls used/); do
    rm apps/$i
done

# /usr/bin/last is now in wtmpdb, but should stay in busybox-util-linux
if [ -e apps/last ]; then
    echo -e "/usr/bin/last" >> filelist-util-linux.txt
    touch used/last
    rm -f apps/last
fi

for i in `cat $DATADIR/busybox/busybox.links` ; do
    prog=`basename $i`
    if [ -f apps/$prog ]; then
	echo $i >> filelist-misc.txt
    fi
done

sed -e 's|$prefix/bin/busybox|$prefix/usr/bin/busybox|g' \
    -e "s|\"bin/busybox\"|\"..$BINDIR/busybox\"|g" \
    -e "s|\"busybox\"|\"..$BINDIR/busybox\"|g" \
    -e "s|\"../bin/busybox\"|\"..$BINDIR/busybox\"|g" \
    -e 's|"../../bin/busybox"|"../bin/busybox"|g' \
    -e "s|$DATADIR/busybox/busybox.links|filelist.txt|g" \
    $BINDIR/busybox.install > busybox.install

cat filelist-*.txt | sort -u > filelist.txt
