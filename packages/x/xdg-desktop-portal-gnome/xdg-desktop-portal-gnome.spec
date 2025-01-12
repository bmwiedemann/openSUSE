#
# spec file for package xdg-desktop-portal-gnome
#
# Copyright (c) 2025 SUSE LLC
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


Name:           xdg-desktop-portal-gnome
Version:        47.1+3
Release:        0
Summary:        A backend implementation for xdg-desktop-portal
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome
Source:         %{name}-%{version}.tar.zst
# PATCH-FIX-UPSTREAM -- https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome/-/merge_requests/189
Patch0:         xdg-desktop-portal-gnome-gtk_init.patch
# PATCH-FIX-UPSTREAM notification-null-icon-pointer.patch -- Fix build with xdg-desktop-portal >= 1.19.1
Patch1:         notification-null-icon-pointer.patch

BuildRequires:  c_compiler
BuildRequires:  fontconfig
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  xdg-desktop-portal-gtk
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 47.alpha
BuildRequires:  pkgconfig(gtk4) >= 4.0
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xdg-desktop-portal) >= 1.19.1
Requires:       xdg-desktop-portal
# Use rich deps to pull in this package when gnome-shell and flatpak (or snapd) are both installed
Supplements:    (gnome-shell and (flatpak or snapd))

%description
A backend implementation for xdg-desktop-portal for the GNOME
desktop environment.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license COPYING
%doc README.md NEWS
%{_userunitdir}/xdg-desktop-portal-gnome.service
%{_libexecdir}/xdg-desktop-portal-gnome
%{_datadir}/applications/xdg-desktop-portal-gnome.desktop
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.gnome.service
%{_datadir}/glib-2.0/schemas/xdg-desktop-portal-gnome.gschema.xml
%{_datadir}/xdg-desktop-portal/portals/gnome.portal

%files lang -f %{name}.lang

%changelog
