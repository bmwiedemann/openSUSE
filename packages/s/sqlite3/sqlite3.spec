#
# spec file for package sqlite3
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define _buildshell /bin/bash
%define oname sqlite
%define tarversion 3500400
%define docversion 3500400
%bcond_with icu
%bcond_without check
Name:           sqlite3
Version:        3.50.4
Release:        0
Summary:        Embeddable SQL Database Engine
License:        SUSE-Public-Domain
Group:          Productivity/Databases/Servers
URL:            https://www.sqlite.org/
Source0:        https://www.sqlite.org/2025/sqlite-src-%{tarversion}.zip
Source1:        baselibs.conf
Source2:        https://www.sqlite.org/2025/sqlite-doc-%{docversion}.zip
Source99:       %{name}-rpmlintrc
Patch0:         sqlite-3.6.23-lemon-system-template.patch
Patch1:         sqlite-3.49.0-fix-lemon-missing-cflags.patch
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
%{?suse_build_hwcaps_libs}

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
Group:          System/Libraries

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

%package -n lemon
Summary:        A parser generator

%description -n lemon
Lemon is an LALR(1) parser generator for C or C++. It does the same
job as bison and yacc. But lemon is not another bison or yacc
clone. It uses a different grammar syntax which is designed to reduce
the number of coding errors. Lemon also uses a more sophisticated
parsing engine that is faster than yacc and bison and which is both
reentrant and thread-safe. Furthermore, Lemon implements features
that can be used to eliminate resource leaks, making is suitable for
use in long-running programs such as graphical user interfaces or
embedded controllers.

%prep
# Version and %%tarversion need to match, but %%docversion might be different,
IFS=. read a b c d <<< "%version"
if [ "%tarversion" != $(printf "%1d%02d%02d%02d" $a $b $c $d) ]
then
	echo "Version %version does not match tarversion %tarversion."
	exit 1
fi

%autosetup -p1 -n sqlite-src-%{tarversion} -a2

rm -v sqlite-doc-%{docversion}/releaselog/current.html
ln -sv `echo %{docversion} | sed "s/\./_/g"`.html sqlite-doc-%{docversion}/releaselog/current.html
find -type f -name sqlite.css~ -delete
cmp sqlite-doc-%{docversion}/fileformat{,2}.html && ln -sf fileformat.html sqlite-doc-%{docversion}/fileformat2.html

%build
export TCLLIBDIR=%tcl_archdir/sqlite%version
export CC=gcc
export CC_FOR_BUILD=gcc
export CFLAGS="%{optflags} \
	-DSQLITE_ENABLE_API_ARMOR \
	-DSQLITE_ENABLE_COLUMN_METADATA \
	-DSQLITE_ENABLE_DBSTAT_VTAB \
	-DSQLITE_ENABLE_HIDDEN_COLUMNS \
	-DSQLITE_ENABLE_FTS3 \
	-DSQLITE_ENABLE_FTS4 \
	-DSQLITE_ENABLE_FTS5 \
	-DSQLITE_ENABLE_JSON1 \
	-DSQLITE_ENABLE_RBU \
	-DSQLITE_ENABLE_RTREE \
	-DSQLITE_ENABLE_UPDATE_DELETE_LIMIT \
	-DSQLITE_SOUNDEX \
	-DSQLITE_ENABLE_UNLOCK_NOTIFY \
	-DSQLITE_SECURE_DELETE \
	-DSQLITE_ENABLE_MATH_FUNCTIONS \
	-DSQLITE_STRICT_SUBTYPE=1 \
	"
%configure \
  --soname=legacy \
  --disable-static \
  --enable-readline \
  --enable-fts3 \
  --enable-fts4 \
  --enable-fts5 \
  --enable-update-limit \
  --enable-rtree \
%if %{with icu}
  --icu-collations \
  --with-icu-config=/usr/bin/icu-config \
%endif
  --enable-session
%make_build sqlite3.c
%make_build

%if %{with check}
%check
%make_build test
%endif

%install
%make_install
install -Dpvm 0644 -t %{buildroot}/%{_mandir}/man1 sqlite3.1
install -Dpvm 0644 -t %{buildroot}/%{_mandir}/mann autoconf/tea/doc/sqlite3.n
install -Dpvm 0755 -t %{buildroot}%{_bindir} lemon
install -Dpvm 0644 -t %{buildroot}%{_datadir}/lemon tool/lempar.c
# tcl bindings are provided by tcl itself
#rm -rf %%{buildroot}%%{_libdir}/tcl/tcl8.?/sqlite3*
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n libsqlite3-0

%files
%license LICENSE.md
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
%doc sqlite-doc-%{docversion}/*

%files -n lemon
%{_bindir}/lemon
%{_datadir}/lemon

%changelog
