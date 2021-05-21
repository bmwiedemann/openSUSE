#
# spec file for package libgda
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

%bcond_with fbclient
# BDB: Currently broken. 
%bcond_with bdb
%define _name libgda
Name:           libgda
Version:        6.0.0
Release:        0
# FIXME: add bdb sql BuildRequires when available
Summary:        GNU Data Access (GDA) Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Databases/Clients
URL:            https://www.gnome-db.org/
Source:         https://download.gnome.org/sources/libgda/6.0/%{_name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM libgda-javadetection-biarch.patch bgo#673560 -- Prepare getsp to be sed'ed for biarch
Patch1:         libgda-javadetection-biarch.patch

BuildRequires:  meson
BuildRequires:  db-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool >= 0.40.6
BuildRequires:  itstool
BuildRequires:  java-devel >= 1.8
BuildRequires:  libgcrypt-devel
BuildRequires:  libopenssl-1_1-devel
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
BuildRequires:  vala >= 0.26.0
BuildRequires:  yelp-tools
BuildRequires:  gtk-doc
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(sqlcipher)
%if %{with fbclient}
BuildRequires:  pkgconfig(fbclient)
%endif
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
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:  pkgconfig(libmariadb)
#!BuildIgnore:  openssl

%description
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package -n glade-catalog-libgda
Summary:        Glade catalog for libgda
Group:          Development/Tools/GUI Builders
Requires:       %{_name}-6_0 = %{version}
Requires:       glade
Supplements:    (glade and %{_name}-devel)

%description -n glade-catalog-libgda
This package provides a catalog for Glade, to allow the use the libgda
widgets in Glade.

%package 6_0-tools
Summary:        GNU Data Access (GDA) Library -- Tools
Group:          Productivity/Databases/Clients
Provides:       %{_name}-6_0 = %{version}
Obsoletes:      %{_name}-6_0 < %{version}

%description 6_0-tools
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

This package provides command-line tools for libgda.

%package -n libgda-ui-6_0-tools
Summary:        GNU Data Access (GDA) Library -- Graphical Tools
Group:          Productivity/Databases/Clients
Supplements:    (%{_name}-6_0-tools and %{_name}-ui-6_0-6_0_0)

%description -n libgda-ui-6_0-tools
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

This package provides graphical tools:
  - gda-browser: a tool to browse databases
  - gda-control-center: configuration tool for libgda

%package -n libgda-6_0-6_0_0
Summary:        GNU Data Access (GDA) Library
Group:          System/Libraries
%if %{with bdb}
Recommends:     %{_name}-6_0-bdb = %{version}
%endif

%description -n libgda-6_0-6_0_0
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package -n typelib-1_0-Gda-6_0
Summary:        GNU Data Access (GDA) Library -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Gda-6_0
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

This package provides the GObject Introspection bindings for
libgda.

%package -n libgda-ui-6_0-6_0_0
Summary:        GNU Data Access (GDA) Library - UI Widgets
Group:          System/Libraries
Recommends:     iso-codes
Supplements:    (libgda-6_0-6_0_0 and gtk3)

%description -n libgda-ui-6_0-6_0_0
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package -n typelib-1_0-Gdaui-6_0
Summary:        GNU Data Access (GDA) Library - UI Widgets -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Gdaui-6_0
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

This package provides the GObject Introspection bindings for
libgda-ui.

%package -n libgda-ui-6_0-plugins
Summary:        GNU Data Access (GDA) Library - Plugins for UI Widgets
Group:          System/Libraries
Supplements:    %{_name}-ui-6_0-6_0_0

%description -n libgda-ui-6_0-plugins
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package -n libgda-report-6_0-6_0_0
Summary:        GNU Data Access (GDA) Library
Group:          System/Libraries

%description -n libgda-report-6_0-6_0_0
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package -n libgda-xslt-6_0-6_0_0
Summary:        GNU Data Access (GDA) Library
Group:          System/Libraries

%description -n libgda-xslt-6_0-6_0_0
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package 6_0-devel
Summary:        GNU Data Access (GDA) Library -- Development Files
Group:          Development/Libraries/C and C++
Requires:       %{_name}-6_0-6_0_0 = %{version}
Requires:       %{_name}-ui-6_0-6_0_0 = %{version}
Requires:       typelib-1_0-Gda-6_0 = %{version}
Requires:       typelib-1_0-Gdaui-6_0 = %{version}
# named libgda-devel on 10.3
Provides:       %{_name}-devel = %{version}
Obsoletes:      %{_name}-devel < %{version}

%description 6_0-devel
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

This package contains all necessary include files and libraries needed
to develop applications that require these.

%package 6_0-doc
Summary:        GNU Data Access (GDA) Library -- Developer Documentation
Group:          Development/Libraries/C and C++
Provides:       %{_name}-doc = %{version}
# named libgda-doc on 10.3
Obsoletes:      %{_name}-doc < %{version}

%description 6_0-doc
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%if %{with bdb}
%package 6_0-bdb
Summary:        Berkeley DB Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{_name}-6_0-6_0_0 = %{version}

%description 6_0-bdb
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.
%endif

%if %{with fbclient}
%package 6_0-firebird
Summary:        Firebird DB Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{_name}-6_0-6_0_0 = %{version}

%description 6_0-firebird
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.
%endif

%package 6_0-ldap
Summary:        LDAP Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{_name}-6_0-6_0_0 = %{version}
Supplements:    (libgda-6_0 and %(cd %{_libdir} ; rpm -qf --queryformat=%%{NAME} `readlink %{_libdir}/libldap.so` ))

%description 6_0-ldap
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package 6_0-mysql
Summary:        MySQL Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{_name}-6_0-6_0_0 = %{version}
Supplements:    (libgda-6_0 and %(cd %{_libdir} ; rpm -qf --queryformat=%%{NAME} `readlink %{_libdir}/libmysqlclient.so` ))
Provides:       %{_name}-mysql = %{version}
Obsoletes:      %{_name}-mysql < %{version}

%description 6_0-mysql
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package 6_0-postgres
Summary:        PostgreSQL Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{_name}-6_0-6_0_0 = %{version}
Supplements:    (libgda-6_0 and %(cd %{_libdir} ; rpm -qf --queryformat=%%{NAME} `readlink %{_libdir}/libpq.so` ))
Provides:       %{_name}-postgres = %{version}
Obsoletes:      %{_name}-postgres < %{version}

%description 6_0-postgres
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package 6_0-sqlcipher
Summary:        SQLCipher Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{_name}-6_0-6_0_0 = %{version}
Requires:       %{_name}-6_0-sqlite = %{version}
Enhances:       %{_name}-6_0-sqlite
Provides:       %{_name}-sqlcipher = %{version}

%description 6_0-sqlcipher
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%package 6_0-sqlite
Summary:        Sqlite Provider for GNU Data Access (GDA)
Group:          Productivity/Databases/Clients
Requires:       %{_name}-6_0-6_0_0 = %{version}
Supplements:    (libgda-6_0 and %(cd %{_libdir} ; rpm -qf --queryformat=%%{NAME} `readlink %{_libdir}/libsqlite3.so` ))
Provides:       %{_name}-sqlite = %{version}
Obsoletes:      %{_name}-sqlite < %{version}

%description 6_0-sqlite
GNU Data Access (GDA) is an attempt to provide uniform access to
different kinds of data sources (databases, information servers,
mail spools, etc). It is a complete architecture that provides
everything needed to access data.

%lang_package -n %{_name}-6_0-6_0_0

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
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
sed -e 's-mysqlclient-libmariadb-g' -i meson.build
%meson \
  -Dui=true \
  -Dexperimental=true \
  -Dldap=true \
  -Ddoc=true \
  -Dtools=true \
  %{nil}
%meson_build

%install
# remove error about java bytecode being for something later than java 1.15 -- see http://en.opensuse.org/Java/Packaging/Cookbook
export NO_BRP_CHECK_BYTECODE_VERSION=true
%meson_install
# X-SuSE-Design is just to make the brp check happy...
%suse_update_desktop_file org.gnome.gda.Browser X-SuSE-Design
mv %{buildroot}%{_mandir}/man1/gda-sql.1* %{buildroot}%{_mandir}/man1/gda-sql-6.0.1*
sed -e 's-#!/usr/bin/env python3-#!/usr/bin/python3-g' -i %{buildroot}%{_bindir}/t*
%find_lang libgda-6.0 %{?no_lang_C}
%fdupes %{buildroot}%{_prefix}

%post -n libgda-6_0-6_0_0 -p /sbin/ldconfig
%postun -n libgda-6_0-6_0_0 -p /sbin/ldconfig
%post -n libgda-ui-6_0-6_0_0 -p /sbin/ldconfig
%postun -n libgda-ui-6_0-6_0_0 -p /sbin/ldconfig
%post -n libgda-report-6_0-6_0_0 -p /sbin/ldconfig
%postun -n libgda-report-6_0-6_0_0 -p /sbin/ldconfig
%post -n libgda-xslt-6_0-6_0_0 -p /sbin/ldconfig
%postun -n libgda-xslt-6_0-6_0_0 -p /sbin/ldconfig

%files -n libgda-6_0-6_0_0-lang -f libgda-6.0.lang

%files -n glade-catalog-libgda
%{_datadir}/glade/catalogs/*
%{_datadir}/glade/pixmaps/*

%files 6_0-tools
# NOTE: Even if it was probably intended by upstream to be in sync with
# the libgda soname, naming scheme is different (5_0-4 for soname, 5_0
# for data files). To be on the safe side, package it separately.
# This package contains only files with "5.0" in its name or path.
%license COPYING
%doc %{_datadir}/libgda-6.0/gda-sql
%{_bindir}/gda-list-config-6.0
%{_bindir}/gda-list-server-op-6.0
%{_bindir}/gda-sql-6.0
%{_mandir}/man1/gda-sql-6.0.1*
# in report-5_0-4
%exclude %{_datadir}/libgda-6.0/gda_trml2html
%exclude %{_datadir}/libgda-6.0/gda_trml2pdf

%files -n libgda-ui-6_0-tools
# gda-browser
%{_bindir}/org.gnome.gda.Browser
%{_datadir}/metainfo/org.gnome.gda.Browser.appdata.xml
%{_datadir}/applications/org.gnome.gda.Browser.desktop
%{_datadir}/pixmaps/org.gnome.gda.Browser.png
%{_datadir}/icons/hicolor/512x512/apps/org.gnome.gda.Browser.png
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.gda.Browser.svg
# gda-control-center
%{_bindir}/gda-control-center-6.0

%files -n libgda-6_0-6_0_0
%license COPYING.LIB
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libgda-6.0.so.*
%dir %{_datadir}/libgda-6.0
%dir %{_datadir}/libgda-6.0/dtd
%{_datadir}/libgda-6.0/information_schema.xml
%{_datadir}/libgda-6.0/dtd/libgda-*.dtd
%dir %{_libdir}/libgda-6.0
%dir %{_libdir}/libgda-6.0/plugins
%dir %{_libdir}/libgda-6.0/providers

%files -n typelib-1_0-Gda-6_0
%{_libdir}/girepository-1.0/Gda-6.0.typelib

%files -n libgda-ui-6_0-6_0_0
%dir %{_datadir}/libgda-6.0/ui
%{_datadir}/libgda-6.0/ui/gdaui-*
%{_libdir}/libgda-ui-6.0.so.*

%files -n typelib-1_0-Gdaui-6_0
%{_libdir}/girepository-1.0/Gdaui-6.0.typelib

%files -n libgda-ui-6_0-plugins
%{_libdir}/libgda-6.0/plugins/libgda-ui-plugins-libgda-6.0.so

%files -n libgda-report-6_0-6_0_0
# NOTE: This library has the same versioning policy, but depends on libgda-sqlite.
%{_datadir}/libgda-6.0/gda_trml2html
%{_datadir}/libgda-6.0/gda_trml2pdf
%{_bindir}/trml2html.py
%{_bindir}/trml2pdf.py
%{_libdir}/libgda-report-6.0.so.*

%files -n libgda-xslt-6_0-6_0_0
%{_libdir}/libgda-xslt-6.0.so.*

%files 6_0-devel
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_includedir}/libgda-6.0/
%{_libdir}/libgda-6.0.so
%{_libdir}/libgda-xslt-6.0.so
%{_libdir}/libgda-report-6.0.so
%{_libdir}/libgda-ui-6.0.so
%{_libdir}/pkgconfig/*-6.0.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/libgda-6.0.vapi
%{_datadir}/vala/vapi/libgda-6.0.deps
%{_datadir}/vala/vapi/libgdaui-6.0.vapi
# demo
%{_bindir}/org.gnome.gda.Demoui
%{_datadir}/libgda-6.0/demo/

%files 6_0-doc
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_datadir}/gtk-doc/html/libgdaui-6.0/
%{_datadir}/gtk-doc/html/libgda-6.0/

%if %{with bdb}
%files 6_0-bdb
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_libdir}/libgda-6.0/providers/libgda-bdb-6.0.so
%endif

%if %{with fbclient}
%files 6_0-firebird
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_libdir}/libgda-6.0/providers/libgda-firebird-client-6.0.so
%endif

%files 6_0-ldap
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_libdir}/libgda-6.0/providers/libgda-ldap-6.0.so

%files 6_0-mysql
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_libdir}/libgda-6.0/providers/libgda-mysql-6.0.so

%files 6_0-postgres
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_libdir}/libgda-6.0/providers/libgda-postgres-6.0.so

%files 6_0-sqlcipher
# NOTE: Files don't conflict with previous version => Use versioned package name
%license providers/sqlcipher/COPYING.sqlcipher
%{_libdir}/libgda-6.0/providers/libgda-sqlcipher-6.0.so

%files 6_0-sqlite
# NOTE: Files don't conflict with previous version => Use versioned package name
%{_libdir}/libgda-6.0/providers/libgda-sqlite-6.0.so


%changelog
