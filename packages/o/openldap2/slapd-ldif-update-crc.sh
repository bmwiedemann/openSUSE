#!/bin/bash
# Script to fix the crc of openldap slapd.d ldifs.
source /usr/lib/openldap/update-crc

if [ -z ${1} ]; then
    echo "Usage: ${0} /etc/openldap/slapd.d/<config ldif to update>"
    exit 1
fi

if [ ! -f "${1}" ]; then
    echo "File ${1} does not exist?"
    echo "Usage: ${0} /etc/openldap/slapd.d/<config ldif to update>"
    exit 1
fi

# Make sure slapd.service is not running.
slapd_running=1

# Don't check if no systemd, we could be in a container.
if [ -f "/usr/bin/systemctl" ]; then
    /usr/bin/systemctl is-active --quiet slapd.service
    slapd_running=$?
fi

if [ $slapd_running -eq 0 ]; then
    echo "Unable to update crc of '${1}' while slapd.service is running ..."
    exit 1
fi

do_update_crc ${1}

echo "Updated crc of ${1}"

