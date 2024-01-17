#!/bin/sh
# set -x
prog=netconsole-server
#
# initialize the netconsole using reasonable defaults (normally just the
# client IP address, and possibly the port.  We can determine the MAC
# address of the client system, IP address, the correct device, and verify
# that we are using an ethernet interface (required for netconsole to work).
#
# Andreas Dilger <adilger@turbolinux.com>  Sep 26, 2001

PATH=$PATH:/sbin:/usr/sbin
default_port=6666
src_port=
src_ip=
dev=
tgt_port=
tgt_hostname=
tgt_ip=
tgt_macaddr=
verbose=
loglevel=

usage()
{
	cat - <<- EOF 1>&2

	Initialize a network message console over UDP.
	See /usr/share/doc/packages/netconsole-tools/netlogging.txt for more details

	usage: $prog [-b] [-d dev] [-m mac] [-p port] target[:port]
		-v	 - be verbose, display arp -a, use modprobe -v
		-n	 - change loglevel (default: leave it as is)
		-b       - use broadcast ethernet MAC address
		-m       - specify remote system MAC address as 01:23:45:67:89:ab (default: detect)
		-p       - local port to use for message traffic (default: $default_port)
		-d       - ethernet device to use for messages (default: detect)
		target   - hostname/IP address of remote netconsole-client
		:port    - port on target netconsole-client (default: like -p)
	EOF
	exit 1
}

while [ $# -ge 1 ]; do case $1 in
	-b) tgt_macaddr=broadcast ;;
	-d) dev=$2; shift ;;
	-m) tgt_macaddr=$2; shift ;;
	-p) src_port=$2; shift ;;
	-n) loglevel=$2; shift ;;
	-v) verbose=-v ;;
	*:*) tgt_hostname=`echo $1 | sed "s/:.*//"`; tgt_port=`echo $1 | sed "s/.*://"` ;;
	*) tgt_hostname=$1 ;;
	esac
	shift
done

[ -z "$tgt_hostname" ] && usage
[ -z "$src_port" ] && src_port=$default_port
[ -z "$tgt_port" ] && tgt_port=$src_port

ping -c 1 $tgt_hostname > /dev/null 2>&1
[ $? -ne 0 ] && echo "$prog: can't ping $tgt_hostname" 1>&2 && usage

# output from arp -a of the form:
# good: host.domain (A.B.C.D) at 00:50:BF:06:48:C1 [ether] on eth0
# bad:  ? (A.B.C.D) at <incomplete> on eth0
if [ "$verbose" != "" ] ; then
	arp -a | grep $tgt_hostname
fi
arp -a | grep $tgt_hostname | { read HOSTNAME IPADDR AT MACADDR TYPE ON IFACE;
	[ "$HOSTNAME" = "?" -a -z "$tgt_macaddr" -a "$tgt_macaddr" != "broadcast" ] && \
		echo "$prog: can't resolve $tgt_hostname MAC" 1>&2 && usage

	[ -z "$tgt_macaddr" ] && tgt_macaddr=$MACADDR
	[ -z "$dev" ] && dev=$IFACE
	[ "$dev" = "$IFACE" -a "$TYPE" != "[ether]" ] && \
		echo "$prog: $dev must be an ethernet interface" 1>&2 && usage
		
	src_ip=`ip -family inet -oneline addr show dev $dev | sed 's@^.*inet \([^/]\+\).*@\1@'`
	tgt_ip=`echo $IPADDR | sed -e "s/[()]//g"`
	if [ "$tgt_macaddr" = "broadcast" ]; then
		tgt_macaddr=
	fi
	/sbin/modprobe $verbose netconsole netconsole="${src_port}@${src_ip}/${dev},${tgt_port}@${tgt_ip}/${tgt_macaddr}"
	if [ "$?" = 0 ] ; then
		if [ "$verbose" != "" ] ; then
			echo
		fi
		if [ "$loglevel" = "" ] ; then
			echo "verify the loglevel. otherwise no message may appear on the remove host, see man dmesg(1)"
		else
			echo "setting loglevel to $loglevel via 'dmesg -n $loglevel'"
			dmesg -n $loglevel
		fi
		echo "now run 'netcat -l -u -p $tgt_port' on host $tgt_ip to see further kernel messages"
	fi
}
