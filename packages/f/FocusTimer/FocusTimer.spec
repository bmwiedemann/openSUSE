#
# spec file for package FocusTimer
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global __requires_exclude typelib\\(Meta\\)
Name:           FocusTimer
Version:        1.1.4
Release:        0
Summary:        A time management utility for GNOME
License:        GPL-3.0-or-later
Group:          Productivity/Office/Other
URL:            https://github.com/focustimerhq/FocusTimer
Source:         https://github.com/focustimerhq/FocusTimer/archive/refs/tags/%{version}.tar.gz
BuildRequires:  (gnome-shell >= 46 with gnome-shell < 51)
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-utils
BuildRequires:  gettext-devel >= 0.19.6
BuildRequires:  meson >= 0.58.0
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.28
BuildRequires:  pkgconfig(appstream-glib) >= 0.7.3
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.10.1
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0.10
BuildRequires:  pkgconfig(gtk4) >= 4.18
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libpeas-2) >= 2.0.0
BuildRequires:  pkgconfig(sqlite3)
Requires:       (gnome-shell >= 46 with gnome-shell < 51)
Requires:       gstreamer
Requires:       gtk3 >= 3.20.0
Recommends:     gstreamer-plugins-base
Provides:       gnome-pomodoro = %{version}-%{release}
Obsoletes:      gnome-pomodoro < %{version}-%{release}

%description
A time management utility for GNOME based on the pomodoro technique.

%lang_package

%prep
%autosetup -p1 -n FocusTimer-%{version}

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang focus-timer %{?no_lang_C}

%check
%ldconfig_scriptlets

%files
%doc README.md NEWS
%license COPYING
%{_bindir}/focus-timer
%{_datadir}/applications/io.github.focustimerhq.FocusTimer.desktop
%{_datadir}/dbus-1/interfaces/io.github.focustimerhq.FocusTimer*.xml
%{_datadir}/dbus-1/services/io.github.focustimerhq.FocusTimer.service
%{_datadir}/focus-timer/
%{_datadir}/glib-2.0/schemas/io.github.focustimerhq.FocusTimer*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%dir %{_datadir}/knotifications6
%{_datadir}/knotifications6/io.github.focustimerhq.FocusTimer.notifyrc
%{_datadir}/metainfo/io.github.focustimerhq.FocusTimer.metainfo.xml

%files lang -f focus-timer.lang

%changelog
