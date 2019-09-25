#
# spec file for package libgda
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


Name:           libgda
Version:        5.2.9
Release:        0
# FIXME: add bdb sql BuildRequires when available
Summary:        GNU Data Access (GDA) Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Databases/Clients
URL:            https://www.gnome-db.org/
Source:         https://download.gnome.org/sources/libgda/5.2/%{name}-%{version}.tar.xz

# PATCH-FIX-UPSTREAM libgda-javadetection-biarch.patch bgo#673560 -- Prepare getsp to be sed'ed for biarch
Patch1:         libgda-javadetection-biarch.patch
# PATCH-FIX-UPSTREAM libgda-no-pg_config.patch dimstar@opensuse.org -- Don't use pg_config to find postgresql. Patch not directly applicable as-is upstream, but fixed in master
Patch7:         libgda-no-pg_config.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  db-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool >= 0.40.6
BuildRequires:  itstool
BuildRequires:  java-devel >= 1.8
BuildRequires:  libgcrypt-devel
BuildRequires:  libopenssl-1_0_0-devel
BuildRequires:  libtool
BuildRequires:  mdbtools-devel
BuildRequires:  mysql
BuildRequires:  mysql-devel
BuildRequires:  ncurses-devel
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  readline-devel
BuildRequires:  unixODBC-devel
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.26.0
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(fbclient)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(goocanvas-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgvc)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(sqlite3)
#!BuildIgnore:  openssl

%description
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package tools
Summary:        GNU Data Access (GDA) Library -- Tools
Group:          Productivity/Databases/Clients
Requires:       %{name}-5_0-tools = %{version}
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description tools
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

This package provides command-line tools for libgda.

%package 5_0-tools
Summary:        GNU Data Access (GDA) Library -- Tools
Group:          Productivity/Databases/Clients
Provides:       %{name}-5_0 = %{version}
Obsoletes:      %{name}-5_0 < %{version}

%description 5_0-tools
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

This package provides command-line tools for libgda.

%package ui-5_0-tools
Summary:        GNU Data Access (GDA) Library -- Graphical Tools
Group:          Productivity/Databases/Clients
Supplements:    packageand(%{name}-5_0-tools:%{name}-ui-5_0-4}

%description ui-5_0-tools
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

This package provides graphical tools:
  - gda-browser: a tool to browse databases
  - gda-control-center: configuration tool for libgda

%package 5_0-4
Summary:        GNU Data Access (GDA) Library
Group:          System/Libraries
Recommends:     %{name}-5_0-4-lang
Recommends:     %{name}-5_0-bdb = %{version}

%description 5_0-4
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package -n typelib-1_0-Gda-5_0
Summary:        GNU Data Access (GDA) Library -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Gda-5_0
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

This package provides the GObject Introspection bindings for
libgda.

%package ui-5_0-4
Summary:        GNU Data Access (GDA) Library - UI Widgets
Group:          System/Libraries
Recommends:     iso-codes
Supplements:    packageand(libgda-5_0-4:gtk3)

%description ui-5_0-4
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package -n typelib-1_0-Gdaui-5_0
Summary:        GNU Data Access (GDA) Library - UI Widgets -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Gdaui-5_0
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

This package provides the GObject Introspection bindings for
libgda-ui.

%package ui-5_0-plugins
Summary:        GNU Data Access (GDA) Library - Plugins for UI Widgets
Group:          System/Libraries
Supplements:    %{name}-ui-5_0-4

%description ui-5_0-plugins
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package report-5_0-4
Summary:        GNU Data Access (GDA) Library
Group:          System/Libraries

%description report-5_0-4
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package xslt-5_0-4
Summary:        GNU Data Access (GDA) Library
Group:          System/Libraries

%description xslt-5_0-4
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package 5_0-devel
Summary:        GNU Data Access (GDA) Library -- Development Files
Group:          Development/Libraries/C and C++
Requires:       %{name}-5_0-4 = %{version}
Requires:       %{name}-ui-5_0-4 = %{version}
Requires:       typelib-1_0-Gda-5_0 = %{version}
Requires:       typelib-1_0-Gdaui-5_0 = %{version}
# named libgda-devel on 10.3
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}

%description 5_0-devel
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

This package contains all necessary include files and libraries needed
to develop applications that require these.

%package 5_0-doc
Summary:        GNU Data Access (GDA) Library -- Developer Documentation
Group:          Development/Libraries/C and C++
Provides:       %{name}-doc = %{version}
# named libgda-doc on 10.3
Obsoletes:      %{name}-doc <= 1.3.91

%description 5_0-doc
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package 5_0-bdb
Summary:        Berkeley DB Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{name}-5_0-4 = %{version}

%description 5_0-bdb
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package 5_0-firebird
Summary:        Firebird DB Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{name}-5_0-4 = %{version}

%description 5_0-firebird
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package 5_0-jdbc
Summary:        JDBC Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{name}-5_0-4 = %{version}
Supplements:    libgda-5_0
Provides:       %{name}-jdbc = %{version}
Obsoletes:      %{name}-jdbc <= 1.3.91

%description 5_0-jdbc
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package 5_0-ldap
Summary:        LDAP Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{name}-5_0-4 = %{version}
Supplements:    packageand(libgda-5_0:%(cd %{_libdir} ; rpm -qf --queryformat=%%{NAME} `readlink %{_libdir}/libldap.so` ))

%description 5_0-ldap
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package 5_0-mdb
Summary:        MDB (Microsoft Access Databases) Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{name}-5_0-4 = %{version}
Supplements:    packageand(libgda-5_0:%(cd %{_libdir} ; rpm -qf --queryformat=%%{NAME} `readlink %{_libdir}/libmdb.so` ))

%description 5_0-mdb
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package 5_0-mysql
Summary:        MySQL Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{name}-5_0-4 = %{version}
Supplements:    packageand(libgda-5_0:%(cd %{_libdir} ; rpm -qf --queryformat=%%{NAME} `readlink %{_libdir}/libmysqlclient.so` ))
Provides:       %{name}-mysql = %{version}
Obsoletes:      %{name}-mysql <= 1.3.91

%description 5_0-mysql
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package 5_0-postgres
Summary:        PostgreSQL Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{name}-5_0-4 = %{version}
Supplements:    packageand(libgda-5_0:%(cd %{_libdir} ; rpm -qf --queryformat=%%{NAME} `readlink %{_libdir}/libpq.so` ))
Provides:       %{name}-postgres = %{version}
Obsoletes:      %{name}-postgres <= 1.3.91

%description 5_0-postgres
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package 5_0-sqlcipher
Summary:        SQLCipher Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{name}-5_0-4 = %{version}
Requires:       %{name}-5_0-sqlite = %{version}
Enhances:       %{name}-5_0-sqlite
Provides:       %{name}-sqlcipher = %{version}

%description 5_0-sqlcipher
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package 5_0-sqlite
Summary:        Sqlite Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{name}-5_0-4 = %{version}
Supplements:    packageand(libgda-5_0:%(cd %{_libdir} ; rpm -qf --queryformat=%%{NAME} `readlink %{_libdir}/libsqlite3.so` ))
Provides:       %{name}-sqlite = %{version}
Obsoletes:      %{name}-sqlite <= 1.3.91

%description 5_0-sqlite
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package 5_0-web
Summary:        Web Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{name}-5_0-4 = %{version}
Provides:       %{name}-web = %{version}

%description 5_0-web
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%lang_package -n %{name}-5_0-4

%prep
%autosetup -p1

%build
autoreconf -fi
export LANG=C.UTF-8
# Patch1 introdcues a --ARCH-- field in getsp, which needs to be replace prior to compilation
getspARCH=%{_target_cpu}
%ifarch x86_64
getspARCH=amd64
%endif
%ifarch %{ix86}
getspARCH=i386
%endif
%ifarch %{arm}
getspARCH=arm
%endif
# IcedTea 2.5.0 have ppc64 as libarch for ppc64le
# except if still build with java 1.7
%ifarch ppc64le
%define ppc64_java %(rpm -qa |grep jdk.devel|grep -Ec '(1_5|1_6)')
%if  0%{ppc64_java}
getspARCH=ppc64
%endif
%endif
%if %{pkg_vcmp java-devel >= 9}
getspARCH=.
%endif
sed -i "s:--ARCH--:$getspARCH:g" getsp.java
# Find the current version of vapigen
VAPIGEN=$(realpath %{_bindir}/vapigen)
VAPIGENVER=${VAPIGEN: -4}
# Due to patch1, getsp.java needs to be rebuilt
javac getsp.java
%configure --with-pic\
    --disable-static \
    --enable-binreloc \
    --enable-default-binary \
    --with-postgres \
    --with-libdir-name=%{_lib} \
    --enable-gda-gi \
    --enable-gdaui-gi \
    --enable-vala VALA_API_VERSION=${VAPIGENVER}
%make_build

%install
# remove error about java bytecode being for something later than java 1.15 -- see http://en.opensuse.org/Java/Packaging/Cookbook
export NO_BRP_CHECK_BYTECODE_VERSION=true
%make_install
# X-SuSE-Design is just to make the brp check happy...
%suse_update_desktop_file gda-browser-5.0 X-SuSE-Design
%suse_update_desktop_file gda-control-center-5.0
# This a test database, we don't want it in the package
rm %{buildroot}%{_sysconfdir}/libgda-5.0/sales_test.db
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang libgda-5.0 %{?no_lang_C}
%find_lang gda-browser %{?no_lang_C} libgda-5.0.lang
# Note for the future: we'll need something like this, but we might want the translations in a tools-lang subpackage
#%%find_lang gda-sql %%{?no_lang_C}
%fdupes %{buildroot}%{_prefix}

%post ui-5_0-tools
%desktop_database_post
%icon_theme_cache_post

%postun ui-5_0-tools
%desktop_database_postun
%icon_theme_cache_postun

%post 5_0-4 -p /sbin/ldconfig
%postun 5_0-4 -p /sbin/ldconfig
%post ui-5_0-4 -p /sbin/ldconfig
%postun ui-5_0-4 -p /sbin/ldconfig
%post report-5_0-4 -p /sbin/ldconfig
%postun report-5_0-4 -p /sbin/ldconfig
%post xslt-5_0-4 -p /sbin/ldconfig
%postun xslt-5_0-4 -p /sbin/ldconfig

%files 5_0-4-lang -f libgda-5.0.lang

%files tools
%{_bindir}/gda-list-config
%{_bindir}/gda-list-server-op
%{_bindir}/gda-sql
%{_mandir}/man1/gda-sql.1*

%files 5_0-tools
# NOTE: Even if it was probably intended by upstream to be in sync with
# the libgda soname, naming scheme is different (5_0-4 for soname, 5_0
# for data files). To be on the safe side, package it separately.
# This package contains only files with "5.0" in its name or path.
%license COPYING
%{_bindir}/gda-list-config-5.0
%{_bindir}/gda-list-jdbc-providers-5.0
%{_bindir}/gda-list-server-op-5.0
%{_bindir}/gda-sql-5.0
%{_bindir}/gda-test-connection-5.0
%{_mandir}/man1/gda-sql-5.0.1*
# For web server embedded in gda-sql
%{_datadir}/libgda-5.0/web/
# in report-5_0-4
%exclude %{_datadir}/libgda-5.0/gda_trml2html
%exclude %{_datadir}/libgda-5.0/gda_trml2pdf

%files ui-5_0-tools
%doc %{_datadir}/help/C/gda-browser/
# gda-browser
%{_bindir}/gda-browser-5.0
%dir %{_datadir}/appdata
%{_datadir}/appdata/gda-browser-5.0.appdata.xml
%{_datadir}/applications/gda-browser-5.0.desktop
%{_datadir}/libgda-5.0/icons/
%{_datadir}/libgda-5.0/pixmaps/gda-browser*.png
%{_datadir}/pixmaps/gda-browser-*.png
# gda-control-center
%{_bindir}/gda-control-center-5.0
%{_datadir}/applications/gda-control-center-5.0.desktop
%{_datadir}/icons/hicolor/*/apps/gda-control-center.*
%{_datadir}/libgda-5.0/pixmaps/gda-control-center*.png

%files 5_0-4
%license COPYING.LIB
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libgda-5.0.so.*
%dir %{_datadir}/libgda-5.0
%dir %{_datadir}/libgda-5.0/dtd
%{_datadir}/libgda-5.0/information_schema.xml
%{_datadir}/libgda-5.0/dtd/libgda-*.dtd
%dir %{_sysconfdir}/libgda-5.0
%config %{_sysconfdir}/libgda-5.0/config
%dir %{_libdir}/libgda-5.0
%dir %{_libdir}/libgda-5.0/plugins
%dir %{_libdir}/libgda-5.0/providers

%files -n typelib-1_0-Gda-5_0
%{_libdir}/girepository-1.0/Gda-5.0.typelib

%files ui-5_0-4
%{_libdir}/libgda-ui-5.0.so.*
%dir %{_datadir}/libgda-5.0/pixmaps
%dir %{_datadir}/libgda-5.0/ui
%{_datadir}/libgda-5.0/dtd/gdaui-layout.dtd
%{_datadir}/libgda-5.0/pixmaps/bin-attachment-16x16.png
%{_datadir}/libgda-5.0/pixmaps/gdaui-*
%{_datadir}/libgda-5.0/ui/gdaui-*
%{_datadir}/libgda-5.0/import_encodings.xml
%{_datadir}/libgda-5.0/server_operation.glade

%files -n typelib-1_0-Gdaui-5_0
%{_libdir}/girepository-1.0/Gdaui-5.0.typelib

%files ui-5_0-plugins
%{_libdir}/libgda-5.0/plugins/gdaui-*.xml
%{_libdir}/libgda-5.0/plugins/libgda-ui-plugins.so
# For syntax highlighting
%{_datadir}/libgda-5.0/language-specs/

%files report-5_0-4
# NOTE: This library has the same versioning policy, but depends on libgda-sqlite.
%{_datadir}/libgda-5.0/gda_trml2html
%{_datadir}/libgda-5.0/gda_trml2pdf
%{_libdir}/libgda-report-5.0.so.*

%files xslt-5_0-4
%{_libdir}/libgda-xslt-5.0.so.*

%files 5_0-devel
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_includedir}/libgda-5.0/
%{_libdir}/libgda-5.0.so
%{_libdir}/libgda-xslt-5.0.so
%{_libdir}/libgda-report-5.0.so
%{_libdir}/libgda-ui-5.0.so
%{_libdir}/pkgconfig/*-5.0.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/libgda-5.0.vapi
%{_datadir}/vala/vapi/libgda-ui-5.0.vapi
# demo
%{_bindir}/gdaui-demo-5.0
%{_datadir}/libgda-5.0/demo/

%files 5_0-doc
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_datadir}/gtk-doc/html/gda-browser/
%{_datadir}/gtk-doc/html/libgda-5.0/

%files 5_0-bdb
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_libdir}/libgda-5.0/providers/libgda-bdb.so
%{_datadir}/libgda-5.0/bdb_*.xml

%files 5_0-firebird
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_libdir}/libgda-5.0/providers/libgda-firebird-client.so
%{_datadir}/libgda-5.0/firebird_*.xml

%files 5_0-jdbc
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_libdir}/libgda-5.0/providers/gdaprovider-5.0.jar
%{_libdir}/libgda-5.0/providers/libgda-jdbc.so
%{_datadir}/libgda-5.0/jdbc_*.xml

%files 5_0-ldap
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_libdir}/libgda-5.0/providers/libgda-ldap.so
%{_datadir}/libgda-5.0/ldap_*.xml

%files 5_0-mdb
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_libdir}/libgda-5.0/providers/libgda-mdb.so
%{_datadir}/libgda-5.0/mdb_*.xml

%files 5_0-mysql
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_libdir}/libgda-5.0/providers/libgda-mysql.so
%{_datadir}/libgda-5.0/mysql_*.xml

%files 5_0-postgres
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_libdir}/libgda-5.0/providers/libgda-postgres.so
%{_datadir}/libgda-5.0/postgres_*.xml

%files 5_0-sqlcipher
# NOTE: Files don't conflict with previous version => Use versioned package name
%license providers/sqlcipher/COPYING.sqlcipher
%{_libdir}/libgda-5.0/providers/libgda-sqlcipher.so
%{_datadir}/libgda-5.0/sqlcipher_*.xml

%files 5_0-sqlite
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_libdir}/libgda-5.0/providers/libgda-sqlite.so
%{_datadir}/libgda-5.0/sqlite_*.xml

%files 5_0-web
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_libdir}/libgda-5.0/providers/libgda-web.so
%{_datadir}/libgda-5.0/web_*.xml
%{_datadir}/libgda-5.0/php/

%changelog
