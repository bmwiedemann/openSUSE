#
# spec file for package gnome-calendar
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


Name:           gnome-calendar
Version:        40.0
Release:        0
Summary:        A calendar application for GNOME
License:        GPL-3.0-or-later
Group:          Productivity/Office/Organizers
URL:            https://wiki.gnome.org/Design/Apps/Calendar
Source0:        https://download.gnome.org/sources/gnome-calendar/40/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(geocode-glib-1.0) >= 3.23
BuildRequires:  pkgconfig(gio-2.0) >= 2.43.4
BuildRequires:  pkgconfig(glib-2.0) >= 2.43.4
BuildRequires:  pkgconfig(goa-1.0) >= 3.2.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.21.2
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.20
BuildRequires:  pkgconfig(gweather-3.0) >= 3.27.2
BuildRequires:  pkgconfig(libdazzle-1.0) >= 3.33.1
BuildRequires:  pkgconfig(libecal-2.0) >= 3.33.2
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.17.1
BuildRequires:  pkgconfig(libedataserverui-1.2) >= 3.17.1
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 2.4
BuildRequires:  pkgconfig(libhandy-1) >= 0.0.9
BuildRequires:  pkgconfig(libical) >= 3.0.5
BuildRequires:  pkgconfig(libsoup-2.4)

%description
Calendar is a calendar application for GNOME.

%package -n gnome-shell-search-provider-gnome-calendar
Summary:        GNOME Shell search provider to return results from the GNOME Calendar
Group:          Productivity/Office/Organizers
Requires:       %{name} = %{version}
Supplements:    packageand(gnome-shell:%{name})

%description -n gnome-shell-search-provider-gnome-calendar
This package contains a search provider to enable GNOME Shell to get
search results from GNOME Calendar.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dtracing=false \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

%check
%meson_test

%files
%license COPYING
%doc NEWS README.md TODO.md
%{_bindir}/gnome-calendar
%{_datadir}/applications/org.gnome.Calendar.desktop
# Own dir for openSUSE Leap 42.1
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.Calendar.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Calendar.service
%{_datadir}/glib-2.0/schemas/org.gnome.calendar.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.calendar.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.*

%files -n gnome-shell-search-provider-gnome-calendar
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Calendar.search-provider.ini

%files lang -f %{name}.lang

%changelog
