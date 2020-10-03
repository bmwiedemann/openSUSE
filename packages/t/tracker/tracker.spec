#
# spec file for package tracker
#
# Copyright (c) 2020 SUSE LLC
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


%define TrackerAPI    3.0
%define RPMTrackerAPI 3_0

Name:           tracker
Version:        3.0.0
Release:        0
Summary:        Object database, tag/metadata database, search tool and indexer
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://wiki.gnome.org/Projects/Tracker
Source0:        https://download.gnome.org/sources/tracker/3.0/%{name}-%{version}.tar.xz

BuildRequires:  asciidoc
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel >= 2.52.0
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libicu-devel >= 4.8.1.1
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  sqlite3-devel >= 3.15.0
BuildRequires:  translation-update-upstream
BuildRequires:  vala >= 0.18.0
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.0
BuildRequires:  pkgconfig(libseccomp) >= 2.0
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.40
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(upower-glib) >= 0.9.0
BuildRequires:  pkgconfig(uuid)
# We want to index files by default, if possible
Recommends:     %{name}-miner-files
# gnome-panel-applet-tracker (aka tracker-search-bar) was removed with tracker 0.16.0
Obsoletes:      gnome-panel-applet-tracker < 0.16.0
# flickr miner was removed with tracker 0.16.0
Obsoletes:      tracker-miner-flickr < 0.16.0
# Removed with tracker 2.0
Obsoletes:      tracker-gui < 1.99.0
Obsoletes:      tracker-miner-evolution < 1.99.0
Obsoletes:      tracker-miner-firefox < 1.99.0
Obsoletes:      tracker-miner-thunderbird < 1.99.0
BuildRequires:  libgupnp-dlna-devel >= 0.9.4

%description
Tracker is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

It consists of a common object database that allows entities to
have an almost infinite number of properties, metadata (both
embedded/harvested as well as user definable), a comprehensive
database of keywords/tags and links to other entities.

It provides context linking and audit trails for file objects.
It has the ability to index, store, harvest metadata, retrieve
and search all types of files and other first class objects.

%package -n typelib-1_0-Tracker-%{RPMTrackerAPI}
Summary:        Introspection bindings for the Tracker Sparql library
Group:          System/Libraries

%description -n typelib-1_0-Tracker-%{RPMTrackerAPI}
Tracker is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

This package provides the GObject Introspection bindings for the
sparql library for Tracker.

%package -n libtracker-sparql-%{RPMTrackerAPI}-0
Summary:        Sparql library for Tracker
Group:          System/Libraries

%description -n libtracker-sparql-%{RPMTrackerAPI}-0
Tracker is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

It consists of a common object database that allows entities to
have an almost infinite number of properties, metadata (both
embedded/harvested as well as user definable), a comprehensive
database of keywords/tags and links to other entities.

It provides context linking and audit trails for file objects.
It has the ability to index, store, harvest metadata, retrieve
and search all types of files and other first class objects.

%package -n tracker-devel
Summary:        Development files for the Tracker indexer
Group:          Development/Libraries/GNOME
Requires:       libtracker-sparql-%{RPMTrackerAPI}-0 = %{version}
Requires:       typelib-1_0-Tracker-%{RPMTrackerAPI} = %{version}

%description -n tracker-devel
Tracker is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

This subpackage contains the headers to make use of its libraries.

%lang_package

%prep
%autosetup -p1
translation-update-upstream po %{name}

%build
%meson \
	-Ddocs=true \
	-Dfunctional_tests=false \
	-Dstemmer=disabled \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}3 %{?no_lang_C}

# Ensure we have a /usr/share/tracker/icons/ folder, so the
# tracker-extras build can put icons in there without having to worry
mkdir -p %{buildroot}%{_datadir}/tracker/icons/
# Let's package the template directory where consumers can put their ontology files
mkdir %{buildroot}%{_datadir}/tracker3/domain-ontologies

%fdupes %{buildroot}%{_datadir}/vala/
%fdupes %{buildroot}%{_datadir}/gtk-doc

#ifnarch %arm
#check
#meson_test
#endif

%post -n libtracker-sparql-%{RPMTrackerAPI}-0 -p /sbin/ldconfig
%postun -n libtracker-sparql-%{RPMTrackerAPI}-0 -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/tracker3
%dir %{_libdir}/tracker-%{TrackerAPI}/
%{_datadir}/bash-completion/completions/tracker3
%{_datadir}/tracker3/
%dir %{_datadir}/tracker3/domain-ontologies
%{_libexecdir}/tracker3/
%{_libexecdir}/tracker-xdg-portal-3
%{_mandir}/man1/tracker3-endpoint.1.gz
%{_mandir}/man1/tracker3-export.1.gz
%{_mandir}/man1/tracker3-import.1.gz
%{_mandir}/man1/tracker3-sparql.1.gz
%{_mandir}/man1/tracker3-sql.1.gz
%{_mandir}/man1/tracker-xdg-portal-3.1.gz
%{_datadir}/dbus-1/services/org.freedesktop.portal.Tracker.service
%{_userunitdir}/tracker-xdg-portal-3.service

%files -n libtracker-sparql-%{RPMTrackerAPI}-0
%{_libdir}/libtracker-sparql*.so.*

%files -n typelib-1_0-Tracker-%{RPMTrackerAPI}
%{_libdir}/girepository-1.0/Tracker-%{TrackerAPI}.typelib

%files -n tracker-devel
%doc AUTHORS README.md NEWS
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libtracker-sparql-3/
%{_datadir}/gtk-doc/html/ontology-3/
%dir %{_datadir}/tracker3
%dir %{_datadir}/tracker3/domain-ontologies
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi
%{_includedir}/tracker-%{TrackerAPI}/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/tracker-sparql-%{TrackerAPI}.pc
%{_libdir}/pkgconfig/tracker-testutils-%{TrackerAPI}.pc
%{_libdir}/tracker-%{TrackerAPI}/trackertestutils

%files lang -f %{name}3.lang

%changelog
