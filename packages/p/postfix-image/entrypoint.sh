#!/bin/bash

DEBUG=${DEBUG:-"0"}

[ "${DEBUG}" = "1" ] && set -x

VIRTUAL_MBOX=${VIRTUAL_MBOX:-"0"}
USE_LDAP=${USE_LDAP:-"0"}
NULLCLIENT=${NULLCLIENT:-"1"}
ENABLE_SUBMISSION=${ENABLE_SUBMISSION:-"0"}
ENABLE_SUBMISSIONS=${ENABLE_SUBMISSIONS:-"0"}

export PATH=/usr/sbin:/sbin:${PATH}

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

set_config_value() {
    local failed
    key=${1}
    value=${2}

    echo "Setting configuration option \"${key}\" with value \"${value}\""
    postconf -e "${key} = ${value}" || failed=1
    if [ "$failed" ]; then
	echo "ERROR: postconf -e ${key} ${value} failed!"
	exit 1
    fi
}

# usage: file_env VAR [DEFAULT]
#    ie: file_env 'SMTP_PASSWORD' 'example'
# (will allow for "$SMTP_PASSWORD_FILE" to fill in the value of
#  "$SMTP_PASSWORD" from a file, especially for Docker's secrets feature)
file_env() {
    var="$1"
    fileVar="${var}_FILE"
    def="${2:-}"
    if [ "${!var:-}" ] && [ "${!fileVar:-}" ]; then
        echo >&2 "error: both $var and $fileVar are set (but are exclusive)"
        exit 1
    fi
    val="$def"
    if [ "${!var:-}" ]; then
        val="${!var}"
    elif [ "${!fileVar:-}" ]; then
        val="$(< "${!fileVar}")"
    fi
    export "$var"="$val"
    unset "$fileVar"
}

update_db() {
    local failed

    while test "x$1" != "x" ; do
        pfmap=/etc/postfix/${1}
        test -e "${pfmap}" && \
            if test "${pfmap}" -nt "${pfmap}.lmdb" -o ! -e "${pfmap}.lmdb" ; then
		echo "rebuilding ${pfmap}.lmdb"
		postmap "${pfmap}" || failed=1
		if [ "$failed" ]; then
		    echo "ERROR: postmap ${pfmap} failed!"
		    exit 1
		fi
            fi
        shift
    done
}

setup_aliases() {
    local failed

    get_alias_maps() {
	test -d /etc/aliases.d && test "$(echo /etc/aliases.d/*)" != "/etc/aliases.d/*" && \
            for i in $(find /etc/aliases.d -maxdepth 1 -type f \
			    '!' -regex ".*\.\(db\|rpmsave\|rpmorig\)" \
			    '!' -regex ".*/\(\.\|#\).*" \
			    '!' -regex ".*~$") ; do
		echo -n "$i ";
	    done
    }

    echo "Building /etc/aliases.lmdb."
    set_config_value "alias_database" "lmdb:/etc/aliases"
    /usr/bin/newaliases

    ALLMAPS="lmdb:/etc/aliases"
    for i in $(get_alias_maps); do
        ALLMAPS="${ALLMAPS}, lmdb:$i"
	echo "Building $i.lmdb"
	postalias "${i}" || failed=1
	if [ "${failed}" ]; then
	    echo "ERROR: postalias ${i} failed!"
	    exit 1
	fi
    done
    set_config_value "alias_maps" "${ALLMAPS}"
}

setup_network() {
    if [ -n "${INET_PROTOCOLS}" ]; then
        set_config_value "inet_protocols" "{$INET_PROTOCOLS}"
    else
        # XXX Containers have ipv6 addresses, but not routeable
        #if ip addr show dev lo | grep -q inet6 ; then
        #    set_config_value "inet_protocols" "all"
        #else
             set_config_value "inet_protocols" "ipv4"
        #fi
    fi

    # Always allow private networks, we are running in a container...
    networks='127.0.0.0/8, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16'
    if [ -n "${SMTP_NETWORKS}" ]; then
        networks+=", ${SMTP_NETWORKS}"
    fi
    set_config_value "mynetworks" "${networks}"
}

setup_relayhost() {
    if [ -n "${SMTP_RELAYHOST}" ]; then
        SMTP_PORT="${SMTP_PORT:-587}"
        set_config_value "relayhost" "${SMTP_RELAYHOST}:${SMTP_PORT}"

	if [ "${NULLCLIENT}" -eq "1" ] && [ -z "${MYDESTINATION}" ] ; then
	    set_config_value "mydestination" ""
	fi
    fi

    if [ -n "${SMTP_USERNAME}" ]; then
        file_env 'SMTP_PASSWORD'
        if [ -z "${SMTP_PASSWORD}" ]; then
            echo "SMTP_PASSWORD is not set"
            exit 1
        fi
        # Add auth credentials to sasl_passwd
        echo "Adding SASL authentication configuration"
        echo "${SMTP_RELAYHOST} ${SMTP_USERNAME}:${SMTP_PASSWORD}" >> /etc/postfix/sasl_passwd
        update_db sasl_passwd
        set_config_value "smtp_sasl_password_maps" "lmdb:/etc/postfix/sasl_passwd"
        set_config_value "smtp_sasl_auth_enable" "yes"
        set_config_value "smtp_sasl_security_options" "noanonymous"
    fi

    if [ -n "${MASQUERADE_DOMAINS}" ]; then
        set_config_value "masquerade_domains" "${MASQUERADE_DOMAINS}"
        # Requires since postfix 2.2
        set_config_value "local_header_rewrite_clients" "static:all"
    fi
}

setup_submission() {
    SMTPD_USE_TLS=${SMTPD_USE_TLS:-"0"}

    if [ "${ENABLE_SUBMISSION}" -eq "1" ]; then
	echo "Enable submission port"

	echo "submission inet n       -       n       -       -       smtpd" >> /etc/postfix/master.cf

	if [ "${SMTPD_USE_TLS}" -eq "1" ]; then
	    echo " -o smtpd_tls_security_level=encrypt" >> /etc/postfix/master.cf
	    echo " -o smtpd_sasl_auth_enable=no" >> /etc/postfix/master.cf
	    #echo " -o smtpd_client_restrictions=permit_sasl_authenticated,reject" >> /etc/postfix/master.cf
	fi
    fi

    if [ "${ENABLE_SUBMISSIONS}" -eq "1" ]; then
	if [ "${SMTPD_USE_TLS}" -eq "1" ]; then
	    echo "Enable submissions port"

	    echo "smtps inet n       -       n       -       -       smtpd" >> /etc/postfix/master.cf
	    echo " -o smtpd_tls_wrappermode=yes" >> /etc/postfix/master.cf
	    echo " -o smtpd_sasl_auth_enable=no" >> /etc/postfix/master.cf
	else
	    echo "WARNING: ENABLE_SUBMISSIONS requires SMTPD_USE_TLS, ignoring!"
	fi
    fi

    if [ "${SMTPD_USE_TLS}" -eq "1" ]; then
	echo "Enable TLS for smtpd"

	SMTPD_TLS_CRT=${SMTPD_TLS_CRT:-"/etc/postfix/ssl/certs/tls.crt"}
	SMTPD_TLS_KEY=${SMTPD_TLS_KEY:-"/etc/postfix/ssl/certs/tls.key"}

	# smtpd_use_tls is deprecated and only for compatibility
	set_config_value "smtpd_use_tls" "yes"
	set_config_value "smtpd_tls_security_level" "may"
	set_config_value "smtpd_tls_CApath" "/etc/ssl/certs"
	set_config_value "smtpd_tls_cert_file" "${SMTPD_TLS_CRT}"
	set_config_value "smtpd_tls_key_file" "${SMTPD_TLS_KEY}"
    fi
}

setup_vhosts() {
    if [ "${USE_LDAP}" -eq "1" ]; then
	LDAP_BASE_DN=${LDAP_BASE_DN:-"dc=example,dc=org"}
	LDAP_SERVER_URL=${LDAP_SERVER_URL:-"ldap://localhost"}
        LDAP_USE_TLS=${LDAP_USE_TLS:-"1"}
        LDAP_BIND_DN=${LDAP_BIND_DN:-"cn=mailAccountReader,ou=Manager,${LDAP_BASE_DN}"}
	file_env LDAP_BIND_PASSWORD
        if [ -z "${LDAP_BIND_PASSWORD}" ]; then
            echo "LDAP_BIND_PASSWORD is not set"
            exit 1
        fi

	# Adjust LDAP variables
	mkdir -p /etc/postfix/ldap
	for map in smtpd_sender_login_maps virtual_alias_domains virtual_alias_maps virtual_gid_maps virtual_mailbox_maps virtual_uid_maps ; do
	    sed -e "s|@LDAP_BASE_DN@|${LDAP_BASE_DN}|g" \
		-e "s|@LDAP_SERVER_URL@|${LDAP_SERVER_URL}|g" \
		-e "s|@LDAP_BIND_DN@|${LDAP_BIND_DN}|g" \
		-e "s|@LDAP_BIND_PASSWORD@|${LDAP_BIND_PASSWORD}|g" \
		"/entrypoint/ldap/${map}" > "/etc/postfix/ldap/${map}"
             if [ "${LDAP_USE_TLS}" = "1" ]; then
                 sed -i -e 's|^start_tls.*|start_tls = yes|g' "/etc/postfix/ldap/${map}"
             else
                 sed -i -e 's|^start_tls.*|start_tls = no|g' "/etc/postfix/ldap/${map}"
	     fi
	     if [ -n "${LDAP_TLS_CA_CRT}" ]; then
		 sed -i -e "s|^#tls_ca_cert_file =.*|tls_ca_cert_file = ${LDAP_TLS_CA_CRT}|g" "/etc/postfix/ldap/${map}"
	     fi
	done

	# Don't use VIRUAL_DOMAINS and ldap:virtual_alias_domains at the same time, postfix does
	# not like this
	if [ -z "${VIRTUAL_DOMAINS}" ]; then
	    set_config_value "virtual_alias_domains" "ldap:/etc/postfix/ldap/virtual_alias_domains"
	fi
	set_config_value "virtual_alias_maps" "ldap:/etc/postfix/ldap/virtual_alias_maps"
	set_config_value "virtual_mailbox_maps" "ldap:/etc/postfix/ldap/virtual_mailbox_maps"
	set_config_value "smtpd_sender_login_maps" "ldap:/etc/postfix/ldap/smtpd_sender_login_maps"
    else
	set_config_value "virtual_mailbox_maps" "lmdb:/etc/postfix/vmaps"
	set_config_value "virtual_mailbox_limit_maps" "lmdb:/etc/postfix/vquota"

	# Only create vmaps if not provided by admin
	if [ ! -f /etc/postfix/vmaps ]; then
	    for mail in ${VIRTUAL_USERS} ; do
		user=${mail%@*}
		domain=${mail#*@}
		echo "${mail} ${domain}/${user}/" >> /etc/postfix/vmaps
		echo "${mail} 0" >> /etc/postfix/vquota
	    done
	fi
	update_db vquota
    fi

    set_config_value "virtual_mailbox_domains" "/etc/postfix/vhosts"
    # Only create vhosts if not provided by admin
    if [ ! -f /etc/postfix/vhosts ]; then
        if [ -n "${VIRTUAL_DOMAINS}" ]; then
	    for d in ${VIRTUAL_DOMAINS}; do
		echo "$d" >> /etc/postfix/vhosts
	    done
        elif [ -n "${SERVER_DOMAIN}" ]; then
	    echo "${SERVER_DOMAIN}" > /etc/postfix/vhosts
	else
	    touch /etc/postfix/vhosts
        fi
    fi
    update_db vmaps

    if [ -n "${LMTP}" ]; then
	# Use LMTP to deliver the mail to the user

	set_config_value "virtual_transport" "lmtp:${LMTP}:24"
    else
	# Store mails local below /var/spool/vmail

	# Create the vmail user with the requested UID, else 5000
	VMAIL_UID="${VMAIL_UID:-5000}"
	if [ -x /usr/sbin/adduser ]; then
	    adduser -D -h /var/spool/vmail -g "Virtual Mail User" -u "${VMAIL_UID}" -s /sbin/nologin vmail
	else
            useradd -d /var/spool/vmail -U -c "Virtual Mail User" -u "${VMAIL_UID}" vmail
	fi
	if [ $? -ne 0 ]; then
            echo "ERROR: creating of vmail user failed! Aborting."
            exit 1
	fi

	if [ ! -d /var/spool/vmail ]; then
            mkdir -p /var/spool/vmail
            chown vmail:vmail /var/spool/vmail
            chmod 775 /var/spool/vmail
	fi

	set_config_value "virtual_mailbox_base" "/var/spool/vmail"
	set_config_value "virtual_minimum_uid" "1000"
	set_config_value "virtual_uid_maps" "static:${VMAIL_UID}"
	set_config_value "virtual_gid_maps" "static:${VMAIL_UID}"
	set_config_value "home_mailbox" "Maildir/"
	# XXX make this configureable and adjust message_size_limit
	set_config_value "virtual_mailbox_limit" "0"
	set_config_value "mailbox_size_limit" "0" # "51200000"
	set_config_value "message_size_limit" "0" # "10240000"
    fi
}

configure_postfix() {

    setup_network

    if [ -n "${SERVER_HOSTNAME}" ]; then
	if [ -z "${SERVER_DOMAIN}" ]; then
	    SERVER_DOMAIN=$(echo "${SERVER_HOSTNAME}" | cut -d"." -f2-)
	fi
	set_config_value "myhostname" "${SERVER_HOSTNAME}"
        set_config_value "mydomain" "${SERVER_DOMAIN}"
    fi

    # Generic settings
    ## Use lmdb instead of "hash" to get rid of BDB
    set_config_value "default_database_type" "lmdb"
    sed -i -e 's|hash:|lmdb:|g' /etc/postfix/main.cf
    ## TLS
    if [ -n "${SMTP_TLS_WRAPPERMODE}" ]; then
       set_config_value "smtp_tls_wrappermode" "${SMTP_TLS_WRAPPERMODE}"
    fi
    SMTP_TLS_SECURITY_LEVEL=${SMTP_TLS_SECURITY_LEVEL:-"may"}
    set_config_value "smtp_tls_security_level" "${SMTP_TLS_SECURITY_LEVEL}"
    set_config_value "smtp_tls_CApath" "/etc/postfix/ssl/cacerts"
    ## Debug only:
    # set_config_value "smtp_tls_loglevel" "2"

    if [ "${VIRTUAL_MBOX}" -eq "1" ]; then
        setup_vhosts
    fi
    if [ -n "${MYDESTINATION}" ]; then
	set_config_value "mydestination" "${MYDESTINATION}"
    else
	set_config_value "mydestination" "\$myhostname, localhost.\$mydomain, localhost"
    fi
    setup_submission
    setup_relayhost

    # Add maps to config and create database
    for i in canonical relocated sender_canonical transport virtual; do
	set_config_value "${i}_maps" "lmdb:/etc/postfix/${i}"
	update_db "${i}"
    done
    set_config_value "smtpd_sender_restrictions" "lmdb:/etc/postfix/access"

    # Log to stdout
    set_config_value "maillog_file" "/dev/stdout"

    # Generate and update maps
    update_db access relay relay_recipients

    setup_aliases
}

setup_spamassassin() {
    if [ -n "${SPAMASSASSIN_HOST}" ]; then
	set_config_value "smtpd_milters" "unix:/run/spamass-milter/socket"
    fi
}

terminate() {
    base=$(basename "$1")
    pid=$(/bin/pidof "$base")

    if [ -n "$pid" ]; then
	echo "Terminating $base..."
	if kill "$pid" ; then
	    echo "Terminating $base failed!"
	fi
    else
	echo "Failure determining PID of $base"
    fi
}

init_trap() {
    trap stop_daemons TERM INT
}

stop_spamassassin() {
    terminate /usr/sbin/spamass-milter
}

stop_postfix() {

    typeset -i sec=$1
    typeset -i ms=$((sec*100))

    (   while ! pidof qmgr > /dev/null 2>&1 ; do
            ((ms-- <= 0)) && break
            usleep 10000
	done
	exec postfix flush
    ) > /dev/null 2>&1 &

    postfix stop
}

stop_daemons() {
    stop_postfix "$@"
    stop_spamassassin
}

#
# Main
#

# if command starts with an option, prepend postfix
if [ "${1:0:1}" = '-' ]; then
        set -- postfix start-fg "$@"
fi

init_trap
setup_timezone
# Update certificates if /etc/pki is mounted from the host
update-ca-certificates
# configure postfix even if postfix will not be started, to
# allow to see the result with postconf for debugging/testing.
configure_postfix
setup_spamassassin

# If host mounting /var/spool/postfix, we need to delete the old pid file
# before starting services
rm -f /var/spool/postfix/pid/master.pid

if [ "$1" = 'postfix' ]; then
    if [ -n "${SPAMASSASSIN_HOST}" ]; then
	mkdir /run/spamass-milter
	chown sa-milter:postfix /run/spamass-milter
	chmod 751 /run/spamass-milter
	su sa-milter -s /bin/sh -c "/usr/sbin/spamass-milter -p /run/spamass-milter/socket -g postfix -f -- -d ${SPAMASSASSIN_HOST}"
    fi
fi
exec "$@"
