#
# spec file for package console
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


Name:           console
Version:        43.0
Release:        0
Summary:        A simple user-friendly terminal emulator for the GNOME desktop
License:        GPL-3.0-only
URL:            https://gitlab.gnome.org/GNOME/console
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM 66b225e.patch -- style: Use accent_fg_color properly
Patch:          https://gitlab.gnome.org/GNOME/console/-/commit/66b225e.patch

BuildRequires:  appstream-glib
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  desktop-file-utils
BuildRequires:  libxml2-tools
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.72
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.72
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.2.beta
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libpcre2-8) >= 10.32
BuildRequires:  pkgconfig(vte-2.91-gtk4) >= 0.69.91

Obsoletes:      nautilus-extension-console < %{version}
Provides:       nautilus-extension-console = %{version}

%description
A simple user-friendly terminal emulator for the GNOME desktop.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang kgx %{?no_lang_C} %{name}.lang

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_bindir}/kgx
%{_datadir}/applications/org.gnome.Console.desktop
%{_datadir}/dbus-1/services/org.gnome.Console.service
%{_datadir}/glib-2.0/schemas/org.gnome.Console.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Console.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Console-symbolic.svg
%{_datadir}/metainfo/org.gnome.Console.metainfo.xml

%files lang -f %{name}.lang

%changelog
