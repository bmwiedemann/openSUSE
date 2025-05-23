#
# spec file for package re
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%global sover   32
%global libname lib%{name}%{sover}
Name:           re
Version:        3.21.1
Release:        0
Summary:        Library for real-time communications with async I/O support
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/baresip/re
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcrypto) >= 1.1.1
BuildRequires:  pkgconfig(zlib)
Obsoletes:      librem4 < %{version}

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
%autosetup -p1

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install
rm -v %{buildroot}/%{_libdir}/libre.a

%ldconfig_scriptlets -n %{libname}

%check
%ctest

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
%dir %{_libdir}/cmake/libre
%{_libdir}/cmake/libre/libre-config.cmake
%{_libdir}/cmake/libre/libre-targets-release.cmake
%{_libdir}/cmake/libre/libre-targets.cmake
%dir %{_libdir}/cmake/re
%{_libdir}/cmake/re/re-config.cmake

%changelog
