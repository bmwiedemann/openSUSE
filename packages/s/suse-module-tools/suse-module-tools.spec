#
# spec file for package suse-module-tools
#
# Copyright (c) 2021 SUSE LLC
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

# missing in SLE15 (systemd-rpm-macros)
%{!?_modulesloaddir: %global _modulesloaddir /usr/lib/modules-load.d}

# Location for modprobe and depmod .conf files
#
# This assumes post-usr-merge (20210527) for Tumbleweed
%if 0%{?suse_version} >= 1550
%global modprobe_dir /usr/lib/modprobe.d
%global depmod_dir /usr/lib/depmod.d
%global with_kernel_sysctl 1
# boot_sysctl may be dropped on TW when we can assume that nobody keeps
# kernel packages around that store sysctl files under /boot
%bcond_without boot_sysctl
%else
%global modprobe_dir /lib/modprobe.d
%global depmod_dir /lib/depmod.d
%global with_boot_sysctl 1
%endif
%global sysctl_dropin %{_unitdir}/systemd-sysctl.service.d/50-kernel-uname_r.conf
%global systemd_units %{?with_boot_sysctl:boot-sysctl.service} %{?with_kernel_sysctl:kernel-sysctl.service}

# List of legacy file systems to be blacklisted by default
%global fs_blacklist adfs affs bfs befs cramfs efs erofs exofs freevxfs hfs hpfs jfs minix nilfs2 ntfs omfs qnx4 qnx6 sysv ufs

# List of all files installed under modprobe.d
# Note: this list contains files installed by previous versions, like 00-system-937216.conf!
%global modprobe_conf_files 00-system 00-system-937216 10-unsupported-modules 50-blacklist 60-blacklist_fs-* 99-local
%global modprobe_conf_rpmsave %(echo "%{modprobe_conf_files}" | sed 's,\\([^ ]*\\),%{_sysconfdir}/modprobe.d/\\1.conf.rpmsave,g')

Name:           suse-module-tools
Version:        16.0.9
Release:        0
Summary:        Configuration for module loading and SUSE-specific utilities for KMPs
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://github.com/openSUSE/suse-module-tools
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.rpmlintrc
BuildRequires:  systemd-rpm-macros
Requires:       /usr/bin/grep
Requires:       /usr/bin/gzip
Requires:       /usr/bin/sed
Requires:       coreutils
Requires:       findutils
Requires:       systemd-rpm-macros
Requires:       rpm
Requires(post): /usr/bin/grep
Requires(post): /usr/bin/sed
Requires(post): coreutils
# Use weak dependencies for dracut and kmod in order to
# keep Ring0 lean. In normal deployments, these packages
# will be available anyway.
Recommends:     dracut
Recommends:     kmod
# This release requires the dracut module 90nvdimm
Conflicts:      dracut < 49.1
# TW: conflict with pre-usrmerge
%if 0%{?suse_version} >= 1550
Conflicts:      filesystem < 15.5-40.2
%endif

%description
This package contains helper scripts for KMP installation and
uninstallation, as well as default configuration files for depmod and
modprobe. These utilities are provided by kmod-compat or
module-init-tools, whichever implementation you choose to install.


%package legacy
Summary:        Legacy "weak-modules" script for Code10
Group:          System/Base
Requires:       %{name}
Requires:       binutils
Supplements:    dkms

%description legacy
This package contains the legacy "weak-modules" script for kernel
module package (KMP) support. It was replaced by "weak-modules2" in
SLE 11 and later. It is still used by the DKMS module packaging framework.

%prep
%setup -q

%build
sed -i 's/@FS_BLACKLIST@.*/%{fs_blacklist}/' README.md

%install
# now assemble the parts for modprobe.conf
cp modprobe.conf/modprobe.conf.common 00-system.conf
%ifarch ppc64le
ln -f modprobe.conf/modprobe.conf.ppc64 modprobe.conf/modprobe.conf.$RPM_ARCH
%endif
if [ -f "modprobe.conf/modprobe.conf.$RPM_ARCH" ]; then
	cat "modprobe.conf/modprobe.conf.$RPM_ARCH" >>00-system.conf
fi
install -d -m 755 "%{buildroot}%{modprobe_dir}"
install -d -m 755 "%{buildroot}%{_sysconfdir}/modprobe.d"
install -pm644 "10-unsupported-modules.conf" \
	"%{buildroot}%{modprobe_dir}/"
install -pm644 00-system.conf "%{buildroot}%{modprobe_dir}/"

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150100
install -pm644 modprobe.conf/modprobe.conf.blacklist "%{buildroot}%{modprobe_dir}/50-blacklist.conf"
%endif
install -d -m 755 "%{buildroot}/%{depmod_dir}"
install -d -m 755 "%{buildroot}%{_sysconfdir}/depmod.d"
install -pm 644 "depmod-00-system.conf" "%{buildroot}%{depmod_dir}/00-system.conf"

# "/usr/lib/module-init-tools" name hardcoded in KMPs, mkinitrd, etc.
install -d -m 755 "%{buildroot}/usr/lib/module-init-tools"
install -pm 755 -t "%{buildroot}/usr/lib/module-init-tools/" \
	weak-modules{,2} driver-check.sh unblacklist lsinitrd-quick

%if 0%{?suse_version} < 1550
# rpm macros and helper
# The RPM Macros have been moved to the package rpm-config-SUSE after CODE15, thus are no longer
# shipped here
install -d -m 755 "%{buildroot}%{_rpmmacrodir}"
install -pm 644 "macros.initrd" "%{buildroot}%{_rpmmacrodir}"
%endif
install -pm 755 "regenerate-initrd-posttrans" "%{buildroot}/usr/lib/module-init-tools/"

install -d -m 755 "%{buildroot}%{_prefix}/bin"
install -pm 755 kmp-install "%{buildroot}%{_bindir}/"

# systemd service(s) to load kernel-specific sysctl settings
install -d -m 755 "%{buildroot}%{_unitdir}/systemd-sysctl.service.d"
echo '[Unit]' >"%{buildroot}%{sysctl_dropin}"
%if %{with kernel_sysctl}
install -m 644 kernel-sysctl.service "%{buildroot}%{_unitdir}"
echo 'Wants=kernel-sysctl.service' >>"%{buildroot}%{sysctl_dropin}"
%endif
%if %{with boot_sysctl}
install -m 644 boot-sysctl.service "%{buildroot}%{_unitdir}"
echo 'Wants=boot-sysctl.service' >>"%{buildroot}%{sysctl_dropin}"
%endif

# Ensure that the sg driver is loaded early (bsc#1036463)
# Not needed in SLE11, where sg is loaded via udev rule.
install -d -m 755 "%{buildroot}%{_modulesloaddir}"
install -pm 644 sg.conf "%{buildroot}%{_modulesloaddir}"
%ifarch ppc64 ppc64le
install -d -m 755 %{buildroot}/usr/lib/systemd/system-generators
install -m 755 udev-trigger-generator %{buildroot}/usr/lib/systemd/system-generators
%endif

mkdir -p %{buildroot}%{_defaultlicensedir}

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150100
for mod in %{fs_blacklist}; do
    echo "\
# DO NOT EDIT THIS FILE!
#
# The $mod file system is blacklisted by default because it isn't actively
# supported by SUSE, not well maintained, or may have security vulnerabilites.
blacklist $mod
# The filesystem can be un-blacklisted by running \"modprobe $mod\".
# See README.md in the %{name} package for details.
install $mod /usr/lib/module-init-tools/unblacklist $mod; /sbin/modprobe --ignore-install $mod
" \
	>%{buildroot}%{modprobe_dir}/60-blacklist_fs-"$mod".conf
done
%endif

%pre
%service_add_pre %{systemd_units}
# Avoid restoring old .rpmsave files in %posttrans
for f in %{modprobe_conf_rpmsave}; do
    if [ -f ${f} ]; then
	mv -f ${f} ${f}.%{name}
    fi
done
if [ -f %{_sysconfdir}/depmod.d/00-system.conf.rpmsave ]; then
    mv -f %{_sysconfdir}/depmod.d/00-system.conf.rpmsave \
          %{_sysconfdir}/depmod.d/00-system.conf.rpmsave.%{name}
fi
exit 0

%post
%service_add_post %{systemd_units}
exit 0

%preun
%service_del_preun %{systemd_units}
exit 0

%postun
%service_del_postun_without_restart %{systemd_units}
exit 0

%posttrans
# If the user had modified any of the configuration files installed under
# /etc, they'll now be renamed to .rpmsave files. Restore them.
for f in %{modprobe_conf_rpmsave}; do
    if [ -f ${f} ]; then
	mv -fv ${f} ${f%.rpmsave}
    fi
done
if [ -f %{_sysconfdir}/depmod.d/00-system.conf.rpmsave ]; then
    mv -fv %{_sysconfdir}/depmod.d/00-system.conf.rpmsave \
           %{_sysconfdir}/depmod.d/00-system.conf
fi
exit 0

%files
%defattr(-,root,root)

%license LICENSE
%doc README.md
%{modprobe_dir}
%dir %{_sysconfdir}/modprobe.d
%{depmod_dir}
%dir %{_sysconfdir}/depmod.d
%if 0%{?suse_version} < 1550
%{_rpmmacrodir}/macros.initrd
%endif
%{_bindir}/kmp-install
/usr/lib/module-init-tools
%exclude /usr/lib/module-init-tools/weak-modules
%{_unitdir}/*.service
%{_unitdir}/systemd-sysctl.service.d
%{_modulesloaddir}
%ifarch ppc64 ppc64le
/usr/lib/systemd/system-generators
%endif

%files legacy
%defattr(-,root,root)
/usr/lib/module-init-tools/weak-modules

%changelog
