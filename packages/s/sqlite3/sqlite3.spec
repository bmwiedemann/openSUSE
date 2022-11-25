#
# spec file for package sqlite3
#
# Copyright (c) 2022 SUSE LLC
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


%define oname sqlite
%define tarversion 3400000
%bcond_with icu
%bcond_without check
Name:           sqlite3
Version:        3.40.0
Release:        0
Summary:        Embeddable SQL Database Engine
License:        SUSE-Public-Domain
Group:          Productivity/Databases/Servers
URL:            https://www.sqlite.org/
Source0:        https://www.sqlite.org/2022/sqlite-src-%{tarversion}.zip
Source1:        baselibs.conf
Source2:        https://www.sqlite.org/2022/sqlite-doc-%{tarversion}.zip
Patch0:         sqlite-src-3390000-func7-pg-181.patch
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  tcl-devel
BuildRequires:  unzip
%if 0%{suse_version} < 1500
# As of 2021 we still need to be able to compile this on SLE-12
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  zlib-devel
%global make_build make
%else
BuildRequires:  pkgconfig(zlib)
%endif
Provides:       %{oname} = %{version}
Obsoletes:      %{oname} < %{version}
%if %{with icu}
BuildRequires:  libicu-devel
%endif

%description
SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

SQLite is not a client library used to connect to a big database
server. SQLite is a server and the SQLite library reads and writes
directly to and from the database files on disk.

SQLite can be used via the sqlite command line tool or via any
application that supports the Qt database plug-ins.

%package -n libsqlite3-0
Summary:        Shared libraries for the Embeddable SQL Database Engine
Group:          Development/Libraries/C and C++

%description -n libsqlite3-0
This package contains the shared libraries for the Embeddable SQL
Database Engine.

SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

SQLite is not a client library used to connect to a big database
server. SQLite is a server and the SQLite library reads and writes
directly to and from the database files on disk.

SQLite can be used via the sqlite command line tool or via any
application that supports the Qt database plug-ins.

%package devel
Summary:        Embeddable SQL Database Engine
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libsqlite3-0 = %{version}
Suggests:       %{name}-doc
Provides:       %{oname}-devel = %{version}
Obsoletes:      %{oname}-devel < %{version}

%description devel
SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

SQLite is not a client library used to connect to a big database
server; SQLite is the server. The SQLite library reads and writes
directly to and from the database files on disk.

SQLite can be used via the sqlite command-line tool or via any
application which supports the Qt database plug-ins.

%package tcl
Summary:        Tcl binding for SQLite
Group:          Development/Libraries/Tcl

%description tcl
This package contains laguage bindings from the Tcl programming
language SQLite.

SQLite is a C library that implements an embeddable SQL database
engine. Programs that link with the SQLite library can have SQL
database access without running a separate RDBMS process.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
BuildArch:      noarch

%description doc

Contains HTML documentation for SQLite: SQL Syntax, C/C++ API and
other documentation found on sqlite.org. The files can be found in
%{_docdir}/%{name}-doc.

%prep
%setup -q -n sqlite-src-%{tarversion} -a2
%autopatch -p1

rm -v sqlite-doc-%{tarversion}/releaselog/current.html
ln -sv `echo %{version} | sed "s/\./_/g"`.html sqlite-doc-%{tarversion}/releaselog/current.html
find -type f -name sqlite.css~ -delete
cmp sqlite-doc-%{tarversion}/fileformat{,2}.html && ln -sf fileformat.html sqlite-doc-%{tarversion}/fileformat2.html

%build
export TCLLIBDIR=%tcl_archdir/sqlite%version
export LIBS="$LIBS -lm %{?with_icu:-licuuc -licui18n}"
export CFLAGS="%{optflags} \
	-DSQLITE_ENABLE_API_ARMOR \
	-DSQLITE_ENABLE_COLUMN_METADATA \
	-DSQLITE_ENABLE_DBSTAT_VTAB \
	-DSQLITE_ENABLE_HIDDEN_COLUMNS \
	-DSQLITE_ENABLE_FTS3 \
	-DSQLITE_ENABLE_FTS4 \
	-DSQLITE_ENABLE_FTS5 \
%if %{with icu}
	-DSQLITE_ENABLE_ICU \
%endif
	-DSQLITE_ENABLE_JSON1 \
	-DSQLITE_ENABLE_RBU \
	-DSQLITE_ENABLE_RTREE \
	-DSQLITE_ENABLE_UPDATE_DELETE_LIMIT \
	-DSQLITE_SOUNDEX \
	-DSQLITE_ENABLE_UNLOCK_NOTIFY \
	-DSQLITE_SECURE_DELETE \
	-DSQLITE_ENABLE_MATH_FUNCTIONS \
	"
%configure \
  --disable-static \
  --enable-readline \
  --enable-fts3 \
  --enable-fts4 \
  --enable-fts5 \
  --enable-update-limit \
  --enable-rtree
%make_build sqlite3.c
%make_build

%if %{with check}
%check
%make_build test
%endif

%install
%make_install
#mkdir -p %{buildroot}/%{_mandir}/man{1,n}/
install -Dp -m 0644 -t %{buildroot}/%{_mandir}/man1 sqlite3.1
install -Dp -m 0644 -t %{buildroot}/%{_mandir}/mann autoconf/tea/doc/sqlite3.n
# tcl bindings are provided by tcl itself
#rm -rf %{buildroot}%{_libdir}/tcl/tcl8.?/sqlite3*
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libsqlite3-0 -p /sbin/ldconfig
%postun -n libsqlite3-0 -p /sbin/ldconfig

%files
%{_bindir}/sqlite3
%{_mandir}/man1/sqlite3.1%{?ext_man}

%files -n libsqlite3-0
%{_libdir}/libsqlite3.so.*

%files devel
%{_includedir}/sqlite3.h
%{_includedir}/sqlite3ext.h
%{_libdir}/libsqlite3.so
%{_libdir}/pkgconfig/sqlite3.pc

%files tcl
%tcl_archdir/*
%doc %_mandir/mann/*

%files doc
%doc sqlite-doc-%{tarversion}/*

%changelog
