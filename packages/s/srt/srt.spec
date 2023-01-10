#
# spec file for package srt
#
# Copyright (c) 2023 SUSE LLC
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


%define sover 1_5

Name:           srt
Version:        1.5.1
Release:        0
Summary:        Secure Reliable Transport (SRT)
License:        MPL-2.0
Group:          Development/Libraries/C and C++
URL:            https://www.srtalliance.org
Source0:        https://github.com/Haivision/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  tcl
BuildRequires:  pkgconfig(openssl)

%description
SRT is a video transport protocol and technology stack
that optimizes streaming performance across unpredictable networks
with secure streams and firewall traversal.

%package -n libsrt%{sover}
Summary:        Secure Reliable Transport (SRT) library
Group:          System/Libraries

%description -n libsrt%{sover}
This package contains a shared system library for Secure Reliable
Transport (SRT).

%package devel
Summary:        Development files for the Secure Reliable Transport (SRT) library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libsrt%{sover} = %{version}

%description devel
This package contains all necessary include files and libraries
needed to develop applications with Secure Reliable Transport
(SRT) support.

%prep
%autosetup -p1

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_INSTALL_BINDIR=%{_bindir} \
	-DCMAKE_INSTALL_LIBDIR=%{_libdir} \
	-DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} \
	-DENABLE_CXX11=ON \
	-DENABLE_SHARED=ON \
        -DENABLE_MONOTONIC_CLOCK=ON \
	-DENABLE_STATIC=OFF \
	%{nil}
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{_prefix}

%post -n libsrt%{sover} -p /sbin/ldconfig
%postun -n libsrt%{sover} -p /sbin/ldconfig

%files
%doc CONTRIBUTING.md README.md
%{_bindir}/%{name}-ffplay
%{_bindir}/%{name}-file-transmit
%{_bindir}/%{name}-live-transmit
%{_bindir}/%{name}-tunnel

%files -n libsrt%{sover}
%license LICENSE
%{_libdir}/libsrt.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libsrt.so
%{_libdir}/pkgconfig/haisrt.pc
%{_libdir}/pkgconfig/srt.pc

%changelog
