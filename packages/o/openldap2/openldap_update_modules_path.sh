#!/bin/bash
# This script has been created to update the OpenLDAP modules path in cn=config
# For details of changing the configuration items' location read these:
# https://www.openldap.org/lists/openldap-software/200812/msg00080.html
# This script writes over the config entry of backend databases location, which files are necessary to run LDAP. The procedure has been created upon this description:
# https://serverfault.com/questions/863274/modify-openldap-cn-config-without-slapd-running

# Author: Zsolt KALMAR (SUSE Linux GmbH) zkalmar@suse.com

# define variables
conf_dir='/etc/openldap/slapd.d'
if [ ! -d ${conf_dir} ] || [ ! -f ${conf_dir}/cn=config.ldif ]
then
	exit 0
fi


tmp_file='/tmp/ldap_conf_tmp.ldif'
backup='/tmp/slapd.d'
res=0

# common functions
create_symlinks () {
if [ ! -f /usr/lib/openldap/back_bdb.so ]; then ln -s /usr/lib64/openldap/back_bdb.so /usr/lib/openldap/back_bdb.so; fi
if [ ! -f /usr/lib/openldap/back_hdb.so ]; then ln -s /usr/lib64/openldap/back_hdb.so /usr/lib/openldap/back_hdb.so; fi
if [ ! -f /usr/lib/openldap/back_mdb.so ]; then ln -s /usr/lib64/openldap/back_mdb.so /usr/lib/openldap/back_mdb.so; fi
if [ ! -f /usr/lib/openldap/syncprov.so ]; then ln -s /usr/lib64/openldap/syncprov.so /usr/lib/openldap/syncprov.so; fi
#logger -p user.info "Update openLDAP: symlinks have been created."
}

cleanup () {
rm -f /usr/lib/openldap/back_bdb.so
rm -f /usr/lib/openldap/back_hdb.so
rm -f /usr/lib/openldap/back_mdb.so
rm -f /usr/lib/openldap/syncprov.so
rm -f ${tmp_file}
#logger -p user.info "Update openLDAP: symlinks have been removed."
}

rm -f ${tmp_file}

# Check if the configuration is containing the inappropriate entry
create_symlinks
res=0
if [ -f /usr/sbin/slapcat ]
then
    /usr/sbin/slapcat -n0 -F ${conf_dir} -l ${tmp_file} -o ldif-wrap=no
    res=$?
fi

if [ $res -ne 0 ]
then
    #logger -p user.error "LDAP Update script: Creating ${tmp_file} has failed during the search of faulty openLDAP entry."
    exit 1
#else
    #logger -p user.info "LDAP Update script: ${tmp_file} has been created."
fi

entry_cnt=`cat ${tmp_file} | grep ^[^#\;] | grep olcModulePath | wc -l`

if [ $entry_cnt -eq 0 ]
then
    #logger -p user.info "LDAP Update script: The current LDAP configuration does not contain the wrong item. Stop applying this script. Bye."
    cleanup
    exit 0
fi

rm -rf ${tmp_file}

# Make sure the LDAP is not running:
/usr/bin/systemctl stop slapd.service
#logger -p user.info "LDAP Update script: openLDAP has been stopped."

# Creating symlinks for the modules required for the slapcat and slapadd
create_symlinks

# Export the config to a text
res=0
if [ -f /usr/sbin/slapcat ]
then
    /usr/sbin/slapcat -n0 -F ${conf_dir} -l ${tmp_file} -o ldif-wrap=no
    res=$?
fi

if [ $res -ne 0 ]
then
    #logger -p user.error "LDAP Update script: Creating ${tmp_file} has failed."
    cleanup
    exit 1
fi

# Create a backup of LDAP config
mkdir ${backup}
cp -r ${conf_dir}/* ${backup}/
res=$?

if [ $res -ne 0 ]
then
    #logger -p user.error "LDAP Update script: Backing up ${conf_dir} has failed."
    exit 1
#else
    #logger -p user.info "LDAP Update script: Back up has been created of openLDAP configuration."
fi

# Remove the configuration item "olcModulePath"
sed -n -i '/olcModulePath/!p'  ${tmp_file}
res=$?

if [ $res -ne 0 ]
then
    #logger -p user.error "LDAP Update script: Removing of entry in ${tmp_file} has failed."
    exit 1
#else
    #logger -p user.info "LDAP Update script: olcModulesPath entry has been removed."
fi

# Remove the current configuration
rm -rf ${conf_dir}/*

# Load the modified configuration
/usr/sbin/slapadd -n0 -F ${conf_dir} -l ${tmp_file}
res=$?

# Catch result code of slapadd
if [ $res -ne 0 ]
then
    #logger -p user.error "LDAP Update script: Implementing new configuration has failed."
    exit 1
else
    #logger -p user.info "LDAP Update script: Implementing new configuration has been succeeded."
    cleanup
fi

# Start the SLAPD with the new configuration
/usr/bin/systemctl start slapd.service
res=$?

if [ $res -ne 0 ]
then
 #logger -p user.error "LDAP Update script: Starting updated LDAP server has been failed."
    exit 1
else
    #logger -p user.info "LDAP Update script: Updated LDAP server has been successfully started."
    # Remove backups
    rm -rf ${backup}
    rm -rf ${tmp_file}
    # Create "/var/adm/openldap_update_modules"
    touch /var/adm/openldap_update_modules
    exit 0
fi
