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

mkdir /var/lib/misc/reconfig_system

#======================================
# Greeting...
#--------------------------------------
echo "Configure image: [$kiwi_iname]..."

#======================================
# add missing fonts
#--------------------------------------
CONSOLE_FONT="eurlatgr.psfu"

#======================================
# prepare for setting root pw, timezone
#--------------------------------------
echo ** "reset machine settings"
passwd -d root
pam-config -a --nullok

# Support SSH into the root user
echo 'PermitEmptyPasswords yes' >> /etc/ssh/sshd_config

rm -f /etc/machine-id \
      /var/lib/zypp/AnonymousUniqueId \
      /var/lib/systemd/random-seed \
      /var/lib/dbus/machine-id

#======================================
# SuSEconfig
#--------------------------------------
echo "** Running suseConfig..."
suseConfig

echo "** Running ldconfig..."
/sbin/ldconfig

#======================================
# Setup baseproduct link
#--------------------------------------
suseSetupProduct

#======================================
# Specify default runlevel
#--------------------------------------
baseSetRunlevel 3

#======================================
# Add missing gpg keys to rpm
#--------------------------------------
suseImportBuildKey

#======================================
# Enable sshd
#--------------------------------------
chkconfig sshd on

# Enable jeos-firstboot
mkdir -p /var/lib/YaST2
touch /var/lib/YaST2/reconfig_system

systemctl mask systemd-firstboot.service
systemctl enable jeos-firstboot.service

# Enable firewalld if installed
if [ -x /usr/sbin/firewalld ]; then
    chkconfig firewalld on
fi

# Set GRUB2 to boot graphically (bsc#1097428)
sed -Ei"" "s/#?GRUB_TERMINAL=.+$/GRUB_TERMINAL=gfxterm/g" /etc/default/grub
sed -Ei"" "s/#?GRUB_GFXMODE=.+$/GRUB_GFXMODE=auto/g" /etc/default/grub

# Systemd controls the console font now
echo FONT="$CONSOLE_FONT" >> /etc/vconsole.conf

#======================================
# SSL Certificates Configuration
#--------------------------------------
echo '** Rehashing SSL Certificates...'
update-ca-certificates

if [ ! -s /var/log/zypper.log ]; then
    > /var/log/zypper.log
fi

#======================================
# Import trusted rpm keys
#--------------------------------------
for i in /usr/lib/rpm/gnupg/keys/gpg-pubkey*asc; do
    # importing can fail if it already exists
    rpm --import $i || true
done

#======================================
# Add repos from control.xml
#--------------------------------------
add-yast-repos
zypper --non-interactive rm -u live-add-yast-repos

# only for debugging
#systemctl enable debug-shell.service

#=====================================
# Enable chrony if installed
#-------------------------------------
if [ -f /etc/chrony.conf ]; then
    suseInsertService chronyd
    for i in 0 1 2 3; do
	echo "server $i.opensuse.pool.ntp.org iburst"
    done > /etc/chrony.d/opensuse.conf
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
# 'master=master'.  By default the master address will be 'master'
cat > /usr/bin/master.sh <<-'EOF'
	#!/bin/sh

	# Default value of master
	master=master

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

suseInsertService salt-minion

#======================================
# Config for jeos-firstboot (Yomi)
#--------------------------------------
cat > /etc/jeos-firstboot.conf <<-EOF
	JEOS_LOCALE="en_US"
	JEOS_KEYTABLE="us"
	JEOS_TIMEZONE="UTC"
	JEOS_PASSWORD_ALREADY_SET=1
EOF

# Not compatible with set -e
baseCleanMount || true

exit 0
