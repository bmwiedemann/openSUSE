#!/bin/bash
# Copyright (c) 2025 SUSE LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
#======================================
# Functions...
#--------------------------------------
test -f /.kconfig && . /.kconfig
test -f /.profile && . /.profile

set -euxo pipefail

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]-[$kiwi_profiles]..."

#======================================
# add missing fonts
#--------------------------------------
# Systemd controls the console font now
echo FONT="eurlatgr.psfu" >> /etc/vconsole.conf

#======================================
# prepare for setting root pw, timezone
#--------------------------------------
echo "** reset machine settings"
rm -f /etc/machine-id \
      /var/lib/zypp/AnonymousUniqueId \
      /var/lib/systemd/random-seed

#======================================
# Specify default systemd target
#--------------------------------------
baseSetRunlevel multi-user.target

#======================================
# Import trusted rpm keys
#--------------------------------------
suseImportBuildKey

#======================================
# Enable sshd
#--------------------------------------
systemctl enable sshd.service

if [ -e /etc/cloud/cloud.cfg ]; then
        systemctl enable cloud-init-local
        systemctl enable cloud-init
        systemctl enable cloud-config
        systemctl enable cloud-final
fi

# Enable jeos-firstboot if installed, disabled by combustion/ignition.
# However, on s390x without KVM the console is not capable of running
# jeos-firstboot, use systemd-firstboot as minimal alternative.
if [[ "$kiwi_profiles" =~ s390x-(dasd|fba|fcp) ]]; then
        systemctl enable systemd-firstboot
        # Enable prompting for the root password
        echo 'root:!unprovisioned' | chpasswd -e
elif rpm -q --whatprovides jeos-firstboot >/dev/null; then
        mkdir -p /var/lib/YaST2
        touch /var/lib/YaST2/reconfig_system
        systemctl mask systemd-firstboot
        systemctl enable jeos-firstboot.service
fi

# Enable firewalld if installed except on VMware
if [ -x /usr/sbin/firewalld ] && [ "$kiwi_profiles" != "VMware" ]; then
        systemctl enable firewalld.service
fi

# Enable NetworkManager if installed
if rpm -q --whatprovides NetworkManager >/dev/null; then
        systemctl enable NetworkManager.service
fi

#======================================
# Add repos from control.xml
#--------------------------------------
if rpm -q live-add-yast-repos; then
	add-yast-repos
	zypper --non-interactive rm -u live-add-yast-repos
fi

#=====================================
# Configure snapper
#-------------------------------------
if [ -x /usr/bin/snapper ]; then
	echo "creating initial snapper config ..."
	# we can't call snapper here as the .snapshots subvolume
	# already exists and snapper create-config doesn't like
	# that.
	cp /etc/snapper/config-templates/default /etc/snapper/configs/root \
		|| cp /usr/share/snapper/config-templates/default /etc/snapper/configs/root
	# Change configuration to match SLES12-SP1 values
	sed -i -e '/^TIMELINE_CREATE=/s/yes/no/' /etc/snapper/configs/root
	sed -i -e '/^NUMBER_LIMIT=/s/50/10/'     /etc/snapper/configs/root

	baseUpdateSysConfig /etc/sysconfig/snapper SNAPPER_CONFIGS root
fi

#=====================================
# Enable chrony if installed
#-------------------------------------
if [ -f /etc/chrony.conf ]; then
	systemctl enable chronyd
fi

#======================================
# Add default kernel boot options
#--------------------------------------
consoles='console=ttyS0,115200 console=tty0'
[[ "$kiwi_profiles" == *"ppc64"* ]] && consoles='console=hvc0,115200 console=tty0'
[[ "$kiwi_profiles" == *"s390x-Cloud"* ]] && consoles='' # autodetect
[[ "$kiwi_profiles" == *"s390x-dasd"* ]] && consoles='hvc_iucv=8'

cmdline=('rw' 'quiet' 'systemd.show_status=1' ${consoles})

[[ "$kiwi_profiles" == *"HyperV"* ]] && cmdline+=('rootdelay=300')

# Configure SELinux if installed
# Note: Because of https://github.com/OSInside/kiwi/issues/2709, the root filesystem
# isn't fully labelled, but the first system snapshot is created after autorelabel
# so this is never visible.
if [[ -e /etc/selinux/config ]]; then
	cmdline+=('security=selinux' 'selinux=1')

	sed -i -e 's|^SELINUX=.*|SELINUX=enforcing|g' \
	       -e 's|^SELINUXTYPE=.*|SELINUXTYPE=targeted|g' \
	       "/etc/selinux/config"
fi

if rpm -q sdbootutil; then
	mkdir -p /etc/kernel
	echo "${cmdline[*]}" > /etc/kernel/cmdline
elif [ -e /etc/default/grub ]; then
	sed -i "s#^GRUB_CMDLINE_LINUX_DEFAULT=.*\$#GRUB_CMDLINE_LINUX_DEFAULT=\"${cmdline[*]}\"#" /etc/default/grub
else
	echo "Unknown bootloader"
	exit 1
fi

# if /etc/zypp/zypp.conf exists, patch it - otherwise rely on packages providing functionality
if [ -f /etc/zypp/zypp.conf ]; then
	#======================================
	# Disable recommends on virtual images (keep hardware supplements, see bsc#1089498)
	#--------------------------------------
	sed -i 's/.*solver.onlyRequires.*/solver.onlyRequires = true/g' /etc/zypp/zypp.conf

	#======================================
	# Disable installing documentation
	#--------------------------------------
	sed -i 's/.*rpm.install.excludedocs.*/rpm.install.excludedocs = yes/g' /etc/zypp/zypp.conf
fi

#======================================
# Configure FDE/BLS specifics
#--------------------------------------
if rpm -q sdbootutil; then
	# FIXME: kiwi needs /boot/efi to exist before syncing the disk image
	mkdir -p /boot/efi

	[ -e /var/lib/YaST2/reconfig_system ] && systemctl enable sdbootutil-enroll.service
fi
