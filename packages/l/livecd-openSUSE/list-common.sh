buildignore poppler-data
buildignore tin
buildignore desktop-translations
buildignore ft2demos
buildignore gimp-help
buildignore gimp-lang
buildignore libreoffice-base
buildignore libreoffice-mailmerge
buildignore libreoffice-math
buildignore libreoffice-filters-optional
buildignore libreoffice-pyuno
buildignore readline-doc
buildignore graphviz
buildignore linux-kernel-headers
buildignore bash-doc
buildignore gimp-plugins-python
buildignore patterns-openSUSE-gnome_basis_opt
buildignore patterns-openSUSE-gnome_admin
buildignore patterns-openSUSE-gnome_multimedia_opt
buildignore patterns-openSUSE-gnome_imaging_opt
buildignore patterns-openSUSE-gnome_office_opt
buildignore patterns-openSUSE-apparmor_opt
buildignore patterns-openSUSE-enhanced_base_opt
buildignore patterns-openSUSE-fonts_opt
buildignore patterns-openSUSE-imaging_opt
buildignore patterns-openSUSE-kde_utilities_opt
buildignore patterns-openSUSE-multimedia_opt
buildignore patterns-openSUSE-non_oss_opt
buildignore patterns-openSUSE-office_opt
buildignore patterns-openSUSE-x11_opt
buildignore patterns-gnome-gnome_basis_opt
buildignore patterns-gmome-gnome_admin
buildignore patterns-gnome-gnome_multimedia_opt
buildignore patterns-gnome-gnome_imaging_opt
buildignore patterns-gnome-gnome_office_opt
buildignore patterns-base-apparmor_opt
buildignore patterns-base-enhanced_base_opt
buildignore patterns-fonts-fonts_opt
buildignore patterns-desktop-imaging_opt
buildignore patterns-kde-kde_utilities_opt
buildignore patterns-desktop-multimedia_opt
buildignore patterns-openSUSE-non_oss_opt
buildignore patterns-office-office_opt
buildignore patterns-base-x11_opt
buildignore patterns-base-x11_enhanced
buildignore make
buildignore netpbm
buildignore p7zip-full
buildignore busybox-static
buildignore inxi

# Just too big
buildignore sane-backends

install branding-openSUSE
install gfxboot i686
install shim x86_64

# Don't pull in any -32bit libs
buildignore glibc-32bit

buildignore libvdpau_r300
buildignore libvdpau_radeonsi
buildignore libvdpau_r600
buildignore pavucontrol
buildignore libqmi-tools

buildignore 'python*-pip'

buildignore multipath-tools-rbd

buildignore acpica
buildignore xorg-x11-Xvnc
buildignore cabextract
buildignore sssd
buildignore db-utils
buildignore dnsmasq
buildignore fribidi
buildignore ipmitool
buildignore irda
buildignore lomoco
buildignore mksh

# Ignore samba
buildignore cifs-utils
buildignore gvfs-backend-samba

# Legacy packages - not actually used, but pull in quite a lot
buildignore xorg-x11
buildignore xorg-x11-essentials
buildignore xorg-x11-server-extra
# config.sh enables autologin and configures the display-manager
install xdm
install sysvinit-tools
# We already have a different desktop
buildignore icewm
# We have enough fonts already
buildignore baekmuk-ttf-fonts
buildignore google-droid-fonts
# pcf fonts aren't really useful anymore
buildignore efont-unicode-bitmap-fonts
buildignore baekmuk-bitmap-fonts
buildignore intlfonts-chinese-big-bitmap-fonts
buildignore xorg-x11-fonts
buildignore xorg-x11-fonts-legacy

buildignore strace
buildignore tcsh
buildignore usbmuxd

# This would otherwise create a password prompt
# See also https://bugzilla.opensuse.org/show_bug.cgi?id=544314 and
# https://bugzilla.opensuse.org/show_bug.cgi?id=537343
buildignore gnome-keyring-pam

buildignore apparmor-docs
buildignore mutt-doc

# Do not buildignore here. Needed by pidgin in Xfce Live CD.
# buildignore cyrus-sasl

# Pulls in libgnustep
buildignore unar

# Pulled in by python3-kiwi in the buildroot
buildignore jing

# Won't work with current firefox anyway
buildignore icedtea-web

# Recommended by base_x11
buildignore tigervnc

# Recommended by enhanced_base
buildignore autofs
buildignore expect
buildignore m4
buildignore mutt
buildignore net-snmp
buildignore procmail
buildignore recode
buildignore spax

# Recommended by rest_cd_core
buildignore awesfx
buildignore espeak
buildignore pam_mount

# Recommended by man
buildignore groff-full

# Pulls in various python2 modules
buildignore tuned

# Printing support needs too much data (PPDs) to be useful
buildignore cups
buildignore cups-client
buildignore system-config-printer
buildignore ghostscript
buildignore ghostscript-fonts-std
buildignore ghostscript-fonts-other
buildignore manufacturer-PPDs
buildignore gutenprint
buildignore hplip-hpijs
buildignore hplip
buildignore system-config-printer-applet
buildignore udev-configure-printer

# systemd-coredump makes no sense on a live image: there are no debuginfo installed
buildignore systemd-coredump
buildignore systemd-doc
buildignore man-pages

# VPNC is no longer
buildignore NetworkManager-vpnc-gnome
buildignore plasma-nm5-vpnc

# smtp_daemon is recommended by mdadm
buildignore busybox-sendmail
buildignore exim
buildignore msmtp-mta
buildignore postfix
buildignore postfix-bdb
buildignore sendmail

# Can't install this with the latest kernel due to boo#1095148
# And virtualbox is build failed on i586 in TW - 20180617 maxlin
buildignore virtualbox-guest-tools
buildignore virtualbox-guest-x11

# bsc#1125156
buildignore intel-gpu-tools

# For certain features in VMs using the spice protocol
install spice-vdagent
# Same for VMware, but unfortunately too big (~15MiB!)
buildignore open-vm-tools

# Pulls in tcl
buildignore usb_modeswitch

# Of course it's too big
buildignore gstreamer-plugins-rs

# Make vim smaller
buildignore vim-data
buildignore vim
install vim-small

# This was previously required by rest_cd_core
install kernel-default
# The compressed (-all) version results in a bigger .iso!
install kernel-firmware
install patterns-base-enhanced_base
installPattern enhanced_base
install patterns-base-x11
installPattern x11
installPattern sw_management

# checkmedia is used for the 'Check media' entry in grub
install checkmedia

# For working with filesystems
install bcache-tools
install btrfsprogs
install cryptsetup
install device-mapper
install dmraid
install dosfstools
install e2fsprogs
install exfatprogs
install jfsutils
install mdadm
install multipath-tools
install ntfs-3g
install ntfsprogs
install nvme-cli
install quota
install xfsdump
install xfsprogs

# This was previously recommended by rest_cd_core
install adaptec-firmware
install atmel-firmware
install b43-fwcutter
install bluez-firmware
install crda
install dmidecode
install efibootmgr
install gtk2-branding-openSUSE
install ipw-firmware
install iw
install libatm1
install lsb-release
install lvm2
install memtest86+ i686,x86_64
install mpt-firmware
install nano
install pptp
install quota
install rsync
install smartmontools
install smbios-utils-python  i686,x86_64
install util-linux
install wireless-regdb
install wpa_supplicant
install xf86-video-ark
install xf86-video-ati
install xf86-video-chips
install xf86-video-fbdev
install xf86-video-i128
install xf86-video-mga
install xf86-video-neomagic
install xf86-video-nouveau
install xf86-video-nv
install xf86-video-qxl
install xf86-video-r128
install xf86-video-savage
install xf86-video-siliconmotion i686,x86_64
install xf86-video-sis
install xf86-video-sisusb
install xf86-video-tdfx
install xf86-video-v4l
install xf86-video-vesa
#install xf86-video-voodoo
install xz
install zd1211-firmware
install zip

# Workaround for bsc#1131492
buildignore ntp
