#!/bin/bash
#================
# FILE          : config.sh
#----------------
# PROJECT       : openSUSE KIWI Image System
# COPYRIGHT     : (c) 2006,2007,2008,2017 SUSE Linux GmbH. All rights reserved
#               :
# AUTHOR        : Marcus Schaefer <ms@suse.de>, Stephan Kulow <coolo@suse.de>, Fabian Vogt <fvogt@suse.com>
#               :
# LICENSE       : BSD
#======================================
# Functions...
#--------------------------------------
test -f /.kconfig && . /.kconfig
test -f /.profile && . /.profile

set -euxo pipefail

pl=$(rpmqpack | grep release-livecd-)

# Get the flavor from the installed (openSUSE|Leap)-release-livecd- RPM
# as <censored> kiwi does not make the flavor accessible
desktop=$(echo "$pl" | awk -F- '{ print $4 }' | tr A-Z a-z)

# Not needed, but required by suse-module-tools (bsc#1116665)
rpm -q binutils && rpm -e --nodeps binutils
# Not needed, but required by dracut-kiwi-live -> cdrkit-cdrtools-compat
rpm -q wodim && rpm -e --nodeps wodim
# Actually a hack: xrdb requires this, but on livecds it's not used
rpm -qa | grep "^cpp" | xargs -r rpm -e --nodeps
rpm -qa | grep "^libisl" | xargs -r rpm -e

# GTK 3 hard-requires this for some reason. The only GTK3 application is Firefox,
# which has its own icons and we have breeze for the rest.
[ "$desktop" = "kde" ] && rpm -e --nodeps adwaita-icon-theme

# Workaround until dropped from xfce4-branding-openSUSE
if [ "$desktop" = "x11" -o "$desktop" = "xfce" ]; then
	if rpm -q xorg-x11-server-Xvfb; then
		rpm -e --nodeps xorg-x11-server-Xvfb
	fi
	rpm -e --nodeps noto-coloremoji-fonts || rpm -e --nodeps google-noto-coloremoji-fonts
fi

#--------------------------------------
# enable and disable services

for i in langset NetworkManager firewalld; do
	systemctl -f enable $i
done

for i in sshd cron wicked purge-kernels; do
	systemctl -f disable $i
done

echo '# multipath needs to be excluded from dracut as it breaks os-prober' > /etc/dracut.conf.d/no-multipath.conf
echo 'omit_dracutmodules+=" multipath "' >> /etc/dracut.conf.d/no-multipath.conf

# Stronger compression for the initrd
echo 'compress="xz -4 --check=crc32 --memlimit-compress=50%"' >> /etc/dracut.conf.d/less-storage.conf

if [ "$desktop" = "x11" ] || [ "$desktop" = "xfce" ]; then
	# Forcibly exclude networking support
	sed -i 's/echo network rootfs-block/echo rootfs-block/' /usr/lib/dracut/modules.d/90kiwi-live/module-setup.sh
	echo 'omit_dracutmodules+=" network "' >> /etc/dracut.conf.d/no-network.conf

	# This only needs to be able to boot the live cd
	echo 'omit_dracutmodules+=" bcache crypt lvm mdraid lunmask "' >> /etc/dracut.conf.d/less-storage.conf

	# Unnecessary modules in the initrd
	echo 'omit_drivers+=" cifs ocfs2 "' >> /etc/dracut.conf.d/less-storage.conf

	# Work around https://github.com/OSInside/kiwi/issues/1751
	sed -i '/omit_dracutmodules=/d' /usr/bin/dracut
fi

if [ "$desktop" = "x11" ]; then
	# Only used for X11 acceleration on vmwgfx, saves ~47MiB
	rpm -e --nodeps Mesa-gallium

	# Generated on boot if missing
	rm /etc/udev/hwdb.bin
fi

cd /

# Import keys for installation
touch /installkey.gpg
gpg --batch --homedir /root/.gnupg --no-default-keyring --ignore-time-conflict --ignore-valid-from --keyring /installkey.gpg --import /usr/lib/rpm/gnupg/keys/*
mkdir -p /pubkeys
for i in /usr/lib/rpm/gnupg/keys/*.asc ; do
	rpm --import $i || true
	ln -s "$i" "/pubkeys/${i##*/}.key"
done

# Craft license.tar.gz used by YaST
EULA_DIR=/etc/YaST2/licenses/base
[ -d "${EULA_DIR}" ] || EULA_DIR=/usr/share/licenses/product/base
(cd "${EULA_DIR}"; tar -cvzf /license.tar.gz *)

# Remove some large locales to save space
rm -rf /usr/{lib,share}/locale/{ca,cs,da,ja,fi,hu,id,ko,nl,pl,tr,ru,sk,sr,sv,uk,vi,cmn_TW,zh}*
rm -rf /usr/share/qt5/translations/*_{ca,cs,da,ja,fi,hu,id,ko,nl,pl,tr,ru,sk,sr,sv,uk,vi,cmn_TW,zh}*
zypper --non-interactive rm yast2-trans-{uk,sv,ru,ja,da,cs,sr,vi} || :

# Some packages really exaggerate here
rm -rf /usr/share/doc/packages/*

# Save more than 200 MiB by removing this, not very useful for lives
rm -rf /lib/firmware/{liquidio,netronome,qed,mrvl,mellanox,qcom,cypress,dpaa2,bnx2x,cxgb4}

# The gems are unpackaged already, no need to store them twice
rm -rf /usr/lib*/ruby/gems/*/cache/

# Not needed, boo#1166406
rm -f /boot/vmlinux*.[gx]z
rm -f /lib/modules/*/vmlinux*.[gx]z

# Decompress kernel modules, better for squashfs (boo#1192457)
find /lib/modules/*/kernel -name '*.ko.xz' -exec xz -d {} +
find /lib/modules/*/kernel -name '*.ko.zst' -exec zstd --rm -d {} +
depmod $(basename /lib/modules/*)

# Add repos from /etc/YaST2/control.xml
add-yast-repos
zypper --non-interactive rm -u live-add-yast-repos

# Install README.BETA where expected by YaST
cp /usr/lib/skelcd/CD1/README.BETA / || :
zypper --non-interactive rm -u skelcd-openSUSE || :

# Remove the zypper locks needed for a slimmer system
zypper rl $(seq 1 $(zypper ll | wc -l))

#======================================
# /etc/sudoers hack to fix #297695 
# (Installation Live CD: no need to ask for password of root)
#--------------------------------------
sed -i -e "s/ALL ALL=(ALL) ALL/ALL ALL=(ALL) NOPASSWD: ALL/" /etc/sudoers 
chmod 0440 /etc/sudoers

/usr/sbin/useradd -m -u 1000 linux -c "Live-CD User" -p ""

# delete passwords
passwd -d root
passwd -d linux
# empty password is ok
pam-config -a --nullok

: > /var/log/zypper.log

# Create fstab if it doesn't exist (Work around boo#1185815)
>>/etc/fstab

# Add Installation and upgrade icons to the desktop
if [ "$desktop" = "kde" ]; then
    # bug 989897, avoid creating desktop directory on KDE so that the default items are added on first login
    cp /usr/share/applications/{installation,upgrade}.desktop /usr/share/kio_desktop/DesktopLinks/
    # Set the application as being "trusted"
    chmod a+x /usr/share/kio_desktop/DesktopLinks/{installation,upgrade}.desktop
elif [ "$desktop" = "xfce" ]; then
    mkdir -p /home/linux/.config /home/linux/Desktop
    echo 'XDG_DESKTOP_DIR="$HOME/Desktop"' > /home/linux/.config/user-dirs.dirs
    cp /usr/share/applications/{installation,upgrade}.desktop /home/linux/Desktop/
    # Set the application as being "trusted"
    chmod a+x /home/linux/Desktop/{installation,upgrade}.desktop
fi
# 'x11' (rescue) does not contain the installer, GNOME Shell has no concept of 'desktop'

chown -R linux /home/linux

chkstat --system --set

ln -s /usr/lib/systemd/system/graphical.target /etc/systemd/system/default.target
baseUpdateSysConfig /etc/sysconfig/displaymanager DISPLAYMANAGER_AUTOLOGIN linux
baseUpdateSysConfig /etc/sysconfig/keyboard YAST_KEYBOARD "english-us,pc104"
baseUpdateSysConfig /etc/sysconfig/keyboard COMPOSETABLE "clear latin1.add"
baseUpdateSysConfig /etc/sysconfig/language RC_LANG ""

baseUpdateSysConfig /etc/sysconfig/console CONSOLE_FONT "eurlatgr.psfu"
baseUpdateSysConfig /etc/sysconfig/console CONSOLE_SCREENMAP trivial
baseUpdateSysConfig /etc/sysconfig/console CONSOLE_MAGIC "(K"
baseUpdateSysConfig /etc/sysconfig/console CONSOLE_ENCODING "UTF-8"

[ "$desktop" = "gnome" ] && displaymanager=gdm
[ "$desktop" = "kde" ] && displaymanager=sddm
[ "$desktop" = "xfce" ] && displaymanager=lightdm
[ "$desktop" = "x11" ] && displaymanager=lightdm
baseUpdateSysConfig /etc/sysconfig/displaymanager DISPLAYMANAGER $displaymanager

# boo#1039756
[ "$desktop" = "gnome" ] && baseUpdateSysConfig /etc/sysconfig/windowmanager DEFAULT_WM gnome

# Disable journal write to disk in live mode, bug 950999
echo "Storage=volatile" >> /etc/systemd/journald.conf

# Remove generated files (boo#1098535)
rm -rf /var/cache/zypp/* /var/lib/zypp/AnonymousUniqueId /var/lib/systemd/random-seed

cat >/etc/systemd/system/fixupbootloader.service <<EOF
# boo#1155545 - LOADER_TYPE has to be nil for the upgrade to work properly.
# Kiwi does not allow changing the file directly, so do it in this ugly way.
[Unit]
Description=Remove LOADER_TYPE from /etc/sysconfig/bootloader
Before=systemd-user-sessions.service

[Service]
Type=oneshot
ExecStart=/usr/bin/gawk -i inplace '!/^LOADER_TYPE=/' /etc/sysconfig/bootloader

[Install]
WantedBy=multi-user.target
EOF

systemctl -f enable fixupbootloader.service
