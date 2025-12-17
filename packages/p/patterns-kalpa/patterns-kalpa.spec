#
# spec file for package patterns-kalpa
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Shawn W Dunn <sfalken@opensuse.org>

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
Summary:        Patterns for Kalpa Desktop
License:        MIT
Group:          Metapackages
URL:            https://codeberg.org/KalpaDesktop/patterns-kalpa
Source0:        %name.rpmlintrc
ExclusiveArch:  x86_64 aarch64

%description
This is an internal package that is used to create the patterns as part
of the installation source setup. Installation of this package does
not make sense.

%package base
Summary:        Kalpa Desktop
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

### Base System Requirements
Requires:       aaa_base
Requires:       audit
Requires:       bash
Requires:       bash-completion
Requires:       branding
Requires:       build-key
Requires:       busybox
Requires:       ca-certificates
Requires:       ca-certificates-mozilla
Requires:       chrony
Requires:       coreutils
Requires:       coreutils-systemd
# curl indirectly needed by ignition via dracut's url-lib
Requires:       curl
Requires:       distribution-release
Requires:       filesystem
Requires:       glibc
Requires:       glibc-locale
Requires:       glibc-locale-base
Requires:       gzip
Requires:       health-checker
Requires:       health-checker-plugins-MicroOS
Requires:       hostname
Requires:       hwinfo
%ifnarch s390x
Requires:       irqbalance
%endif
Requires:       kernel-default
%ifnarch %{arm}
Requires:       kdump
%endif
Conflicts:      krb5-mini
Requires:       less
Requires:       lastlog2
Requires:       libnss_usrfiles2
Requires:       microos-tools
Requires:       openSUSE-build-key
Requires:       pam
Requires:       pam-config
Requires:       polkit-default-privs
Requires:       procps
Requires:       rpm
Requires:       shadow
Requires:       snapper
Requires:       vim
Requires:       wtmpdb
# people are addicted to sudo
Requires:       sudo
Requires:       systemd
Requires:       systemd-coredump
Requires:       systemd-experimental
Requires:       system-group-wheel
Requires:       systemd-zram-service
Requires:       terminfo-base
Requires:       timezone
Requires:       udisks2
Requires:       unzip
Requires:       upower
Requires:       usbutils
Requires:       util-linux
Requires:       wget
Requires:       wtmpdb
Requires:       xdg-utils
Requires:       yast2-logs
Requires:       group(nobody)
Requires:       user(nobody)

Obsoletes:      suse-build-key < 12.1

Conflicts:      gettext-runtime-mini

### Bootloader Requirements
%dnl Kalpa will be sticking with grub2 for the time being
%dnl Requires:       dracut-pcr-signature
%dnl Requires:       efibootmgr
%dnl Requires:       sdbootutil-rpm-scriptlets
%dnl Requires:       sdbootutil-snapper
%dnl Requires:       systemd-boot
Requires:       uefi_mbr
Requires:       (grub2-snapper-plugin if (grub2 or grub2-common))
Requires:       grub2-common
%ifarch x86_64
Requires:       biosdevname
Requires:       grub2-x86_64-efi
%endif
%ifarch aarch64
Requires:       grub2-arm64-efi
%endif
%ifarch aarch64 x86_64
Requires:       mokutil
Requires:       shim
%endif
Requires:       (grub2-branding-openSUSE if branding-openSUSE)
%dnl TPM-2.0 support (boo#1211835)
Requires:       uefi_mbr
Requires:       tpm2.0-abrmd
Requires:       tpm2-0-tss
Requires:       tpm2.0-tools




### Filesystem Support
Requires:       btrfsmaintenance
Requires:       btrfsprogs
# Support CIFS mounting via mount (boo#1225682)
Requires:       cifs-utils
Requires:       dosfstools
# exfat is an important filesystem too (boo#1222955)
Requires:       exfatprogs
# Add gvfs and gvfs-backends for usability with some flatpaks (boo#1216667)
Requires:       gvfs
Requires:       gvfs-backends
# Add for mounting network shares in userspace (boo#1210125)
Requires:       kdenetwork-filesharing
Requires:       kdnssd
Requires:       kio-fuse
Requires:       ntfs-3g
Requires:       ntfsprogs


### Firstboot Configuration
Requires:       combustion
Requires:       ignition-dracut


### SELinux requirements
Requires:       container-selinux
Requires:       policycoreutils
Requires:       policycoreutils-python-utils
Requires:       selinux-policy-targeted
Requires:       selinux-tools


### Virtualization and container support
Requires:       distrobox
Requires:       podman
Requires:       qemu-guest-agent
Requires:       spice-vdagent

### Device support requirements
## Audio Support: Pipewire is the Default sound server
Requires:       alsa-ucm-conf
Requires:       gstreamer-plugin-pipewire
Requires:       pipewire-alsa
Requires:       pipewire-pulseaudio
Requires:       phonon-vlc-qt6
Requires:       plasma6-pa
## Printing and Scanning Support
Requires:       cups
Requires:       cups-filters
Requires:       cups-pk-helper
Requires:       epson-inkjet-printer-escpr
Requires:       ghostscript
Requires:       hplip-hpijs
Requires:       kde-print-manager
Requires:       OpenPrintingPPDs
Requires:       printer-driver-brlaser
# Scanner Support (boo#1214614)
Requires:       sane-backends
Requires:       system-config-printer-common
Requires:       system-config-printer-dbus-service
Requires:       udev-configure-printer
## Thunderbolt device management (boo#1208150)
Requires:       bolt
## Bluetooth
Requires:       bluedevil6
Requires:       bluez-cups
Requires:       bluez-firmware
# Support bluetooth file transfer (boo#1225682)
Requires:       bluez-obexd
## For i2c dev handling and permissions
Requires:       ddcutil-i2c-udev-rules
## Add steam-devices to negate users needing to after install
Requires:       steam-devices
# Needed to ensure Kalpa are able to handle varied hardware out of the box
# and not just during installation
Requires:       kernel-firmware-all
Requires:       sof-firmware
# Support screen rotation (boo#1222711)
Requires:       iio-sensor-proxy
## Support wacom tablets
Requires:       libinput-udev
# Add switcheroo-control
Requires:       switcheroo-control
# Support Vulkan (boo#1223443)
Requires:       libvulkan_radeon
Requires:       libvulkan_intel
# Support fingerprint scanners (boo#1212071)
Requires:       fprintd
Requires:       fprintd-pam
# Add Mesa-demos-egl for kinfocenter6 (kde#502129)
Requires:       Mesa-demo-egl

# from data/COMMON-DESKTOP
Requires:       desktop-data
Requires:       desktop-file-utils
#
# Now the real packages
#
# #332596
# Pull in plasma-branding-Kalpa for firstboot setup
Requires:       plasma-branding-Kalpa

### Power Management
Requires:       (power-profiles-daemon or tuned-ppd)
Suggests:       tuned-ppd
# Some basic system tools
Requires:       ark
Requires:       falkon
Requires:       kate
Requires:       konsole
# Add KDE Partition Manager (boo#1212925)
Requires:       partitionmanager

### Networking requirements
%if 0%{is_opensuse}
Requires:       avahi
%endif
Requires:       ethtool
Requires:       fcoe-utils
Requires:       iproute2
Requires:       iputils
# For Mobile Broadband Support (boo#1230006)
Requires:       libmbim
Requires:       NetworkManager
Requires:       NetworkManager-bluetooth
Requires:       NetworkManager-openvpn
Requires:       NetworkManager-wifi
Requires:       openvpn-auth-pam-plugin
Requires:       plasma6-nm
Requires:       plasma6-nm-openconnect
Requires:       plasma6-nm-openvpn
Requires:       wireguard-tools


### Package management
Requires:       discover-backend-flatpak
Requires:       discover-backend-fwupd
Requires:       discover6-notifier
Requires:       transactional-update
Requires:       transactional-update-zypp-config
Requires:       transactional-update-notifier
Requires:       zypper
# zypper ps is useless in transactional mode. It also checks for
# /run/reboot-needed though which is created by transactional-update
Requires:       zypper-needs-restarting


### Plasma requirements
Requires:       aurorae6
Requires:       breeze6-wallpapers
Requires:       desktop-data
Requires:       desktop-file-utils
Requires:       ffmpegthumbs
Requires:       flatpak-kcm6
Requires:       kaccounts-integration
Requires:       kaccounts-providers
Requires:       kde-gtk-config6
Requires:       kde-gtk-config6-gtk3
Requires:       kde-inotify-survey
Requires:       kdeconnect-kde
Requires:       kdegraphics-thumbnailers
Requires:       kdeplasma6-addons
Requires:       kf6-baloo-file
Requires:       kf6-purpose
Requires:       kf6-qqc2-desktop-style
Requires:       kgamma6
Requires:       khelpcenter
Requires:       kio-extras
Requires:       kio-gdrive
Requires:       ksshaskpass6
Requires:       kunifiedpush
Requires:       kwalletmanager
Requires:       libappindicator-gtk3
Requires:       ocean-sound-theme6
Requires:       oxygen5-sounds
Requires:       pam_kwallet6
Requires:       pinentry
Requires:       plasma-browser-integration
Requires:       plasma6-session
Requires:       plasma6-desktop-emojier
Requires:       plasma6-systemmonitor
Requires:       plasma6-workspace-wallpapers
Requires:       qt6-imageformats
Requires:       sddm-qt6
Requires:       sddm-kcm6
# Needed for proper theming support with GTK Flatpaks
Requires:       xdg-desktop-portal-gtk
Requires:       xdg-desktop-portal-kde6


### Themeing and Branding
# Add Aeon-check
Requires:       aeon-check
Requires:       branding-openSUSE
Requires:       distribution-logos-openSUSE-Kalpa
Requires:       (gtk4-metatheme-breeze if gtk4)
Requires:       (gtk2-metatheme-breeze if gtk2)
Requires:       (gtk3-metatheme-breeze if gtk3)
Requires:       hicolor-icon-theme-branding-openSUSE
Requires:       Kalpa-release
Requires:       plasma-branding-Kalpa
Requires:       systemd-icon-branding-openSUSE
Requires:       systemd-presets-branding-Kalpa
%dnl Disabling for now, while sorting out the new installer
%dnl Requires:       systemd-repart-branding-Kalpa
%dnl Requires:       x86_64_v3-branding-Kalpa


### Applications
Requires:       dolphin
Requires:       falkon-kde
Requires:       fastfetch
Requires:       kate
Requires:       just
Requires:       konsole
Requires:       yakuake
# Add KDE Partition Manager (boo#1212925)
Requires:       partitionmanager
Requires:       spectacle
Requires:       susepaste
Requires:       vim
Requires:       openssh


### Fonts
Requires:       adobe-sourcecodepro-fonts
Requires:       adobe-sourcesans3-fonts
Requires:       adobe-sourcesanspro-fonts
Requires:       adobe-sourceserifpro-fonts
Requires:       adwaita-fonts
Requires:       cantarell-fonts
Requires:       dejavu-fonts
Requires:       ghostscript-fonts-std
Requires:       ghostscript-fonts-std-converted
Requires:       google-carlito-fonts
Requires:       google-noto-sans-cjk-fonts
Requires:       google-noto-coloremoji-fonts
Requires:       google-noto-sans-symbols-fonts
Requires:       google-noto-sans-symbols2-fonts
Requires:       google-opensans-fonts
Requires:       google-roboto-fonts
Requires:       hack-fonts
Requires:       ibm-plex-mono-fonts
Requires:       liberation-fonts
Requires:       suse-fonts



####
%dnl ### Packages formerly provided by x11
%dnl Requires:       xf86-input-libinput
%dnl Requires:       xorg-x11-fonts-core
%dnl Requires:       xorg-x11-server
%dnl Recommends:     dejavu-fonts
%dnl Recommends:     libyui-qt
%dnl Recommends:     libyui-qt-pkg
%dnl Recommends:     noto-sans-fonts
%dnl Recommends:     tigervnc
%dnl Recommends:     x11-tools
%dnl Recommends:     xdmbgrd
%dnl Recommends:     xorg-x11-Xvnc
%dnl Recommends:     xorg-x11-driver-video
%dnl Recommends:     xorg-x11-essentials
%dnl Recommends:     xorg-x11-fonts
%dnl Recommends:     xorg-x11-server-extra
%dnl Recommends:     xterm
%dnl Recommends:     xtermset
%dnl Recommends:     yast2-control-center
# bsc#1071953
%dnl %ifnarch s390 s390x
%dnl Recommends:     xf86-input-vmmouse
%dnl Recommends:     xf86-input-wacom
%dnl %endif


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
