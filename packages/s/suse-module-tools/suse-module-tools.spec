#
# spec file for package suse-module-tools
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


# Define _rpmmacrodir if it's not defined yet
%{!?_rpmmacrodir: %global _rpmmacrodir %{_rpmconfigdir}/macros.d}
%define modules_load_dir /usr/lib/modules-load.d

# List of legacy file systems to be blacklisted by default
%global fs_blacklist adfs affs bfs befs cramfs efs erofs exofs freevxfs f2fs hfs hpfs jfs minix nilfs2 ntfs omfs qnx4 qnx6 sysv ufs

%if 0%{?sle_version} >= 120200 && 0%{?sle_version} < 150000
%global softdep_br_netfilter 1
%endif

Name:           suse-module-tools
Version:        15.3.3
Release:        0
Summary:        Configuration for module loading and SUSE-specific utilities for KMPs
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://github.com/openSUSE/suse-module-tools
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.rpmlintrc
Requires:       coreutils
Requires:       findutils
Requires:       grep
Requires:       gzip
Requires:       rpm
Requires:       sed
# Use weak dependencies for mkinitrd and kmod in order to
# keep Ring0 lean. In normal deployments, these packages
# will be available anyway.
Recommends:     mkinitrd
%if 0%{?suse_version} >= 1315
Recommends:     kmod
%else
Recommends:     modutils
%endif
# This release requires the dracut fix for bsc#1127891
Conflicts:      dracut < 44.2

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

%description legacy
This package contains the legacy "weak-modules" script for kernel
module package (KMP) support. It was replaced by "weak-modules2" in
SLE 11 and later.

%prep
%setup -q

%build

%install
# now assemble the parts for modprobe.conf
cp modprobe.conf/modprobe.conf.common 00-system.conf
if [ -f "modprobe.conf/modprobe.conf.$RPM_ARCH" ]; then
	cat "modprobe.conf/modprobe.conf.$RPM_ARCH" >>00-system.conf
fi
install -d -m 755 "%{buildroot}%{_sysconfdir}/modprobe.d"
install -pm644 "10-unsupported-modules.conf" \
	"%{buildroot}%{_sysconfdir}/modprobe.d/"
install -pm644 00-system.conf "%{buildroot}%{_sysconfdir}/modprobe.d/"

%if 0%{?softdep_br_netfilter}
# softdep bridge->br_netfilter, SLE only
install -pm644 modprobe.conf/00-system-937216.conf %{buildroot}%{_sysconfdir}/modprobe.d
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150100
install -pm644 modprobe.conf/modprobe.conf.blacklist "%{buildroot}%{_sysconfdir}/modprobe.d/50-blacklist.conf"
%endif
install -pm644 modprobe.conf/modprobe.conf.local "%{buildroot}%{_sysconfdir}/modprobe.d/99-local.conf"
install -d -m 755 "%{buildroot}%{_sysconfdir}/depmod.d"
install -pm 644 "depmod-00-system.conf" \
	"%{buildroot}%{_sysconfdir}/depmod.d/00-system.conf"

# "/usr/lib/module-init-tools" name hardcoded in KMPs, mkinitrd, etc.
install -d -m 755 "%{buildroot}/usr/lib/module-init-tools"
install -pm 755 weak-modules{,2} "%{buildroot}/usr/lib/module-init-tools/"
install -pm 755 driver-check.sh "%{buildroot}/usr/lib/module-init-tools/"

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

# systemd service to load /boot/sysctl.conf-`uname -r`
install -d -m 755 "%{buildroot}%{_unitdir}/systemd-sysctl.service.d"
install -pm 644 50-kernel-uname_r.conf "%{buildroot}%{_unitdir}/systemd-sysctl.service.d"

# Ensure that the sg driver is loaded early (bsc#1036463)
# Not needed in SLE11, where sg is loaded via udev rule.
install -d -m 755 "%{buildroot}%{modules_load_dir}"
install -pm 644 sg.conf "%{buildroot}%{modules_load_dir}"

mkdir -p %{buildroot}%{_defaultlicensedir}

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150100
for mod in %{fs_blacklist}; do
    echo "\
# The $mod file system is blacklisted by default because it isn't actively
# supported by SUSE, not well maintained, or may have security vulnerabilites.
# To enable autoloading the $mod file system module, comment out the
# \"blacklist $mod\" statement below. ENABLE AT YOUR OWN RISK.
#
# File system modules loaded at installation time of the %{name} package
# are not blacklisted. This is achieved by commenting out the blacklist
# line in the post-installation script. To prevent the post-installation
# script from modifying this file, delete the line containing \"THIS FILE MAY
# BE MODIFIED\" at the bottom.
blacklist $mod
# __THIS FILE MAY BE MODIFIED__" \
	>%{buildroot}%{_sysconfdir}/modprobe.d/60-blacklist_fs-"$mod".conf
done
%endif

%post
%if 0%{?sle_version} >= 150000
# Delete obsolete unsupported-modules file from SLE11
rm -f %{_sysconfdir}/modprobe.d/unsupported-modules
%else
# Logic for releases below CODE 15
%if 0%{?is_opensuse} == 1
allowed=1
%else
allowed=0
%endif
test_allow_on_install()
{
	# configure handling of unsupported modules
	# default is to allow them
	allow=1
	# if the obsolete LOAD_UNSUPPORTED_MODULES_AUTOMATICALLY variable is
	# set to no, don't allow (this was used in SLES 9 and 10)
	if test -e %{_sysconfdir}/sysconfig/hardware/config; then
		. %{_sysconfdir}/sysconfig/hardware/config
		if test "x$LOAD_UNSUPPORTED_MODULES_AUTOMATICALLY" = "xno"; then
			allow=0
		fi
		# obsolete
		rm %{_sysconfdir}/sysconfig/hardware/config
	fi
	# don't change the setting during upgrade
	if test "$1" != 1; then
		allow=
		return
	fi
	# on SLES, the default is not to allow unsupported modules
	if grep -qs "Enterprise Server" %{_sysconfdir}/os-release; then
		allow=0
	else
		return
	fi
	# unless the admin passed "oem-modules=1" to the kernel during install
	if grep -qs '\<oem-modules=1\>' /proc/cmdline; then
		allow=1
		return
	fi
	# or if the installer already loaded some unsupported modules
	# (see TAINT_NO_SUPPORT in /etc/src/linux/include/linux/kernel.h)
	tainted=$(cat /proc/sys/kernel/tainted 2>/dev/null || echo 0)
	if test $((tainted & (1<<30))) != 0; then
		allow=1
		return
	fi
}
# upgrade from old locations
if test -e %{_sysconfdir}/modprobe.d/unsupported-modules; then
	mv -f %{_sysconfdir}/modprobe.d/unsupported-modules \
		%{_sysconfdir}/modprobe.d/10-unsupported-modules.conf
fi
test_allow_on_install "$@"
if test -n "$allow" -a "$allow" != "$allowed"; then
	sed -ri 's/^( *allow_unsupported_modules *) [01]/\1 '"$allow"'/' \
		%{_sysconfdir}/modprobe.d/10-unsupported-modules.conf
fi
%endif

# upgrade from old locations
if test -e %{_sysconfdir}/modprobe.conf.local; then
	mv -f %{_sysconfdir}/modprobe.conf.local \
		%{_sysconfdir}/modprobe.d/99-local.conf
fi

# Avoid systems becoming unbootable by blacklisting filesystem
# modules. Modules loaded at installation time will not be
# blacklisted (the blacklist statement is commented out).
# config(noreplace) makes sure that this is not overwritten by rpm.
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150100
for mod in %{fs_blacklist}; do
	conf=%{_sysconfdir}/modprobe.d/60-blacklist_fs-"$mod".conf
	if [ -f "$conf" ] && \
	    grep -q '^# __THIS FILE MAY BE MODIFIED__$' "$conf" && \
            sed '/^nodev/d;' /proc/filesystems | grep -q "\<$mod\>"; then
		sed -i '
/^# next line was commented out by postinstall script of %{name}$/d
/^blacklist '"$mod"'/{i\
# next line was commented out by postinstall script of %{name}
s/^/# /
}' "$conf"
	fi
done
%endif

%files
%defattr(-,root,root)

%if 0%{?sle_version:%{sle_version}}%{!?sle_version:150000} <= 120200
%dir %{_defaultlicensedir}
%endif
%license LICENSE
%doc README.SUSE
%dir %{_sysconfdir}/modprobe.d
%config %{_sysconfdir}/modprobe.d/00-system.conf
%if 0%{?softdep_br_netfilter}
%config(noreplace) %{_sysconfdir}/modprobe.d/00-system-937216.conf
%endif
%config(noreplace) %{_sysconfdir}/modprobe.d/10-unsupported-modules.conf
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150100
%config(noreplace) %{_sysconfdir}/modprobe.d/50-blacklist.conf
%config(noreplace) %{_sysconfdir}/modprobe.d/60-blacklist_fs-*.conf
%endif
%config(noreplace) %{_sysconfdir}/modprobe.d/99-local.conf
%dir %{_sysconfdir}/depmod.d
%config %{_sysconfdir}/depmod.d/00-system.conf
%if 0%{?suse_version} < 1550
%{_rpmmacrodir}/macros.initrd
%endif
%{_bindir}/kmp-install
/usr/lib/module-init-tools
%exclude /usr/lib/module-init-tools/weak-modules
%{_unitdir}/systemd-sysctl.service.d
%dir %{modules_load_dir}
%{modules_load_dir}/sg.conf

%files legacy
%defattr(-,root,root)
/usr/lib/module-init-tools/weak-modules

%changelog
