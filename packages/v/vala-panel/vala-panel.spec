#
# spec file for package vala-panel
#
# Copyright (c) 2022 SUSE LLC
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


%define _rev    741b80c641591494e9f0ccc4cd19b0cd
Name:           vala-panel
Version:        0.5.0
Release:        0
Summary:        A Gtk3 desktop panel based on Vala
License:        GPL-3.0-or-later
URL:            https://gitlab.com/vala-panel-project/vala-panel
Source:         %{url}/-/archive/%{version}/vala-panel-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM 52f40ce779cfa224266dd427cfe57afd83a28362.diff -- Fix duplicate language target
Patch0:         https://gitlab.com/vala-panel-project/vala-panel/-/commit/52f40ce779cfa224266dd427cfe57afd83a28362.diff
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  meson >= 0.51
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.34
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.52.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.14.0
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.4.7
Recommends:     %{name}-lang
Recommends:     %{name}-plugin-sntray
Recommends:     %{name}-plugins-base = %{version}
Recommends:     %{name}-runner = %{version}
Suggests:       %{name}-plugin-appmenu
Suggests:       %{name}-plugins-wnck = %{version}

%description
Vala Panel is a desktop panel written in Vala and Gtk3.
Initially it was a fork of LXPanel but 0.2.0 is completely
rewritten in Vala. It offers same functionality as LXPanel but:
 * It has a slightly bigger memory usage.
 * X11 dependency is stripped from panel core (but it is not tested
   on another display servers, such as Wayland and Mir, right now).
 * Some of former LXPanel plugins are separate binaries now
   and live in another packages (volume applet for example).

%lang_package

%package devel
Summary:        Development files for vala-panel
Requires:       %{name} = %{version}
Requires:       pkgconfig(gtk+-3.0)
Requires:       pkgconfig(libpeas-1.0)
Requires:       pkgconfig(libwnck-3.0)

%description devel
Vala Panel is a desktop panel written in Vala and Gtk3.

This is a development package for vala-panel.

%package runner
Summary:        Commands runner for vala-panel
Requires:       %{name} = %{version}

%description runner
Vala Panel is a desktop panel written in Vala and Gtk3.

This is a simple commands runner for vala-panel.

%package plugins-base
Summary:        Plugins for vala-panel -- non-X11 plugins

%description plugins-base
Vala Panel is a desktop panel written in Vala and Gtk3.

This package contains main plugins for vala-panel: clock,
launchbar, applications menu and so on.

%package plugins-wnck
Summary:        Plugins for vala-panel -- X11 plugins

%description plugins-wnck
Vala Panel is a desktop panel written in Vala and Gtk3.

This package contains X11 plugins for vala-panel: tasklist,
system tray, and others.

%prep
%autosetup -p1

%build
%meson -Dwnck=enabled
%meson_build

%install
%meson_install
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%config %{_sysconfdir}/xdg/vala-panel/
%{_bindir}/vala-panel*
%exclude %{_bindir}/vala-panel-runner
%{_datadir}/glib-2.0/schemas/org.valapanel.gschema.xml
%{_libdir}/libvalapanel.so.*
%{_datadir}/vala/
%{_datadir}/vala-panel/
%{_datadir}/glib-2.0/schemas/org.valapanel.toplevel.gschema.xml
%{_datadir}/applications/org.valapanel.application.desktop
%{_datadir}/icons/hicolor/scalable/apps/panel.svg
%{_datadir}/appdata/org.valapanel.application.appdata.xml
%{_mandir}/man?/vala-panel.?%{?ext_man}

%files lang -f %{name}.lang

%files devel
%{_libdir}/libvalapanel.so
%{_includedir}/vala-panel/
%{_libdir}/pkgconfig/vala-panel.pc

%files runner
%{_bindir}/vala-panel-runner
%{_mandir}/man1/vala-panel-runner.1%{?ext_man}

%files plugins-base
%{_datadir}/glib-2.0/schemas/org.valapanel.builtin.gschema.xml
%{_datadir}/glib-2.0/schemas/org.valapanel.plugins.gschema.xml
%dir %{_libdir}/vala-panel/
%dir %{_libdir}/vala-panel/applets/
%{_libdir}/vala-panel/applets/libclock.so
%{_libdir}/vala-panel/applets/libcpu.so
%{_libdir}/vala-panel/applets/libdirmenu.so
%{_libdir}/vala-panel/applets/libkbled.so
%{_libdir}/vala-panel/applets/liblaunchbar.so
%{_libdir}/vala-panel/applets/libmenumodel.so
%{_libdir}/vala-panel/applets/libseparator.so
%{_libdir}/vala-panel/applets/libmonitors.so

%files plugins-wnck
%{_datadir}/glib-2.0/schemas/org.valapanel.X.gschema.xml
%{_libdir}/vala-panel/applets/libdeskno.so
%{_libdir}/vala-panel/applets/libtasklist-xfce.so
%{_libdir}/vala-panel/applets/libwincmd.so
%{_libdir}/vala-panel/applets/libpager.so
%{_libdir}/vala-panel/applets/libbuttons.so
%{_libdir}/vala-panel/applets/libnetmon.so

%changelog
