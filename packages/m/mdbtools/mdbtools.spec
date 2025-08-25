#
# spec file for package mdbtools
#
# Copyright (c) 2022 SUSE LLC
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


%define libmdb    libmdb3
%define libmdbsql libmdbsql3
Name:           mdbtools
Version:        1.0.1
Release:        0
Summary:        A Suite of Libraries and Programs to Access Microsoft Access Databases
License:        GPL-2.0-or-later
Group:          Productivity/Databases/Tools
URL:            https://github.com/mdbtools
Source0:        https://github.com/mdbtools/mdbtools/releases/download/v%{version}/mdbtools-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(odbc)
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(readline)
%else
BuildRequires:  readline-devel
%endif

%description
Mdbtools contains:
mdb-dump -- simple hex dump utility for looking at mdb files
mdb-schema -- prints DDL for the specified table
mdb-export -- export table to CSV format
mdb-tables -- a simple dump of table names to be used with shell scripts
mdb-header -- generates a C header to be used in exporting mdb data to a C prog
mdb-parsecvs -- generates a C program given a CSV file made with mdb-export
mdb-sql -- demo SQL engine program
mdb-ver -- print version of database

%package devel
Summary:        All files necessary for development with the MDB Tools libraries
Group:          Development/Libraries/C and C++
Requires:       %{libmdbsql} = %{version}
Requires:       %{libmdb} = %{version}

%description devel
Mdbtools contains:
mdb-dump -- simple hex dump utility for looking at mdb files
mdb-schema -- prints DDL for the specified table
mdb-export -- export table to CSV format
mdb-tables -- a simple dump of table names to be used with shell scripts
mdb-header -- generates a C header to be used in exporting mdb data to a C prog
mdb-parsecvs -- generates a C program given a CSV file made with mdb-export
mdb-sql -- demo SQL engine program
mdb-ver -- print version of database

%package -n %{libmdb}
Summary:        MDB Tools ODBC driver for unixODBC
Group:          Productivity/Databases/Tools

%description -n %{libmdb}
Contains shared library %{libmdb} from %{name}

%package -n %{libmdbsql}
Summary:        MDB Tools ODBC driver for unixODBC
Group:          Productivity/Databases/Tools

%description -n %{libmdbsql}
Contains shared library %{libmdbsql} from %{name}

%prep
%autosetup -p1

%build
%configure \
  --disable-static \
  --with-pic \
  --with-unixodbc=%{_prefix} \
  %{nil}
%make_build

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %{libmdb}
%ldconfig_scriptlets -n %{libmdbsql}

%files
%license COPYING*
%doc AUTHORS NEWS HACKING
%{_bindir}/mdb-array
%{_bindir}/mdb-count
%{_bindir}/mdb-export
%{_bindir}/mdb-header
%{_bindir}/mdb-hexdump
%{_bindir}/mdb-json
%{_bindir}/mdb-parsecsv
%{_bindir}/mdb-prop
%{_bindir}/mdb-queries
%{_bindir}/mdb-schema
%{_bindir}/mdb-sql
%{_bindir}/mdb-tables
%{_bindir}/mdb-ver
%{_mandir}/man1/*.1%{?ext_man}
%{_datadir}/bash-completion/completions/mdb-*

%files -n %{libmdb}
%license COPYING*
%{_libdir}/libmdb.so.3*

%files -n %{libmdbsql}
%license COPYING*
%{_libdir}/libmdbsql.so.3*

%files devel
%license COPYING*
%{_includedir}/mdb*.h
%{_libdir}/libmdbsql.so
%{_libdir}/libmdb.so
%dir %{_libdir}/odbc
%{_libdir}/odbc/libmdbodbc.so
%{_libdir}/odbc/libmdbodbcW.so
%{_libdir}/pkgconfig/libmdb.pc
%{_libdir}/pkgconfig/libmdbsql.pc

%changelog
