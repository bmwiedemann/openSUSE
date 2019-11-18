#
# spec file for package patterns-microos
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           patterns-microos
Version:        5.0
Release:        0
Summary:        Patterns for openSUSE MicroOS
License:        MIT
Group:          Metapackages
Url:            http://en.opensuse.org/Patterns
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
#Obsolete CaaSP Patterns
Provides:       patterns-caasp-MicroOS
Obsoletes:      patterns-caasp-MicroOS <= 4.0
Requires:       aaa_base
Requires:       audit
Requires:       bash
Requires:       btrfsmaintenance
Requires:       btrfsprogs
Requires:       ca-certificates
Requires:       ca-certificates-mozilla
Requires:       chrony
Requires:       coreutils
Requires:       cracklib-dict-small
Requires:       dosfstools
Requires:       dracut
Requires:       elfutils
Requires:       fcoe-utils
Requires:       filesystem
Requires:       glibc
Requires:       grub2
Requires:       grub2-snapper-plugin
Requires:       haveged
Requires:       health-checker
Requires:       health-checker-plugins-MicroOS
Requires:       hwinfo
Requires:       iputils
Requires:       kbd
Requires:       kdump
Requires:       kernel-base
Requires:       kmod
Requires:       kubic-locale-archive
Requires:       less
Requires:       login
Requires:       logrotate
Requires:       microos-tools
Requires:       nano
Requires:       net-tools
Requires:       openssh
Requires:       pam
Requires:       parted
Requires:       pciutils
Requires:       pkg-config
Requires:       procps
Requires:       rebootmgr
Requires:       rpm
Requires:       shadow
Requires:       snapper
Requires:       sudo
Requires:       supportutils
Requires:       sysconfig
Requires:       sysfsutils
Requires:       systemd
Requires:       systemd-presets-branding-MicroOS
Requires:       tallow
Requires:       terminfo
Requires:       timezone
Requires:       transactional-update
Requires:       transactional-update-zypp-config
Requires:       udev
Requires:       vlan
Requires:       which
Requires:       wicked
Requires:       xfsprogs
Requires:       yast2-logs
Requires:       zypper
Requires:       zypper-needs-restarting
Conflicts:      gettext-runtime-mini
Conflicts:      krb5-mini
%ifarch x86_64
Requires:       biosdevname
%endif
Requires:       openSUSE-MicroOS-release
Requires:       openSUSE-build-key
Obsoletes:      suse-build-key < 12.1
%ifnarch s390x
Requires:       grub2-branding-openSUSE
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
%ifnarch s390x
Requires:       irqbalance
%endif
%ifarch x86_64
Requires:       mokutil
Requires:       shim
%endif
Requires:       system-group-hardware
Requires:       system-group-wheel
Requires:       system-user-nobody

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
Requires:       pattern() = microos_base
#Obsolete CaaSP Patterns
Provides:       patterns-caasp-MicroOS-defaults
Obsoletes:      patterns-caasp-MicroOS-defaults <= 4.0
Requires:       systemd-logger

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
#Obsolete CaaSP Patterns
Provides:       patterns-caasp-hardware
Obsoletes:      patterns-caasp-hardware <= 4.0
%ifarch armv7l armv7hl
Requires:       kernel-lpae
%else
Requires:       kernel-default
%endif
Requires:       kernel-firmware

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
#Obsolete CaaSP Patterns
Provides:       patterns-caasp-apparmor
Obsoletes:      patterns-caasp-apparmor <= 4.0
Requires:       apparmor-parser
Requires:       apparmor-profiles
Requires:       apparmor-utils

%description apparmor
Packages required to enable Apparmor on openSUSE MicroOS.

%package selinux
Summary:        SELinux Support
Group:          Metapackages
Provides:       pattern() = microos_selinux
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 9055
#Obsolete CaaSP Patterns
Provides:       patterns-caasp-selinux
Obsoletes:      patterns-caasp-selinux <= 4.0
Requires:       checkpolicy
Requires:       mcstrans
Requires:       policycoreutils
Requires:       restorecond
Requires:       selinux-tools

%description selinux
This are packages which are required to enable SELinux on openSUSE MicroOS

%package sssd_ldap
Summary:        LDAP client
Group:          Metapackages
Provides:       pattern() = microos_sssd_ldap
Provides:       pattern-category() = MicroOS
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 9060
Provides:       pattern-visible()
#Obsolete CaaSP Patterns
Provides:       patterns-caasp-sssd-ldap
Obsoletes:      patterns-caasp-sssd-ldap <= 4.0
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
#Obsolete CaaSP Patterns
Provides:       patterns-caasp-ima_evm
Obsoletes:      patterns-caasp-ima_evm <= 4.0
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
#Obsolete CaaSP Patterns
Provides:       patterns-caasp-cloud
Obsoletes:      patterns-caasp-cloud <= 4.0
Requires:       cloud-init
Requires:       cloud-init-config-MicroOS

%description cloud
Packages required to enable openSUSE MicroOS in the Cloud.

%package onlyDVD
Summary:        Packages only for the DVD of openSUSE MicroOS
Group:          Metapackages
Provides:       pattern-category() = MicroOS
Requires:       bcache-tools
Requires:       cracklib-dict-full
Requires:       cryptsetup
Requires:       glibc-locale
Requires:       iscsiuio
Requires:       multipath-tools
Requires:       open-iscsi
%ifarch %ix86 x86_64
Requires:       hyper-v
Requires:       open-vm-tools
%endif
Requires:       tftpboot-installation-openSUSE-MicroOS-%{_arch}
%ifarch %ix86 x86_64
Requires:       ucode-amd
Requires:       ucode-intel
Requires:       vim
%endif
Requires:       wpa_supplicant
Provides:       pattern() = microos_onlyDVD
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 9900
Requires:       pattern() = microos_apparmor
Requires:       pattern() = microos_cloud
Requires:       pattern() = microos_hardware
Requires:       pattern() = microos_ima_evm
Requires:       pattern() = microos_sssd_ldap
#Obsolete CaaSP Patterns
Provides:       patterns-caasp-onlyDVD
Obsoletes:      patterns-caasp-onlyDVD <= 4.0

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
Requires:       pattern() = microos_ima_evm
Requires:       pattern() = microos_selinux
Requires:       pattern() = microos_sssd_ldap
#Obsolete CaaSP Patterns
Provides:       patterns-caasp-alt-onlyDVD
Obsoletes:      patterns-caasp-alt-onlyDVD <= 4.0

%description alt_onlyDVD
Alternative additional packages on a openSUSE MicroOS DVD.

%prep
# empty on purpose

%build
# empty on purpose

%install
mkdir -p %buildroot/usr/share/doc/packages/patterns-microos/
for i in basesystem base defaults hardware ima_evm apparmor selinux sssd_ldap cloud \
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

%files cloud
%defattr(-,root,root)
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/cloud.txt

%files onlyDVD
%defattr(-,root,root)
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/onlyDVD.txt

%files alt_onlyDVD
%defattr(-,root,root)
%dir %{_docdir}/patterns-microos
%{_docdir}/patterns-microos/alt_onlyDVD.txt

%changelog
