#
# spec file for package open-lldp
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


%define libname liblldp_clif1
Name:           open-lldp
Summary:        Link Layer Discovery Protocol (LLDP) Agent
License:        GPL-2.0-only
Group:          System/Daemons
Version:        1.0.1+69.e8f522565f5a
Release:        0
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libconfig-devel
BuildRequires:  libnl3-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
URL:            https://github.com/intel/openlldp
Source:         %{name}-v%{version}.tar.xz
Patch0:         disable-werror.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       dcbd = %{version}
Obsoletes:      dcbd < %{version}
Provides:       lldpad = %{version}
Obsoletes:      lldpad < %{version}
BuildRequires:  pkgconfig(systemd)
%systemd_requires

%description
This package contains the Link Layer Discovery Protocol (LLDP) Agent
with Data Center Bridging (DCB) for Intel(R) Network Connections
'lldpad' plus the configuration tools 'dcbtool' and 'lldptool'.

%package -n %{libname}
Summary:        Link Layer Discovery Protocol (LLDP) libraries
Group:          System/Libraries

%description -n %{libname}
This package contains the Link Layer Discovery Protocol (LLDP) libraries

%package devel
Summary:        Link Layer Discovery Protocol (LLDP) Agent
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       %{name} = %{version}
Provides:       dcbd-devel = %{version}
Obsoletes:      dcbd-devel < %{version}
Provides:       lldpad-devel = %{version}
Obsoletes:      lldpad-devel < %{version}

%description devel
This package contains the Link Layer Discovery Protocol (LLDP) Agent
with Data Center Bridging (DCB) for Intel(R) Network Connections
'lldpad' plus the configuration tools 'dcbtool' and 'lldptool'.

%prep
%setup -n %{name}-v%{version}
%patch0 -p1

%build
%global optflags %{optflags} -fcommon
autoreconf -vi
%configure \
	--disable-static
%make_build

%check
%make_build check

%install
mkdir -p %{buildroot}/var/lib/lldpad
%makeinstall
# remove la archives
rm -rf %{buildroot}/%{_libdir}/*.la
ln -s service %{buildroot}%{_sbindir}/rclldpad

%post
%{fillup_only -n lldpad}
%service_add_post lldpad.service lldpad.socket

%pre
%service_add_pre lldpad.service lldpad.socket

%preun
%service_del_preun lldpad.service lldpad.socket

%postun
%service_del_postun lldpad.service lldpad.socket

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%doc README ChangeLog
%dir /var/lib/lldpad
%{_unitdir}/*
%{_sbindir}/*
%{_mandir}/man3/*
%{_mandir}/man8/*
%{_datadir}/bash-completion/completions/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
