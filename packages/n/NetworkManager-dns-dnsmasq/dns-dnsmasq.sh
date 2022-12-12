#! /bin/bash
#
# dns-dnsmasq
#
# Writing IP4 and IP6 DNS server addresses to /var/run/dnsmasq-forwarders.conf
#

unset POSIXLY_CORRECT ; set +o posix # we are using non-posix bash features

DESTFILE="/var/run/dnsmasq-forwarders.conf"

function debug {
    echo "<debug> $1" | systemd-cat -t `basename $0`
}

function error {
    echo "<error> $1" | systemd-cat -t `basename $0`
}

function ip6_dns_addresses ()
{
    local ns
    
    for ns in $1; do
        # Adding "%<device>" to the ip6 address
        echo -n " ${ns}%$DEVICE_IP_IFACE"
    done
}

function dump_dnsmasq_forwarders ()
{
    local NAMESERVER=()
    local ns

    cat << EOT
### This file has been updated/generated directly by the
### NetworkManager script /usr/lib/NetworkManager/dispatcher.d/dns-dnsmasq
EOT
    for ns in $1; do
        # resolv.conf supports up to 3 nameserver,
        # but AFAIK not for dnsmasq  ...	
        #[ ${#NAMESERVER[@]} -lt 3 ] || break

        NAMESERVER=(${NAMESERVER[@]} ${ns})
    done
    if [ ${#NAMESERVER[@]} -gt 0 ]; then
        for ns in ${NAMESERVER[@]}; do
            echo "nameserver ${ns}"
        done
    fi    
}

function write_dnsmasq_forwarders {
    debug "write_named_forwarders: $1 "

    if ! dump_dnsmasq_forwarders "$@" > "$DESTFILE" ; then
	error "Cannot write settings to $DESTFILE"
        return 2
    fi
    debug "dns settings written to $DESTFILE"
    return 0
}

# The environment variable ROOT indicates the root of the system to be
# managed by SuSEconfig when that root is not '/'
r="$ROOT"

if test "$UID" != "0" -a "$USER" != root -a -z "$ROOT" ; then
    debug "You must be root to start $0."
    exit 1
fi

. "$r/etc/sysconfig/network/config"

COMMAND="$2"

if [ "$NETWORKMANAGER_DNS_FORWARDER" != "dnsmasq" -a "$NETCONFIG_DNS_FORWARDER" != "dnsmasq" ]; then
    debug "NETWORKMANAGER_DNS_FORWARDER is not set to \"dnsmasq\" in /etc/sysconfig/network/config -> exit"
    exit 0;
fi

case "$COMMAND" in
    up|dhcp4-change|dhcp6-change)
	IP6_DNS_ADDESS=`ip6_dns_addresses "$IP6_NAMESERVERS"`
	write_dnsmasq_forwarders "$IP4_NAMESERVERS $IP6_DNS_ADDESS"
        RET=$?
	if [ $RET -ne 0 ]; then
	    exit $RET
	fi
	# here we should reload services if needed
	# => not needed, dnsmasq polls and reloads itself	
	exit 0
        ;;
    pre-down|down|vpn-pre-down)
	debug "do nothing while disconneting"
        exit 0
        ;;
    *)
        exit 0
        ;;
esac

