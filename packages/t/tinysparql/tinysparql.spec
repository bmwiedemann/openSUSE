#
# spec file for package tinysparql
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2010 Luis Medinas, Portugal
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


%define tinysparqlAPI    3.0
%define RPMtinysparqlAPI 3_0

Name:           tinysparql
Version:        3.8.2
Release:        0
Summary:        Object database, tag/metadata database, search tool and indexer
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://gitlab.gnome.org/GNOME/tinysparql
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  asciidoc
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel >= 2.52.0
BuildRequires:  gobject-introspection-devel
BuildRequires:  graphviz
BuildRequires:  intltool
BuildRequires:  libgupnp-dlna-devel >= 0.9.4
BuildRequires:  meson >= 0.53
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-gobject
BuildRequires:  sqlite3-devel >= 3.35.2
BuildRequires:  vala >= 0.18.0
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(icu-i18n) > 4.8.1.1
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.0
BuildRequires:  pkgconfig(libseccomp) >= 2.0
BuildRequires:  pkgconfig(libsoup-3.0) >= 2.99.2
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(upower-glib) >= 0.9.0
BuildRequires:  pkgconfig(uuid)
# We want to index files by default, if possible
#Recommends:     %{name}-miner-files
# gnome-panel-applet-tracker (aka tracker-search-bar) was removed with tracker 0.16.0
Obsoletes:      gnome-panel-applet-tracker < 0.16.0
# flickr miner was removed with tracker 0.16.0
Obsoletes:      tracker-miner-flickr < 0.16.0
# Removed with tracker 2.0
Obsoletes:      tracker-gui < 1.99.0
Obsoletes:      tracker-miner-evolution < 1.99.0
Obsoletes:      tracker-miner-firefox < 1.99.0
Obsoletes:      tracker-miner-thunderbird < 1.99.0
# Rename to tinysparql
Obsoletes:      tracker < 3.7.99
Provides:       tracker = %{version}

%description
tinysparql is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

It consists of a common object database that allows entities to
have an almost infinite number of properties, metadata (both
embedded/harvested as well as user definable), a comprehensive
database of keywords/tags and links to other entities.

It provides context linking and audit trails for file objects.
It has the ability to index, store, harvest metadata, retrieve
and search all types of files and other first class objects.

%package -n typelib-1_0-Tracker-%{RPMtinysparqlAPI}
Summary:        Introspection bindings for the tinysparql Sparql library
Group:          System/Libraries

%description -n typelib-1_0-Tracker-%{RPMtinysparqlAPI}
tinysparql is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

This package provides the GObject Introspection bindings for the
sparql library for tinysparql.

%package -n libtracker-sparql-%{RPMtinysparqlAPI}-0
Summary:        Sparql library for tinysparql
Group:          System/Libraries

%description -n libtracker-sparql-%{RPMtinysparqlAPI}-0
tinysparql is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

It consists of a common object database that allows entities to
have an almost infinite number of properties, metadata (both
embedded/harvested as well as user definable), a comprehensive
database of keywords/tags and links to other entities.

It provides context linking and audit trails for file objects.
It has the ability to index, store, harvest metadata, retrieve
and search all types of files and other first class objects.

%package devel
Summary:        Development files for the tinysparql indexer
Group:          Development/Libraries/GNOME
Requires:       libtracker-sparql-%{RPMtinysparqlAPI}-0 = %{version}
Requires:       typelib-1_0-Tracker-%{RPMtinysparqlAPI} = %{version}
# Rename to tinysparql
Obsoletes:      tracker-devel < 3.7.99

%description devel
tinysparql is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

This subpackage contains the headers to make use of its libraries.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Ddocs=true \
	-Dstemmer=disabled \
	%{nil}
%meson_build

#%%check
#%%meson_test

%install
%meson_install
%find_lang %{name}3 %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}/vala/

%ldconfig_scriptlets -n libtracker-sparql-%{RPMtinysparqlAPI}-0

%post
%systemd_user_post %{name}-xdg-portal-3.service

%preun
%systemd_user_preun %{name}-xdg-portal-3.service

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%dir %{_libdir}/%{name}-%{tinysparqlAPI}
%{_libdir}/%{name}-%{tinysparqlAPI}/libtracker-http-soup3.so
%{_libdir}/%{name}-%{tinysparqlAPI}/libtracker-parser-libicu.so
%{_libexecdir}/%{name}-sql
%{_libexecdir}/%{name}-xdg-portal-3
%{_mandir}/man1/tinysparql-endpoint.1%{ext_man}
%{_mandir}/man1/tinysparql-export.1%{ext_man}
%{_mandir}/man1/tinysparql-import.1%{ext_man}
%{_mandir}/man1/tinysparql-introspect.1%{ext_man}
%{_mandir}/man1/tinysparql-query.1%{ext_man}
%{_mandir}/man1/tinysparql-sql.1%{ext_man}
%{_mandir}/man1/tinysparql-xdg-portal-3.1%{ext_man}
%{_datadir}/dbus-1/services/org.freedesktop.portal.Tracker.service
%{_userunitdir}/%{name}-xdg-portal-3.service

%files -n libtracker-sparql-%{RPMtinysparqlAPI}-0
%{_libdir}/libtracker-sparql*.so.*
%{_libdir}/libtinysparql-*.so.*

%files -n typelib-1_0-Tracker-%{RPMtinysparqlAPI}
%{_libdir}/girepository-1.0/Tracker-%{tinysparqlAPI}.typelib
%{_libdir}/girepository-1.0/Tsparql-%{tinysparqlAPI}.typelib

%files devel
%doc AUTHORS README.md NEWS
%doc %{_datadir}/doc/Tsparql-%{tinysparqlAPI}
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi
%{_includedir}/%{name}-%{tinysparqlAPI}/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/tracker-sparql-%{tinysparqlAPI}.pc
%{_libdir}/pkgconfig/%{name}-%{tinysparqlAPI}.pc

%files lang -f %{name}3.lang

%changelog
