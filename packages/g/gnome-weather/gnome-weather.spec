#
# spec file for package gnome-weather
#
# Copyright (c) 2023 SUSE LLC
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


%define full_name org.gnome.Weather
Name:           gnome-weather
Version:        44.0
Release:        0
Summary:        Weather App for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://apps.gnome.org/app/org.gnome.Weather
Source0:        https://download.gnome.org/sources/gnome-weather/44/%{name}-%{version}.tar.xz

# PATCH-FIX-UPSTREAM gnome-weather-BackgroundService-service-fails-to-start.patch bsc#1209391 glgo#GNOME/gnome-weather!132 xwang@suse.com -- org.gnome.Weather.BackgroundService fails to start
Patch0:         gnome-weather-BackgroundService-service-fails-to-start.patch

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  intltool >= 0.26
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gjs-1.0) >= 1.71.0
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 2.3.1
BuildArch:      noarch

%description
GNOME 3 weather app that does:

  * Display current conditions;
  * Display forecasts;
  * Show radar maps;
  * Notify on hazardous weather conditions.

%package -n gnome-shell-search-provider-gnome-weather
Summary:        GNOME Weather -- Search Provider for GNOME Shell
Group:          Productivity/Other
Requires:       %{name} = %{version}
Supplements:    (gnome-shell and %{name})

%description -n gnome-shell-search-provider-gnome-weather
This package contains a search provider to enable GNOME Shell to get
search results from GNOME Weather.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	--libdir=%{_prefix}/unused-in-noarch \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{full_name} %{?no_lang_C} %{name}.lang

%check
%meson_test

%files
%license COPYING.md
%doc NEWS README.md
%{_bindir}/%{name}
%{_datadir}/metainfo/org.gnome.Weather.appdata.xml
%{_datadir}/applications/org.gnome.Weather.desktop
%{_datadir}/%{full_name}/
%{_datadir}/dbus-1/services/org.gnome.Weather.service
%{_datadir}/dbus-1/services/org.gnome.Weather.BackgroundService.service
%{_datadir}/glib-2.0/schemas/org.gnome.Weather.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{full_name}*
%{_datadir}/icons/hicolor/scalable/status/*

%files -n gnome-shell-search-provider-gnome-weather
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Weather.search-provider.ini

%files lang -f %{name}.lang

%changelog
