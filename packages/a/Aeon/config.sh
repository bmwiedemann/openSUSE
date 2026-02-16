#!/bin/bash
# Copyright (c) 2020 SUSE LLC
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

echo "Configure image: [$kiwi_iname]-[$kiwi_profiles]..."

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
baseSetRunlevel graphical.target

#======================================
# Import trusted rpm keys
#--------------------------------------
suseImportBuildKey

#======================================
# Set hostname by DHCP
#--------------------------------------
baseUpdateSysConfig /etc/sysconfig/network/dhcp DHCLIENT_SET_HOSTNAME yes

# Add repos from /etc/YaST2/control.xml
if [ -x /usr/sbin/add-yast-repos ]; then
	add-yast-repos
	zypper --non-interactive rm -u live-add-yast-repos
fi

#=====================================
# Configure snapper
#-------------------------------------
if [ "${kiwi_btrfs_root_is_snapshot-false}" = 'true' ]; then
        echo "creating initial snapper config ..."
        cp /etc/snapper/config-templates/default /etc/snapper/configs/root \
		|| cp /usr/share/snapper/config-templates/default /etc/snapper/configs/root
        baseUpdateSysConfig /etc/sysconfig/snapper SNAPPER_CONFIGS root

	# Adjust parameters
	sed -i'' 's/^TIMELINE_CREATE=.*$/TIMELINE_CREATE="no"/g' /etc/snapper/configs/root
	sed -i'' 's/^NUMBER_LIMIT=.*$/NUMBER_LIMIT="2-10"/g' /etc/snapper/configs/root
	sed -i'' 's/^NUMBER_LIMIT_IMPORTANT=.*$/NUMBER_LIMIT_IMPORTANT="4-10"/g' /etc/snapper/configs/root
fi

#=====================================
# Enable chrony if installed
#-------------------------------------
if [ -f /etc/chrony.conf ]; then
	systemctl enable chronyd
fi

#=====================================
# Storage configuration
#-------------------------------------

# The %post script can't edit /etc/fstab sys due to https://github.com/OSInside/kiwi/issues/945
# so use the kiwi custom hack
cat >/etc/fstab.script <<"EOF"
#!/bin/sh
set -eux

# https://bugzilla.opensuse.org/show_bug.cgi?id=1246605 change 'ro' to 'ro=vfs'
gawk -i inplace '$2 == "/" && $4 == "compress=zstd:1,ro" { $4 = "compress=zstd:1,ro=vfs" } { print $0 }' /etc/fstab

# Relabel /etc. While kiwi already relabelled it earlier, there are some files created later (boo#1210604).
# The "gawk -i inplace" above also removes the label on /etc/fstab.
if [ -e /etc/selinux/config ]; then
        . /etc/selinux/config
        setfiles -e /proc -e /sys -e /dev /etc/selinux/${SELINUXTYPE}/contexts/files/file_contexts /etc
fi
EOF

chmod a+x /etc/fstab.script

#======================================
# Enable NetworkManager
#--------------------------------------
systemctl enable NetworkManager

#======================================
# Enable ZYPP_SINGLE_RPMTRANS
#--------------------------------------
echo '[main]' > /usr/etc/zypp/zypp.conf.d/singletrans.conf
echo 'techpreview.ZYPP_SINGLE_RPMTRANS=1' >> /usr/etc/zypp/zypp.conf.d/singletrans.conf

#======================================
# Add default kernel boot options
#--------------------------------------
serialconsole='console=ttyS0,115200'

cmdline=('quiet' 'loglevel=2' 'systemd.show_status=0' "${serialconsole}" 'console=tty0' 'vt.global_cursor_default=0')

ignition_platform='metal'

if [ -n "${ignition_platform}" ]; then
	cmdline+=("ignition.platform.id=${ignition_platform}")
fi

#======================================
# If SELinux is installed, configure it like transactional-update setup-selinux
#--------------------------------------
if [[ -e /etc/selinux/config ]]; then
	cmdline+=("security=selinux selinux=1")
	# Adjust selinux config
	sed -i -e 's|^SELINUX=.*|SELINUX=enforcing|g' \
	    -e 's|^SELINUXTYPE=.*|SELINUXTYPE=targeted|g' \
	    "/etc/selinux/config"

	# Move an /.autorelabel file from initial installation to writeable location
	test -f /.autorelabel && mv /.autorelabel /etc/selinux/.autorelabel
fi

if [ -e /etc/default/grub ]; then
	sed -i "s#^GRUB_CMDLINE_LINUX_DEFAULT=.*\$#GRUB_CMDLINE_LINUX_DEFAULT=\"${cmdline[*]}\"#" /etc/default/grub
else
	echo "${cmdline[*]}" > /etc/kernel/cmdline
fi

#======================================
# systemd-boot specifics
#--------------------------------------
if rpm -q sdbootutil; then
	for d in /usr/lib/modules/*; do
		test -d "$d" || continue
		depmod -a "${d##*/}"
	done
	ENTRY_TOKEN=$(. /usr/lib/os-release; echo $ID)
	mkdir -p /etc/kernel
	echo "$ENTRY_TOKEN" > /etc/kernel/entry-token
	# FIXME: kiwi needs /boot/efi to exist before syncing the disk image
	mkdir -p /boot/efi
	mkdir -p /boot/efi/loader/entries
        echo -e "LOADER_TYPE=systemd-boot\nSECURE_BOOT=yes" > /etc/sysconfig/bootloader
fi

#======================================
# Aeon specifics
#--------------------------------------

echo 'ExecStartPre=/bin/sh -c "echo 'Please wait.. setting up your computer.. this may take a few minutes'"' >> /usr/lib/dracut/modules.d/30ignition/ignition-disks.service
echo 'StandardOutput=tty' >> /usr/lib/dracut/modules.d/30ignition/ignition-disks.service

setsebool -P selinuxuser_execmod 1
setsebool -P selinuxuser_execheap 1
setsebool -P selinuxuser_execstack 1

# gh#AeonDesktop/project#7
systemctl mask systemd-growfs-root.service

#======================================
# tik specifics - all of the below has to be undone by tik's SelfInstallCleanup post module or systemd-repart-branding-Aeon to ExcludeFiles=
#--------------------------------------

mkdir -p /ignition

useradd -m tik
usermod -aG wheel tik

cat >> /etc/sudoers.d/51-tik << "EOF"
tik ALL = (root) NOPASSWD: ALL
EOF

cat >> /etc/polkit-1/rules.d/10-tik.rules << "EOF"
polkit.addRule(function(action, subject) {
    if (subject.user == "tik") {
        return polkit.Result.YES;
    }
});
EOF

chown tik:users /ignition

mkdir -p /home/tik/.local/share/applications/
chown -R tik:users /home/tik/.local/
cat >> /home/tik/.local/share/applications/org.opensuse.tik.desktop << "EOF"
[Desktop Entry]
Name=Aeon Desktop Installer
Comment=Installs Aeon Desktop
Exec=/usr/bin/tik
Icon=distributor-logo-Aeon-symbolic
Type=Application
Categories=System;
Name[en_GB]=Aeon Desktop Installer
EOF

ln -s /home/tik/.local/share/applications/org.opensuse.tik.desktop /home/tik/.config/autostart/org.opensuse.tik.desktop
rm /home/tik/.config/autostart/aeon-firstboot.desktop

mkdir -p /home/tik/.config/gtk-3.0
echo "file:///ignition" >> /home/tik/.config/gtk-3.0/bookmarks

sed -i 's/DISPLAYMANAGER_AUTOLOGIN=""/DISPLAYMANAGER_AUTOLOGIN="tik"/' /etc/sysconfig/displaymanager

