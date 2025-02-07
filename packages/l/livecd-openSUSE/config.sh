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

# Make the image smaller, work around a hard dep by plasma6-desktop -> signon-ui and kdeplasma6-addons
if rpm -q libQt6WebEngineCore6; then
	rpm -e --nodeps libQt6WebEngineCore6
fi

# Reuse what the macro does
rpm --eval "%fdupes /usr/share/licenses" | sh

#--------------------------------------
# enable and disable services

for i in langset NetworkManager firewalld chronyd; do
	systemctl -f enable $i
done

for i in sshd cron wicked purge-kernels; do
	systemctl -f disable $i || true
done

echo '# multipath needs to be excluded from dracut as it breaks os-prober' > /etc/dracut.conf.d/no-multipath.conf
echo 'omit_dracutmodules+=" multipath "' >> /etc/dracut.conf.d/no-multipath.conf

# Stronger compression for the initrd
echo 'compress="xz -9 --check=crc32 --memlimit-compress=50%"' >> /etc/dracut.conf.d/less-storage.conf

# Smaller initrd where necessary
if [ "$desktop" = "x11" ] || [ "$desktop" = "xfce" ]; then
	# Forcibly exclude networking support
	sed -i 's/echo network rootfs-block/echo rootfs-block/' /usr/lib/dracut/modules.d/90kiwi-live/module-setup.sh
	echo 'omit_dracutmodules+=" network qemu-net rdma "' >> /etc/dracut.conf.d/no-network.conf

	# This only needs to be able to boot the live cd
	echo 'omit_dracutmodules+=" bcache crypt lvm lunmask mdraid nvdimm "' >> /etc/dracut.conf.d/less-storage.conf

	# Unnecessary modules in the initrd
	echo 'omit_drivers+=" ceph chcr cifs csiostor cxgb4 intel_qat ocfs2 bnx2fc qedf "' >> /etc/dracut.conf.d/less-storage.conf

	# Work around https://github.com/OSInside/kiwi/issues/1751
	sed -i '/omit_dracutmodules=/d' /usr/bin/dracut
fi

# Only used for OpenCL and X11 acceleration on vmwgfx (?), saves ~50MiB
rpm -e --nodeps Mesa-gallium
# Too big and will have to be dropped anyway (unmaintained, known security issues)
rm -rf /usr/lib*/libmfxhw*.so.* /usr/lib*/mfx/

if [ "$desktop" = "x11" ]; then
	# Generated on boot if missing
	rm /etc/udev/hwdb.bin
	# xfce4-pulseaudio-plugin is omitted, remove it from the panel config.
	# To avoid having to mess with IDs, just replace it with a separator.
	sed -i 's/"pulseaudio"/"separator"/' /etc/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml
fi

# Kernel modules (+ firmware) for X13s
if [ "$(arch)" == "aarch64" ]; then
	echo 'add_drivers+=" clk-rpmh dispcc-sc8280xp gcc-sc8280xp gpucc-sc8280xp nvmem_qcom-spmi-sdam qcom_hwspinlock qcom_q6v5 qcom_q6v5_pas qnoc-sc8280xp pmic_glink pmic_glink_altmode smp2p spmi-pmic-arb leds-qcom-lpg "'  > /etc/dracut.conf.d/x13s_modules.conf
	echo 'add_drivers+=" nvme phy_qcom_qmp_pcie pcie-qcom-ep i2c_hid_of i2c_qcom_geni leds-qcom-lpg pwm_bl qrtr pmic_glink_altmode gpio_sbu_mux phy_qcom_qmp_combo panel-edp msm phy_qcom_edp "' >> /etc/dracut.conf.d/x13s_modules.conf
	echo 'install_items+=" /lib/firmware/qcom/sc8280xp/LENOVO/21BX/qcadsp8280.mbn.xz /lib/firmware/qcom/sc8280xp/LENOVO/21BX/qccdsp8280.mbn.xz "' >> /etc/dracut.conf.d/x13s_modules.conf
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
rm -rf /usr/{lib,share}/locale/{a,b,c,da,dz,e,fa,fi,g,h,i,ja,k,l,m,n,o,p,r,s,t,u,v,w,z}*
rm -rf /usr/share/qt5/translations/*_{ca,cs,da,es,it,ja,fi,hu,id,ko,nl,pl,pr_BR,tr,ro,ru,sk,sr,sv,uk,vi,cmn_TW,zh}*
zypper --non-interactive rm yast2-trans-{uk,sv,ru,ja,da,cs,sr,vi} || :

# Some packages really exaggerate here
rm -rf /usr/share/doc/packages/*

# Save more than 150 MiB by removing this, not very useful for lives
rm -rf /lib/firmware/{amdgpu/{gc_,isp,psp}*,amdnpu,liquidio,netronome,qca,qed,mrvl,mellanox,cypress,dpaa2,bnx2x,cxgb4,intel/vsc,intel/ipu,ueagle-atm,xe}
if [ "$(arch)" == "aarch64" ]; then
	# Keep some qcom firmware for Lenovo X13s and delete others (save ~50MiB)
	rm -rf /lib/firmware/qcom/{apq8016,apq8096,qcm2290,qrb4210,sdm845,sm8250,venus*,vpu*}
else
	rm -rf /lib/firmware/qcom
fi
# the new, optional nvidia gsp firmware blobs are huge - ~ 70MB
find /lib/firmware/nvidia -name gsp | xargs -r rm -rf 

# Remove the mellanox kernel drivers (firmware is removed too)
rm -rf /lib*/modules/*/kernel/drivers/net/ethernet/mellanox

# The gems are unpackaged already, no need to store them twice
rm -rf /usr/lib*/ruby/gems/*/cache/

# Not needed, boo#1166406
rm -f /boot/vmlinux*.[gx]z /lib/modules/*/vmlinux*.[gx]z
# Also not needed
rm -f /boot/System.map-* /lib/modules/*/System.map

# Decompress kernel modules, better for squashfs (boo#1192457)
find /lib/modules/*/kernel -name '*.ko.xz' -exec xz -d {} +
find /lib/modules/*/kernel -name '*.ko.zst' -exec zstd --rm -d {} +
for moddir in /lib/modules/*; do
	depmod "$(basename "$moddir")"
done

# Add repos from /etc/YaST2/control.xml
add-yast-repos
zypper --non-interactive rm -u live-add-yast-repos

# Install README.BETA where expected by YaST
cp /usr/lib/skelcd/CD1/README.BETA / || :
zypper --non-interactive rm -u skelcd-openSUSE || :

# Remove the zypper locks needed for a slimmer system
zypper rl $(seq 1 $(zypper ll | wc -l))

#======================================
# sudoers hack to fix #297695 
# (Installation Live CD: no need to ask for password of root)
#--------------------------------------
echo "linux ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/50-livecd

/usr/sbin/useradd -m -u 1000 linux -c "Live-CD User" -p ""

# delete passwords
passwd -d root
passwd -d linux
# empty password is ok
pam-config -a --nullok

: > /var/log/zypper.log
: > /var/log/tallylog

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
