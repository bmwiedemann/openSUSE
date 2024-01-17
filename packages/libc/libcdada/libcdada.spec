#
# spec file for package libcdada
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2021, Martin Hauke <mardnh@gmx.de>
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


%define sover 0
Name:           libcdada
Version:        0.4.0
Release:        0
Summary:        Basic data structures in C (libstdc++ wrapper)
License:        BSD-2-Clause
Group:          Development/Languages/C and C++
URL:            https://msune.github.io/libcdada/
#Git-Clone:     https://github.com/msune/libcdada.git
Source:         https://github.com/msune/libcdada/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  python3
BuildRequires:  valgrind

%description
Library that offers basic data structures (list, set, map, ..)
in a C API for user-space applications.

Key features:
 - No "magic" MACROs, and no need to modify data structures
   (except, perhaps, for __attribute__((packed)))
 - Uses C++ standard library as the backend for most data structures

%package -n libcdada%{sover}
Summary:        Basic data structures in C (libstdc++ wrapper)
Group:          System/Libraries

%description -n libcdada%{sover}
Library that offers basic data structures (list, set, map, ..)
in a C API for user-space applications.

Key features:
 - No "magic" MACROs, and no need to modify your data structures
   (except, perhaps, for __attribute__((packed)))
 - Uses C++ standard library as the backend for most data structures

%package devel
Summary:        Development files for libcdada
Group:          Development/Libraries/C and C++
Requires:       libcdada%{sover} = %{version}
Requires:       python3

%description devel
This package contains libraries and header files for developing
applications that use libcdada.

%prep
%autosetup
sed -i 's|#!%{_bindir}/env python3|#!%{_bindir}/python3|g' tools/cdada-gen

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install
rm -fv %{buildroot}/%{_libdir}/*.{a,la}

%check
%make_build check

%post   -n libcdada%{sover} -p /sbin/ldconfig
%postun -n libcdada%{sover} -p /sbin/ldconfig

%files -n libcdada%{sover}
%license LICENSE
%doc AUTHORS CHANGELOG.md README.md
%doc doc/
%{_libdir}/libcdada.so.%{sover}*

%files devel
%{_bindir}/cdada-gen
%{_includedir}/cdada.h
%{_includedir}/cdada
%{_libdir}/libcdada.so

%changelog
