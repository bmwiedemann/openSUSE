#
# spec file for package glom
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010 Dominique Leuenberger, Amsterdam, The Netherlands.
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


%define api    1.32
%define apiRPM 1_32
Name:           glom
Version:        1.31.6
Release:        0
Summary:        Database designer and user interface
# This is indeed GPL-3.0+, see http://git.gnome.org/browse/glom/commit/?id=6b16a90f8ea902d91db85656cc11c6a951d42ced
License:        GPL-3.0-or-later
Group:          Productivity/Databases/Clients
URL:            http://www.glom.org/
# FIXME: once bnc#793882 is fixed, re-enable %%check section
Source:         http://download.gnome.org/sources/glom/1.31/%{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  intltool
BuildRequires:  iso-codes-devel
BuildRequires:  itstool
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  postgresql-server
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(evince-view-3.0)
BuildRequires:  pkgconfig(gdkmm-3.0) >= 3.4.0
BuildRequires:  pkgconfig(giomm-2.4) >= 2.47.4
BuildRequires:  pkgconfig(glibmm-2.4) > 2.47.4
BuildRequires:  pkgconfig(goocanvas-2.0) >= 2.0.1
BuildRequires:  pkgconfig(goocanvasmm-2.0) >= 1.90.11
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.18.0
BuildRequires:  pkgconfig(gtksourceviewmm-3.0) >= 3.18.0
BuildRequires:  pkgconfig(libarchive) >= 3.0
BuildRequires:  pkgconfig(libepc-1.0) >= 0.4.0
BuildRequires:  pkgconfig(libgda-5.0) >= 5.2.1
BuildRequires:  pkgconfig(libgda-mysql-5.0)
BuildRequires:  pkgconfig(libgda-postgres-5.0)
BuildRequires:  pkgconfig(libgdamm-5.0) >= 4.99.10
BuildRequires:  pkgconfig(libxml++-3.0) >= 2.24.0
BuildRequires:  pkgconfig(libxslt) >= 1.1.10
BuildRequires:  pkgconfig(pygobject-3.0) >= 2.29.0
BuildRequires:  pkgconfig(sigc++-2.0) >= 2.9.2
# libgda-5_0-postgres is required to be able to start glom (bnc#772551)
Requires:       libgda-5_0-postgres
# For pg_dump/pg_restore, needed by Export Backup and Restore Backup menu items
Requires:       postgresql
# This is unfortunately needed for now, should get fixed upstream at some point
Requires:       postgresql-server
# python-glom is a hard requirement to launch glom (bnc#772551)
Requires:       python3-glom
# Glom verifies fot gi.repository.Gda Python Module (bnc#772551)
Requires:       typelib(Gda)
Recommends:     %{name}-lang
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_python3-devel
%else
BuildRequires:  boost-devel
%endif

%description
With Glom you can design database systems - the database and the user
interface.

    * Glom has high-level features such as relationships, lookups,
      related fields, related records, calculated fields, drop-down
      choices, searching, reports, users and groups.
    * Glom keeps things simple. It has Numeric, Text, Date, Time,
      Boolean, and Image field types.
    * Glom systems require almost no programming, but you may use
      Python for calculated fields or buttons.
    * Each Glom system can be translated for multiple languages and
      countries.

%package -n lib%{name}-devel
Summary:        Database designer and user interface - Development files
Group:          Development/Libraries/C and C++
Requires:       glibmm2-devel
Requires:       lib%{name}-%{apiRPM}-0 = %{version}
Requires:       libgdamm-devel

%description -n lib%{name}-devel
With Glom you can design database systems - the database and the user
interface.

    * Glom has high-level features such as relationships, lookups,
      related fields, related records, calculated fields, drop-down
      choices, searching, reports, users and groups.
    * Glom keeps things simple. It has Numeric, Text, Date, Time,
      Boolean, and Image field types.
    * Glom systems require almost no programming, but you may use
      Python for calculated fields or buttons.
    * Each Glom system can be translated for multiple languages and
      countries.

This package contains development files to create extensions for glom.

%package -n lib%{name}-%{apiRPM}-0
Summary:        Database designer and user interface - Library
Group:          System/Libraries

%description -n lib%{name}-%{apiRPM}-0
With Glom you can design database systems - the database and the user
interface.

    * Glom has high-level features such as relationships, lookups,
      related fields, related records, calculated fields, drop-down
      choices, searching, reports, users and groups.
    * Glom keeps things simple. It has Numeric, Text, Date, Time,
      Boolean, and Image field types.
    * Glom systems require almost no programming, but you may use
      Python for calculated fields or buttons.
    * Each Glom system can be translated for multiple languages and
      countries.

%package -n python3-%{name}
Summary:        Database designer and user interface - Python bindings
# Automatically trigger installation if we have python3 and glom installed.
Group:          Development/Languages/Python
Supplements:    packageand(glom:python3)
Obsoletes:      python-glom

%description -n python3-%{name}
With Glom you can design database systems - the database and the user
interface.

    * Glom has high-level features such as relationships, lookups,
      related fields, related records, calculated fields, drop-down
      choices, searching, reports, users and groups.
    * Glom keeps things simple. It has Numeric, Text, Date, Time,
      Boolean, and Image field types.
    * Glom systems require almost no programming, but you may use
      Python for calculated fields or buttons.
    * Each Glom system can be translated for multiple languages and
      countries.

%lang_package

%prep
%setup -q

%build
%configure \
          PYTHON_VERSION="%{python3_version}" \
          PYTHON=python3 \
          --disable-static \
          --disable-dependency-tracking \
          --disable-update-mime-database \
          --disable-documentation \
          --enable-ui-tests \
          --with-postgres-utils=%{_bindir}
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file %{name}
%find_lang %{name} %{?no_lang_C}

%if 0
# disabled until bnc#793882 is fixed
%check
make %{?_smp_mflags} check
%endif

%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%post -n lib%{name}-%{apiRPM}-0 -p /sbin/ldconfig
%postun -n lib%{name}-%{apiRPM}-0 -p /sbin/ldconfig

%files
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_bindir}/glom_create_from_example
%{_bindir}/glom_export_po
%{_bindir}/glom_export_po_all
%{_bindir}/glom_import_po_all
%{_bindir}/glom_test_connection
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%dir %{_datadir}/appdata/
%{_datadir}/appdata/glom.appdata.xml

%files -n lib%{name}-devel
%{_includedir}/%{name}-%{api}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc

%files -n lib%{name}-%{apiRPM}-0
%{_libdir}/*.so.*

%files -n python3-%{name}
%{python3_sitearch}/*.so

%files lang -f %{name}.lang

%changelog
