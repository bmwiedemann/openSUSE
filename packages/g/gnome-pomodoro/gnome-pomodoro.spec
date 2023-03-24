#
# spec file for package gnome-pomodoro
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


%global __requires_exclude typelib\\(Meta\\)
Name:           gnome-pomodoro
Version:        0.22.1
Release:        0
Summary:        A time management utility for GNOME
License:        GPL-3.0-or-later
Group:          Productivity/Office/Other
URL:            https://gnomepomodoro.org
Source:         https://github.com/codito/%{name}/archive/%{version}.tar.gz
Source99:       gnome-pomodoro-rpmlintrc

# PATCH-FIX-UPSTREAM e67bf9d0d0ea3604654145aa7e40d239d3d8109d.patch -- Mark extension as compatible with GNOME Shell 44
Patch:          https://github.com/gnome-pomodoro/gnome-pomodoro/commit/e67bf9d0d0ea3604654145aa7e40d239d3d8109d.patch

BuildRequires:  desktop-file-utils
BuildRequires:  docbook-utils
BuildRequires:  gettext >= 0.19.6
BuildRequires:  gnome-common
BuildRequires:  gnome-shell < 45
BuildRequires:  gnome-shell >= 3.36.0
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.28
BuildRequires:  pkgconfig(appstream-glib) >= 0.7.3
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-2.0) >= 2.38.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.10.1
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.16.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0.10
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcanberra) >= 0.30
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.5.0
BuildRequires:  pkgconfig(sqlite3)
Requires:       gnome-shell < 45
Requires:       gnome-shell >= 3.36.0
Requires:       gstreamer
Requires:       gtk3 >= 3.20.0
Requires:       hicolor-icon-theme
Recommends:     gstreamer-plugins-base

%description
A GNOME utility that helps managing time according to Pomodoro Technique. It
intends to improve productivity and focus by taking short breaks after every
25 minutes of work.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print
desktop-file-edit %{buildroot}/%{_datadir}/applications/*.desktop \
    --set-key=X-AppInstall-Package --set-value=%{name}

%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.Pomodoro.desktop

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files lang -f %{name}.lang

%files
%doc README.md NEWS
%license COPYING
%{_bindir}/gnome-pomodoro
%{_datadir}/metainfo/org.gnome.Pomodoro.appdata.xml
%{_datadir}/applications/org.gnome.Pomodoro.desktop
%{_datadir}/dbus-1/services/org.gnome.Pomodoro.service
%{_datadir}/glib-2.0/schemas/org.gnome.pomodoro.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.pomodoro.plugins.actions.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.pomodoro.plugins.gnome.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.pomodoro.plugins.sounds.gschema.xml
%{_datadir}/gnome-pomodoro/
%{_datadir}/gnome-shell/extensions/pomodoro@arun.codito.in
%{_datadir}/icons/hicolor/*/apps/*
#make it work for :42
%dir %{_datadir}/metainfo
%{_libdir}/gnome-pomodoro/
%{_libdir}/libgnome-pomodoro.so*

%changelog
