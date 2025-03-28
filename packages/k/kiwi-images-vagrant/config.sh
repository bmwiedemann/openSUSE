#!/bin/bash
#================
# FILE          : config.sh
#----------------
# PROJECT       : openSUSE KIWI Image System
# COPYRIGHT     : (c) 2021 SUSE LLC
#               :
# AUTHOR        : Marcus Schaefer <ms@suse.de>
#               : Dan Čermák <dcermak@suse.com>
#               :
# BELONGS TO    : Operating System images
#               :
# DESCRIPTION   : configuration script for SUSE based
#               : operating systems
#               :
#               :
# STATUS        : BETA
#----------------

set -euo pipefail

#======================================
# necessary for running with "set -u"
# until kiwi 9.22.3
#======================================
export DEBUG=1

#======================================
# Functions...
#--------------------------------------
test -f /.kconfig && . /.kconfig
test -f /.profile && . /.profile

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

#======================================
# Setup baseproduct link
#--------------------------------------
suseSetupProduct

#======================================
# Add missing gpg keys to rpm
#--------------------------------------
suseImportBuildKey

#======================================
# Disable recommends
#--------------------------------------
sed -i 's/.*solver.onlyRequires.*/solver.onlyRequires = true/g' /etc/zypp/zypp.conf

#======================================
# Exclude docs installation
#--------------------------------------
sed -i 's/.*rpm.install.excludedocs.*/rpm.install.excludedocs = yes/g' /etc/zypp/zypp.conf

#======================================
# Exclude the installation of multiversion kernels
#--------------------------------------
sed -i 's/^multiversion/# multiversion/' /etc/zypp/zypp.conf

#======================================
# Setup default target, multi-user
#--------------------------------------
baseSetRunlevel 3

#==========================================
# remove package docs
#------------------------------------------
rm -rf /usr/share/doc/packages/*
rm -rf /usr/share/doc/manual/*
rm -rf /opt/kde*

#======================================
# only basic version of vim is
# installed; no syntax highlighting
# only perform the modification if
# /etc/vimrc is actually there
#--------------------------------------
if [ -f /etc/vimrc ]; then
    sed -i -e's/^syntax on/" syntax on/' /etc/vimrc
fi

function vagrantSetup {
    # This function configures the image to work as a vagrant box.
    # These are the following steps:
    # - add the vagrant user to /etc/sudoers
    # - insert the insecure vagrant ssh key
    # - create the default /vagrant share
    # - apply some recommended ssh settings

    # insert the default insecure ssh key from here:
    # https://github.com/hashicorp/vagrant/blob/master/keys/vagrant.pub
    mkdir -p /home/vagrant/.ssh/
    chmod 0700 /home/vagrant/.ssh/
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key" > /home/vagrant/.ssh/authorized_keys
    chmod 0600 /home/vagrant/.ssh/authorized_keys
    chown -R vagrant:vagrant /home/vagrant/

    # apply recommended ssh settings for vagrant boxes
    SSHD_CONFIG=/etc/ssh/sshd_config.d/99-vagrant.conf
    if [[ ! -d "$(dirname ${SSHD_CONFIG})" ]]; then
        SSHD_CONFIG=/etc/ssh/sshd_config
        # prepend the settings, so that they take precedence
        echo -e "UseDNS no\nGSSAPIAuthentication no\n$(cat ${SSHD_CONFIG})" > ${SSHD_CONFIG}
    else
        echo -e "UseDNS no\nGSSAPIAuthentication no" > ${SSHD_CONFIG}
    fi

    # vagrant assumes that it can sudo without a password
    # => add the vagrant user to the sudoers list
    SUDOERS_LINE="vagrant ALL=(ALL) NOPASSWD: ALL"
    if [ -d /etc/sudoers.d ]; then
        echo "$SUDOERS_LINE" >| /etc/sudoers.d/vagrant
        visudo -cf /etc/sudoers.d/vagrant
        chmod 0440 /etc/sudoers.d/vagrant
    else
        echo "$SUDOERS_LINE" >> /etc/sudoers
        visudo -cf /etc/sudoers
    fi

    # the default shared folder
    mkdir -p /vagrant
    chown -R vagrant:vagrant /vagrant

    # SSH service
    baseInsertService sshd

    # start vboxsf service only if the guest tools are present
    if rpm -q virtualbox-guest-tools 2> /dev/null; then
        echo vboxsf > /etc/modules-load.d/vboxsf.conf
    fi

    # drop any network udev rules for libvirt, so that the networks are called
    # ethX
    # this is not required for Virtualbox as it handles networking differently
    # and doesn't need this hack
    if [ "${kiwi_profiles}" != "virtualbox" ]; then
        Rm -f /etc/udev/rules.d/*-net.rules
    fi

    # setup DHCP on eth0 properly
    cat << EOF > /etc/sysconfig/network/ifcfg-eth0
STARTMODE=auto
BOOTPROTO=dhcp
EOF
}

vagrantSetup

#=================================================
# "Disable" purge-kernels so that the process is not
# blocking zypper pointlessly during the first boot
#=================================================
Rm -f /boot/do_purge_kernels

#=================================================
# enable haveged to get enough entropy in a VM
# see: bsc#1131369
#-------------------------------------------------
baseInsertService haveged

#=================================================
# configure openSUSE repositories from YaST
#-------------------------------------------------

# Leap 42.3's os-release is missing " around some of the values
# => filter them out since they are present in later releases
OS_ID=$(grep '^ID=' /etc/os-release | awk -F'=' '{ print $2 }'| sed 's/"//g')

if [ $(expr match "${OS_ID^^}" "OPENSUSE") -gt 7 ]; then
    add-yast-repos
fi

exit 0
