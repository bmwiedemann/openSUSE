#! /bin/bash
#
# dns-bind.sh
#
# Writing IP4 and IP6 DNS server addresses to /etc/named.d/forwarders.conf
#

unset POSIXLY_CORRECT ; set +o posix # we are using non-posix bash features

DESTFILE="/etc/named.d/forwarders.conf"

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

function dump_named_forwarders ()
{
    local NAMESERVER=()
    local ns

    cat << EOT
### This file has been updated/generated directly by the
### NetworkManager script /usr/lib/NetworkManager/dispatcher.d/dns-bind
EOT
    for ns in $1; do
        # According to Bind 9 Administrators Reference Manual
        # there is no limit for forwarders.
        #[ ${#NAMESERVER[@]} -lt 3 ] || break

        NAMESERVER=(${NAMESERVER[@]} ${ns})
    done
    {
        echo "forwarders {"
        for ns in ${NAMESERVER[@]}; do
            echo "	${ns};"
        done
        echo "};"
    }
}

function write_named_forwarders {
    debug "write_named_forwarders: $1 "

    if ! dump_named_forwarders "$@" > "$DESTFILE" ; then
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

if [ "$NETWORKMANAGER_DNS_FORWARDER" != "bind" -a "$NETCONFIG_DNS_FORWARDER" != "bind" ]; then
    debug "NETWORKMANAGER_DNS_FORWARDER is not set to \"bind\" in /etc/sysconfig/network/config -> exit"
    exit 0;
fi

case "$COMMAND" in
    up|dhcp4-change|dhcp6-change)
	IP6_DNS_ADDESS=`ip6_dns_addresses "$IP6_NAMESERVERS"`
	write_named_forwarders "$IP4_NAMESERVERS $IP6_DNS_ADDESS"
        RET=$?
	if [ $RET -ne 0 ]; then
	    exit $RET
	fi
	# here we should reload services if needed
	if systemctl --quiet is-active named.service &>/dev/null ; then
	    systemctl reload named.service &>/dev/null
	fi
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

