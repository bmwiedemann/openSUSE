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
CONSOLE_FONT="eurlatgr.psfu"

#======================================
# prepare for setting root pw, timezone
#--------------------------------------
echo "** reset machine settings"
rm -f /etc/machine-id \
      /var/lib/zypp/AnonymousUniqueId \
      /var/lib/systemd/random-seed

#======================================
# Specify default runlevel
#--------------------------------------
systemctl set-default graphical.target

# Leap 16 specific
if rpm -q --whatprovides gdm-systemd >/dev/null; then
systemctl enable gdm.service
fi
#======================================
# Add missing gpg keys to rpm
#--------------------------------------
suseImportBuildKey


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

# only for debugging
#systemctl enable debug-shell.service

#=====================================
# Configure snapper
#-------------------------------------
if [ -x /usr/bin/snapper ]; then
        echo "creating initial snapper config ..."
        # we can't call snapper here as the .snapshots subvolume
        # already exists and snapper create-config doens't like
        # that.
        cp /usr/share/snapper/config-templates/default /etc/snapper/configs/root
        # Change configuration to match SLES12-SP1 values
        # Adjust parameters
        sed -i'' 's/^TIMELINE_CREATE=.*$/TIMELINE_CREATE="no"/g' /etc/snapper/configs/root
        sed -i'' 's/^NUMBER_LIMIT=.*$/NUMBER_LIMIT="2-10"/g' /etc/snapper/configs/root
        sed -i'' 's/^NUMBER_LIMIT_IMPORTANT=.*$/NUMBER_LIMIT_IMPORTANT="4-10"/g' /etc/snapper/configs/root

        baseUpdateSysConfig /etc/sysconfig/snapper SNAPPER_CONFIGS root
fi

#=====================================
# Enable chrony if installed
#-------------------------------------
if [ -f /etc/chrony.conf ]; then
	suseInsertService chronyd
fi

#======================================
# Add default kernel boot options
#--------------------------------------

# Ensure splash=silent is set this went recently away with Agama.
cmdline=('rw' 'quiet' 'systemd.show_status=1' 'splash=silent')

# Configure SELinux if installed
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

	# Set GRUB2 to boot graphically (bsc#1097428)
	sed -Ei"" "s/#?GRUB_TERMINAL=.+$/GRUB_TERMINAL=gfxterm/g" /etc/default/grub
	sed -Ei"" "s/#?GRUB_GFXMODE=.+$/GRUB_GFXMODE=auto/g" /etc/default/grub
else
	echo "Unknown bootloader"
	exit 1
fi

cat >>/etc/fstab.script <<"EOF"
# Relabel /etc. While kiwi already relabelled it earlier, there are some files created later (boo#1210604).
if [ -e /etc/selinux/config ]; then
       . /etc/selinux/config
       touch /etc/sysconfig/bootloader # Make sure this exists so it gets labelled
       setfiles -e /proc -e /sys -e /dev /etc/selinux/${SELINUXTYPE}/contexts/files/file_contexts /etc
fi
EOF

chmod a+x /etc/fstab.script

#======================================
# Reduced jeos-firstboot for OEM
# which basically only asks for root password
#--------------------------------------
if rpm -q --whatprovides jeos-firstboot >/dev/null; then
# Disable most of plugins only on gnome-variant where gnome-initial-setup does the job
if rpm -q --whatprovides gdm >/dev/null; then

cat > /etc/jeos-firstboot.conf << 'EOF'
JEOS_TIMEZONE='UTC'
JEOS_LOCALE='en_US'
JEOS_KEYTABLE='en'
# JEOS_PASSWORD_ALREADY_SET='yes'
JEOS_EULA_ALREADY_AGREED='yes'
JEOS_HIDE_SUSECONNECT='yes'
JEOS_ASK_CONSOLE=1

EOF

# List of modules to disable (located under /usr/share/jeos-firstboot/modules)
modules=(
  network
  otp
  ssh_enroll
  status_mail
  user
)

# Disable selected (all) jeos-firstboot modules by making them symlink to /dev/null
for mod in "${modules[@]}"; do
  dest="/etc/jeos-firstboot/modules/$mod"
  mkdir -p "$(dirname "$dest")"
  ln -sf /dev/null "$dest"
done
fi

# Enable jeos-firstboot
mkdir -p /var/lib/YaST2
touch /var/lib/YaST2/reconfig_system

systemctl mask systemd-firstboot.service
systemctl enable jeos-firstboot.service

fi

# Explicitly enable NetworkManager
# Network was off without it
systemctl enable NetworkManager

exit 0
