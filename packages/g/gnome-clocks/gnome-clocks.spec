#
# spec file for package gnome-clocks
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012 Dominique Leuenberger, Amsterdam, The Netherlands.
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


Name:           gnome-clocks
Version:        3.36.2
Release:        0
Summary:        Clock application designed for GNOME 3
License:        GPL-2.0-or-later
Group:          Productivity/Office/Other
URL:            https://live.gnome.org/Design/Apps/Clock
Source0:        https://download.gnome.org/sources/gnome-clocks/3.36/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  vala >= 0.23.3
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(geocode-glib-1.0) >= 1.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.58
BuildRequires:  pkgconfig(glib-2.0) >= 2.58
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.8
BuildRequires:  pkgconfig(gobject-2.0) >= 2.58
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsound) >= 0.98
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(gweather-3.0) >= 3.32.0
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 2.4
BuildRequires:  pkgconfig(libhandy-0.0) >= 0.0.10

%description
A nice simple app to show the time, date, and alarms.

%package -n gnome-shell-search-provider-gnome-clocks
Summary:        GNOME Clocks -- Search Provider for GNOME Shell
Group:          Productivity/Office/Other
Requires:       %{name} = %{version}
Supplements:    packageand(gnome-shell:%{name})

%description -n gnome-shell-search-provider-gnome-clocks
This package contains a search provider to enable GNOME Shell to get
search results from GNOME Clocks.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_datadir}

%files
%license LICENSE.md
%doc README.md NEWS.md
%doc %{_datadir}/help/C/gnome-clocks/
%{_bindir}/%{name}
%{_datadir}/metainfo/org.gnome.clocks.metainfo.xml
%{_datadir}/dbus-1/services/org.gnome.clocks.service
%{_datadir}/glib-2.0/schemas/org.gnome.clocks.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.clocks*
%{_datadir}/applications/org.gnome.clocks.desktop

%files -n gnome-shell-search-provider-gnome-clocks
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.clocks.search-provider.ini

%files lang -f %{name}.lang

%changelog
