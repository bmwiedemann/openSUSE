#
# spec file for package gnome-weather
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


%define _name org.gnome.Weather
Name:           gnome-weather
Version:        3.32.2
Release:        0
Summary:        Weather App for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://live.gnome.org/Design/Apps/Weather
Source0:        https://download.gnome.org/sources/gnome-weather/3.32/%{name}-%{version}.tar.xz

BuildRequires:  intltool >= 0.26
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gjs-1.0) >= 1.50.0
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(gweather-3.0) >= 3.25.91
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 2.3.1
Recommends:     %{name}-lang
BuildArch:      noarch

%description
GNOME 3 weather app that does:
* display current conditions
* display forecasts
* show radar maps
* notify on hazardous weather conditions

%package -n gnome-shell-search-provider-gnome-weather
Summary:        GNOME Weather -- Search Provider for GNOME Shell
Group:          Productivity/Other
Requires:       %{name} = %{version}
Supplements:    packageand(gnome-shell:%{name})

%description -n gnome-shell-search-provider-gnome-weather
This package contains a search provider to enable GNOME Shell to get
search results from GNOME Weather.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file %{_name} Utility DesktopUtility
%find_lang %{_name} %{?no_lang_C} %{name}.lang

%files
%license COPYING.md
%{_bindir}/%{name}
%{_datadir}/metainfo/org.gnome.Weather.appdata.xml
%{_datadir}/applications/org.gnome.Weather.desktop
%{_datadir}/%{_name}/
%{_datadir}/dbus-1/services/org.gnome.Weather.service
%{_datadir}/dbus-1/services/org.gnome.Weather.BackgroundService.service
%{_datadir}/glib-2.0/schemas/org.gnome.Weather.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{_name}*

%files -n gnome-shell-search-provider-gnome-weather
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Weather.search-provider.ini

%files lang -f %{name}.lang

%changelog
