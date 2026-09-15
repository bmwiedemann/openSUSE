#
# spec file for package librist
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover   4
%define libname %{name}%{sover}
Name:           librist
Version:        0.2.20
Release:        0
Summary:        Reliable Internet Stream Transport protocol
License:        BSD-2-Clause
URL:            https://code.videolan.org/rist/librist
Source0:        https://code.videolan.org/rist/librist/-/archive/v%{version}/librist-v%{version}.tar.gz
Source99:       baselibs.conf
#PATCH-FIX-OPENSUSE Add missing headers for EAP (bsc#1257934)
Patch1:         librist-EAP-headers.patch
#PATCH-FIX-OPENSUSE Exclude multicast tests as UDP are silently dropped by the kernel in isolated build envs (bsc#1257934)
Patch2:         librist-skip-multicast-tests-in-buildenvs.patch
Group:          Development/Libraries/C and C++
BuildRequires:  gnutls-devel
BuildRequires:  libnettle-devel
BuildRequires:  meson >= 0.47
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcjson)
BuildRequires:  pkgconfig(libmicrohttpd)

%description
A library that can be used to speak the RIST protocol (as defined by Video
Services Forum (VSF) Technical Recommendations TR-06-1 and TR-06-2).

%package -n %{libname}
Summary:        Reliable Internet Stream Transport protocol
Group:          System/Libraries

%description -n %{libname}
A library that can be used to speak the RIST protocol (as defined by Video
Services Forum (VSF) Technical Recommendations TR-06-1 and TR-06-2).

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n rist-tools
Summary:        User tools for %{name}
Group:          Productivity/Multimedia/Video/Editors and Convertors

%description -n rist-tools
This package contains the user tools for the RIST protocol library.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%meson -Duse_gnutls=true -Duse_nettle=true -Duse_mbedtls=false
%meson_build

%install
%meson_install
chmod -x %{buildroot}%{_includedir}/%{name}/*.h
chmod -x docs/*

%check
%meson_test

%ldconfig_scriptlets -n %{libname}

%files -n rist-tools
%license COPYING
%doc CONTRIBUTING.md
%doc README.md
%doc docs
%{_bindir}/rist*
%{_bindir}/udp2udp

%files -n %{libname}
%license COPYING
%{_libdir}/*.so.*

%files devel
%license COPYING
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
