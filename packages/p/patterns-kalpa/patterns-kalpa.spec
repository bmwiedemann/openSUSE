#
# spec file for package patterns-kalpa
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%bcond_with betatest

Name:           patterns-kalpa
Version:        6.0
Release:        0
Summary:        Patterns for openSUSE Kalpa
License:        MIT
Group:          Metapackages
URL:            http://en.opensuse.org/Patterns
Source0:        %name.rpmlintrc
ExclusiveArch:  x86_64 %arm32 aarch64 ppc64le s390x riscv64

%description
This is an internal package that is used to create the patterns as part
of the installation source setup. Installation of this package does
not make sense.

%package base
Summary:        openSUSE Kalpa
Group:          Metapackages
Provides:       pattern() = kalpa_base
Provides:       pattern-category() = Kalpa
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9200
Provides:       pattern-visible()
%if %{with betatest}
# need to require it as recommends are off
Requires:       pattern() = update_test
%endif

### Packages formerly provided by minimal_base
Requires:       branding
Requires:       build-key
Requires:       distribution-release
Requires:       filesystem

### Packages formerly provided by bootloader
Requires:       (grub2-snapper-plugin if grub2)
Requires:       grub2
%ifarch x86_64
# XXX: not sure this really belongs here. More like a kernel
# rather than bootloader related thing?
Requires:       biosdevname
%endif
%ifnarch s390x ppc64 ppc64le
%if 0%{?is_opensuse}
Requires:       (grub2-branding-openSUSE if branding-openSUSE)
%else
%if 0%{?sle_version}
Requires:       (grub2-branding-SLE if branding-SLE)
%endif
%endif
%endif
%ifarch x86_64
Requires:       grub2-x86_64-efi
%endif
%ifarch aarch64
Requires:       MozillaFirefox
Requires:       grub2-arm64-efi
%endif
%ifarch armv7l armv7hl
Requires:       grub2-arm-efi
Requires:       grub2-arm-uboot
%endif
%ifarch aarch64 x86_64
Requires:       mokutil
Requires:       shim
%endif

### Packages formerly provided by base/basesystem
Requires:       /usr/bin/hostname
Requires:       aaa_base
Requires:       bash
Requires:       branding-openSUSE
Requires:       btrfsprogs
Requires:       ca-certificates
Requires:       ca-certificates-mozilla
Requires:       coreutils
Requires:       coreutils-systemd
Requires:       glibc
Suggests:       busybox-hostname
Requires:       NetworkManager
Requires:       NetworkManager-wifi
Requires:       iproute2
Requires:       lastlog2
Requires:       libnss_usrfiles2
Requires:       openSUSE-build-key
Requires:       pam
Requires:       pam-config
Requires:       procps
Requires:       rebootmgr
Requires:       rpm
Requires:       shadow
Requires:       systemd
Requires:       util-linux
Requires:       group(nobody)
Requires:       user(nobody)

####
Requires:       btrfsmaintenance
Requires:       busybox
Requires:       chrony
# curl indirectly needed by ignition via dracut's url-lib
Requires:       curl
# probably needed for fsck.fat on efi partitions
Requires:       /usr/bin/gzip
Requires:       Kalpa-release
Requires:       dosfstools
Requires:       glibc-locale-base
Suggests:       busybox-gzip
Requires:       health-checker
Requires:       health-checker-plugins-MicroOS
Requires:       iputils
Requires:       issue-generator
%ifnarch %{arm}
Requires:       kdump
%endif
Requires:       less
Requires:       microos-tools
Requires:       openssh
Requires:       snapper
Requires:       vim-small
Requires:       wtmpdb
# people are addicted to sudo
Requires:       sudo
Requires:       system-group-wheel
Requires:       systemd-presets-branding-Kalpa
Requires:       terminfo-base
Requires:       timezone
Conflicts:      gettext-runtime-mini
Conflicts:      krb5-mini
Obsoletes:      suse-build-key < 12.1
Requires:       yast2-logs

### Packages formerly provided by base_zypper
Requires:       transactional-update
Requires:       transactional-update-zypp-config
Requires:       zypper
# zypper ps is useless in transactional mode. It also checks for
# /run/reboot-needed though which is created by transactional-update
Requires:       zypper-needs-restarting

### Packages formerly provided by defaults
Requires:       audit
Requires:       systemd-coredump

### Packages formerly provided by hardware
Requires:       ethtool
%ifnarch s390x
Requires:       irqbalance
%endif
Requires:       fcoe-utils
Requires:       hwinfo
Requires:       susepaste

### Packages formerly provided by selinux
Requires:       container-selinux
Requires:       policycoreutils
Requires:       selinux-policy-targeted
Requires:       selinux-tools

### Packages formerly provided by x11
Requires:       xf86-input-libinput
Requires:       xorg-x11-fonts-core
Requires:       xorg-x11-server
# Recommend something other than xdm, default to lightdm
Recommends:     dejavu-fonts
Recommends:     libyui-qt
Recommends:     libyui-qt-pkg
Recommends:     noto-sans-fonts
Recommends:     tigervnc
Recommends:     x11-tools
Recommends:     xdmbgrd
Recommends:     xorg-x11-Xvnc
Recommends:     xorg-x11-driver-video
Recommends:     xorg-x11-essentials
Recommends:     xorg-x11-fonts
Recommends:     xorg-x11-server-extra
Recommends:     xterm
Recommends:     xtermset
Recommends:     yast2-control-center
# bsc#1071953
%ifnarch s390 s390x
Recommends:     xf86-input-vmmouse
Recommends:     xf86-input-wacom
%endif

### Packages formerly provided by desktop-common
# PipeWire is the default sound server
Requires:       gstreamer-plugin-pipewire
Requires:       pipewire-alsa
Requires:       pipewire-pulseaudio
# Allow users to print (and add some common printer drivers)
Requires:       OpenPrintingPPDs
Requires:       bluez-cups
Requires:       cups
Requires:       cups-filters
Requires:       cups-pk-helper
Requires:       ghostscript
Requires:       hplip-hpijs
Requires:       system-config-printer-common
Requires:       system-config-printer-dbus-service
Requires:       udev-configure-printer
# Add thunderbolt device management (boo#1208150)
Requires:       bolt
# Common tools
Requires:       bash-completion
Requires:       bluez-firmware
Requires:       glibc-locale
Requires:       hicolor-icon-theme-branding-openSUSE
Requires:       policycoreutils-python-utils
Requires:       polkit-default-privs
Requires:       systemd-icon-branding-openSUSE
Requires:       udisks2
Requires:       unzip
Requires:       upower
Requires:       usbutils
Requires:       wget
Requires:       xdg-utils
# For i2c dev handling and permissions
Requires:       ddcutil-i2c-udev-rules
# Support ntfs drives
Requires:       ntfs-3g
Requires:       ntfsprogs
# More "comfortable" base package versions
Requires:       gzip
Requires:       hostname
%if 0%{is_opensuse}
Requires:       avahi
%endif
# Desktop notifications about transactional update succeeding/failing
# for the masses
Requires:       transactional-update-notifier
# Needed by both GNOME and KDE for theming of GTK-based flatpak apps properly
Requires:       xdg-desktop-portal-gtk
# Needed to ensure MicroOS Desktop systems are be able to handle varied hardware out
# of the box, and not only during the system installation.
Requires:       kernel-firmware-all
Requires:       sof-firmware

# from data/COMMON-DESKTOP
Requires:       desktop-data
Requires:       desktop-file-utils
#
# Now the real packages
#
# #332596
# Pull in plasma-branding-MicroOS for firstboot setup
#Requires:       plasma-branding-MicroOS
Requires:       plasma-branding-Kalpa

# Some basic system tools
Requires:       featherpad
Requires:       konsole
# Add KDE Partition Manager (boo#1212925)
Requires:       partitionmanager

# Add ksshaskpass5 (boo#1215407)
Requires:       ksshaskpass6

# Recommended by kde_plasma
Requires:       bluedevil6
Requires:       breeze6-wallpapers
Requires:       dolphin
Requires:       kde-print-manager
Requires:       kgamma6
Requires:       kwrited6
Requires:       phonon-vlc-qt6
Requires:       plasma6-nm

# Manually pull in baloo5-file to better support desktip search functions/desktop integration
Requires:       kf6-baloo-file

# For NetworkManager support of openVPN Connections
Requires:       NetworkManager-openvpn
Requires:       openvpn-auth-pam-plugin
Requires:       plasma6-nm-openconnect
Requires:       plasma6-nm-openvpn

Requires:       kdeplasma6-addons
Requires:       kio-extras
Requires:       kwalletmanager
Requires:       pinentry
Requires:       plasma5-session
Requires:       plasma6-pa
Requires:       sddm-qt6

# Additional Fonts to cover Unicode Symbols not provided by kde_plasma
Requires:       noto-sans-math-fonts
Requires:       google-noto-sans-cjk-fonts

# Recommends and Supplements won't work so pull in manually
Requires:       discover-backend-flatpak
Requires:       discover-backend-fwupd
Requires:       kde-gtk-config6
Requires:       kde-gtk-config6-gtk3
Requires:       plasma-browser-integration
# Requires:       plasma5-defaults-openSUSE
Requires:       purpose
Requires:       qqc2-desktop-style
Requires:       xdg-desktop-portal-kde6

# Recommended by powerdevil5, but allow tlp as alternative
Requires:       (power-profiles-daemon or tlp)
Suggests:       power-profiles-daemon

# Doesnt depend on PackageKit, but also works for other backends
Requires:       discover6-notifier

# Spectacle to be able to take screenshots out of the box
Requires:       spectacle

# KAccounts to be installed by default (boo#1216397)
Requires:       kaccounts-integration
Requires:       kaccounts-providers
Requires:       kio-gdrive

# Default Plasma app to quickly use emojis
Requires:       plasma6-desktop-emojier
Requires:       google-noto-coloremoji-fonts

# Breeze GTK2, GTK3, and GTK4
Requires:       (gtk4-metatheme-breeze if gtk4)
Requires:       (gtk2-metatheme-breeze if gtk2)
Requires:       (gtk3-metatheme-breeze if gtk3)

# Default Plasma sounds for applications
Requires:       ocean-sound-theme6
Requires:       oxygen5-sounds

# Plasma system monitor
Requires:       plasma6-systemmonitor

# For seeing thumbnails in Dolphin
Requires:       qt6-imageformats
Requires:       ffmpegthumbs
Requires:       kdegraphics-thumbnailers

# For being able to change SDDM Settings
Requires:       sddm-kcm6

# Add for mounting network shares in userspace (boo#1210125)
Requires:       kio-fuse
Requires:       kdenetwork-filesharing
Requires:       kdnssd

# Add kcm_flatpak for managing flatpak permissions (boo#1208256)
Requires:       flatpak-kcm6

# Add pam_kwallet to unlock the password store automatically
Requires:       pam_kwallet6

# KDE Connect to communicate to phone devices
Requires:       kdeconnect-kde

# Add gvfs and gvfs-backends for usability with some flatpaks (boo#1216667)
Requires:       gvfs
Requires:       gvfs-backends

# Add steam-devices to negate users needing to after install
Requires:       steam-devices

# Warn when apps are using all inotify watches and prompts the user to raise it
Requires:       kde-inotify-survey

# For crisp status notifier systray icons
Requires:       libappindicator-gtk3

### Packages formerly provided by kiwi file
Requires:       kernel-default
### systemd-zram stuff
Requires:       systemd-zram-service
### Virtualization support
Requires:       spice-vdagent
Requires:       qemu-guest-agent

# bug#1218439
Requires:       tpm2.0-abrmd
Requires:       tpm2-0-tss
Requires:       tpm2.0-tools

%description base
This is the openSUSE Kalpa base system. It contains only fully working immutable desktop system.

%prep
# empty on purpose

%build
# empty on purpose

%install
mkdir -p %{buildroot}%{_docdir}/patterns-kalpa/
PATTERNS='
    base
'
for i in $PATTERNS; do
    echo "This file marks the pattern $i to be installed." \
        > %{buildroot}%{_docdir}/patterns-kalpa/${i}.txt
done

%files base
%dir %{_docdir}/patterns-kalpa
%{_docdir}/patterns-kalpa/base.txt

%changelog
