#
# spec file for package mdbtools
#
# Copyright (c) 2021 SUSE LLC
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
Version:        0.9.3
Release:        0
Summary:        A Suite of Libraries and Programs to Access Microsoft Access Databases
License:        GPL-2.0-or-later
Group:          Productivity/Databases/Tools
URL:            https://github.com/mdbtools
Source0:        https://github.com/mdbtools/mdbtools/releases/download/v%{version}/mdbtools-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  txt2man
BuildRequires:  unixODBC-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)

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
Requires:       flex
Requires:       glib2-devel
Requires:       unixODBC-devel

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
%autosetup

%build
autoreconf -fiv
%configure \
  --disable-static \
  --with-pic \
  --with-unixodbc=%{_prefix} \
  --disable-gmdb2 \
  --disable-gtk-doc \
  %{nil}
%make_build

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libmdb} -p /sbin/ldconfig
%post -n %{libmdbsql} -p /sbin/ldconfig
%postun -n %{libmdb} -p /sbin/ldconfig
%postun -n %{libmdbsql} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS HACKING
%{_bindir}/mdb-*
%{_mandir}/man1/mdb-*.1%{?ext_man}
%{_datadir}/bash-completion/completions/mdb-*

%files -n %{libmdb}
%{_libdir}/libmdb.so.3*

%files -n %{libmdbsql}
%{_libdir}/libmdbsql.so.3*

%files devel
%{_includedir}/mdb*.h
%{_libdir}/libmdbsql.so
%{_libdir}/libmdb.so
%{_libdir}/libmdbodbc.so
%{_libdir}/libmdbodbcW.so
%{_libdir}/pkgconfig/libmdb.pc
%{_libdir}/pkgconfig/libmdbsql.pc

%changelog
