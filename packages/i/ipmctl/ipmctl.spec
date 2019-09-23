#
# spec file for package ipmctl
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define abi     3
#define vgit    .1547861714.b7a59da
%define vgit    %{nil}
%define vSafeC  3.3.v03032018+git7.59eba324
%bcond_with     precompiledSafeC

Name:           ipmctl
Version:        01.00.00.3440
Release:        0
Summary:        Utility for managing Intel Optane DC persistent memory modules
License:        BSD-3-Clause
Group:          System/Management
Url:            https://github.com/intel/ipmctl
%if "%{vgit}" == ""
Source:         https://github.com/intel/ipmctl/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
Source:         %{name}-%{version}%{vgit}.tar.gz
%endif
Source1:        ChangeLog.xz
Source2:        %{name}-rpmlintrc
Source10:       safeclib-%{vSafeC}.tar.xz
Source11:       mkSafeC
Source12:       safeclib-patches.tar
Patch1:         ipmctl-python3.patch

Recommends:     logrotate
%if %{defined pythons}
BuildRequires:  %{pythons}
%else
BuildRequires:  python
%endif
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libndctl) >= 58.2
# for SafeC
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool

# no 'Conflicts' for 'zypper patch'
Obsoletes:      lib%{name}2
# for impctl
Obsoletes:      ixpdimm-cli < 01.00.00.3000
# for (obsoleted) libipmctl2 et.al.
Obsoletes:      ipmctl-data < %{version}
Obsoletes:      ixpdimm-data < 01.00.00.3000
Obsoletes:      ixpdimm_sw < 01.00.00.3000
Obsoletes:      libixpdimm < 01.00.00.3000
Obsoletes:      libixpdimm-cim < 01.00.00.3000
Obsoletes:      libixpdimm-cli < 01.00.00.3000
Obsoletes:      libixpdimm-common < 01.00.00.3000
Obsoletes:      libixpdimm-core < 01.00.00.3000

ExclusiveArch:  x86_64

%description
Utility for managing Intel Optane DC persistent memory modules
Supports functionality to:
* Discover PMMs on the platform.
* Provision the platform memory configuration.
* View and update the firmware on PMMs.
* Configure data-at-rest security on PMMs.
* Monitor PMM health.
* Track performance of PMMs.
* Debug and troubleshoot PMMs.

%package monitor
Summary:        Daemon for monitoring the status of Intel PMM
Group:          System/Monitoring
%{?systemd_requires}
Obsoletes:      ixpdimm-monitor < 01.00.00.3000

%description monitor
A monitor daemon for monitoring the health and status of Intel Optane DC persistent memory modules

%package devel
Summary:        Development packages for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Obsoletes:      ixpdimm-devel < 01.00.00.3000
Obsoletes:      ixpdimm_sw-devel < 01.00.00.3000

%description devel
API for development of Intel Optane DC persistent memory management utilities.

%prep
%setup -q -n %{name}-%{version}%{vgit} -a 10
%patch1 -p1

! grep -lri 'INTEL CONFIDENTIAL' || exit 1

%if %{with precompiledSafeC}
  tar xfJ ../../SOURCES/safeclib-prebuild.tar.xz || sleep 5
%endif

%build
/bin/bash -ex "%{SOURCE11}" "%{SOURCE12}" "%{?_smp_mflags}"
export PKG_CONFIG_PATH=$PWD/contrib/lib/pkgconfig
%cmake -DBUILDNUM=%{version} -DCMAKE_INSTALL_PREFIX=/ \
    -DLINUX_PRODUCT_NAME=%{name} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} \
    -DCMAKE_INSTALL_BINDIR=%{_bindir} \
    -DCMAKE_INSTALL_DATAROOTDIR=%{_datadir} \
    -DCMAKE_INSTALL_MANDIR=%{_mandir} \
    -DCMAKE_INSTALL_LOCALSTATEDIR=%{_localstatedir} \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
    -DINSTALL_UNITDIR=%{_unitdir} \
    -DRELEASE=ON \
    -DRPM_BUILD=ON
%make_jobs

%install
%cmake_install
mkdir -p %{buildroot}%{_sbindir}
ln -sf service %{buildroot}%{_sbindir}/rc%{name}-monitor
rm -f %{buildroot}%{_datadir}/doc/ipmctl/ipmctl_default.conf
rm -f %{buildroot}%{_libdir}/*.so.%{abi}
install -m 444 -p "%{SOURCE1}" .

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%pre monitor
%service_add_pre ipmctl-monitor.service

%post monitor
%service_add_post ipmctl-monitor.service

%preun monitor
%service_del_preun ipmctl-monitor.service

%postun monitor
%service_del_postun ipmctl-monitor.service

%files
%defattr(-,root,root)
%license LICENSE contrib/COPYING.*
%doc README.md CONTRIBUTING.md Documentation/ipmctl/ipmctl.txt
%doc ChangeLog.xz
%{_bindir}/%{name}

#files data
%doc output/release/%{name}_default.conf
%config %{_sysconfdir}/%{name}.conf
%config %{_sysconfdir}/logrotate.d/%{name}
%dir %{_localstatedir}/log/%{name}
#files -n lib%%{name}%%{abi}
%{_libdir}/lib%{name}.so.%{abi}.*

%files monitor
%defattr(-,root,root)
%license LICENSE
%{_bindir}/%{name}-monitor
%{_sbindir}/rc%{name}-monitor
%{_unitdir}/%{name}-monitor.service

%files devel
%defattr(-,root,root)
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc
%{_includedir}/nvm_types.h
%{_includedir}/nvm_management.h
%{_includedir}/export_api.h
%{_includedir}/NvmSharedDefs.h

%changelog
