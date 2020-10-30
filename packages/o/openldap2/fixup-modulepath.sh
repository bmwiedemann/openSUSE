#!/bin/bash

source /usr/lib/openldap/update-crc

conf_dir='/etc/openldap/slapd.d'
tgt_ldif="${conf_dir}/cn=config.ldif"
if [ ! -d ${conf_dir} ] || [ ! -f ${tgt_ldif} ]
then
	exit 0
fi

# Make sure slapd.service is not running.
slapd_running=1

# Don't check if no systemd, we could be in a container.
if [ -f "/usr/bin/systemctl" ]; then
    /usr/bin/systemctl is-active --quiet slapd.service
    slapd_running=$?
fi

if [ $slapd_running -eq 0 ]; then
    echo "Unable to update crc of '${tgt_ldif}' while slapd.service is running ..."
    exit 1
fi

# Remove the module path.
sed -n -i '/olcModulePath/!p'  ${tgt_ldif}

res=$?

if [ $res -ne 0 ]
then
    echo "Failed to remove olcModulePath in ${tgt_ldif}"
    exit 1
else
    do_update_crc ${tgt_ldif}
    echo "Updated crc of ${tgt_ldif}"
fi




