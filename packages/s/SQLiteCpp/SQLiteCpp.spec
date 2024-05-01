#
# spec file for package SQLiteCpp
#
# Copyright (c) 2024 SUSE LLC
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
Version:        3.3.1
Release:        0
Summary:        A C++ SQLite3 wrapper
License:        MIT
URL:            https://srombauts.github.io/SQLiteCpp
Source:         https://github.com/SRombauts/SQLiteCpp/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  gtest
BuildRequires:  meson
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
%autosetup
sed -iE "s/\r$//" README.md

%build
%meson \
  -DSQLITE_ENABLE_COLUMN_METADATA=true \
  -DSQLITECPP_BUILD_TESTS=true \
  -DSQLITECPP_BUILD_EXAMPLES=true \
  -Dcpp_std=c++14 \
	%{nil}
%meson_build

%install
%meson_install

%check
%meson_test

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

%changelog
