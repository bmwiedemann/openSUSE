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

# Location for modprobe and depmod .conf files
#
# This assumes post-usr-merge (20210527) for Tumbleweed
%global modprobe_dir /usr/lib/modprobe.d
%global depmod_dir /usr/lib/depmod.d
%global dracutlibdir %{_prefix}/lib/dracut
%global with_kernel_sysctl 1
# boot_sysctl may be dropped on TW when we can assume that nobody keeps
# kernel packages around that store sysctl files under /boot
%bcond_without boot_sysctl
%global sysctl_dropin %{_unitdir}/systemd-sysctl.service.d/50-kernel-uname_r.conf
%global systemd_units %{?with_boot_sysctl:boot-sysctl.service} %{?with_kernel_sysctl:kernel-sysctl.service}

# List of legacy file systems to be blacklisted by default
%global fs_blacklist adfs affs bfs befs cramfs efs erofs exofs f2fs freevxfs hfs hfsplus hpfs jffs2 jfs kafs minix nilfs2 ntfs ntfs3 omfs orangefs pstore qnx4 qnx6 reiserfs romfs sysv ufs zonefs

# List of all files installed under modprobe.d
# Note: this list contains files installed by previous versions, like 00-system-937216.conf!
%global modprobe_conf_files 00-system 00-system-937216 10-unsupported-modules 50-blacklist 60-blacklist_fs-* 99-local
%global modprobe_conf_rpmsave %(echo "%{modprobe_conf_files}" | sed 's,\\([^ ]*\\),%{_sysconfdir}/modprobe.d/\\1.conf.rpmsave,g')

Name:           suse-module-tools
Version:        16.0.45
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
Provides:       udev-extra-rules = 0.3.0
Obsoletes:      udev-extra-rules < 0.3.0
Provides:       system-tuning-common-SUSE = 0.3.0
Obsoletes:      system-tuning-common-SUSE < 0.3.0
# Use weak dependencies for dracut and kmod in order to
# keep Ring0 lean. In normal deployments, these packages
# will be available anyway.
Recommends:     dracut
Recommends:     kmod
# This release requires the dracut module 90nvdimm
Conflicts:      dracut < 49.1
# TW: conflict with pre-usrmerge
Conflicts:      filesystem < 16

%description
This package contains helper scripts for KMP installation and
uninstallation, as well as default configuration files for depmod and
modprobe.


%package scriptlets
Summary:        Kernel rpm scriptlets
Provides:       suse-kernel-rpm-scriptlets = 0
Requires:       suse-module-tools = %{version}
Provides:       suse-module-tools:/usr/lib/module-init-tools/kernel-scriptlets

%description scriptlets
Scripts called by the SUSE kernel packages on installation

%prep
%setup -q

%build
sed -i 's/@FS_BLACKLIST@.*/%{fs_blacklist}/' README.md

%install
install -d -m 755 "%{buildroot}%{modprobe_dir}"
install -d -m 755 "%{buildroot}%{_sysconfdir}/modprobe.d"

install -pm644 -t "%{buildroot}%{modprobe_dir}" modprobe.conf/common/*.conf
if [ -d modprobe.conf/%{_arch} ]; then
    install -pm644 -t "%{buildroot}%{modprobe_dir}" modprobe.conf/%{_arch}/*.conf
fi
%ifarch i386
install -pm644 -t "%{buildroot}%{modprobe_dir}" modprobe.conf/x86_64/*.conf
%endif
%ifarch ppc64le
install -pm644 -t "%{buildroot}%{modprobe_dir}" modprobe.conf/ppc64/*.conf
%endif

install -d -m 755 "%{buildroot}/%{depmod_dir}"
install -d -m 755 "%{buildroot}%{_sysconfdir}/depmod.d"
install -pm 644 "depmod-00-system.conf" "%{buildroot}%{depmod_dir}/00-system.conf"

# "/usr/lib/module-init-tools" name hardcoded in other packages
install -d -m 755 "%{buildroot}/usr/lib/module-init-tools"
install -pm 755 -t "%{buildroot}/usr/lib/module-init-tools/" \
	weak-modules2 driver-check.sh unblacklist lsinitrd-quick get_dracut_drivers
install -pm 755 "regenerate-initrd-posttrans" "%{buildroot}/usr/lib/module-init-tools/"
install -d -m 755 "%{buildroot}/usr/lib/module-init-tools/kernel-scriptlets"
install -pm 755 "kernel-scriptlets/cert-script" "%{buildroot}/usr/lib/module-init-tools/kernel-scriptlets"
install -pm 755 "kernel-scriptlets/inkmp-script" "%{buildroot}/usr/lib/module-init-tools/kernel-scriptlets"
install -pm 755 "kernel-scriptlets/kmp-script" "%{buildroot}/usr/lib/module-init-tools/kernel-scriptlets"
install -pm 755 "kernel-scriptlets/rpm-script" "%{buildroot}/usr/lib/module-init-tools/kernel-scriptlets"
for i in "pre" "preun" "post" "posttrans" "postun" ; do
    ln -s cert-script %{buildroot}/usr/lib/module-init-tools/kernel-scriptlets/cert-$i
    ln -s inkmp-script %{buildroot}/usr/lib/module-init-tools/kernel-scriptlets/inkmp-$i
    ln -s kmp-script %{buildroot}/usr/lib/module-init-tools/kernel-scriptlets/kmp-$i
    ln -s rpm-script %{buildroot}/usr/lib/module-init-tools/kernel-scriptlets/rpm-$i
done

install -d -m 755 %{buildroot}%{dracutlibdir}/dracut.conf.d
install -pm 644 10-unblacklist.conf %{buildroot}%{dracutlibdir}/dracut.conf.d
install -d -m 755 "%{buildroot}%{_prefix}/bin"

# systemd service(s) to load kernel-specific sysctl settings
install -d -m 755 "%{buildroot}%{_unitdir}/systemd-sysctl.service.d"
echo '[Unit]' >"%{buildroot}%{sysctl_dropin}"
%if %{with kernel_sysctl}
install -pm 644 kernel-sysctl.service "%{buildroot}%{_unitdir}"
echo 'Wants=kernel-sysctl.service' >>"%{buildroot}%{sysctl_dropin}"
%endif
%if %{with boot_sysctl}
install -pm 644 boot-sysctl.service "%{buildroot}%{_unitdir}"
echo 'Wants=boot-sysctl.service' >>"%{buildroot}%{sysctl_dropin}"
%endif

install -d -m 755 "%{buildroot}%{_modulesloaddir}"
for _x in modules-load.d/*.conf; do
    [ -e "$_x" ] || continue
    install -pm 644 -t "%{buildroot}%{_modulesloaddir}" "$_x"
done

%ifarch ppc64 ppc64le
install -d -m 755 %{buildroot}/usr/lib/systemd/system-generators
install -pm 755 udev-trigger-generator %{buildroot}/usr/lib/systemd/system-generators
%endif

# udev rules (formerly system-tuning-common-SUSE, udev-extra-rules)
install -d -m 755 %{buildroot}%{_udevrulesdir}
install -pm 644 udevrules/*.rules %{buildroot}%{_udevrulesdir}

mkdir -p %{buildroot}%{_defaultlicensedir}

for mod in %{fs_blacklist}; do
    echo "\
# DO NOT EDIT THIS FILE!
#
# The $mod file system is blacklisted by default because it isn't actively
# supported by SUSE.
blacklist $mod
# The filesystem can be un-blacklisted by running \"modprobe $mod\".
# See README.md in the %{name} package for details.
install $mod /usr/lib/module-init-tools/unblacklist $mod; /sbin/modprobe --ignore-install $mod
" \
	>%{buildroot}%{modprobe_dir}/60-blacklist_fs-"$mod".conf
done

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
%udev_rules_update
%service_add_post %{systemd_units}
exit 0

%preun
%service_del_preun %{systemd_units}
exit 0

%postun
%udev_rules_update
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
%dir /usr/lib/module-init-tools
/usr/lib/module-init-tools/driver-check.sh
/usr/lib/module-init-tools/lsinitrd-quick
/usr/lib/module-init-tools/unblacklist
/usr/lib/module-init-tools/weak-modules2
/usr/lib/module-init-tools/get_dracut_drivers
%{_unitdir}/*.service
%{_unitdir}/systemd-sysctl.service.d
%{_modulesloaddir}
%{_udevrulesdir}
%dir %{dracutlibdir}
%{dracutlibdir}/dracut.conf.d
%ifarch ppc64 ppc64le
/usr/lib/systemd/system-generators
%endif
#
%files scriptlets
/usr/lib/module-init-tools/kernel-scriptlets
/usr/lib/module-init-tools/regenerate-initrd-posttrans

%changelog
