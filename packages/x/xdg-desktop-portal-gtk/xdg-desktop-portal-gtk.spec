#
# spec file for package xdg-desktop-portal-gtk
#
# Copyright (c) 2020 SUSE LLC
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


Name:           xdg-desktop-portal-gtk
Version:        1.6.0
Release:        0
Summary:        Backend implementation for xdg-desktop-portal using GTK+
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://github.com/flatpak/xdg-desktop-portal-gtk
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM xdg-dpg-support-mutter-pipewire-3-api.patch -- screencast: Bump supported Mutter version to 3
Patch0:         xdg-dpg-support-mutter-pipewire-3-api.patch

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(xdg-desktop-portal) >= 1.5
# Requires the xdg-desktop-portal service to be available
Requires:       xdg-desktop-portal
# Users of GTK+ 3.0 and flatpak would enjoy this integration
Supplements:    (gtk3 and (flatpak or snapd))
%if 0%{?suse_version} >= 1330
BuildRequires:  pkgconfig(gtk+-wayland-3.0) >= 3.21.5
%endif

%description
A backend implementation for xdg-desktop-portal that is using GTK+ and
various pieces of GNOME infrastructure, such as the org.gnome.Shell.Screenshot
or org.gnome.SessionManager D-Bus interfaces.

%lang_package

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}

%files
%license COPYING
%{_libexecdir}/xdg-desktop-portal-gtk
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.gtk.service
%dir %{_datadir}/xdg-desktop-portal
%dir %{_datadir}/xdg-desktop-portal/portals
%{_datadir}/xdg-desktop-portal/portals/gtk.portal
%{_datadir}/applications/xdg-desktop-portal-gtk.desktop
%{_userunitdir}/xdg-desktop-portal-gtk.service

%files lang -f %{name}.lang

%changelog
