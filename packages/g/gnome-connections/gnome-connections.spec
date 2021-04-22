#
# spec file for package gnome-connections
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


Name:           gnome-connections
Version:        40.0.1
Release:        0
Summary:        A remote desktop client for GNOME
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        GPL-3.0-or-later
URL:            https://wiki.gnome.org/Apps/Connections
Source:         https://download.gnome.org/sources/gnome-connections/40/%{name}-%{version}.tar.xz
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(freerdp2) >= 2.0.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.50
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtk-vnc-2.0) > 0.4.4
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires:  pkgconfig(winpr2) >= 2.0.0

%description
A remote desktop client for the GNOME desktop environment.

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}
# gtk-frdp is a subproject, do not offer it for consumption outside
rm -rf %{buildroot}%{_includedir}/%{name}/gtk-frdp/
rm %{buildroot}%{_libdir}/gnome-connections/pkgconfig/gtk-frdp-0.1.pc
rm %{buildroot}%{_datadir}/gnome-connections/gir-1.0/GtkFrdp-0.1.gir
rm %{buildroot}%{_datadir}/gnome-connections/vapi/gtk-frdp-0.1.deps
rm %{buildroot}%{_datadir}/gnome-connections/vapi/gtk-frdp-0.1.vapi


%files
%license COPYING
%{_bindir}/gnome-connections
%dir %{_libdir}/gnome-connections
%dir %{_libdir}/gnome-connections/girepository-1.0
%{_libdir}/gnome-connections/girepository-1.0/GtkFrdp-0.1.typelib
%{_libdir}/gnome-connections/libgtk-frdp-0.1.so
%{_datadir}/appdata/org.gnome.Connections.appdata.xml
%{_datadir}/applications/org.gnome.Connections.desktop
%{_datadir}/dbus-1/services/org.gnome.Connections.service
%{_datadir}/glib-2.0/schemas/org.gnome.Connections.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Connections.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Connections-symbolic.svg
%{_datadir}/mime/packages/org.gnome.Connections.xml

%files lang -f %{name}.lang

%changelog
