#!/bin/bash

DEBUG=${DEBUG:-"0"}

[ "${DEBUG}" -eq "1" ] && set -x

HOSTNAME=${HOSTNAME:-$(hostname)}
REALM=

export PATH=/usr/sbin:/sbin:${PATH}

CONFIG_FILE="/etc/samba/smb.conf"
KRB5_CONF_FILE="/etc/krb5.conf.d/addc.conf"

setup_timezone() {
    if [ -n "$TZ" ]; then
	TZ_FILE="/usr/share/zoneinfo/$TZ"
	if [ -f "$TZ_FILE" ]; then
	    echo "Setting container timezone to: $TZ"
	    ln -snf "$TZ_FILE" /etc/localtime
	else
	    echo "Cannot set timezone \"$TZ\": timezone does not exist."
	fi
    fi
}

provision() {
    IFS=: read -r domain_name password function_level rfc2307 <<<"$1"

    if [ -z "$function_level" ]; then
        function_level=2008_R2
    fi
    if [ -n "$rfc2307" ] && [ "$rfc2307" == "yes" ]; then
        rfc2307="--use-rfc2307"
    fi

    echo "Provisioning the domain $domain_name..."
    REALM=${domain_name^^}
    init_krb5_conf
    rm $CONFIG_FILE
    nb_name=${domain_name%%.*}
    samba-tool domain provision --domain="$nb_name" --realm="$domain_name" --adminpass="$password" --host-name="$HOSTNAME" --function-level="$function_level" $rfc2307
    echo "DONE"
}

domain_join() {
    IFS=: read -r domain_name type admin password <<<"$1"

    if [ "$type" != "DC" ] && [ "$type" != "RODC" ]; then
        echo "Invalid domain role '$type'."
        exit 1
    fi
    echo "Joining domain $domain_name as a domain controller..."
    REALM=${domain_name^^}
    init_krb5_conf
    rm $CONFIG_FILE
    samba-tool domain join "$domain_name" $type -U "$admin" --password="$password"
    echo "DONE"
}

init_krb5_conf() {
    cat >"$KRB5_CONF_FILE" <<EOT
[libdefaults]
    default_realm = $REALM

[realms]
    $REALM = {
        kdc = $HOSTNAME
    }
EOT
}

show_help() {
            cat <<EOT
Samba ADDC container

The container will be configured as a samba addc and requires:
 * Either a domain to join, or name to be promoted as.

Options:
 -d <domain_name:type:admin:password>
    Configure an Active Directory domain controller in an existing domain.
     * domain_name      Required, domain name of the new/joining domain
     * type             Required, DC or RODC
     * admin            Required, the domain Administrator
     * password         Required, the Administrator password
 -p <domain_name:password>[:function_level:rfc2307]
    Provision a new Active Directory domain.
     * domain_name      Required, domain name of the new/joining domain
     * password         Required, the Administrator password
     * function_level   Optional, [2000|2003|2008|2008_R2] Domain and forest function level, default is 2008_R2
     * rfc2307          Optional, [yes|no] Use AD to store posix attributes (default = no)
 -h
    Display help text and exit

Environment variables:
  DEBUG=[0|1]		Enable debug mode
  TZ=<timezone>		Set timezone

EOT
}

#
# Main
#

setup_timezone

while getopts ":p:d:h" opt; do
    case $opt in
	h)
            show_help
            exit 0
            ;;
	p)
	    provision "$OPTARG"
	    ;;
	d)
	    domain_join "$OPTARG"
	    ;;
	\?)
            echo "Invalid option: -$OPTARG"
            echo
            show_help
            exit 1
            ;;
	:)
            echo "Error: option -$OPTARG requires an argument."
            echo
            show_help
            exit 1
            ;;
    esac
done

exec catatonit -- samba -F --debug-stdout --no-process-group --configfile="$CONFIG_FILE" < /dev/null
