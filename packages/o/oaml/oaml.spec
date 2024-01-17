#
# spec file for package oaml
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


%define lname lib%{name}1
Name:           oaml
Version:        1.3.4
Release:        0
Summary:        Open Adaptive Music Library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/marcelofg55/oaml/
Source:         https://github.com/marcelofg55/oaml/archive/v%{version}/oaml-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Link-to-pthread-unconditionnally.patch
# PATCH-FIX-OPENSUSE
Patch1:         0001-Don-t-hardcode-lib.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)

%description
OAML is a library for implementing adaptive music in games.

%package devel
Summary:        Development files for OAML, the Open Adaptive Music library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
OAML is a library for implementing adaptive music in games.
This package contains the development files for oaml.

%package -n %{lname}
Summary:        Open Adaptive Music library
Group:          System/Libraries

%description -n %{lname}
OAML is a library for implementing adaptive music in games.
This package contains the shared library.

%prep
%autosetup -p1

%build
%cmake -DENABLE_STATIC=OFF
%cmake_build

%install
%cmake_install

%post -n %{lname}   -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSE.md
%{_libdir}/lib%{name}.so.*

%files devel
%doc README.md
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/oaml
%{_includedir}/oaml.h
%{_libdir}/cmake/oaml/oaml.cmake
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/oaml.pc

%changelog
