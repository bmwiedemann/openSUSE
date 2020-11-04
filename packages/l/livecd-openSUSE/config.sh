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

exec | tee /var/log/config.log
exec 2>&1

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

# GTK 3 hard-requires this for some reason. The only GTK3 application is Firefox,
# which has its own icons and we have breeze for the rest.
[ "$desktop" = "kde" -o "$desktop" = "x11" ] && rpm -e --nodeps adwaita-icon-theme

#--------------------------------------
# enable and disable services

for i in langset NetworkManager firewalld spice-vdagentd; do
	systemctl -f enable $i
done

for i in sshd cron wicked purge-kernels; do
	systemctl -f disable $i
done

echo '# multipath needs to be excluded from dracut as it breaks os-prober' > /etc/dracut.conf.d/no-multipath.conf
echo 'omit_dracutmodules+=" multipath "' >> /etc/dracut.conf.d/no-multipath.conf

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
rm -rf /usr/share/locale/{uk,sv,ru,ja,da,cs,sr,vi}
zypper --non-interactive rm yast2-trans-{uk,sv,ru,ja,da,cs,sr,vi} || :

# Some packages really exaggerate here
rm -rf /usr/share/doc/packages/*

# Save more than 200 MiB by removing this, not very useful for lives
rm -rf /lib/firmware/{liquidio,netronome,qed,mrvl,mellanox,qcom}

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

if [ "$desktop" = "kde" ]; then
    # bug 989897, avoid creating desktop directory on KDE so that the default items are added on first login
    cp /usr/share/applications/installation.desktop /usr/share/kio_desktop/DesktopLinks/
    # Also show the update icon if the .desktop file is available
    cp /usr/share/applications/upgrade.desktop /usr/share/kio_desktop/DesktopLinks/ || :
    # Set the application as being "trusted"
    chmod a+x /usr/share/kio_desktop/DesktopLinks/installation.desktop
    chmod a+x /usr/share/kio_desktop/DesktopLinks/upgrade.desktop || :
elif [ "$desktop" = "xfce" ]; then
    # Add Installation icon to desktop folder
    mkdir -p /home/linux/.config /home/linux/Desktop
    echo 'XDG_DESKTOP_DIR="$HOME/Desktop"' > /home/linux/.config/user-dirs.dirs
    cp /usr/share/applications/installation.desktop /home/linux/Desktop/
    # Set the application as being "trusted"
    chown -R linux /home/linux/Desktop/installation.desktop
    chmod a+x /home/linux/Desktop/installation.desktop
# else case disabled: 'x11' (rescue) does not contain the installer, GNOME Shell has no concept of 'desktop'
#else
#    # Add Installation icon to desktop folder
#    mkdir -p /home/linux/.config /home/linux/Desktop
#    echo 'XDG_DESKTOP_DIR="$HOME/Desktop"' > /home/linux/.config/user-dirs.dirs
#    ln -s /usr/share/applications/installation.desktop /home/linux/Desktop/
#    # Set the application as being "trusted"
#    chmod a+x /home/linux/Desktop/installation.desktop
fi

chown -R linux /home/linux

chkstat --system --set

ln -s /usr/lib/systemd/system/runlevel5.target /etc/systemd/system/default.target
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

# Remove netronome firmware (part of kernel-firmware): this sums up to 125MB
rm -rf /lib/firmware/netronome/

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
