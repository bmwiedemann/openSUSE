#!/bin/bash
# Copyright (c) 2019 SUSE LLC
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
echo ** "reset machine settings"
sed -i 's/^root:[^:]*:/root:*:/' /etc/shadow
rm -f /etc/machine-id \
      /var/lib/zypp/AnonymousUniqueId \
      /var/lib/systemd/random-seed \
      /var/lib/dbus/machine-id

# Remove root password
passwd -d root
pam-config -a --nullok

# Support SSH into the root user
echo 'PermitEmptyPasswords yes' >> /etc/ssh/sshd_config

#======================================
# Specify default runlevel
#--------------------------------------
baseSetRunlevel multi-user.target

#======================================
# Add missing gpg keys to rpm
#--------------------------------------
suseImportBuildKey

#======================================
# Enable sshd
#--------------------------------------
systemctl enable sshd.service

# Enable jeos-firstboot
mkdir -p /var/lib/YaST2
touch /var/lib/YaST2/reconfig_system

systemctl mask systemd-firstboot.service
systemctl enable jeos-firstboot.service

# Enable firewalld if installed
if [ -x /usr/sbin/firewalld ]; then
    systemctl enable firewalld
fi

#======================================
# Add repos from control.xml
#--------------------------------------
if grep -q opensuse /usr/lib/os-release; then
    add-yast-repos
    zypper --non-interactive rm -u live-add-yast-repos
fi

#=====================================
# Configure snapper
#-------------------------------------
if [ "${kiwi_btrfs_root_is_snapshot-false}" = 'true' ]; then
    echo "creating initial snapper config ..."
    # we can't call snapper here as the .snapshots subvolume
    # already exists and snapper create-config doesn't like
    # that.
    cp /etc/snapper/config-templates/default /etc/snapper/configs/root
    # Change configuration to match SLES12-SP1 values
    sed -i -e '/^TIMELINE_CREATE=/s/yes/no/' /etc/snapper/configs/root
    sed -i -e '/^NUMBER_LIMIT=/s/50/10/'     /etc/snapper/configs/root

    baseUpdateSysConfig /etc/sysconfig/snapper SNAPPER_CONFIGS root
fi

#=====================================
# Enable chrony if installed
#-------------------------------------
if [ -f /etc/chrony.conf ]; then
    systemctl enable chronyd.service
fi

#======================================
# Disable recommends on virtual images (keep hardware supplements, see bsc#1089498)
#--------------------------------------
sed -i 's/.*solver.onlyRequires.*/solver.onlyRequires = true/g' /etc/zypp/zypp.conf

#======================================
# Disable installing documentation
#--------------------------------------
sed -i 's/.*rpm.install.excludedocs.*/rpm.install.excludedocs = yes/g' /etc/zypp/zypp.conf

#======================================
# Configure salt-minion (Yomi)
#--------------------------------------
# Add a random UUID grains to identify as a valid image
uuid=$(uuidgen --md5 --namespace @dns --name http://opensuse.org/$((RANDOM%10)))
cat >> /etc/salt/grains <<-EOF
	# Valid UUID generated during the image creation
	uuid: $uuid
EOF

# Enable autosign via UUID and configure the master address
cat >> /etc/salt/minion.d/autosign.conf <<-EOF
	# Enable autosign via UUID grains
	autosign_grains:
	    - uuid
EOF

# Opt-in for the new way of executing modules within states (only
# required pre-Sodium releases)
cat >> /etc/salt/minion.d/module.run.conf <<-EOF
	# New way of executing modules within states
	use_superseded:
	    - module.run
EOF

mkdir -p /etc/systemd/system/salt-minion.service.d/

# Add a systemd overlay for salt-minion.service that will set the
# master address to looking for.  We can inject the master address via
# the boot parameters, using the variable 'master'.  For example:
# 'master=10.0.2.2'.  By default the master address will be 'salt'
cat > /usr/bin/master.sh <<-'EOF'
	#!/bin/sh

	# Default value of master
	master=salt

	# Search for the parameter 'master=' in /proc/cmdline
	for arg in $(cat /proc/cmdline); do
	    [[ "$arg" =~ ^master=.*$ ]] && master="${arg#master=}"
	done

	[ -f /etc/salt/minion.d/master.conf ] || echo "master: $master" > /etc/salt/minion.d/master.conf
EOF
chmod a+x /usr/bin/master.sh

cat > /etc/systemd/system/salt-minion.service.d/10-master.conf <<-EOF
	[Service]
	ExecStartPre=/usr/bin/master.sh
EOF

# Add a systemd overlay for salt-minion.service, that will add into
# the minion_id the based on some priorities:
#
#   - minion_id boot parameter
#   - hostname (FQDN) if is different from localhost
#   - the MAC address of the first interface
#
# This algorithm replaces the default minion ID, that is the
# IP address of the main interface.
cat > /usr/bin/minion_id.sh <<-'EOF'
	#!/bin/sh

	# Search for the parameter 'minion_id=' in /proc/cmdline
	for arg in $(cat /proc/cmdline); do
	    [[ "$arg" =~ ^minion_id=.*$ ]] && minion_id="${arg#minion_id=}"
	done

	# If there is not parameter, take the hostname
	[ -z "$minion_id" ] && minion_id=$(hostname -f)

	# Get the MAC address of the first interface if hostname is localhost
	shopt -s extglob
	[ "$minion_id" == localhost ] && minion_id=$(cat $(ls -1 /sys/class/net/!(lo)/address | sort | head -n 1))

	[ -f /etc/salt/minion_id ] || echo "$minion_id" > /etc/salt/minion_id
EOF
chmod a+x /usr/bin/minion_id.sh

cat > /etc/systemd/system/salt-minion.service.d/20-minion-id.conf <<-EOF
	[Service]
	ExecStartPre=/usr/bin/minion_id.sh
EOF

systemctl enable salt-minion.service

#======================================
# Config for jeos-firstboot (Yomi)
#--------------------------------------
cat > /etc/jeos-firstboot.conf <<-EOF
	JEOS_LOCALE="en_US.UTF-8"
	JEOS_KEYTABLE="us"
	JEOS_TIMEZONE="UTC"
	JEOS_PASSWORD_ALREADY_SET=1
	JEOS_EULA_ALREADY_AGREED=1
	JEOS_HIDE_SUSECONNECT=1
EOF

#======================================
# Config for nano editor (Yomi)
#--------------------------------------
cat > /etc/nanorc <<-EOF
	include "/usr/share/nano/*.nanorc"
	set suspend
EOF
