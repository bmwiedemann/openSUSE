#
# spec file for package leveldb
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


Name:           leveldb
Version:        1.22
Release:        0
Summary:        A key/value-store
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/google/leveldb
Source0:        https://github.com/google/leveldb/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  snappy-devel

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
%setup -q

%build
# unfortunately a two-pass build is needed for shared and static libs
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build
cd ..
%cmake -DBUILD_SHARED_LIBS=OFF
%cmake_build

%install
%cmake_install
# collect shared libs built in the first pass
cp -a build/libleveldb.so* %{buildroot}%{_libdir}
# cmake_install omits db_bench
install -d -m 0755 %{buildroot}%{_bindir}
cp -a build/db_bench %{buildroot}%{_bindir}

%check
%ctest

%post   -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/db_bench

%files -n %{lib_name}
%defattr(-,root,root,-)
%{_libdir}/libleveldb.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS LICENSE NEWS README.md TODO doc/*
%{_includedir}/leveldb/
%{_libdir}/libleveldb.so

%files devel-static
%defattr(-,root,root,-)
%{_libdir}/libleveldb.a
%{_libdir}/cmake/

%changelog
