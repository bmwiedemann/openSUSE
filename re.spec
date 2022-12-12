#
# spec file for package re
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


%global sover   12
%global libname lib%{name}%{sover}
Name:           re
Version:        2.10.0
Release:        0
Summary:        Library for real-time communications with async I/O support
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/baresip/re
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig

%description
Libre is a library for real-time communications
with async IO support and a complete SIP stack with support for protocols
such as SDP, RTP/RTCP, STUN/TURN/ICE, BFCP, HTTP and DNS Client.

%package -n %{libname}
Summary:        Library for real-time communications with async IO support
Group:          System/Libraries

%description -n %{libname}
Libre is a library for real-time communications
with async I/O support and a complete SIP stack with support for protocols
such as SDP, RTP/RTCP, STUN/TURN/ICE, BFCP, HTTP and DNS Client.

%package devel
Summary:        Development files for libre
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}-%{release}

%description devel
Libre is a portable and generic library for real-time communications
with async I/O support and a complete SIP stack with support for protocols
such as SDP, RTP/RTCP, STUN/TURN/ICE, BFCP, HTTP and DNS Client.

This subpackage contains libraries and header files for developing
applications that want to make use of libre.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install
rm -v %{buildroot}/%{_libdir}/libre.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc CHANGELOG.md README.md
%{_libdir}/libre.so.%{sover}*

%files devel
%license LICENSE
%{_includedir}/re
#%%{_datadir}/re
%{_libdir}/libre.so
%{_libdir}/pkgconfig/libre.pc
%dir %{_libdir}/cmake/re
%{_libdir}/cmake/re/re-config.cmake

%changelog
