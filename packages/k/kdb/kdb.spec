#
# spec file for package kdb
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover 4
Name:           kdb
Version:        3.2.0
Release:        0
Summary:        Database Connectivity and Creation Framework
License:        LGPL-2.0-only
Group:          Productivity/Office/Other
URL:            https://community.kde.org/KDb
Source0:        https://download.kde.org/stable/%{name}/src/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         Fix-build-with-PostgreSQL-12.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  libicu-devel
BuildRequires:  libmysqlclient-devel
BuildRequires:  libmysqld-devel
BuildRequires:  pkgconfig
BuildRequires:  python-base
BuildRequires:  sqlite3-devel
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
%if 0%{?suse_version} > 1500
BuildRequires:  postgresql-server-devel
%else
BuildRequires:  postgresql-devel
%endif

%description
A database connectivity and creation framework for various database vendors

%package -n libKDb3-%{sover}
Summary:        The library for the Database Connectivity and Creation Framework
Group:          System/Libraries
Recommends:     %{name}-lang >= %{version}
Obsoletes:      calligra-kexi-mssql-driver < %{version}
Obsoletes:      calligra-kexi-xbase-driver < %{version}
Provides:       %{name} = %{version}

%description -n libKDb3-%{sover}
The library for the database connectivity and creation framework for various database vendors

%package devel
Summary:        Development package for kdb
Group:          Development/Libraries/KDE
Requires:       libKDb3-%{sover} = %{version}

%description devel
The development package for the database connectivity and creation framework

%package mysql-driver
Summary:        Database connectivity and creation framework - MySQL driver
Group:          Productivity/Office/Suite
Supplements:    packageand(libKDb3-%{sover}:mariadb)
Obsoletes:      calligra-kexi-mysql-driver < %{version}
Provides:       calligra-kexi-mysql-driver = %{version}

%description mysql-driver
This package contains the MySQL driver for the Database connectivity and creation framework

%package postgresql-driver
Summary:        Database connectivity and creation framework - PostgreSQL driver
Group:          Productivity/Office/Suite
Supplements:    packageand(libKDb3-%{sover}:postgresql)
Obsoletes:      calligra-kexi-postgresql-driver < %{version}
Provides:       calligra-kexi-postgresql-driver = %{version}

%description postgresql-driver
This package contains the PostgreSQL driver for the Database connectivity and creation framework

%package sqlite3-driver
Summary:        Database connectivity and creation framework - SQLite3 driver
Group:          Productivity/Office/Suite
Supplements:    packageand(libKDb3-%{sover}:sqlite3)
Obsoletes:      calligra-kexi-sqlite3-driver < %{version}
Provides:       calligra-kexi-sqlite3-driver = %{version}

%description sqlite3-driver
This package contains the SQLite3 driver for the Database connectivity and creation framework

%lang_package

%prep
%setup -q
%autopatch -p1

%build
%cmake_kf5 -d build
%make_jobs

%install
  %kf5_makeinstall -C build
  %find_lang %{name} %{name}.lang --all-name --with-qt

  # Contains bogus entries
  rm -f %{buildroot}%{_libdir}/pkgconfig/KDb3.pc

%post -n libKDb3-%{sover} -p /sbin/ldconfig
%postun -n libKDb3-%{sover} -p /sbin/ldconfig

%files -n libKDb3-%{sover}
%license COPYING.LIB
%{_libdir}/libKDb3.so.*

%files devel
%license COPYING*
%{_includedir}/KDb3/
%{_libdir}/cmake/KDb3/
#%%{_libdir}/pkgconfig/KDb3.pc
%{_kf5_mkspecsdir}/qt_KDb3.pri
%{_libdir}/libKDb3.so

%files sqlite3-driver
%license COPYING*
%{_bindir}/kdb3_sqlite3_dump
%dir %{_kf5_plugindir}/kdb3
%{_kf5_plugindir}/kdb3/kdb_sqlitedriver.so
%dir %{_kf5_plugindir}/kdb3/sqlite3
%{_kf5_plugindir}/kdb3/sqlite3/kdb_sqlite_icu.so

%files postgresql-driver
%license COPYING*
%dir %{_kf5_plugindir}/kdb3
%{_kf5_plugindir}/kdb3/kdb_postgresqldriver.so

%files mysql-driver
%license COPYING*
%dir %{_kf5_plugindir}/kdb3
%{_kf5_plugindir}/kdb3/kdb_mysqldriver.so

%files lang -f %{name}.lang

%changelog
