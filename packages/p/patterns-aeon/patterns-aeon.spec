#
# spec file for package patterns-aeon
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

Name:           patterns-aeon
Version:        5.0
Release:        0
Summary:        Patterns for openSUSE Aeon
License:        MIT
Group:          Metapackages
URL:            http://en.opensuse.org/Patterns
Source0:        %name.rpmlintrc
ExclusiveArch:  x86_64 aarch64

%description
This is an internal package that is used to create the patterns as part
of the installation source setup. Installation of this package does
not make sense.

%package base
Summary:        openSUSE Aeon
Group:          Metapackages
Provides:       pattern() = aeon_base
Provides:       pattern-category() = Aeon
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9200
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
Requires:       sdbootutil-snapper
Requires:       dracut-pcr-signature
Requires:       efibootmgr
Requires:       sdbootutil-rpm-scriptlets
Requires:       shim
Requires:       uefi_mbr

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
Requires:       NetworkManager-bluetooth
Requires:       NetworkManager-wifi
Requires:       iproute2
Requires:       lastlog2
Requires:       libnss_usrfiles2
Requires:       openSUSE-build-key
Requires:       pam
Requires:       pam-config
Requires:       procps
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
Requires:       Aeon-release
Requires:       dosfstools
Requires:       glibc-locale-base
Suggests:       busybox-gzip
Requires:       health-checker
Requires:       health-checker-plugins-MicroOS
Requires:       iputils
%ifnarch %{arm}
Requires:       kdump
%endif
Requires:       less
Requires:       microos-tools
Requires:       snapper
Requires:       vim-small
Requires:       wtmpdb
# people are addicted to sudo
Requires:       sudo
Requires:       systemd-presets-branding-Aeon
Requires:       terminfo-base
Requires:       timezone
Conflicts:      gettext-runtime-mini
Conflicts:      krb5-mini
Obsoletes:      suse-build-key < 12.1
Requires:       yast2-logs
# exfat is an important filesystem too boo#1222955
Requires:       exfatprogs

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

### Packages formerly provided by selinux
Requires:       container-selinux
Requires:       policycoreutils
Requires:       policycoreutils-python-utils
Requires:       selinux-policy-targeted
Requires:       selinux-tools

### Packages formerly provided by x11
Requires:       xf86-input-libinput
Requires:       xorg-x11-fonts-core
Requires:       xorg-x11-server

### Packages formerly provided by desktop-common
# PipeWire is the default sound server
Requires:       gstreamer-plugin-pipewire
Requires:       pipewire-alsa
Requires:       pipewire-pulseaudio
# Support UCM Profiles boo#1218510
Requires:       alsa-ucm-conf
# Allow users to print (and add some common printer drivers)
Requires:       OpenPrintingPPDs
Requires:       bluez-cups
Requires:       cups
Requires:       cups-filters
Requires:       cups-pk-helper
Requires:       epson-inkjet-printer-escpr
Requires:       ghostscript
Requires:       hplip-hpijs
Requires:       system-config-printer-common
Requires:       system-config-printer-dbus-service
Requires:       udev-configure-printer
# Support scanners boo#1214614
Requires:       sane-backends
# Add thunderbolt device management (boo#1208150)
Requires:       bolt
# Common tools
Requires:       bash-completion
Requires:       bluez-firmware
Requires:       glibc-locale
Requires:       hicolor-icon-theme-branding-openSUSE
Requires:       polkit-default-privs
Requires:       systemd-icon-branding-openSUSE
Requires:       udisks2
Requires:       unzip
Requires:       upower
Requires:       wget
Requires:       xdg-utils
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

### Packages formerly provided by desktop-gnome
Requires:       gsettings-backend-dconf
Requires:       distribution-logos-openSUSE-Aeon
Requires:       gdm-branding-Aeon
# gnome-initial-setup requirements
Requires:       gnome-initial-setup
Requires:       desktop-file-utils
Requires:       gjs
Requires:       gnome-menus-branding-openSUSE
Requires:       system-group-wheel
#
# Now the real packages
#
# #332596
Requires:       gnome-keyring-pam
# implied by gnome-keyring-pam
#Requires:     gnome-keyring
Requires:       gnome-disk-utility
# boo#1215343
Requires:       gnome-backgrounds
# implied by gdm
#Requires: gnome-shell
#Requires: gnome-settings-daemon
# implied by gnome-shell
#Requires:       gnome-control-center
#
# Default sessions:
# - We also explicitly put the packages required by those sessions, in case
#   gnome-session-*-session is not installable, to make sure the livecd is
#   somehow a bit usable
#
Requires:       gnome-session-default-session
# ensure we have wayland session available (and used by default)
Requires:       gnome-session-wayland
# boo#1090117
Requires:       flatpak
Requires:       gnome-branding-Aeon
Requires:       gnome-color-manager
#Requires:       gnome-packagekit
Requires:       gnome-software
Requires:       gnome-system-monitor
Requires:       gnome-terminal
Requires:       gnome-tweak-tool
Requires:       gnome-user-docs
# bnc#879466
Requires:       gpgme
# for online accounts and calendar integration
Requires:       gnome-bluetooth
# for display color profile support boo#1210492
Requires:       gnome-control-center-color
# for desktop remote access
Requires:       gnome-remote-desktop
# for shell remote access
Requires:       openssh
# needed to ensure bluetooth is enabled at startup (glgo#GNOME/gnome-bluetooth#110)
Requires:       bluez-auto-enable-devices
Requires:       gnome-control-center-goa
Requires:       gnome-online-accounts
Requires:       gnome-shell-calendar
# For seeing thumbnails in Nautilus
Requires:       jxl-thumbnailer
Requires:       gdk-pixbuf-thumbnailer
Requires:       gsf-office-thumbnailer
Requires:       rsvg-thumbnailer
# So that GNOME shell extensions can be installed
Requires:       chrome-gnome-shell
# So users can be configured and have pretty face thumbnails
Requires:       gnome-control-center-users
Requires:       gnome-control-center-user-faces
# we need something for xdg-su
Requires:       gnome-shell-search-provider-nautilus
Requires:       libgnomesu
Requires:       nautilus
Requires:       nautilus-extension-terminal
# Some extensions add context menus to nautilus using python scripts (example GSConnect)
# For this to work we need nautilus-python bindings
Requires:       python3-nautilus
Requires:       nautilus-share
# For encrypting and decrypting files to work in Nautilus
Requires:       nautilus-extension-seahorse
Requires:       seahorse-daemon
# So Trash and mounting USB sticks work in Nautilus
Requires:       gvfs-backends
Requires:       gvfs-backend-afc
Requires:       gvfs-backend-goa
Requires:       gvfs-fuse
# We need the icons to work
Requires:       adwaita-icon-theme
# We need this for accessability and the lack of it causes big performance issues (boo#1204564)
Requires:       at-spi2-core
# Some fonts
Requires:       adobe-sourcecodepro-fonts
Requires:       adobe-sourcesanspro-fonts
Requires:       adobe-sourceserifpro-fonts
Requires:       dejavu-fonts
Requires:       ghostscript-fonts-other
Requires:       ghostscript-fonts-std
Requires:       google-carlito-fonts
Requires:       google-droid-fonts
Requires:       google-opensans-fonts
Requires:       google-roboto-fonts
Requires:       noto-coloremoji-fonts
Requires:       noto-emoji-fonts
Requires:       noto-sans-fonts
# So that GNOME keyring works
Requires:       gcr-ssh-askpass
Requires:       gcr3-ssh-askpass
# So that GNOME prompt for ssh password works
Requires:       openssh-askpass-gnome
# So that GNOME pinentry works
Requires:       pinentry-gnome3
Requires:       gvfs-backend-samba
Requires:       samba
# So that GNOME builtin screen recorder works
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-good
# #509829
Requires:       xdg-user-dirs-gtk
Requires:       yelp
# Polkit integration with GNOME
Requires:       polkit-gnome
# https://build.opensuse.org/request/show/921373
Requires:       xdg-desktop-portal-gnome
# ensure laptop power support is there
Requires:       power-profiles-daemon

# add steam-devices
Requires:       steam-devices

#
# Low-level parts that we need
#
%if 0%{is_opensuse}
# bnc#430161
Requires:       NetworkManager-openconnect-gnome
Requires:       NetworkManager-openvpn-gnome
Requires:       canberra-gtk-play
#
# Branding
#
# #591535
Requires:       gtk2-branding-openSUSE
Requires:       gtk3-branding-openSUSE
Requires:       gtk4-branding-openSUSE
%endif
### Packages formerly provided by kiwi file
Requires:       kernel-default
### systemd-zram stuff
Requires:       systemd-zram-service
### Virtualisation support
Requires:       spice-vdagent
Requires:       qemu-guest-agent
### Container / Distrobox boo#1222909
Requires:       distrobox
Requires:       podman

# bug#1211835 - TPM2.0 support
Requires:       tpm2.0-abrmd
Requires:       tpm2-0-tss
Requires:       tpm2.0-tools

### x86_64_v3 support is mandatory on Aeon
Requires:       x86_64_v3-branding-Aeon

### Aeons partitions are defined to use systemd-repart
# systemd-experimental is temproarily required for repart
Requires:       systemd-experimental
Requires:       systemd-repart-branding-Aeon

### Firstboot Configuration
Requires:       ignition-dracut
Requires:       combustion

### Support screen rotation boo#1222711
Requires:       iio-sensor-proxy

### Support Vulkan boo#1223443
Requires:       libvulkan_radeon
Requires:       libvulkan_intel

### Support fingerprint scanners boo#1212071
Requires:       fprintd
Requires:       fprintd-pam

### Support bluetooth filetransfer boo#1225682
Requires:       bluez-obexd

### Support CIFS mounting via mount boo#1216138
Requires:       cifs-utils

%description base
This is the openSUSE Aeon base system. It contains only fully working immutable desktop system.

%prep
# empty on purpose

%build
# empty on purpose

%install
mkdir -p %{buildroot}%{_docdir}/patterns-aeon/
PATTERNS='
    base
'
for i in $PATTERNS; do
    echo "This file marks the pattern $i to be installed." \
        > %{buildroot}%{_docdir}/patterns-aeon/${i}.txt
done

%files base
%dir %{_docdir}/patterns-aeon
%{_docdir}/patterns-aeon/base.txt

%changelog
