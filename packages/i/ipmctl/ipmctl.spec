#
# spec file for package ipmctl
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


%define abi     5
#define vgit    .1547861714.b7a59da
%define vgit    %{nil}

Name:           ipmctl
Version:        03.00.00.0468
Release:        0
Summary:        Utility for managing Intel Optane persistent memory modules
License:        BSD-3-Clause
Group:          System/Management
URL:            https://github.com/intel/ipmctl
%if "%{vgit}" == ""
Source:         https://github.com/intel/ipmctl/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
Source:         %{name}-%{version}%{vgit}.tar.gz
%endif
Source1:        ChangeLog.xz
Source2:        %{name}-rpmlintrc
Patch1:         ipmctl-static-EDK2.patch.xz

Recommends:     logrotate
%if %{defined pythons}
BuildRequires:  %{pythons}
%else
BuildRequires:  python
%endif
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libndctl) >= 58.2
BuildRequires:  pkgconfig(systemd)
# required for documentation
BuildRequires:  rubygem(asciidoctor)

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
Utility for managing Intel Optane persistent memory modules (PMem module)
Supports functionality to:
- Discover PMem modules on the platform.
- Provision the platform memory configuration.
- View and update the firmware on PMem modules.
- Configure data-at-rest security on PMem modules.
- Monitor PMem module health.
- Track performance of PMem modules.
- Debug and troubleshoot PMem modules.

%package devel
Summary:        Development packages for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Obsoletes:      ixpdimm-devel < 01.00.00.3000
Obsoletes:      ixpdimm_sw-devel < 01.00.00.3000

%description devel
API for development of Intel Optane persistent memory management utilities.

%prep
%setup -q -n %{name}-%{version}%{vgit}
%patch1 -p1

perl -pi.00 -e '
  s[(CMAKE_INSTALL_)DATAROOT(DIR\})/ipmctl][${1}SYSCONF${2}];
  s[(INI_INSTALL_FILEPATH "\$\{CMAKE_INSTALL_)DATAROOT(DIR\}")][${1}SYSCONF${2}];
  s[(-DINI_INSTALL_FILEPATH="\$\{INI_INSTALL_FILEPATH\})/ipmctl][${1}];
' CMakeLists.txt
diff -u CMakeLists.txt{.00,} || sleep 4

! grep -lri 'INTEL CONFIDENTIAL' || exit 1

%build
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
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_sbindir}
rm -f %{buildroot}%{_datadir}/doc/ipmctl/ipmctl_default.conf
rm -f %{buildroot}%{_datadir}/doc/ipmctl/LICENSE
rm -f %{buildroot}%{_datadir}/doc/ipmctl/thirdpartynotice.txt
rm -f %{buildroot}%{_datadir}/doc/ipmctl/edk2_License.txt
install -m 444 -p "%{SOURCE1}" .

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md
%doc opensource
%doc Documentation/ipmctl/*
%doc ChangeLog.xz
%{_bindir}/%{name}
%{_mandir}/man1/*

#files data
%doc output/release/%{name}_default.conf
%config %{_sysconfdir}/%{name}.conf
%config %{_sysconfdir}/logrotate.d/%{name}
%dir %{_localstatedir}/log/%{name}

#files -n lib%%{name}%%{abi}
%{_libdir}/lib%{name}.so.%{abi}*

%files devel
%defattr(-,root,root)
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc
%{_includedir}/nvm_types.h
%{_includedir}/nvm_management.h
%{_includedir}/export_api.h
%{_includedir}/NvmSharedDefs.h

%changelog
