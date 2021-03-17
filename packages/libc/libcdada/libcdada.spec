#
# spec file for package libcdada
#
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
Version:        0.3.4
Release:        0
Summary:        Basic data structures in C (libstdc++ wrapper)
License:        BSD-2-Clause
Group:          Development/Languages/C and C++
URL:            https://msune.github.io/libcdada/
#Git-Clone:     https://github.com/msune/libcdada.git
Source:         https://github.com/msune/libcdada/archive/v%{version}.tar.gz#/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  valgrind
BuildRequires:  python3

%description
Small library that offers basic data structures (list, set, map, ..)
in a pure C API for user-space applications.

Key features:
 - Easy to use, portable
 - No "magic" MACROs, and no need to modify your data structures
   (except, perhaps, for __attribute__((packed)))
 - Uses C++ standard library as the backend for most data structures
 - Reasonable performance

%package -n libcdada%{sover}
Summary:        Basic data structures in C (libstdc++ wrapper)
Group:          System/Libraries

%description -n libcdada%{sover}
Small library that offers basic data structures (list, set, map, ..)
in a pure C API for user-space applications.

Key features:
 - Easy to use, portable
 - No "magic" MACROs, and no need to modify your data structures
   (except, perhaps, for __attribute__((packed)))
 - Uses C++ standard library as the backend for most data structures
 - Reasonable performance

%package devel
Summary:        Development files for libcdada
Group:          Development/Libraries/C and C++
Requires:       libcdada%{sover} = %{version}
Requires:       python3

%description devel
This package contains libraries and header files for developing
applications that use libcdada.

%prep
%setup -q
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
