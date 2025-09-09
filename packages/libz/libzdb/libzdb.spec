#
# spec file for package libzdb
#
# Copyright (c) 2024 SUSE LLC
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


%define sover 17
Name:           libzdb
Version:        3.4.1
Release:        0
Summary:        Zild Database Library
License:        GPL-3.0-or-later
Group:          System/Libraries
URL:            https://www.tildeslash.com/libzdb/
Source0:        http://www.tildeslash.com/%{name}/dist/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(sqlite3)
# for pg_config
BuildRequires:  postgresql-server-devel
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(mysqlclient)
%else
BuildRequires:  mysql-devel
%endif

%description
The Zild Database Library implements a small, fast, and easy to use
database API with thread-safe connection pooling. The library can connect
transparently to multiple database systems, has zero configuration and
connections are specified via a standard URL scheme.

%package -n %{name}%{sover}
Summary:        Shared library for libzdb
Group:          System/Libraries
Provides:       libzdb

%description -n %{name}%{sover}
Zild Database Library

This package contains the shared libzdb library

%package devel
Summary:        Development files for libzdb
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
The libraries and header files for developing applications that use libzdb

%prep
%autosetup -p1

%build
%configure \
  --disable-static \
  --enable-openssl \
  --enable-sqliteunlock \
  --enable-protected \
  --enable-optimized \
  %{nil}
%make_build

%install
%make_install
# remove static libs
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license COPYING
%doc AUTHORS CHANGES README
%{_libdir}/%{name}.so.%{sover}{,.*}

%files devel
%license COPYING
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/zdb.pc
%{_includedir}/zdb

%changelog
