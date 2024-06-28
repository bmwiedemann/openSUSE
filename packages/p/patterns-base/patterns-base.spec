#
# spec file for package patterns-base
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
Name:           patterns-base
Version:        20200505
Release:        0
Summary:        Patterns for Installation (base patterns)
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
Source1:        pattern-definition-32bit.txt
Source2:        create_32bit-patterns_file.pl
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains all the base / core patterns (and those that don't fit well anywhere else).

################################################################################

# bsc#1088669 - only provide 32bit pattern for 64bit intel
%ifarch x86_64
%package 32bit
%pattern_basetechnologies
Summary:        32-Bit Runtime Environment
Group:          Metapackages
Provides:       pattern() = 32bit
Provides:       pattern-icon() = pattern-cli
Provides:       pattern-order() = 1180
Provides:       pattern-visible()
%{obsolete_legacy_pattern 32bit}

%description 32bit
This will install the 32-bit variant of all selected patterns. This allows to execute 32-bit software.

%files 32bit
%dir %{_docdir}/patterns
%{_docdir}/patterns/32bit.txt
%endif

################################################################################

%package apparmor
%pattern_basetechnologies
Summary:        AppArmor
Group:          Metapackages
Provides:       pattern() = apparmor
Provides:       pattern-icon() = pattern-apparmor
Provides:       pattern-order() = 1100
Provides:       pattern-visible()
Requires:       apparmor-abstractions
Requires:       apparmor-parser
Requires:       apparmor-profiles
Requires:       pattern() = minimal_base
Recommends:     apparmor-docs
Recommends:     apparmor-utils
Recommends:     yast2-apparmor
Suggests:       pam_apparmor
%{obsolete_legacy_pattern apparmor}
%if 0%{?is_opensuse}
Requires:       audit
%else
Recommends:     audit
%endif

%description apparmor
AppArmor is an application security framework that provides mandatory access control for programs. It protects from exploitation of software flaws and compromised systems. It offers an advanced tool set that automates the development of per-program application security without requiring additional knowledge.

%files apparmor
%dir %{_docdir}/patterns
%{_docdir}/patterns/apparmor.txt

################################################################################

%package basesystem
%pattern_basetechnologies
Summary:        Base System (alias pattern for base)
Group:          Metapackages
Provides:       pattern() = basesystem
Provides:       pattern-icon() = pattern-basis
Requires:       pattern() = base

%description basesystem
This is the base runtime system.  It contains only a basic multiuser booting system. For running on real hardware, you need to add additional packages and pattern to make this pattern useful on its own.

%files basesystem
%dir %{_docdir}/patterns
%{_docdir}/patterns/basesystem.txt

################################################################################

%package base
%pattern_basetechnologies
Summary:        Base System
Group:          Metapackages
Provides:       pattern() = base
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1030
Provides:       pattern-visible()
Requires:       aaa_base
Requires:       bash
Requires:       ca-certificates-mozilla
Requires:       coreutils
Requires:       coreutils-systemd
Requires:       glibc
Requires:       libnss_usrfiles2
Requires:       pam
Requires:       pam-config
Requires:       pattern() = minimal_base
# Support multiversion(kernel) (jsc#SLE-10162)
Requires:       purge-kernels-service
Requires:       rpm
Requires:       system-user-nobody
Requires:       systemd
Requires:       util-linux
# Add some static base tool in case system explodes; Recommend only, as users are free to uninstall it
Recommends:     busybox-static
Recommends:     elfutils
Recommends:     glibc-locale-base
Recommends:     hostname
Recommends:     iproute2
Recommends:     issue-generator
Recommends:     lastlog2
Recommends:     pam_pwquality
Recommends:     shadow
Recommends:     system-group-trusted
Recommends:     system-group-wheel
Recommends:     system-user-bin
Recommends:     system-user-daemon
Recommends:     terminfo
Recommends:     terminfo-iterm
Recommends:     terminfo-screen
Recommends:     timezone
Recommends:     wtmpdb
Recommends:     service(network)
# We don't necessarily want zypper in specific minimal environments
# e.g. buildroots and locked down appliance environments
Recommends:     zypper
# We don't necessarily want procps but it's highly useful in default
# installations
Recommends:     procps
# If anything requests "kernel", pick the full kernel package by default
Suggests:       kernel-default
# we have two providers for 'pkgconfig(jack)' - prefer the real one to the one from pipewire
Suggests:       libjack-devel
# We have two providers for libcurl.so.4: libcurl4 and libcurl-mini4. Prefer the fully featured one
Suggests:       libcurl4
# We have two providers for libz.so.1: libz1 and libz1-ng-compat1. Favor the legacy one for now
Suggests:       libz1
# There are multiple providers for /usr/bin/openssl and openssl(cli); defaulting to openssl
Suggests:       openssl
# In line with above: the default openssl version is 1.1 for now; at the moment, the meta package does not provide all symbols needed
Suggests:       openssl-1_1
# if anything wants to recommend an MTA, openSUSE defaults to postfix (boo#1136078)
Suggests:       postfix
# We have two providers of psmisc, favour the regular one (not the busybox one)
Suggests:       psmisc
# we have two providers for 'pulseaudio' - prefer pipewire or pipewire depending on suse_version
# we have two providers for 'service(network)' - prefer NM or wicked depending on suse_version
%if 0%{?suse_version} > 1500
Suggests:       pipewire-pulseaudio
Suggests:       NetworkManager
%else
Suggests:       pulseaudio
Suggests:       wicked
%endif
# hint for aaa_base requiring /usr/bin/xz
Suggests:       xz
%{obsolete_legacy_pattern base}
%{obsolete_legacy_pattern minimal}
%if %{with betatest}
Requires:       aaa_base-malloccheck
%endif
%if 0%{?sle_version}
Recommends:     SUSEConnect
Recommends:     btrfsprogs
# SLES users expect all FS tools to be installed
# bsc#1095916
Recommends:     e2fsprogs
Recommends:     rollback-helper
Recommends:     xfsprogs
%endif
%ifarch ppc64 ppc64le
# bsc#1098849
Requires:       ppc64-diag
%endif

%description base
This is the base runtime system.  It contains only a basic multiuser booting system. For running on real hardware, you need to add additional packages and pattern to make this pattern useful on its own.

%files base
%dir %{_docdir}/patterns
%{_docdir}/patterns/base.txt

################################################################################

# This pattern contains everything the SLES x11 package used to have that
# doesn't need to be in the openSUSE x11 package
%package basic_desktop
%pattern_graphicalenvironments
Summary:        A basic desktop (based on IceWM)
Group:          Metapackages
Provides:       pattern() = basic_desktop
Provides:       pattern-order() = 1802
%if 0%{?is_opensuse}
Provides:       pattern-icon() = pattern-x11
Provides:       pattern-visible()
%endif
Requires:       pattern() = x11
# choose icewm-default if you have a choice
# icewm-lite is too lightweight in new release
Requires:       icewm-default
Requires:       icewm-theme-branding
Recommends:     libgnomesu
Recommends:     openssh-askpass-gnome

%description basic_desktop
This pattern installs a rather basic desktop (icewm)

%files basic_desktop
%dir %{_docdir}/patterns
%{_docdir}/patterns/basic_desktop.txt

################################################################################

%if 0%{?is_opensuse}
%package console
%pattern_basetechnologies
Summary:        Console Tools
Group:          Metapackages
Provides:       pattern() = console
Provides:       pattern-icon() = pattern-cli
Provides:       pattern-order() = 1120
Provides:       pattern-visible()
Requires:       pattern() = enhanced_base
Recommends:     at
Recommends:     bc
Recommends:     ed
Recommends:     emacs-nox
Recommends:     libyui-ncurses
Recommends:     libyui-ncurses-pkg
Recommends:     mc
Recommends:     mosh
Recommends:     mtools
Recommends:     sensors
Recommends:     susepaste
Recommends:     susepaste-screenshot
Recommends:     tmux
Recommends:     w3m
Suggests:       alpine
Suggests:       bsd-games
Suggests:       cnetworkmanager
Suggests:       convert
Suggests:       dar
Suggests:       ding
Suggests:       gcal
Suggests:       grepmail
Suggests:       irssi
Suggests:       lftp
Suggests:       links
Suggests:       lynx
Suggests:       minicom
Suggests:       mlocate
Suggests:       mutt
Suggests:       ncftp
Suggests:       pico
Suggests:       pinfo
Suggests:       slrn
Suggests:       units
Suggests:       vlock
%{obsolete_legacy_pattern console}

%description console
Applications useful for those using the console and no graphical desktop environment.

%files console
%dir %{_docdir}/patterns
%{_docdir}/patterns/console.txt
%endif

################################################################################

%package documentation
%pattern_documentation
Summary:        Help and Support Documentation
Group:          Metapackages
Provides:       pattern() = documentation
Provides:       pattern-icon() = pattern-documentation
Provides:       pattern-order() = 1005
Provides:       pattern-visible()
Requires:       man
Requires:       pattern() = minimal_base
Recommends:     man-pages
# note pam is in every install so no point in using packageand
Recommends:     pam-manpages
%{obsolete_legacy_pattern documentation}

%description documentation
Help and Support Documentation

%files documentation
%dir %{_docdir}/patterns
%{_docdir}/patterns/documentation.txt

################################################################################

%package enhanced_base
%pattern_basetechnologies
Summary:        Enhanced Base System
Group:          Metapackages
Provides:       pattern() = enhanced_base
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1060
Provides:       pattern-visible()
Requires:       pattern() = base
%if 0%{?is_opensuse}
Recommends:     pattern() = documentation
Recommends:     pattern() = sw_management
Recommends:     pattern() = yast2_basis
%endif
Requires:       openssh
Recommends:     aaa_base-extras
# getfacl and setfacl
Recommends:     acl
# getattr and setattr
Recommends:     attr
Recommends:     autofs
Recommends:     bash-completion
Recommends:     bind-utils
# compressor is interesting
Recommends:     bzip2
# #375103
Recommends:     cifs-utils
Recommends:     command-not-found
Recommends:     cpio
Recommends:     cpupower
Recommends:     cryptsetup
Recommends:     curl
# bnc#430895
# cyrus-sasl-saslauthd
# delta rpms are considered cool for updates
Recommends:     deltarpm
Recommends:     diffutils
Recommends:     dos2unix
Recommends:     e2fsprogs
Recommends:     ethtool
Recommends:     file
Recommends:     fillup
Recommends:     findutils
# firewall by default
Recommends:     firewalld
Recommends:     fuse
Recommends:     gawk
Recommends:     gettext-runtime
Recommends:     glibc-locale
Recommends:     gpart
Recommends:     gpg2
Recommends:     gpm
Recommends:     grep
Recommends:     gzip
Recommends:     hdparm
Recommends:     hwinfo
Recommends:     info
Recommends:     initviocons
# ping is required for network tests
Recommends:     iputils
Recommends:     irqbalance
Recommends:     kmod-compat
# #303857
Recommends:     kpartx
Recommends:     krb5
# pager
Recommends:     less
Recommends:     logrotate
Recommends:     lsscsi
# man by default (#304687)
Recommends:     man
# needed for detecting software raid - required by yast2-storage too
Recommends:     mdadm
Recommends:     multipath-tools
# split out of ncurses
Recommends:     ncurses-utils
Recommends:     net-snmp
Recommends:     netcat-openbsd
Recommends:     netcfg
Recommends:     nfs-client
Recommends:     nfsidmap
# Kernel 5.15+ has an improved R/W ntfs module.
# Use ntfs-3g anyway because udisks has issues with mount option handling:
# https://github.com/storaged-project/udisks/issues/932
#if 0%{?suse_version} < 1550
# mount NTFS rw (bsc#1087242)
Recommends:     ntfs-3g
#endif
Recommends:     ntfsprogs
# TODO: should this be in more places
Recommends:     pam-config
Recommends:     parted
Recommends:     pciutils
Recommends:     pciutils-ids
Recommends:     perl-Bootloader
Recommends:     perl-base
Recommends:     pinentry
Recommends:     plymouth
# fuser (psmisc) by default (#304694)
Recommends:     psmisc
Recommends:     rsync
Recommends:     screen
Recommends:     sed
Recommends:     sg3_utils
Recommends:     smartmontools
Recommends:     sudo
Recommends:     systemd-coredump
Recommends:     time
Recommends:     timezone
#SUSE hardware tunings
Recommends:     udev-extra-rules
# lsusb is good for debugging USB devices - #401593
Recommends:     usbutils
# Our editor of choice
Recommends:     vim
Recommends:     wget
Recommends:     xz
Recommends:     zisofs-tools
# DELL computers mainly #403270, but #441079
Suggests:       biosdevname
Suggests:       cpupower
# #437252
Suggests:       pam_ssh
Suggests:       xfsprogs
Suggests:       zip
%{obsolete_legacy_pattern enhanced_base}
%if 0%{?sle_version}
# in SLE we still want /var/log/messages as all of the docu refers to it
# TODO: if we still want it everywhere it should move back to base
Recommends:     rsyslog
%else
# go for journal in TW (boo#1143144)
Recommends:     systemd-logger
%endif
%ifarch aarch64 %{ix86} x86_64
Recommends:     dmidecode
%endif
%ifarch ppc
Recommends:     hfsutils
%endif
%ifarch ppc
# #303737
Recommends:     mouseemu
Recommends:     pdisk
Recommends:     powerpc32
%endif
# Other packages we have in openSUSE and not SLE-15
%if 0%{?is_opensuse}
Recommends:     dmraid
Recommends:     dosfstools
Recommends:     ifplugd
Recommends:     klogd
Recommends:     mpt-status
# boo#1034493
Recommends:     nano
Recommends:     openldap2-client
Recommends:     prctl
Recommends:     procinfo
Recommends:     procmail
Recommends:     providers
# fuser (psmisc) by default (#304694)
Recommends:     psmisc
Recommends:     setserial
Recommends:     sharutils
Recommends:     smp_utils
Recommends:     spax
# useful for debugging
Recommends:     strace
Recommends:     terminfo
# having a ftp command line client is good for moving log files
Recommends:     tnftp
Recommends:     tuned
Recommends:     vlan
Recommends:     wireless-tools
Recommends:     wol
Suggests:       acpid
Suggests:       cracklib-dict-full
# needed as soon as you want to do kerberos authentication
Suggests:       cyrus-sasl-gssapi
Suggests:       delayacct-utils
# Hint for zypper to prefer ed over busybox-ed
Suggests:       ed
Suggests:       groff
Suggests:       hfsutils
# bnc#388570
Suggests:       kerneloops
Suggests:       mailx
Suggests:       man-pages
Suggests:       man-pages-posix
Suggests:       ocfs2-tools
Suggests:       pwgen
Suggests:       unzip
Suggests:       w3m-el
# delta apply
Suggests:       xdelta
# tool for xfs
Suggests:       xfsdump
%ifarch %{ix86} x86_64
Recommends:     acpica
%endif
%ifarch x86_64
Recommends:     mcelog
%endif
%ifarch aarch64 x86_64
Recommends:     numactl
%endif
# #754959
%ifarch %{ix86} x86_64
Suggests:       hyper-v
%endif
%endif

%description enhanced_base
This is the enhanced base runtime system with lots of convenience packages.

%files enhanced_base
%dir %{_docdir}/patterns
%{_docdir}/patterns/enhanced_base.txt

################################################################################

%package fips
%pattern_primaryfunctions
Summary:        FIPS 140-2 specific packages
Group:          Metapackages
Provides:       pattern() = fips
Provides:       pattern-icon() = pattern-basis-addon
Provides:       pattern-order() = 3010
Provides:       pattern-visible()
Requires:       (dracut-fips if dracut)
Requires:       (libcryptsetup12-hmac if libcryptsetup12)
Requires:       (libcryptsetup12-hmac-32bit if libcryptsetup12-32bit)
Requires:       (libfreebl3-hmac if libfreebl3)
Requires:       (libfreebl3-hmac-32bit if libfreebl3-32bit)
Requires:       (libgcrypt20-hmac if libgcrypt20)
Requires:       (libgnutls30-hmac if libgnutls30)
Requires:       (libgnutls30-hmac-32bit if libgnutls30-32bit)
Requires:       (libopenssl-3-fips-provider if libopenssl3)
Requires:       (libopenssl-fips-provider if libopenssl)
Requires:       (libopenssl1_0_0-hmac if libopenssl1_0_0)
Requires:       (libopenssl1_0_0-hmac-32bit if libopenssl1_0_0-32bit)
Requires:       (libopenssl1_1-hmac if libopenssl1_1)
Requires:       (libopenssl1_1-hmac-32bit if libopenssl1_1-32bit)
Requires:       (libsoftokn3-hmac if libsoftokn3)
Requires:       (libsoftokn3-hmac-32bit if libsoftokn3-32bit)
Requires:       (openssh-fips if openssh-clients)
Requires:       (openssh-fips if openssh-server)
Requires:       (strongswan-hmac if strongswan)
Provides:       patterns-sles-fips = %{version}
Obsoletes:      patterns-sles-fips < %{version}
Provides:       patterns-server-enterprise-fips = %{version}
Obsoletes:      patterns-server-enterprise-fips < %{version}
Provides:       patterns-server-enterprise-fips-32bit = %{version}
Obsoletes:      patterns-server-enterprise-fips-32bit < %{version}

%description fips
This pattern installs the FIPS 140-2 specific packages that complete the various
cryptographic modules in use. It is required if you want to run the
machine with "fips=1".

Please note that this pattern only enables FIPS 140-2 compliant operation, it does
not directly make the system FIPS 140-2 certified nor validated.

Please refer to SUSE official statements on the state of FIPS 140-2 certification.

%files fips
%dir %{_docdir}/patterns
%{_docdir}/patterns/fips.txt

################################################################################

%package minimal_base
%pattern_basetechnologies
Summary:        Minimal Appliance Base
Group:          Metapackages
Provides:       pattern() = minimal_base
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 5190
Provides:       pattern-visible()
Requires:       branding
# those packages are actually useless as they don't use
# %_keyringpath but we need them eg for kiwi
Requires:       build-key
Requires:       distribution-release
Requires:       filesystem
# Tell the solver to default to the main product
Suggests:       openSUSE-release
%{obsolete_legacy_pattern minimal_base}

%description minimal_base
This is the minimal runtime system. It is really a minimal system. It is intended as base for Appliances.

%files minimal_base
%dir %{_docdir}/patterns
%{_docdir}/patterns/minimal_base.txt

################################################################################

%package bootloader
%pattern_basetechnologies
Summary:        Bootloader
Group:          Metapackages
Provides:       pattern() = bootloader
Requires:       (grub2-snapper-plugin if snapper)
#
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

%description bootloader
This pattern holds files required for booting the system

%files bootloader
%dir %{_docdir}/patterns
%{_docdir}/patterns/bootloader.txt

################################################################################

%if 0%{?is_opensuse}
%package selinux
%pattern_basetechnologies
Summary:        SELinux
Group:          Metapackages
Provides:       pattern() = selinux
Provides:       pattern-icon() = pattern-selinux
Provides:       pattern-order() = 1110
Provides:       pattern-visible()
Requires:       policycoreutils
Requires:       selinux-autorelabel
Requires:       selinux-policy
Requires:       selinux-tools
Requires:       pattern() = minimal_base
Recommends:     checkpolicy
Recommends:     container-selinux
Recommends:     restorecond
Recommends:     selinux-policy-targeted

%description selinux
Security-Enhanced Linux (SELinux) provides a mechanism for supporting access control security policies, including mandatory access controls (MAC).
Its architecture strives to separate enforcement of security decisions from the security policy, and streamlines the amount of software involved with security policy enforcement.

%files selinux
%dir %{_docdir}/patterns
%{_docdir}/patterns/selinux.txt
%endif

################################################################################

%package sw_management
%pattern_basetechnologies
Summary:        Software Management
Group:          Metapackages
Provides:       pattern() = sw_management
Provides:       pattern-icon() = pattern-software-management
Provides:       pattern-order() = 1360
Provides:       pattern-visible()
Recommends:     pattern() = sw_management_x11
%if 0%{?sle_version}
Recommends:     lifecycle-data
Recommends:     zypper-lifecycle-plugin
%endif
# Zypper is the basic sw_management stack for *SUSE
Requires:       zypper
%{obsolete_legacy_pattern sw_management}

%description sw_management
This pattern provides a graphical application and a command line tool for keeping your system up to date.

%files sw_management
%dir %{_docdir}/patterns
%{_docdir}/patterns/sw_management.txt

################################################################################

%package transactional_base
%pattern_basetechnologies
Summary:        Transactional Base System
Group:          Metapackages
Provides:       pattern() = transactional_base
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 1050
Requires:       read-only-root-fs
Requires:       rebootmgr
Requires:       systemd-presets-branding-transactional-server
Requires:       transactional-update
Requires:       transactional-update-zypp-config
# Useful outside of MicroOS and needed for e.g. SELinux relabelling
Requires:       microos-tools
Requires:       pattern() = base
Suggests:       health-checker

%description transactional_base
This is the base system for a host updated by Transactional Updates. Includes Tools for systems with a read-only root filesystem.

%files transactional_base
%dir %{_docdir}/patterns
%{_docdir}/patterns/transactional_base.txt

################################################################################

%if 0%{?is_opensuse}
%package update_test
%pattern_basetechnologies
Summary:        Tests for the Update Stack
Group:          Metapackages
Provides:       pattern() = update_test
Provides:       pattern-icon() = pattern-tests
Provides:       pattern-order() = 1380
Provides:       pattern-visible()
Requires:       update-test-affects-package-manager
Requires:       update-test-interactive
Requires:       update-test-optional
Requires:       update-test-reboot-needed
Requires:       update-test-security
Requires:       update-test-trivial
%{obsolete_legacy_pattern update_test}

%description update_test
Packages used for testing that the update stack works.  These tiny packages do not have any functionality themselves.

%files update_test
%dir %{_docdir}/patterns
%{_docdir}/patterns/update_test.txt
%endif

################################################################################

%package x11
%pattern_graphicalenvironments
Summary:        X Window System
Group:          Metapackages
Provides:       pattern() = x11
Provides:       pattern-icon() = pattern-x11
Provides:       pattern-order() = 1800
Provides:       pattern-visible()
Requires:       pattern() = base
%if 0%{?is_opensuse}
Recommends:     pattern() = x11_enhanced
%else
# Requires to be safe on upgrade path for SLE
Requires:       pattern() = basic_desktop
%endif
Requires:       xf86-input-libinput
Requires:       xorg-x11-fonts-core
Requires:       xorg-x11-server
# Recommend something other than xdm, default to lightdm
Recommends:     (gdm or lightdm or sddm)
Recommends:     dejavu-fonts
Recommends:     noto-sans-fonts
Recommends:     x11-tools
Recommends:     xdmbgrd
Recommends:     xorg-x11-Xvnc
Recommends:     xorg-x11-driver-video
Recommends:     xorg-x11-essentials
Recommends:     xorg-x11-fonts
Recommends:     xorg-x11-server-extra
Recommends:     xterm
Recommends:     xtermset
Suggests:       lightdm
%{obsolete_legacy_pattern x11}
# bsc#1071953
%ifnarch s390 s390x
Recommends:     xf86-input-vmmouse
Recommends:     xf86-input-wacom
%endif

%description x11
The X Window System provides the only standard platform-independent networked graphical window system bridging the heterogeneous platforms in today's enterprise: from network servers to desktops, thin clients, laptops, and handhelds, independent of operating system and hardware.

%files x11
%dir %{_docdir}/patterns
%{_docdir}/patterns/x11.txt

################################################################################

%package x11_enhanced
%pattern_graphicalenvironments
Summary:        X Window System
Group:          Metapackages
Provides:       pattern() = x11_enhanced
Provides:       pattern-icon() = pattern-x11
Provides:       pattern-order() = 1801
# For SLE-15-SPX - install basis and server here to keep behavior functionally the same
# Jump / Leap can follow the same setup as Tumbleweed
%if !0%{?is_opensuse}
Recommends:     pattern() = yast2_basis
Recommends:     pattern() = yast2_server
%endif
Requires:       pattern() = enhanced_base
Requires:       pattern() = fonts
Requires:       pattern() = x11
Recommends:     pattern() = x11_yast
Recommends:     pattern() = yast2_desktop
# 1057377
Requires:       glibc-locale
Requires:       glibc-locale-base
Requires:       xkeyboard-config
Requires:       xorg-x11-essentials
Recommends:     cabextract
# Bug 424707 - Feature "Command not found" for openSUSE by default
Recommends:     command-not-found
Recommends:     dbus-1-glib
Recommends:     dbus-1-x11
Recommends:     dialog
Recommends:     fontconfig
Recommends:     fonts-config
Recommends:     fribidi
Recommends:     ghostscript-x11
Recommends:     numlockx
Recommends:     opensuse-welcome
# #353229 - drag in empty replacements
Recommends:     translation-update
# autoconfig new printers - bnc#808014
Recommends:     udev-configure-printer
# make it possible to install firefox or chromium
Recommends:     web_browser
Recommends:     xauth
Recommends:     xdmbgrd
Recommends:     xkeyboard-config
Recommends:     xorg-x11-fonts
Recommends:     xorg-x11-fonts-core
Recommends:     yast2-control-center-gnome
# Recommend yast2-network until the Generic Desktop Role defaults to NetworkManager
# At worst people need a way to switch from Wicked to NetworkManager.
Recommends:     yast2-network
# This will install Firefox if no other browser is selected
Suggests:       MozillaFirefox
Suggests:       MozillaFirefox-translations
%if 0%{?is_opensuse}
# #394406
Suggests:       desktop-data-openSUSE-extra
%else
Recommends:     MozillaFirefox-branding-SLE
Recommends:     desktop-data-SLE
%endif
%if 0%{?is_opensuse}
# people love having numlock configurable
Recommends:     numlockx
Recommends:     openssh-askpass
Recommends:     susepaste
Recommends:     susepaste-screenshot
# needed e.g. for nvidia drivers
# #302566
Recommends:     x11-tools
Recommends:     xorg-x11-libX11-ccache
Suggests:       MozillaThunderbird
Suggests:       WindowMaker
Suggests:       WindowMaker-applets
Suggests:       WindowMaker-themes
Suggests:       gvim
Suggests:       hexchat
Suggests:       unclutter
Suggests:       wpa_supplicant-gui
Suggests:       xlockmore
Suggests:       xorg-x11-driver-video-radeonhd
Suggests:       xorg-x11-driver-video-unichrome
# #389816
Suggests:       xorg-x11-server-sdk
%endif

%description x11_enhanced
The X Window System provides the only standard platform-independent networked graphical window system bridging the heterogeneous platforms in today's enterprise: from network servers to desktops, thin clients, laptops, and handhelds, independent of operating system and hardware.

%files x11_enhanced
%dir %{_docdir}/patterns
%{_docdir}/patterns/x11_enhanced.txt

################################################################################

%ifarch armv6hl armv7hl aarch64
%package x11_raspberrypi
%pattern_graphicalenvironments
Summary:        X Window System
Group:          Metapackages
Provides:       pattern() = x11_raspberrypi
Provides:       pattern-icon() = pattern-x11
Provides:       pattern-order() = 1803
Provides:       pattern-visible()
# Use only Requires - it's meant to be used on JeOS, which ignores Recommends
# Based on SUSE:SLE-15:GA:RaspberryPI/kiwi-templates-SLES15-JeOS/JeOS.kiwi
# Patterns
Requires:       pattern() = base
Requires:       pattern() = x11
# Other X11 packages
Requires:       gtk2-metatheme-adwaita
Requires:       gtk3-metatheme-adwaita
# X11/IceWM-specific packages
Requires:       icewm
Requires:       icewm-default
Requires:       icewm-lite
Requires:       icewm-theme-branding
# bsc#1095870
Requires:       libyui-ncurses-pkg
Requires:       libyui-qt-pkg
# for IceWM taskbar mailbox icon (bsc#1093913)
Requires:       mutt
Requires:       mutt-lang
Requires:       polkit-default-privs
Requires:       polkit-gnome-lang
Requires:       x11-tools
Requires:       x11perf
Requires:       xauth
Requires:       xbacklight
Requires:       xclock
Requires:       xconsole
Requires:       xcursor-themes
Requires:       xcursorgen
Requires:       xdg-user-dirs
Requires:       xdg-user-dirs-gtk
Requires:       xdg-user-dirs-gtk-lang
Requires:       xdg-utils
Requires:       xdm
Requires:       xdmbgrd
Requires:       xdpyinfo
Requires:       xev
Requires:       xeyes
# Drivers
Requires:       xf86-input-evdev
Requires:       xf86-input-libinput
Requires:       xf86-video-fbdev
Requires:       xfd
Requires:       xfontsel
Requires:       xgamma
Requires:       xhost
Requires:       xinit
Requires:       xinput
Requires:       xkbcomp
Requires:       xkbevd
Requires:       xkbprint
Requires:       xkbutils
Requires:       xkeyboard-config
Requires:       xkill
Requires:       xlogo
Requires:       xlsatoms
Requires:       xlsclients
Requires:       xlsfonts
Requires:       xmag
Requires:       xmessage
Requires:       xmodmap
Requires:       xorg-x11
Requires:       xorg-x11-fonts-core
Requires:       xorg-x11-server
Requires:       xorg-x11-server-extra
Requires:       xprop
Requires:       xrandr
Requires:       xrdb
Requires:       xrestop
Requires:       xscope
Requires:       xscreensaver
Requires:       xscreensaver-data
Requires:       xset
Requires:       xsetmode
Requires:       xsetpointer
Requires:       xsetroot
Requires:       xterm
Requires:       xtermset
Requires:       xvinfo
Requires:       xwd
Requires:       xwininfo
Requires:       yast2-control-center-qt
Requires:       yast2-packager
Requires:       yast2-snapper
Requires:       yast2-x11
# Branding
%if ! 0%{?is_opensuse}
Requires:       MozillaFirefox-branding-SLE
%endif

%description x11_raspberrypi
The X Window System provides the only standard platform-independent networked graphical window system bridging the heterogeneous platforms in today's enterprise: from network servers to desktops, thin clients, laptops, and handhelds, independent of operating system and hardware.

%files x11_raspberrypi
%dir %{_docdir}/patterns
%{_docdir}/patterns/x11_raspberrypi.txt
%endif

################################################################################

%prep

%build

%install
mkdir -p %{buildroot}%{_docdir}/patterns
for i in apparmor base enhanced_base minimal_base sw_management x11 x11_enhanced; do
    echo "This file marks the pattern $i to be installed." \
    >"%{buildroot}%{_docdir}/patterns/$i.txt"
    echo "This file marks the pattern $i to be installed." \
    >"%{buildroot}%{_docdir}/patterns/$i-32bit.txt"
done

# These packages don't generate a 32bit pattern
for i in basesystem bootloader basic_desktop documentation fips transactional_base \
%if 0%{?is_opensuse}
console selinux update_test \
%else
%ifnarch s390 s390x
32bit \
%endif
%endif
%ifarch armv6hl armv7hl aarch64
x11_raspberrypi \
%endif
; do
    echo "This file marks the pattern $i to be installed." \
    >"%{buildroot}%{_docdir}/patterns/$i.txt"
done

%ifarch x86_64
echo "This file marks the pattern 32bit to be installed." \
>"%{buildroot}%{_docdir}/patterns/32bit.txt"
%endif

#
# This file is created at check-in time. Sorry for the inconsistent workflow :(
#
%include %{SOURCE1}

%changelog
