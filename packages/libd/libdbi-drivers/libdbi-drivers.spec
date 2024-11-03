#
# spec file for package libdbi-drivers
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%if 0%{?suse_version} == 1110
%define build_freetds 0
%else 
%define build_freetds 1
%endif

Name:           libdbi-drivers
Version:        0.9.0.g53
Release:        0
Summary:        Database drivers for libdbi
License:        LGPL-2.1+
Group:          Productivity/Databases/Servers
URL:            http://libdbi-drivers.sf.net/
#Source:        http://downloads.sf.net/libdbi-drivers/%name-%version.tar.gz
Source:		%name-%version.tar.xz
Patch1:         0001-build-adjust-configure-for-postgresql-10-11.patch
Patch2:         0001-build-resolve-build-failure-due-to-mismatching-types.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
%if %build_freetds
BuildRequires:  freetds-devel
%endif
BuildRequires:  libdbi-devel >= 0.9.0.g30
BuildRequires:  libtool
BuildRequires:  mysql-devel
BuildRequires:  openjade
BuildRequires:  postgresql-devel
BuildRequires:  sqlite3-devel
BuildRequires:  xz
%define build_doc 0
%if %build_doc
# Only needed when doc is not already prebuilt
BuildRequires:  docbook-dsssl-stylesheets
BuildRequires:  openjade
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  texlive-jadetex
BuildRequires:  texlive-pdftex-bin
%endif

%description
libdbi implements a database-independent abstraction layer in C,
similar to the DBI/DBD layer in Perl. Drivers are distributed
separately from the library itself.

%package dbd-freetds
Summary:        FreeTDS driver for libdbi
Group:          System/Libraries

%description dbd-freetds
This driver provides connectivity to FreeTDS database servers
through the libdbi database independent abstraction layer. Switching
a program's driver does not require recompilation or rewriting source
code.

%package dbd-mysql
Summary:        MySQL driver for libdbi
Group:          System/Libraries

%description dbd-mysql
This driver provides connectivity to MySQL database servers through
the libdbi database independent abstraction layer. Switching a
program's driver does not require recompilation or rewriting source
code.

%package dbd-pgsql
Summary:        PostgreSQL driver for libdbi
Group:          System/Libraries

%description dbd-pgsql
This driver provides connectivity to PostgreSQL database servers
through the libdbi database independent abstraction layer. Switching
a program's driver does not require recompilation or rewriting source
code.

%package dbd-sqlite3
Summary:        SQLite3 driver for libdbi
Group:          System/Libraries

%description dbd-sqlite3
This driver provides connectivity to SQLite 3.x database servers through the
libdbi database independent abstraction layer. Switching a program's driver
does not require recompilation or rewriting source code.

%prep
%autosetup -p1
chmod a-x COPYING

# Fake the __DATE__ so we do not needelessly rebuild
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %_sourcedir/%name.changes '+%%b %%e %%Y')
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/" drivers/*/*.c

%build
if [ ! -e configure ]; then
	autoreconf -fi
fi
%configure		\
%if %build_freetds
	--with-freetds				\
%endif
	--with-mysql 				\
	--with-pgsql 				\
	--with-sqlite3      \
	--with-dbi-incdir="%_includedir/dbi"	\
	--with-dbi-libdir="%_libdir"		\
	--disable-static			\
	--docdir="%_docdir/%name" --disable-docs
%make_build

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete

%check
make check || :

%if %build_freetds
%files dbd-freetds
%license COPYING
%dir %_libdir/dbd
%_libdir/dbd/libdbdfreetds.so
%endif

%files dbd-mysql
%license COPYING
%dir %_libdir/dbd
%_libdir/dbd/libdbdmysql.so

%files dbd-pgsql
%license COPYING
%dir %_libdir/dbd
%_libdir/dbd/libdbdpgsql.so

%files dbd-sqlite3
%license COPYING
%dir %_libdir/dbd
%_libdir/dbd/libdbdsqlite3.so

%changelog
