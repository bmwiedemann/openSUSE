#
# spec file for package kdump
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


%bcond_with calibrate

%if 0%{?is_opensuse}
%if 0%{suse_version} > 1500
%define distro_prefix tumbleweed.%{_arch}
%else
%define distro_prefix leap%{sle_version}.%{_arch}
%endif
%else
%if 0%{suse_version} >= 1600
%define distro_prefix alp%{suse_version}.%{_arch}
%else
%define distro_prefix sle%{sle_version}.%{_arch}
%endif
%endif

%ifarch aarch64
%define qemu qemu-arm qemu-uefi-aarch64
%else
%ifarch %arm
%define qemu qemu-arm
%else
%ifarch %ix86 x86_64
%define qemu qemu-x86
%else
%ifarch %power64
%define qemu qemu-ppc
%else
%ifarch riscv64
%define qemu qemu-extra
%else
%define qemu qemu-%{_target_cpu}
%endif
%endif
%endif
%endif
%endif

%define dracutlibdir %{_prefix}/lib/dracut

Name:           kdump
Version:        2.0.7
Release:        0
Summary:        Kernel crash dump scripts and utilities
License:        GPL-2.0-or-later
Group:          System/Kernel
URL:            https://github.com/openSUSE/kdump
Source:         %{name}-%{version}.tar.xz
Source1:        calibrate.conf.all
BuildRequires:  asciidoc
BuildRequires:  cmake >= 3.7
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  util-linux-systemd
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
#!BuildIgnore:  fop
%if %{with calibrate}
BuildRequires:  %qemu
BuildRequires:  dhcp-client
BuildRequires:  dracut >= 047
BuildRequires:  iputils
BuildRequires:  kernel-default
BuildRequires:  lftp
BuildRequires:  makedumpfile
BuildRequires:  openssh-clients
BuildRequires:  pciutils
BuildRequires:  procps
BuildRequires:  python3
%ifnarch s390x
BuildRequires:  qemu-ipxe
BuildRequires:  qemu-vgabios
%endif
%endif
Requires:       /usr/bin/sed
Requires:       dracut >= 047
Requires:       kexec-tools
Requires:       makedumpfile
%ifarch ppc64 ppc64le
Requires:       servicelog
BuildRequires:  servicelog
%endif

# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %fillup_prereq
PreReq:         /usr/bin/mkdir
PreReq:         /usr/bin/rm
PreReq:         /usr/bin/touch
Recommends:     cifs-utils
Recommends:     lftp
Recommends:     nfs-client
Recommends:     openssh-clients
Suggests:       mailx
# update should detect the split-off from kexec-tools
Provides:       kexec-tools:%{_initddir}/kdump
ExcludeArch:    s390 ppc %arm32
%if 0%{?sle_version}
ExcludeArch:    %ix86
%endif
%{?systemd_ordering}

%description
kdump is a package that includes several scripts for kdump, including
the kdump service and configuration files

The kernel package and this package are all that are required for a
crash dump to occur. However, if you wish to debug the crash dump
yourself you will need several debugging packages installed for each
kernel flavor and release you wish to debug.

For example, if you are debugging kernel-default, you will need:
- kernel-default-debuginfo
- kernel-default-devel
- kernel-default-devel-debuginfo

These packages are not needed to create the dump and can be installed
after a crash dump has occured.

%prep
%setup -q
cp %{SOURCE1} calibrate.conf.all

%build
export CXXFLAGS="%{optflags} -std=c++11"
%cmake \
%if %{with calibrate}
	-DCALIBRATE=ON
%else
	-DCALIBRATE=OFF
%endif

# run make directly instead of cmake_build, which would run make in parallel
# and try to group output, preventing any debugging output from qemu if it
# fails to exit
make VERBOSE=1

%check
%ctest

%install
%cmake_install
# empty directory
mkdir -p %{buildroot}%{_localstatedir}/crash
mkdir -p %{buildroot}%{_localstatedir}/lib/kdump

%if !%{with calibrate}
# get distro_prefix-prefixed lines from calibrate.conf.all
grep "^%distro_prefix:" calibrate.conf.all | cut -f 2- -d: > %{buildroot}/usr/lib/kdump/calibrate.conf
if ! test -s %{buildroot}/usr/lib/kdump/calibrate.conf; then
echo "no calibration data for %distro_prefix in calibrate.conf.all, see packaging/suse/calibrate/README"
false
fi
%else
# save the distro_prefix
echo "GENERATED_ON=%{distro_prefix}" >> %{buildroot}/usr/lib/kdump/calibrate.conf
echo "generated calibrate.conf:"
cat  %{buildroot}/usr/lib/kdump/calibrate.conf
%endif

# symlink for init script
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rckdump

%pre
%service_add_pre kdump.service
%service_add_pre kdump-early.service
%service_add_pre kdump-notify.service
exit 0

%post
# change only permission if the file exists before /etc/sysconfig/kdump
# has been created from %%{_fillupdir}/sysconfig.kdump
change_permission=0
if [ ! -f %{_sysconfdir}/sysconfig/kdump ] ; then
    change_permission=1
fi
%{fillup_only -n kdump}
%service_add_post kdump.service
%service_add_post kdump-early.service
%service_add_post kdump-notify.service
# ensure newly added kdump-*.service is-enabled matches prior state
if [ -x %{_bindir}/systemctl ] && %{_bindir}/systemctl is-enabled kdump.service &>/dev/null ; then
	%{_bindir}/systemctl reenable kdump.service || :
fi
if [ "$change_permission" = 1 ]; then
    chmod 0600 %{_sysconfdir}/sysconfig/kdump
fi
# if /var/log/dump is empty, make it a symlink to /var/crash
if test -d %{_localstatedir}/log/dump && rmdir %{_localstatedir}/log/dump >/dev/null 2>&1 ||
        ! test -d %{_localstatedir}/log/dump ; then
    ln -snf %{_localstatedir}/crash %{_localstatedir}/log/dump
fi
%ifarch ppc64 ppc64le
servicelog_notify --remove --command=/usr/lib/kdump/kdump-migrate-action.sh
servicelog_notify --add --command=/usr/lib/kdump/kdump-migrate-action.sh --match='refcode="#MIGRATE" and serviceable=0' --type=EVENT --method=pairs_stdin
%endif
exit 0

%preun
%ifarch ppc64 ppc64le
if [ $1 -eq 0 ]; then
	# removal, not upgrade
	servicelog_notify --remove --command=/usr/lib/kdump/kdump-migrate-action.sh
fi
%endif
echo "Stopping kdump ..."
%service_del_preun kdump.service
%service_del_preun kdump-early.service
%service_del_preun kdump-notify.service
exit 0

%postun
if [ $1 -gt 0 ]; then
	# upgrade
	# force regeneration of kdumprd
	touch %{_sysconfdir}/sysconfig/kdump
else
	# removal
	# delete symbolic link
	rm %{_localstatedir}/log/dump >/dev/null 2>&1 || true
fi
%service_del_postun kdump.service
%service_del_postun kdump-early.service
%service_del_postun kdump-notify.service
exit 0

%files
%defattr(-,root,root)
%license COPYING
%doc README NEWS
%{_sbindir}/kdumptool
%{_sbindir}/mkdumprd
%{_mandir}/man5/kdump.5%{?ext_man}
%{_mandir}/man7/kdump.7%{?ext_man}
%{_mandir}/man8/mkdumprd.8%{?ext_man}
%{_fillupdir}/sysconfig.kdump
%dir %{dracutlibdir}
%dir %{dracutlibdir}/modules.d
%{dracutlibdir}/modules.d/*
%dir /usr/lib/kdump
/usr/lib/kdump/*
%{_unitdir}/kdump.service
%{_unitdir}/kdump-early.service
%{_unitdir}/kdump-notify.service
%{_sbindir}/rckdump
%dir /var/lib/kdump

%changelog
