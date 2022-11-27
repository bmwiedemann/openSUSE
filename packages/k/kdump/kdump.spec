#
# spec file for package kdump
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


%bcond_with calibrate

%if 0%{?is_opensuse}
%if 0%{suse_version} > 1500
%define distro_suffix tumbleweed.%{_arch}
%else
%define distro_suffix leap%{sle_version}.%{_arch}
%endif
%else
%define distro_suffix sle%{sle_version}.%{_arch}
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
%define qemu qemu-%{_target_cpu}
%endif
%endif
%endif
%endif

%define dracutlibdir %{_prefix}/lib/dracut

Name:           kdump
Version:        1.0.2+git26.gc6fab38
Release:        0
Summary:        Script for kdump
License:        GPL-2.0-or-later
Group:          System/Kernel
URL:            https://github.com/openSUSE/kdump
Source:         %{name}-%{version}.tar.xz
Source1:        %{name}-calibrate.tar.bz2
Source2:        %{name}-rpmlintrc
BuildRequires:  asciidoc
BuildRequires:  cmake >= 3.7
BuildRequires:  gcc-c++
BuildRequires:  libblkid-devel
BuildRequires:  libcurl-devel
BuildRequires:  libelf-devel
BuildRequires:  libesmtp-devel
BuildRequires:  libmount-devel
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  systemd-sysvinit
BuildRequires:  util-linux-systemd
BuildRequires:  wicked
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
#!BuildIgnore:  fop
%if %{with calibrate}
BuildRequires:  %qemu
BuildRequires:  dhcp-client
BuildRequires:  dracut >= 047
BuildRequires:  iputils
BuildRequires:  kernel-default
BuildRequires:  makedumpfile
BuildRequires:  procps
BuildRequires:  python3
BuildRequires:  qemu-ipxe
BuildRequires:  qemu-vgabios
BuildRequires:  systemd-sysvinit
BuildRequires:  util-linux-systemd
BuildRequires:  wicked
%endif
Requires:       /usr/bin/sed
Requires:       curl
Requires:       dracut >= 047
Requires:       kexec-tools
Requires:       makedumpfile
Requires:       openssh
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
Recommends:     nfs-client
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
%setup -q -D -T -a 1

%build
export CXXFLAGS="%{optflags} -std=c++11"
%cmake \
%if %{with calibrate}
	-DCALIBRATE=ON
%else
	-DCALIBRATE=OFF
%endif

%cmake_build

%check
%ctest

%install
%cmake_install
# empty directory
mkdir -p %{buildroot}%{_localstatedir}/crash

# Install pre-built calibrate.conf
%if !%{with calibrate}
cp calibrate/calibrate.conf.%{distro_suffix} %{buildroot}/usr/lib/kdump/calibrate.conf
%endif

# symlink for init script
rm %{buildroot}%{_initddir}/boot.kdump
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rckdump

%pre
%service_add_pre kdump.service
%service_add_pre kdump-early.service

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
# ensure newly added kdump-early.service is-enabled matches prior state
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

%preun
%ifarch ppc64 ppc64le
servicelog_notify --remove --command=/usr/lib/kdump/kdump-migrate-action.sh
%endif
echo "Stopping kdump ..."
%service_del_preun kdump.service
%service_del_preun kdump-early.service

%postun
# force regeneration of kdumprd
touch %{_sysconfdir}/sysconfig/kdump
# delete symbolic link
rm %{_localstatedir}/log/dump >/dev/null 2>&1 || true
%service_del_postun kdump.service
%service_del_postun kdump-early.service

%files
%defattr(-,root,root)
%license COPYING
%doc ChangeLog README NEWS
%{_sbindir}/kdumptool
%{_sbindir}/mkdumprd
%{_mandir}/man5/kdump.5%{?ext_man}
%{_mandir}/man7/kdump.7%{?ext_man}
%{_mandir}/man8/kdumptool.8%{?ext_man}
%{_mandir}/man8/mkdumprd.8%{?ext_man}
%{_fillupdir}/sysconfig.kdump
%dir %{dracutlibdir}
%dir %{dracutlibdir}/modules.d
%{dracutlibdir}/modules.d/*
%dir /usr/lib/kdump
/usr/lib/kdump/*
%{_unitdir}/kdump.service
%{_unitdir}/kdump-early.service
%{_sbindir}/rckdump

%changelog
