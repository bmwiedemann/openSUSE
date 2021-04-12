#
# spec file for package folks
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


%define soversion      25
%define module_version 46
%define with_telepathy  1
%define with_tracker    0
%define with_zeitgeist  0
Name:           folks
Version:        0.14.0
Release:        0
Summary:        Library to create metacontacts from multiple sources
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://telepathy.freedesktop.org/wiki/Folks
Source:         https://download.gnome.org/sources/folks/0.14/%{name}-%{version}.tar.xz
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson >= 0.49
BuildRequires:  pkgconfig
BuildRequires:  python3-dbusmock
BuildRequires:  readline-devel
BuildRequires:  vala >= 0.22.0.28
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.6
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44.0
BuildRequires:  pkgconfig(libebook-1.2) >= 3.13.90
BuildRequires:  pkgconfig(libebook-contacts-1.2) >= 3.7.90
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.33.2
BuildRequires:  pkgconfig(libxml-2.0)
%if %{with_telepathy}
BuildRequires:  pkgconfig(telepathy-glib) >= 0.19.9
%endif
%if %{with_tracker}
BuildRequires:  pkgconfig(tracker-sparql-2.0)
%endif
%if %{with_zeitgeist}
BuildRequires:  pkgconfig(zeitgeist-2.0) >= 0.9.14
%endif
Requires:       python3-dbusmock

%description
libfolks is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers) to create metacontacts.

%package -n libfolks%{soversion}
Summary:        Library to create metacontacts from multiple sources
# To make lang package installable
# We assume that future -data packages remain backwards compatible
Group:          System/Libraries
Requires:       folks-data >= %{version}
Provides:       %{name} = %{version}

%description -n libfolks%{soversion}
libfolks is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers) to create metacontacts.

%package data
Summary:        Data files for libfolks, a library to create metacontacts from many sources
Group:          System/Libraries
%glib2_gsettings_schema_requires
Obsoletes:      libfolks-data < %{version}
Provides:       libfolks-data = %{version}

%description data
libfolks is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers) to create metacontacts.

This package provides mandatory data files for the library to work.

%package -n typelib-1_0-Folks-0_6
Summary:        Introspection bindings for libfolks
Group:          System/Libraries

%description -n typelib-1_0-Folks-0_6
libfolks is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers) to create metacontacts.

This package provides the GObject Introspection bindings for libfolks.

%package -n typelib-1_0-FolksEds-0_6
Summary:        Introspection bindings for libfolks-eds
Group:          System/Libraries

%description -n typelib-1_0-FolksEds-0_6
libfolks is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers) to create metacontacts.

This package provides the GObject Introspection bindings for libfolks.

%package -n typelib-1_0-FolksTelepathy-0_6
Summary:        Introspection bindings for libfolks-telepathy
Group:          System/Libraries

%description -n typelib-1_0-FolksTelepathy-0_6
libfolks is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers) to create metacontacts.

This package provides the GObject Introspection bindings for libfolks.

%package -n typelib-1_0-FolksTracker-0_6
Summary:        Introspection bindings for libfolks-tracker
Group:          System/Libraries

%description -n typelib-1_0-FolksTracker-0_6
libfolks is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers) to create metacontacts.

This package provides the GObject Introspection bindings for libfolks.

%package -n libfolks-eds%{soversion}
Summary:        Evolution Data Server backend for libfolks
Group:          System/Libraries
Supplements:    packageand(libfolks%{soversion}:evolution-data-server)

%description -n libfolks-eds%{soversion}
libfolks is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers) to create metacontacts.

%package -n libfolks-tracker%{soversion}
Summary:        Tracker backend for libfolks
Group:          System/Libraries
Supplements:    packageand(libfolks%{soversion}:libtracker-sparql-1_0-0)

%description -n libfolks-tracker%{soversion}
libfolks is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers) to create metacontacts.

%package -n libfolks-telepathy%{soversion}
Summary:        Telepathy backend for libfolks
Group:          System/Libraries

%description -n libfolks-telepathy%{soversion}
libfolks is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers) to create metacontacts.

%package tools
Summary:        Additional utilities related to libfolks
# the folks-import tool is useful for old pidgin users
Group:          Development/Libraries/GNOME
Supplements:    packageand(libfolks1:pidgin)

%description tools
libfolks is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers) to create metacontacts.

This package provides tools based on libfolks, like an importer for Pidgin
metacontacts.

%package devel
Summary:        Development files for libfolks
Group:          Development/Libraries/GNOME
Requires:       libfolks%{soversion} = %{version}
Requires:       libfolks-eds%{soversion} = %{version}
%if %{with_telepathy}
Requires:       libfolks-telepathy%{soversion} = %{version}
%endif
Requires:       typelib-1_0-Folks-0_6 = %{version}
Requires:       typelib-1_0-FolksEds-0_6 = %{version}
Requires:       typelib-1_0-FolksTelepathy-0_6 = %{version}
%if %{with_tracker}
Requires:       libfolks-tracker%{soversion} = %{version}
Requires:       typelib-1_0-FolksTracker-0_6 = %{version}
%endif

%description devel
libfolks is a library that aggregates people from multiple sources (e.g.
Telepathy connection managers) to create metacontacts.

This package provides the development files.

%lang_package

%prep
%autosetup -p1

%build
%define _lto_cflags %{nil}
%meson \
%if %{with_tracker}
	-Dtracker_backend=true \
%endif
%if %{with_zeitgeist}
	-Dzeitgeist=true \
%endif
%if ! %{with_telepathy}
        -Dtelepathy_backend=false \
%endif
	%{nil}
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print
# We don't need the gconf -> gsettings convesion tool anymore
# it was not installed in the previous versions and did not
# cause bug reports.
rm %{buildroot}/usr/share/GConf/gsettings/folks.convert
%find_lang folks %{?no_lang_C}

%post -n libfolks%{soversion} -p /sbin/ldconfig
%postun -n libfolks%{soversion} -p /sbin/ldconfig

%post -n libfolks-eds%{soversion} -p /sbin/ldconfig
%postun -n libfolks-eds%{soversion} -p /sbin/ldconfig

%post -n libfolks-tracker%{soversion} -p /sbin/ldconfig
%postun -n libfolks-tracker%{soversion} -p /sbin/ldconfig

%post -n libfolks-telepathy%{soversion} -p /sbin/ldconfig
%postun -n libfolks-telepathy%{soversion} -p /sbin/ldconfig

%files -n libfolks%{soversion}
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libfolks.so.%{soversion}*
%{_libdir}/libfolks-dummy.so.%{soversion}*
%dir %{_libdir}/folks
%dir %{_libdir}/folks/%{module_version}
%dir %{_libdir}/folks/%{module_version}/backends
%{_libdir}/folks/%{module_version}/backends/bluez/
%{_libdir}/folks/%{module_version}/backends/dummy/
%{_libdir}/folks/%{module_version}/backends/key-file/
%{_libdir}/folks/%{module_version}/backends/ofono/

%files data
%{_datadir}/glib-2.0/schemas/org.freedesktop.folks.gschema.xml

%files -n typelib-1_0-Folks-0_6
%{_libdir}/girepository-1.0/Folks-0.6.typelib
%{_libdir}/girepository-1.0/FolksDummy-0.6.typelib

%files -n typelib-1_0-FolksEds-0_6
%{_libdir}/girepository-1.0/FolksEds-0.6.typelib

%files -n libfolks-eds%{soversion}
%{_libdir}/libfolks-eds.so.%{soversion}*
%dir %{_libdir}/folks/%{module_version}/backends/eds
%{_libdir}/folks/%{module_version}/backends/eds/eds.so

%if %{with_telepathy}
%files -n typelib-1_0-FolksTelepathy-0_6
%{_libdir}/girepository-1.0/FolksTelepathy-0.6.typelib

%files -n libfolks-telepathy%{soversion}
%{_libdir}/libfolks-telepathy.so.%{soversion}*
%dir %{_libdir}/folks/%{module_version}/backends/telepathy
%{_libdir}/folks/%{module_version}/backends/telepathy/telepathy.so
%endif

%if %{with_tracker}
%files -n typelib-1_0-FolksTracker-0_6
%{_libdir}/girepository-1.0/FolksTracker-0.6.typelib

%files -n libfolks-tracker%{soversion}
%{_libdir}/libfolks-tracker.so.%{soversion}*
%dir %{_libdir}/folks/%{module_version}/backends/tracker
%{_libdir}/folks/%{module_version}/backends/tracker/tracker.so
%endif

%files tools
%{_bindir}/folks-import
%{_bindir}/folks-inspect

%files devel
%{_includedir}/folks/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/Folks-0.6.gir
%{_datadir}/gir-1.0/FolksDummy-0.6.gir
%{_datadir}/gir-1.0/FolksEds-0.6.gir
%if %{with_telepathy}
%{_datadir}/gir-1.0/FolksTelepathy-0.6.gir
%{_datadir}/vala/vapi/folks-telepathy.*
%endif
%if %{with_tracker}
%{_datadir}/gir-1.0/FolksTracker-0.6.gir
%{_datadir}/vala/vapi/folks-tracker.*
%endif
%{_datadir}/vala/vapi/folks.*
%{_datadir}/vala/vapi/folks-dummy.*
%{_datadir}/vala/vapi/folks-eds.*

%files lang -f %{name}.lang

%changelog
