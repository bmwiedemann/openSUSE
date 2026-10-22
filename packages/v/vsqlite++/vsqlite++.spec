#
# spec file for package vsqlite++
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


%define lib_name libvsqlitepp
%define sover   0
Name:           vsqlite++
Version:        0.4.2
Release:        0
Summary:        Well designed C++ sqlite 3.x wrapper library
License:        BSD-3-Clause
URL:            https://github.com/vinzenz/vsqlite--
Source0:        https://github.com/vinzenz/vsqlite--/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.21
BuildRequires:  gcc-c++ >= 11
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sqlite3)

%description
VSQLite++ is a C++ wrapper for sqlite3 using the C++ standard library.
VSQLite++ is designed to be easy to use and focuses on simplicity.

%package -n %{lib_name}%{sover}
Summary:        Well designed C++ sqlite 3.x wrapper library

%description -n %{lib_name}%{sover}
VSQLite++ is a C++ wrapper for sqlite3 using the C++ standard library.
VSQLite++ is designed to be easy to use and focuses on simplicity.

%package devel
Summary:        Development files for %{name}
Requires:       %{lib_name}%{sover} = %{version}

%description devel
This package contains development files for %{name}.

%prep
%autosetup -n vsqlite---%{version}

%build
%cmake -DBUILD_TESTING=OFF -DVSQLITE_BUILD_EXAMPLES=OFF -DVSQLITE_BUNDLED_SQLITE=OFF
%cmake_build

%install
%cmake_install
# Upstream excludes include/sqlite/private from install, but public
# <sqlite/function.hpp> includes <sqlite/private/private_accessor.hpp>
mkdir -p %{buildroot}%{_includedir}/sqlite/private
install -m 644 include/sqlite/private/*.hpp %{buildroot}%{_includedir}/sqlite/private/
# COPYING is shipped as %%license in the shlib package
rm %{buildroot}%{_docdir}/%{name}/COPYING

%ldconfig_scriptlets -n %{lib_name}%{sover}

%files devel
%{_docdir}/%{name}
%{_includedir}/sqlite
%{_libdir}/libvsqlitepp.so
%{_libdir}/cmake/vsqlitepp

%files -n %{lib_name}%{sover}
%license COPYING
%{_libdir}/libvsqlitepp.so.%{sover}*

%changelog
