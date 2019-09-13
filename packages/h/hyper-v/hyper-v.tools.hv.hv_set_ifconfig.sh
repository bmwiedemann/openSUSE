#!/bin/bash
#
# In the interest of keeping the KVP daemon code free of distro specific
# information; the kvp daemon code invokes this external script to configure
# the interface.
#
# The only argument to this script is the configuration file that is to
# be used to configure the interface.
#
# Here is the format of the ip configuration file:
#
# HWADDR=macaddr
# DEVICE=interface name
# BOOTPROTO=<protocol> (where <protocol> is "dhcp" if DHCP is configured
#                       or "none" if no boot-time protocol should be used)
#
# IPADDR0=ipaddr1
# IPADDR1=ipaddr2
# IPADDRx=ipaddry (where y = x + 1)
#
# NETMASK0=netmask1
# NETMASKx=netmasky (where y = x + 1)
#
# GATEWAY=ipaddr1
# GATEWAYx=ipaddry (where y = x + 1)
#
# DNSx=ipaddrx (where first DNS address is tagged as DNS1 etc)
#
# IPV6 addresses will be tagged as IPV6ADDR, IPV6 gateway will be
# tagged as IPV6_DEFAULTGW and IPV6 NETMASK will be tagged as
# IPV6NETMASK.
#
# The host can specify multiple ipv4 and ipv6 addresses to be
# configured for the interface. Furthermore, the configuration
# needs to be persistent. A subsequent GET call on the interface
# is expected to return the configuration that is set via the SET
# call.
#
cfg=$1
if ! test -f "${cfg}"
then
	: expect configuration datafile as first argument
	exit 1
fi
# send subshell output to syslog
(
# copied from /etc/sysconfig/network/scripts/functions
mask2pfxlen() {
	local i octet width=0 mask=(${1//./ })
	test ${#mask[@]} -eq 4 || return 1
	for octet in 0 1 2 3
	do
		test "${mask[octet]}" -ge 0 -a "${mask[octet]}" -le 255 || return 1
		for i in 128 192 224 240 248 252 254 255
		do
			test ${mask[octet]} -ge $i && ((width++))
		done
	done
	echo $width
	return 0
}

pfxlen2mask() {
	test -n "$1" || return 1
	local o i n=0 adr=() len=$(($1))
	for o in 0 1 2 3
	do
		adr[$o]=0
		for i in 128 64 32 16 8 4 2 1
		do
			((n++ < len)) && ((adr[$o] = ${adr[$o]} + $i))
		done
	done
	echo ${adr[0]}.${adr[1]}.${adr[2]}.${adr[3]}
	return 0
}

# remove known config variables from environment 
unset HWADDR
unset BOOTPROTO
unset DEVICE
unset ${!IPADDR*}
unset ${!NETMASK*}
unset ${!GATEWAY*}
unset ${!IPV6ADDR*}
unset ${!IPV6NETMASK*}
unset ${!IPV6_DEFAULTGW*}
unset ${!DNS*}
. "$1"
#
if test -z "${DEVICE}"
then
	echo "Missing DEVICE= in ${cfg}"
	exit 1
fi
#
t_ifcfg=`mktemp`
t_ifroute=`mktemp`
_exit() {
	rm -f "${t_ifcfg}" "${t_ifroute}"
}
trap _exit EXIT
#
if test -z "${t_ifcfg}" || test -z "${t_ifroute}"
then
	exit 1
fi
#
# Create ifcfg-* file
(
	echo "STARTMODE=auto"
	#
	if test -n "${HWADDR}"
	then
		: # ignore HWADDR, it just repeats the existing MAC value
	fi
	#
	if test "${BOOTPROTO}" = "dhcp"
	then
		echo "BOOTPROTO=dhcp"
	elif test -n "${!IPADDR*}${!IPV6ADDR*}"
	then
		echo "BOOTPROTO=static"
	fi
	# single index for all ipv4 and ipv6 adresses in final ifcfg file
	i=0
	idx=""
	# loop through all ipv4 adresses
	for var in ${!IPADDR*}
	do
		index=${var#IPADDR}
		pfx=
		# find corresponding NETMASK variable
		eval nm=\$NETMASK${index}
		# if specified, calculate prefix
		if test -n "${nm}"
		then
			pfx=`mask2pfxlen "${nm}" 2>/dev/null`
		fi
		# if not specified, force prefix
		if test -z "${pfx}"
		then
			pfx="32"
		fi
		# construct actual value
		eval val=\$IPADDR${index}
		# write config variable
		echo "IPADDR${idx}='${val}/${pfx}'"
		idx="_$((++i))"
	done
	# loop through all ipv6 adresses
	for var in ${!IPV6ADDR*}
	do
		index=${var#IPV6ADDR}
		# find corresponding IPV6NETMASK variable
		eval pfx=\$IPV6NETMASK${index}
		# if not specified, force prefix
		if test -z "${pfx}"
		then
			pfx=128
		fi
		# construct actual value
		eval val=\$IPV6ADDR${index}
		# write config variable
		echo "IPADDR${idx}='${val}/${pfx}'"
		idx="_$((++i))"
	done

) >> "${t_ifcfg}"

# Create ifroute-* file
(
	if test -n "${GATEWAY}"
	then
		echo "default $GATEWAY - $DEVICE"
	fi
	if test -n "${IPV6_DEFAULTGW}"
	then
		echo "default $IPV6_DEFAULTGW - $DEVICE"
	fi
) >> "${t_ifroute}"
# Only a single default gateway is supported
unset GATEWAY IPV6_DEFAULTGW
if test -n "${!GATEWAY*}${!IPV6_DEFAULTGW*}"
then
	echo "WARNING: multiple gateways not supported: ${!GATEWAY*} ${!IPV6_DEFAULTGW*}"
fi

# collect DNS info
_DNS_=
for var in ${!DNS*}
do
	eval val=\$${var}
	if test -n "${_DNS_}"
	then
		_DNS_="${_DNS_} ${val}"
	else
		_DNS_=${val}
	fi
done
#
echo "$0: working on network interface ifcfg-${DEVICE}"
cp -fb ${t_ifcfg} "/etc/sysconfig/network/ifcfg-${DEVICE}"
cp -fb ${t_ifroute} "/etc/sysconfig/network/ifroute-${DEVICE}"
if test -w /etc/sysconfig/network/config
then
	sed -i "s@^NETCONFIG_DNS_STATIC_SERVERS=.*@NETCONFIG_DNS_STATIC_SERVERS='$_DNS_'@"  /etc/sysconfig/network/config
	netconfig update -m dns
fi
ifdown "${DEVICE}"
ifup "${DEVICE}"
) 2>&1 | logger -t "${0##*/}[$PPID / $$]"
