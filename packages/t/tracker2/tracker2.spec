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


%define TrackerAPI    2.0
%define RPMTrackerAPI 2_0

Name:           tracker2
%define _name   tracker
Version:        2.3.6
Release:        0
Summary:        Object database, tag/metadata database, search tool and indexer
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://wiki.gnome.org/Projects/Tracker
Source0:        https://download.gnome.org/sources/tracker/2.3/%{_name}-%{version}.tar.xz

# PATCH-FIX-UPSTREAM tracker-ontology-upgrades.patch boo#1170587 dimstar@opensuse.org -- Fix ontology migration from very old tracker versions
Patch1:         tracker-ontology-upgrades.patch

BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel >= 2.46.0
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libicu-devel >= 4.8.1.1
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  sqlite3-devel >= 3.8.3
BuildRequires:  translation-update-upstream
BuildRequires:  vala >= 0.18.0
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.0
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libseccomp) >= 2.0
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.40
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6
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
Provides:       tracker = %{version}
Obsoletes:      tracker <= %{version}
Obsoletes:      tracker-lang <= %{version}
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

# This package name is not correct as per SLPP, but the 'lib' lives in a
# private directory: the symbol provided is libtracker-common.so() (same
# name across multiple versions of tracker).
# Yet, different libtracker-miner-* packages require their explicit
# version of libtracker-common.so as they link is done using rpath.
%package -n libtracker-common-%{RPMTrackerAPI}
Summary:        Convenience libraries for Tracker
Group:          System/Libraries
Requires:       %{name}
# Obsolete old tracker libs, bnc#876649
Obsoletes:      libtracker-extract-0_16-0
# Obsolete tracker 1.0 - this is not a 'real' slpp package, thus can be obsoleted
Obsoletes:      libtracker-common-1_0

%description -n libtracker-common-%{RPMTrackerAPI}
Tracker is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

This package contains private convenience libraries for the
various tracker libraries.

%package -n libtracker-control-%{RPMTrackerAPI}-0
Summary:        Control library for Tracker
# rpm autodetects libtracker-common.so() symbol, which is provided by all versions of libtracker-common, so we need to help with an explicit Requires.
Group:          System/Libraries
Requires:       libtracker-common-%{RPMTrackerAPI}

%description -n libtracker-control-%{RPMTrackerAPI}-0
Tracker is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

It consists of a common object database that allows entities to
have an almost infinite number of properties, metadata (both
embedded/harvested as well as user definable), a comprehensive
database of keywords/tags and links to other entities.

It provides context linking and audit trails for file objects.
It has the ability to index, store, harvest metadata, retrieve
and search all types of files and other first class objects.

%package -n libtracker-miner-%{RPMTrackerAPI}-0
Summary:        Miner library for Tracker
# rpm autodetects libtracker-common.so() symbol, which is provided by all versions of libtracker-common, so we need to help with an explicit Requires.
Group:          System/Libraries
Requires:       libtracker-common-%{RPMTrackerAPI}

%description -n libtracker-miner-%{RPMTrackerAPI}-0
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

%package -n typelib-1_0-TrackerControl-%{RPMTrackerAPI}
Summary:        Introspection bindings for the Tracker Control library
Group:          System/Libraries

%description -n typelib-1_0-TrackerControl-%{RPMTrackerAPI}
Tracker is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

This package provides the GObject Introspection bindings for the
extract library for Tracker.

%package -n typelib-1_0-TrackerMiner-%{RPMTrackerAPI}
Summary:        Introspection bindings for the Tracker Miner library
Group:          System/Libraries

%description -n typelib-1_0-TrackerMiner-%{RPMTrackerAPI}
Tracker is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

This package provides the GObject Introspection bindings for the
miner library for Tracker.

%package -n libtracker-sparql-%{RPMTrackerAPI}-0
Summary:        Sparql library for Tracker
# rpm autodetects libtracker-common.so() symbol, which is provided by all versions of libtracker-common, so we need to help with an explicit Requires.
Group:          System/Libraries
Requires:       libtracker-common-%{RPMTrackerAPI}

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

%package devel
Summary:        Development files for the Tracker indexer
Group:          Development/Libraries/GNOME
Requires:       libtracker-control-%{RPMTrackerAPI}-0 = %{version}
Requires:       libtracker-miner-%{RPMTrackerAPI}-0 = %{version}
Requires:       libtracker-sparql-%{RPMTrackerAPI}-0 = %{version}
Requires:       typelib-1_0-Tracker-%{RPMTrackerAPI} = %{version}
Requires:       typelib-1_0-TrackerControl-%{RPMTrackerAPI} = %{version}
Requires:       typelib-1_0-TrackerMiner-%{RPMTrackerAPI} = %{version}
Provides:       tracker-devel = %{version}
Obsoletes:      tracker-devel <= %{version}

%description devel
Tracker is a desktop-neutral object database, tag/metadata database,
search tool and indexer.

This subpackage contains the headers to make use of its libraries.

%lang_package

%prep
%autosetup -p1 -n %{_name}-%{version}
translation-update-upstream po %{_name}

%build
%meson \
	-Ddocs=true \
	-Dfunctional_tests=false \
	-Dstemmer=disabled \
	-Dsystemd_user_services=%{_userunitdir}
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{_name} %{?no_lang_C}

# Ensure we have a /usr/share/tracker/icons/ folder, so the
# tracker-extras build can put icons in there without having to worry
mkdir -p %{buildroot}%{_datadir}/tracker/icons/

%fdupes %{buildroot}%{_datadir}/vala/
%fdupes %{buildroot}%{_datadir}/gtk-doc
rm -f %{buildroot}%{_libdir}/tracker-%{TrackerAPI}/libtracker-common.a

%ifnarch %arm
%check
%meson_test
%endif

%post -n libtracker-control-%{RPMTrackerAPI}-0 -p /sbin/ldconfig
%postun -n libtracker-control-%{RPMTrackerAPI}-0 -p /sbin/ldconfig
%post -n libtracker-miner-%{RPMTrackerAPI}-0 -p /sbin/ldconfig
%postun -n libtracker-miner-%{RPMTrackerAPI}-0 -p /sbin/ldconfig
%post -n libtracker-sparql-%{RPMTrackerAPI}-0 -p /sbin/ldconfig
%postun -n libtracker-sparql-%{RPMTrackerAPI}-0 -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/tracker
%{_libexecdir}/tracker-store
%{_userunitdir}/tracker-store.service
%dir %{_libdir}/tracker-%{TrackerAPI}/
%{_datadir}/bash-completion/completions/tracker
%{_datadir}/tracker/
%{_datadir}/dbus-1/services/org.freedesktop.Tracker1.service
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.DB.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.FTS.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.Store.gschema.xml
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.gschema.xml
%{_mandir}/man1/tracker-daemon.1%{ext_man}
%{_mandir}/man1/tracker-export.1%{ext_man}
%{_mandir}/man1/tracker-index.1%{ext_man}
%{_mandir}/man1/tracker-info.1%{ext_man}
%{_mandir}/man1/tracker-reset.1%{ext_man}
%{_mandir}/man1/tracker-search.1%{ext_man}
%{_mandir}/man1/tracker-sparql.1%{ext_man}
%{_mandir}/man1/tracker-sql.1%{ext_man}
%{_mandir}/man1/tracker-status.1%{ext_man}
%{_mandir}/man1/tracker-store.1%{ext_man}
%{_mandir}/man1/tracker-tag.1%{ext_man}

%files -n libtracker-common-%{RPMTrackerAPI}
%{_libdir}/tracker-%{TrackerAPI}/libtracker-data.so
%{_datadir}/glib-2.0/schemas/org.freedesktop.Tracker.enums.xml

%files -n libtracker-control-%{RPMTrackerAPI}-0
%{_libdir}/libtracker-control*.so.*

%files -n libtracker-miner-%{RPMTrackerAPI}-0
%{_libdir}/libtracker-miner*.so.*

%files -n libtracker-sparql-%{RPMTrackerAPI}-0
%{_libdir}/libtracker-sparql*.so.*

%files -n typelib-1_0-Tracker-%{RPMTrackerAPI}
%{_libdir}/girepository-1.0/Tracker-%{TrackerAPI}.typelib

%files -n typelib-1_0-TrackerControl-%{RPMTrackerAPI}
%{_libdir}/girepository-1.0/TrackerControl-%{TrackerAPI}.typelib

%files -n typelib-1_0-TrackerMiner-%{RPMTrackerAPI}
%{_libdir}/girepository-1.0/TrackerMiner-%{TrackerAPI}.typelib

%files devel
%doc AUTHORS README.md NEWS
%{_libdir}/lib*.so
%{_libdir}/tracker-%{TrackerAPI}/trackertestutils
%{_includedir}/tracker-%{TrackerAPI}/
%{_libdir}/pkgconfig/tracker-control-%{TrackerAPI}.pc
%{_libdir}/pkgconfig/tracker-miner-%{TrackerAPI}.pc
%{_libdir}/pkgconfig/tracker-sparql-%{TrackerAPI}.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libtracker-miner/
%{_datadir}/gtk-doc/html/libtracker-control/
%{_datadir}/gtk-doc/html/ontology/
%{_datadir}/gtk-doc/html/libtracker-sparql/
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi

%files lang -f %{_name}.lang

%changelog
