#
# spec file for package leveldb
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


Name:           leveldb
Version:        1.23
Release:        0
Summary:        A key/value-store
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/google/leveldb
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-FEATURE-OPENSUSE detect-system-gtest.patch -- https://github.com/google/leveldb/pull/912
Patch0:         detect-system-gtest.patch
# PATCH-FIX-OPENSUSE enable-rtti.patch -- Enable rtti support again, needed for ceph
Patch1:         enable-rtti.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  snappy-devel
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(benchmark)
BuildRequires:  pkgconfig(sqlite3)
%{?suse_build_hwcaps_libs}

%description
leveldb implements a system for maintaining a persistent key/value store.

%define lib_name libleveldb1

%package -n %{lib_name}
Summary:        Shared library from leveldb
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n %{lib_name}
leveldb implements a system for maintaining a persistent key/value store.

This package holds the shared library of leveldb.

%package devel
Summary:        Development files for leveldb
Group:          Development/Libraries/C and C++
Requires:       %{lib_name} = %{version}

%description devel
leveldb implements a system for maintaining a persistent key/value store.

This package holds the development files for leveldb.

%package devel-static
Summary:        Development files for statically link leveldb
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description devel-static
leveldb implements a system for maintaining a persistent key/value store.

This package holds the development files for statically linking leveldb.

%prep
%autosetup -p1

%build
# unfortunately a two-pass build is needed for shared and static libs
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build
cd ..
%define __builddir build_static
%cmake -DBUILD_SHARED_LIBS=OFF
%cmake_build

%install
# Install shared libraries
%define __builddir build
%cmake_install
# collect static libs built in the second pass
cp -a build_static/libleveldb.a %{buildroot}%{_libdir}
# cmake_install omits db_bench
install -d -m 0755 %{buildroot}%{_bindir}
cp -a build_static/db_bench %{buildroot}%{_bindir}

%check
%define __builddir build_static
%ctest

%post   -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files
%{_bindir}/db_bench

%files -n %{lib_name}
%license LICENSE
%{_libdir}/libleveldb.so.*

%files devel
%doc AUTHORS NEWS README.md TODO doc/*
%{_includedir}/leveldb/
%{_libdir}/libleveldb.so
%{_libdir}/cmake/leveldb

%files devel-static
%{_libdir}/libleveldb.a

%changelog
