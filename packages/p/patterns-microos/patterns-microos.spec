#
# spec file for package patterns-microos
#
# Copyright (c) 2020 SUSE LLC
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
ExclusiveArch:  x86_64 armv7l armv7hl aarch64 ppc64le s390x

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
Requires:       aaa_base
Requires:       bash
Requires:       branding-openSUSE
Requires:       btrfsprogs
Requires:       ca-certificates
Requires:       ca-certificates-mozilla
Requires:       coreutils
Requires:       hostname
Requires:       iproute2
Requires:       login
Requires:       openSUSE-build-key
Requires:       pam
Requires:       procps
Requires:       rebootmgr
Requires:       rpm
Requires:       shadow
Requires:       snapper
Requires:       systemd
Requires:       wicked
Requires:       zypper
####
Requires:       btrfsmaintenance
Requires:       chrony
# curl indirectly needed by ignition via dracut's url-lib
Requires:       curl
# probably needed for fsck.fat on efi partitions
Requires:       dosfstools
Requires:       glibc-locale-base
Requires:       haveged
Requires:       health-checker
Requires:       health-checker-plugins-MicroOS
# ping!
Requires:       MicroOS-release
Requires:       iputils
Requires:       issue-generator
Requires:       kdump
Requires:       less
Requires:       microos-tools
Requires:       openssh
Requires:       vim-small
# people are addicted to sudo
Requires:       sudo
Requires:       supportutils
Requires:       systemd-presets-branding-MicroOS
Requires:       tallow
Requires:       terminfo-base
# timezone-base with only UTC useful?
Requires:       timezone
Requires:       transactional-update
Requires:       transactional-update-zypp-config
# zypper ps is useless in transactional mode. It also checks for
# /run/reboot-needed though which is created by transactional-update
Requires:       zypper-needs-restarting
Conflicts:      gettext-runtime-mini
Conflicts:      krb5-mini
Obsoletes:      suse-build-key < 12.1
Requires:       yast2-logs

%description base
This is the openSUSE MicroOS runtime system. It contains only a minimal multiuser
booting system.

%package defaults
Summary:        openSUSE MicroOS defaults
Group:          Metapackages
Provides:       pattern() = microos_defaults
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9011
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
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9080
Provides:       pattern-visible()
Requires:       attr
Requires:       dracut-ima
Requires:       ima-evm-utils
Requires:       keyutils

%description ima_evm
Packages required to enable IMA/EVM on openSUSE MicroOS.

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

%package desktop-gnome
Summary:        MicroOS GNOME Desktop
Group:          Metapackages
Provides:       pattern() = microos_gnome_desktop
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 9100
Provides:       pattern-visible()
Requires:       gdm-branding-MicroOS
Requires:       pattern() = gnome_basic
Requires:       pattern() = x11
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
Requires:       gnome-power-manager
# implied by gdm
#Requires: gnome-shell
#Requires: gnome-settings-daemon
# implied by gnome-shell
#Requires:       gnome-control-center
#
# Default sessions
# - Put in Recommends for now, to make sure the livecd will always build; but
#   ideally, should be in Requires
# - We also we explicitly put the packages required by those sessions, in case
#   gnome-session-*-session is not installable, to make sure the livecd is
#   somehow a bit usable
#
Requires:       gnome-session-default-session
# boo#1090117
Requires:       gnome-shell-classic
Requires:       gnome-terminal
# bnc#879466
Requires:       gnome-user-docs
Requires:       gpgme
# we need something for xdg-su
Requires:       file-roller
Requires:       flatpak
Requires:       gnome-calculator
Requires:       gnome-packagekit
Requires:       gnome-software
Requires:       gnome-system-monitor
Requires:       gnome-tweak-tool
Requires:       gnome-usage
# for online accounts and calendar integration
Requires:       gnome-bluetooth
Requires:       gnome-control-center-goa
Requires:       gnome-online-accounts
Requires:       gnome-shell-calendar
# For seeing thumbnails in Nautilus
Requires:       gdk-pixbuf-thumbnailer
Requires:       gsf-office-thumbnailer
Requires:       rsvg-thumbnailer
# So that GNOME shell extensions can be installed
Requires:       chrome-gnome-shell
Requires:       libgnomesu
Requires:       nautilus
Requires:       nautilus-extension-terminal
Requires:       nautilus-share
# So Trash and mounting USB sticks work in Nautilus
Requires:       gvfs-backends
Requires:       udisks2
# Allow users to print (and add some common printer drivers)
Requires:       OpenPrintingPPDs
Requires:       cups
Requires:       cups-filters
Requires:       hplip-hpijs
# We need the icons to work
Requires:       adwaita-icon-theme
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
Requires:       polkit-default-privs
# Pulseaudio is the default sound server
Requires:       pulseaudio-module-bluetooth
Requires:       pulseaudio-module-gsettings
Requires:       pulseaudio-module-x11
# So that GNOME keyring works
Requires:       gcr-ssh-askpass
Requires:       samba
# implied by gnome-bluetooth
#Requires:       bluez
Requires:       bluez-firmware
# #509829
Requires:       xdg-user-dirs-gtk
Requires:       yelp
#
# Low-level parts that we need
#
%if 0%{is_opensuse}
# bnc#430161
Requires:       NetworkManager
%endif
%if 0%{is_opensuse}
Requires:       canberra-gtk-play
%endif
%if 0%{is_opensuse}
Requires:       avahi
#
# Branding
#
# #591535
Requires:       gio-branding-openSUSE
Requires:       gtk2-branding-openSUSE
Requires:       gtk3-branding-openSUSE
Requires:       hicolor-icon-theme-branding-openSUSE

#PackageKit
Requires:       PackageKit
Requires:       PackageKit-branding-openSUSE
%endif

%description desktop-gnome
Packages required for the openSUSE MicroOS Desktop with GNOME.

%package desktop-kde
Summary:        MicroOS KDE Plasma Desktop
Group:          Metapackages
Provides:       pattern() = microos_kde_desktop
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 9101
Provides:       pattern-visible()
Requires:       pattern() = kde_plasma

# Some basic system tools
Requires:       kate
Requires:       konsole

# Recommended by kde_plasma
Requires:       bluedevil5
Requires:       breeze5-wallpapers
Requires:       dolphin
Requires:       kde-print-manager
Requires:       kdeconnect-kde
Requires:       kgamma5
Requires:       kwrited5
Requires:       phonon4qt5-backend-gstreamer
Requires:       plasma-nm5
Requires:       plasma5-addons
Requires:       plasma5-pa
Requires:       plasma5-pk-updates
Requires:       plasma5-session-wayland
Requires:       sddm
# Not useful with excludedocs...
#Requires:       khelpcenter5
Requires:       kio-extras5
Requires:       kwalletmanager5
Requires:       pinentry-qt5

Requires:       alsa-plugins-pulse
Requires:       pulseaudio
Requires:       pulseaudio-module-x11
Requires:       pulseaudio-module-zeroconf
Requires:       pulseaudio-utils

# Recommends and Supplements won't work, so pull in manually
Requires:       discover-backend-flatpak
Requires:       pipewire
Requires:       plasma5-defaults-openSUSE
Requires:       qqc2-desktop-style
Requires:       sddm-theme-openSUSE
Requires:       xdg-desktop-portal-kde

%description desktop-kde
Packages required for the openSUSE MicroOS with KDE Plasma

%package onlyDVD
Summary:        Packages only for the DVD of openSUSE MicroOS
Group:          Metapackages
Provides:       pattern-category() = MicroOS
Requires:       apparmor-utils
Requires:       bcache-tools
Requires:       cryptsetup
Requires:       glibc-locale
Requires:       iscsiuio
Requires:       kernel-firmware
Requires:       lvm2
Requires:       multipath-tools
Requires:       nvme-cli
Requires:       open-iscsi
%ifarch %ix86 x86_64
Requires:       hyper-v
Requires:       open-vm-tools
%endif
Requires:       pam_pwquality
Requires:       policycoreutils-python-utils
Requires:       tftpboot-installation-openSUSE-MicroOS-%{_arch}
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
for i in basesystem base defaults hardware ima_evm apparmor selinux cockpit sssd_ldap cloud desktop-gnome desktop-kde \
    onlyDVD alt_onlyDVD; do
	echo "This file marks the pattern $i to be installed." >%buildroot/usr/share/doc/packages/patterns-microos/$i.txt
done

%files basesystem
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/basesystem.txt

%files base
%defattr(-,root,root)
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/base.txt

%files defaults
%defattr(-,root,root)
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/defaults.txt

%files hardware
%defattr(-,root,root)
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/hardware.txt

%files sssd_ldap
%defattr(-,root,root)
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/sssd_ldap.txt

%files ima_evm
%defattr(-,root,root)
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/ima_evm.txt

%files apparmor
%defattr(-,root,root)
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/apparmor.txt

%files selinux
%defattr(-,root,root)
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/selinux.txt

%files cockpit
%defattr(-,root,root)
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/cockpit.txt

%files cloud
%defattr(-,root,root)
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/cloud.txt

%files desktop-gnome
%defattr(-,root,root)
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/desktop-gnome.txt

%files desktop-kde
%defattr(-,root,root)
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/desktop-kde.txt

%files onlyDVD
%defattr(-,root,root)
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/onlyDVD.txt

%files alt_onlyDVD
%defattr(-,root,root)
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/alt_onlyDVD.txt

%changelog
