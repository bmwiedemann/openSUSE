#
# spec file for package SQLiteCpp
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define shlib libsqlitecpp0
Name:           SQLiteCpp
Version:        3.3.3
Release:        0
Summary:        A C++ SQLite3 wrapper
License:        MIT
URL:            https://srombauts.github.io/SQLiteCpp
Source:         https://github.com/SRombauts/SQLiteCpp/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-required-C-version-for-CMake-builds.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-Generate-pkgconfig-file-also-from-CMake-build.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  gtest
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sqlite3)

%description
SQLiteC++ (SQLiteCpp) is a C++ SQLite3 wrapper. It offers
an encapsulation around the native C APIs of SQLite, with a few intuitive and
well documented C++ classes.

%package -n %{shlib}
Summary:        C++ wrapper for SQLite3

%description -n %{shlib}
This package provides the shared library for SQLiteCpp.

%package devel
Summary:        Headers and sources for SQLiteCpp, a C++ SQLite wrapper
Requires:       %{shlib} = %{version}
Requires:       pkgconfig(sqlite3)

%description devel
This package provides the headers and sources for developing against SQLiteCpp.

%prep
%autosetup -p1
sed -iE "s/\r$//" README.md
# Make SONAME lowercase for compatibility with meson build - https://github.com/SRombauts/SQLiteCpp/issues/542
echo 'set_property(TARGET SQLiteCpp PROPERTY OUTPUT_NAME "sqlitecpp")' >> CMakeLists.txt

%build
%cmake \
  -DSQLITECPP_INTERNAL_SQLITE:BOOL=false \
  -DSQLITE_ENABLE_COLUMN_METADATA=true \
  -DSQLITECPP_BUILD_TESTS=true \
  -DSQLITECPP_BUILD_EXAMPLES=true \
  %{nil}
%cmake_build

%install
%cmake_install
# Remove ROS specific file
rm %{buildroot}%{_datadir}/%{name}/package.xml

%check
%ctest --parallel 1

%ldconfig_scriptlets -n %{shlib}

%files -n %{shlib}
%license LICENSE.txt
%{_libdir}/lib*.so.0

%files devel
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{_includedir}/%{name}/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/SQLiteCpp

%changelog
