#
# spec file for package patterns-microos
#
# Copyright (c) 2022 SUSE LLC
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

Name:           patterns-microos
Version:        5.0
Release:        0
Summary:        Patterns for openSUSE MicroOS
License:        MIT
Group:          Metapackages
URL:            http://en.opensuse.org/Patterns
Source0:        %name-rpmlintrc
ExclusiveArch:  x86_64 %arm32 aarch64 ppc64le s390x riscv64

%description
This is an internal package that is used to create the patterns as part
of the installation source setup. Installation of this package does
not make sense.

%package basesystem
Summary:        openSUSE MicroOS Base System (alias pattern for microos_base)
Group:          Metapackages
Provides:       pattern() = basesystem
Provides:       pattern-icon() = pattern-kubic
Requires:       pattern() = microos_base

%description basesystem
This is the openSUSE MicroOS runtime system. It contains only a minimal multiuser
booting system.

%package base
Summary:        openSUSE MicroOS
Group:          Metapackages
Provides:       pattern() = microos_base
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9010
Provides:       pattern-visible()
Requires:       pattern() = bootloader
Requires:       pattern() = minimal_base
%if %{with betatest}
# need to require it as recommends are off
Requires:       pattern() = update_test
%endif
### openSUSE base system
Requires:       /usr/bin/hostname
Requires:       aaa_base
Requires:       bash
Requires:       branding-openSUSE
Requires:       btrfsprogs
Requires:       ca-certificates
Requires:       ca-certificates-mozilla
Requires:       coreutils
Requires:       glibc
Suggests:       busybox-hostname
Requires:       NetworkManager
Requires:       NetworkManager-wifi
Requires:       iproute2
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
Requires:       MicroOS-release
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
# people are addicted to sudo
Requires:       sudo
Requires:       systemd-presets-branding-MicroOS
Requires:       terminfo-base
Requires:       timezone
Conflicts:      gettext-runtime-mini
Conflicts:      krb5-mini
Obsoletes:      suse-build-key < 12.1
Requires:       yast2-logs

%description base
This is the openSUSE MicroOS runtime system. It contains only a minimal multiuser
booting system.

%package base-zypper
Summary:        openSUSE MicroOS using Zypper
Group:          Metapackages
Provides:       pattern() = microos_base_zypper
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9011
Provides:       pattern-visible()
Requires:       transactional-update
Requires:       transactional-update-zypp-config
Requires:       zypper
Requires:       pattern() = microos_base
# zypper ps is useless in transactional mode. It also checks for
# /run/reboot-needed though which is created by transactional-update
Requires:       zypper-needs-restarting

%description base-zypper
This is the openSUSE MicroOS runtime system using the Zypper package manager.
It contains only a minimal multiuser booting system.

%package base-microdnf
Summary:        openSUSE MicroOS using Micro DNF
Group:          Metapackages
Provides:       pattern() = microos_base_microdnf
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9012
Provides:       pattern-visible()
Requires:       libdnf-plugin-txnupd
Requires:       microdnf
Requires:       pattern() = microos_base
# We need repository configuration from somewhere, so
# make sure one gets installed
Requires:       (libdnf-repo-config-zypp or rpm-repos-openSUSE)
Suggests:       libdnf-repo-config-zypp

%description base-microdnf
This is the openSUSE MicroOS runtime system using the Micro DNF package manager.
It contains only a minimal multiuser booting system.

%package base-packagekit
Summary:        openSUSE MicroOS using PackageKit
Group:          Metapackages
Provides:       pattern() = microos_base_packagekit
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9013
Provides:       pattern-visible()
Requires:       PackageKit
Requires:       PackageKit-branding-openSUSE
Requires:       libdnf-plugin-txnupd
Requires:       pattern() = microos_base
# We need repository configuration from somewhere, so
# make sure one gets installed
Requires:       (libdnf-repo-config-zypp or rpm-repos-openSUSE)
Suggests:       libdnf-repo-config-zypp

%description base-packagekit
This is the openSUSE MicroOS runtime system using the PackageKit service.
It contains only a minimal multiuser booting system.

%package defaults
Summary:        openSUSE MicroOS defaults
Group:          Metapackages
Provides:       pattern() = microos_defaults
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9020
Requires:       audit
Requires:       systemd-logger
Requires:       pattern() = microos_base

%description defaults
This provides default packages for openSUSE MicroOS which can be optionally
replaced by alternatives.

%package hardware
Summary:        Hardware Support
Group:          Metapackages
Provides:       pattern() = microos_hardware
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9030
Provides:       pattern-visible()
Requires:       ethtool
%ifnarch s390x
Requires:       irqbalance
%endif
Requires:       fcoe-utils
Requires:       hwinfo

%description hardware
Packages required to install openSUSE MicroOS on real hardware.

%package apparmor
Summary:        Apparmor Support
Group:          Metapackages
Provides:       pattern() = microos_apparmor
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-apparmor
Provides:       pattern-order() = 9050
Provides:       pattern-visible()
Requires:       apparmor-parser
Requires:       apparmor-profiles

%description apparmor
Packages required to enable Apparmor on openSUSE MicroOS.

%package selinux
Summary:        SELinux Support
Group:          Metapackages
Provides:       pattern() = microos_selinux
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 9055
Provides:       pattern-visible()
Requires:       container-selinux
Requires:       policycoreutils
Requires:       selinux-policy-targeted
Requires:       selinux-tools

%description selinux
This are packages which are required to enable SELinux on openSUSE MicroOS

%package cockpit
Summary:        Web based remote system managemet
Group:          Metapackages
Provides:       pattern() = microos_cockpit
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 9060
Provides:       pattern-visible()
Requires:       cockpit-podman
Requires:       cockpit-system
# If PackageKit pattern is installed, pull in Cockpit's PackageKit module
Requires:       (cockpit-packagekit if patterns-microos-base-packagekit)

%description cockpit
Packages required to run the Cockpit system management service.
For the web service the cockpit-ws container is required.

%package sssd_ldap
Summary:        LDAP client
Group:          Metapackages
Provides:       pattern() = microos_sssd_ldap
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 9070
Provides:       pattern-visible()
Requires:       sssd
Requires:       sssd-ldap

%description sssd_ldap
Packages required to enable LDAP client support via sssd on openSUSE MicroOS.

%package ima_evm
Summary:        IMA/EVM Support
Group:          Metapackages
Provides:       pattern() = microos_ima_evm
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-basis-addon
Provides:       pattern-order() = 9080
Provides:       pattern-visible()
Requires:       attr
Requires:       dracut-ima
Requires:       ima-evm-utils
Requires:       keyutils

%description ima_evm
Packages required to enable IMA/EVM on openSUSE MicroOS.

%package ra_agent
Summary:        Remote Attestation (Agent) Support
Group:          Metapackages
Provides:       pattern() = microos_ra_agent
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-basis-addon
Provides:       pattern-order() = 9085
Provides:       pattern-visible()
%ifarch %{ix86} ia64 x86_64 %{arm} aarch64
Requires:       dmidecode
%endif
Requires:       rust-keylime
Requires:       pattern() = microos_ima_evm

%description ra_agent
Packages required to enable remote attestation via the Rust Keylime
agent on openSUSE MicroOS.

%package ra_verifier
Summary:        Remote Attestation (Verifier) Support
Group:          Metapackages
Provides:       pattern() = microos_ra_verifier
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-basis-addon
Provides:       pattern-order() = 9086
Provides:       pattern-visible()
Requires:       keylime-firewalld
Requires:       keylime-registrar
Requires:       keylime-tenant
Requires:       keylime-verifier

%description ra_verifier
Packages required to enable remote attestation via Keylime verifier on
openSUSE MicroOS.

%package cloud
Summary:        Support for Cloud
Group:          Metapackages
Provides:       pattern() = microos_cloud
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 9090
Provides:       pattern-visible()
Requires:       cloud-init
Requires:       cloud-init-config-MicroOS

%description cloud
Packages required to enable openSUSE MicroOS in the Cloud.

%package desktop-common
Summary:        Common packages for Desktops on MicroOS
Group:          Metapackages
Provides:       pattern() = microos_desktop_common
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-x11
Provides:       pattern-order() = 9100
Requires:       pattern() = x11

# PipeWire is the default sound server
Requires:       gstreamer-plugin-pipewire
Requires:       pipewire-alsa
Requires:       pipewire-pulseaudio
# This approach unfortunately breaks Tumbleweed (boo#1194264)
#Obsoletes:      alsa-plugins-pulse < 1.3
#Obsoletes:      pulseaudio < 14.3
#Obsoletes:      pulseaudio-module-bluetooth < 14.3
#Obsoletes:      pulseaudio-module-gsettings < 14.3
#Obsoletes:      pulseaudio-module-x11 < 14.3
#Obsoletes:      pulseaudio-module-zeroconf < 14.3

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

%description desktop-common
Packages required for openSUSE MicroOS Desktops.

%package desktop-gnome
Summary:        MicroOS GNOME Desktop
Group:          Metapackages
Provides:       pattern() = microos_gnome_desktop
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-gnome
Provides:       pattern-order() = 9100
Provides:       pattern-visible()
Requires:       gdm-branding-MicroOS
Requires:       pattern() = gnome_basic
Requires:       pattern() = microos_base_zypper
Requires:       pattern() = microos_desktop_common
# gnome-initial-setup requirements
Requires:       gnome-initial-setup
Requires:       gjs
Requires:       gnome-menus-branding-openSUSE
Requires:       system-group-wheel
# from data/COMMON-DESKTOP
Requires:       desktop-data
Requires:       desktop-file-utils
#
# Now the real packages
#
# #332596
Requires:       gnome-keyring-pam
# implied by gnome-keyring-pam
#Requires:     gnome-keyring
Requires:       gnome-disk-utility
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
Requires:       gnome-branding-MicroOS
Requires:       gnome-color-manager
#Requires:       gnome-packagekit
Requires:       gnome-shell-classic
Requires:       gnome-software
Requires:       gnome-terminal
Requires:       gnome-tweak-tool
Requires:       gnome-usage
Requires:       gnome-user-docs
# bnc#879466
Requires:       gpgme
# for online accounts and calendar integration
Requires:       gnome-bluetooth
# needed to ensure bluetooth is enabled at startup (glgo#GNOME/gnome-bluetooth#110)
Requires:       bluez-auto-enable-devices
Requires:       gnome-control-center-goa
Requires:       gnome-online-accounts
Requires:       gnome-shell-calendar
# For seeing thumbnails in Nautilus
Requires:       gdk-pixbuf-thumbnailer
Requires:       gsf-office-thumbnailer
Requires:       rsvg-thumbnailer
# So that GNOME shell extensions can be installed
Requires:       chrome-gnome-shell
# we need something for xdg-su
Requires:       gnome-shell-search-provider-nautilus
Requires:       libgnomesu
Requires:       nautilus
Requires:       nautilus-extension-terminal
Requires:       nautilus-share
# For encrypting and decrypting files to work in Nautilus
Requires:       nautilus-extension-seahorse
Requires:       seahorse-daemon
# So Trash and mounting USB sticks work in Nautilus
Requires:       gvfs-backends
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
Requires:       (power-profiles-daemon or tlp)
Suggests:       power-profiles-daemon
#
# Low-level parts that we need
#
%if 0%{is_opensuse}
# bnc#430161
Requires:       NetworkManager
Requires:       NetworkManager-openvpn-gnome
Requires:       canberra-gtk-play
#
# Branding
#
# #591535
Requires:       gtk2-branding-openSUSE
Requires:       gtk3-branding-openSUSE
%endif

%description desktop-gnome
Packages required for the openSUSE MicroOS Desktop with GNOME.

%package desktop-kde
Summary:        MicroOS KDE Plasma Desktop
Group:          Metapackages
Provides:       pattern() = microos_kde_desktop
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-kde
Provides:       pattern-order() = 9101
Provides:       pattern-visible()
Requires:       pattern() = kde_plasma
Requires:       pattern() = microos_desktop_common
# Pull in transactional-update
Requires:       pattern() = microos_base_zypper

# Pull in plasma-branding-MicroOS for firstboot setup
Requires:       plasma-branding-MicroOS

# Some basic system tools
Requires:       kate
Requires:       konsole

# Recommended by kde_plasma
Requires:       bluedevil5
Requires:       breeze5-wallpapers
Requires:       dolphin
Requires:       kde-print-manager
Requires:       kgamma5
Requires:       kwrited5
Requires:       phonon4qt5-backend-gstreamer
Requires:       plasma-nm5
# For NetworkManager support of openVPN Connections
Requires:       NetworkManager-openvpn
Requires:       openvpn-auth-pam-plugin
Requires:       plasma-nm5-openvpn
Requires:       plasma5-addons
Requires:       plasma5-pa
Requires:       plasma5-session-wayland
Requires:       sddm
# Not useful with excludedocs...
#Requires:       khelpcenter5
Requires:       kio-extras5
Requires:       kwalletmanager5
Requires:       pinentry-qt5

# Additional Fonts to cover Unicode Symbols not provided by the fonts pulled in by kde_plasma Pattern
Requires:       noto-sans-math-fonts
Requires:       google-noto-sans-cjk-fonts

# Recommends and Supplements won't work, so pull in manually
Requires:       discover-backend-flatpak
#Requires:       discover-backend-packagekit
Requires:       kde-gtk-config5
Requires:       kde-gtk-config5-gtk3
Requires:       plasma-browser-integration
Requires:       plasma5-defaults-openSUSE
Requires:       purpose
Requires:       qqc2-desktop-style
Requires:       sddm-theme-openSUSE
Requires:       xdg-desktop-portal-gnome
Requires:       xdg-desktop-portal-kde
# Recommended by powerdevil5, but allow tlp as alternative
Requires:       (power-profiles-daemon or tlp)
Suggests:       power-profiles-daemon

# Doesn't depend on PackageKit, but also works for other backends
Requires:       discover-notifier

%description desktop-kde
Packages required for the openSUSE MicroOS with KDE Plasma

%package onlyDVD
Summary:        Packages only for the DVD of openSUSE MicroOS
Group:          Metapackages
Provides:       pattern-category() = MicroOS
Requires:       apparmor-utils
Requires:       bcache-tools
Requires:       crda
Requires:       cryptsetup
Requires:       firewalld
Requires:       iscsiuio
#extra items for DVD, not every install
Requires:       ModemManager
Requires:       NetworkManager-wwan
# Firmware packages with proper "Supplements:" (see bsc#1184767)
Requires:       kernel-firmware-all
Requires:       lvm2
Requires:       multipath-tools
Requires:       nvme-cli
Requires:       open-iscsi
%ifarch %ix86 x86_64 aarch64
Requires:       hyper-v
Requires:       open-vm-tools
%endif
Requires:       pam_pwquality
Requires:       policycoreutils-python-utils
Requires:       qemu-guest-agent
Requires:       spice-vdagent
Requires:       tftpboot-installation-openSUSE-MicroOS-%{_target_cpu}
%ifarch %ix86 x86_64
Requires:       ucode-amd
Requires:       ucode-intel
%endif
Requires:       wpa_supplicant
Requires:       xfsprogs
Provides:       pattern() = microos_onlyDVD
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 9900
Requires:       pattern() = microos_apparmor
Requires:       pattern() = microos_cloud
Requires:       pattern() = microos_hardware
Requires:       pattern() = microos_ima_evm
Requires:       pattern() = microos_ra_agent
Requires:       pattern() = microos_sssd_ldap

%description onlyDVD
Additional packages on a openSUSE MicroOS DVD.

%package alt_onlyDVD
Summary:        Alternative Packages only for the DVD of openSUSE MicroOS
Group:          Metapackages
Provides:       pattern-category() = MicroOS
Requires:       kernel-default-base
Provides:       pattern() = microos_alt_onlyDVD
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 9901
Requires:       pattern() = microos_apparmor
Requires:       pattern() = microos_cloud
Requires:       pattern() = microos_cockpit
Requires:       pattern() = microos_ima_evm
Requires:       pattern() = microos_ra_verifier
Requires:       pattern() = microos_selinux
Requires:       pattern() = microos_sssd_ldap

%description alt_onlyDVD
Alternative additional packages on a openSUSE MicroOS DVD.

%prep
# empty on purpose

%build
# empty on purpose

%install
mkdir -p %buildroot/usr/share/doc/packages/patterns-microos/
for i in basesystem base base_zypper base_microdnf base_packagekit \
    defaults hardware ima_evm ra_agent ra_verifier apparmor selinux cockpit \
    sssd_ldap cloud desktop-common desktop-gnome desktop-kde onlyDVD alt_onlyDVD; do
	echo "This file marks the pattern $i to be installed." >%buildroot/usr/share/doc/packages/patterns-microos/$i.txt
done

%files basesystem
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/basesystem.txt

%files base
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/base.txt

%files base-zypper
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/base_zypper.txt

%files base-microdnf
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/base_microdnf.txt

%files base-packagekit
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/base_packagekit.txt

%files defaults
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/defaults.txt

%files hardware
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/hardware.txt

%files sssd_ldap
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/sssd_ldap.txt

%files ima_evm
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/ima_evm.txt

%files ra_agent
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/ra_agent.txt

%files ra_verifier
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/ra_verifier.txt

%files apparmor
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/apparmor.txt

%files selinux
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/selinux.txt

%files cockpit
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/cockpit.txt

%files cloud
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/cloud.txt

%files desktop-common
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/desktop-common.txt

%files desktop-gnome
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/desktop-gnome.txt

%files desktop-kde
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/desktop-kde.txt

%files onlyDVD
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/onlyDVD.txt

%files alt_onlyDVD
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/alt_onlyDVD.txt

%changelog
