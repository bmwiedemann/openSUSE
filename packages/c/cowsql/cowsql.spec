#
# spec file for package cowsql
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define lname libcowsql0
Name:           cowsql
Version:        1.15.8
Release:        0
Summary:        Embeddable, replicated and fault tolerant SQL engine
License:        LGPL-3.0-only WITH LGPL-3.0-linking-exception
URL:            https://github.com/cowsql/cowsql
Source:         https://github.com/cowsql/cowsql/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(libuv) >= 1.8.0
# technically >= 0.18, but needs the cowsql/raft fork and breaks with canonical/raft 0.18.1
# specify 0.22.0 as this is the first package with the cowsql/raft fork
BuildRequires:  pkgconfig(raft) >= 0.22.0
BuildRequires:  pkgconfig(sqlite3) >= 3.22.0

%description
cowsql is a C library that implements an embeddable and replicated SQL database
engine with high availability and automatic failover.

cowsql extends SQLite with a network protocol that can connect together various
instances of your application and have them act as a highly-available cluster,
with no dependency on external databases.

%package -n %{lname}
Summary:        Embeddable, replicated and fault tolerant SQL engine

%description -n %{lname}
cowsql is a C library that implements an embeddable and replicated SQL database
engine with high availability and automatic failover.

cowsql extends SQLite with a network protocol that can connect together various
instances of your application and have them act as a highly-available cluster,
with no dependency on external databases.

This package contains the share library.

%package devel
Summary:        Embeddable, replicated and fault tolerant SQL engine
Requires:       %{lname} = %{version}

%description devel
cowsql is a C library that implements an embeddable and replicated SQL database
engine with high availability and automatic failover.

cowsql extends SQLite with a network protocol that can connect together various
instances of your application and have them act as a highly-available cluster,
with no dependency on external databases.

This package contains the files necessary for developing and building
applications using the library.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %{lname}

%check
%make_build check

%files devel
%license LICENSE
%doc AUTHORS README.md
%{_includedir}/cowsql.h
%{_libdir}/libcowsql.so
%{_libdir}/pkgconfig/cowsql.pc

%files -n %{lname}
%license LICENSE
%{_libdir}/libcowsql.so.*

%changelog
