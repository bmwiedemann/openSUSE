#
# spec file for package workrave
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


%define upstream_version    1_11_1
Name:           workrave
Version:        1.11.1
Release:        0
Summary:        Recovery and prevention of Repetitive Strain Injury program
License:        GPL-3.0-or-later AND LGPL-2.0-or-later AND HPND
URL:            https://www.workrave.org
Source:         https://github.com/rcaelers/workrave/archive/v%{upstream_version}.tar.gz
# PATCH-FIX-UPSTREAM fix-appstream-id-case.patch gh#rcaelers/workrave#710 -- AppStream id must match desktop-id case
Patch0:         fix-appstream-id-case.patch
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-Jinja2
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(spdlog)
BuildRequires:  pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:  pkgconfig(ayatana-indicator3-0.4)
BuildRequires:  pkgconfig(dbusmenu-glib-0.4)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gobject-introspection-no-export-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xtst)

%description
Workrave is a program that assists in the recovery and prevention of
Repetitive Strain Injury (RSI). The program frequently alerts you to
take micro-pauses, rest breaks and restricts you to your daily limit.

%package devel
Summary:        Development files for %{name}
BuildArch:      noarch

%description devel
GObject introspection files for developing Workrave applets.

%prep
%autosetup -p1 -n %{name}-%{upstream_version}

%build
%cmake \
  -DWITH_GNOME45:BOOL=ON \
  -DWITH_GNOME_CLASSIC_PANEL:BOOL=OFF \
  -DWITH_MATE:BOOL=OFF \
  -DWITH_XFCE4:BOOL=OFF \
  -DWITH_DBUS:BOOL=ON \
  -DWITH_GSTREAMER:BOOL=ON \
  -DWITH_PULSE:BOOL=ON \
  -DWITH_DBUSMENU:BOOL=ON \
  -DWITH_INDICATOR:BOOL=ON \
  -DWITH_APPINDICATOR:BOOL=ON \
  -DWITH_WAYLAND:BOOL=ON \
  -DWITH_TESTS:BOOL=OFF \
  -DCMAKE_INSTALL_SYSCONFDIR:PATH=%{_sysconfdir}
%cmake_build

%install
%cmake_install
# GIR is generated only with indicator support; the panel plugin is not shipped
rm -rf %{buildroot}%{_libdir}/ayatana-indicators3 \
       %{buildroot}%{_libdir}/indicators3
rm -f %{buildroot}%{_libdir}/libworkrave-gtk4-private-1.0.so \
      %{buildroot}%{_libdir}/libworkrave-private-1.0.so
%fdupes %{buildroot}%{_prefix}
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.workrave.Workrave.desktop
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/org.workrave.Workrave.desktop

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/workrave
%{_datadir}/applications/org.workrave.Workrave.desktop
%{_datadir}/dbus-1/services/org.workrave.Workrave.service
%{_datadir}/glib-2.0/schemas/org.workrave.*.xml
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}/
%{_datadir}/sounds/%{name}/
%{_datadir}/metainfo/org.workrave.Workrave.metainfo.xml
%config %{_sysconfdir}/xdg/autostart/org.workrave.Workrave.desktop
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/extensions
%{_datadir}/gnome-shell/extensions/workrave@workrave.org/
%dir %{_datadir}/cinnamon
%dir %{_datadir}/cinnamon/applets
%{_datadir}/cinnamon/applets/workrave@workrave.org/
%{_libdir}/libworkrave-private-1.0.so.*
%{_libdir}/libworkrave-gtk4-private-1.0.so.*
%{_libdir}/girepository-1.0/Workrave-*.typelib

%files devel
%{_datadir}/gir-1.0/Workrave-*.gir

%changelog
