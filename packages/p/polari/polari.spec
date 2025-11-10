#
# spec file for package polari
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2013 Dominique Leuenberger, Amsterdam, The Netherlands
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


Name:           polari
Version:        49.0
Release:        0
Summary:        An IRC Client for GNOME
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Networking/IRC
URL:            https://wiki.gnome.org/Apps/Polari
Source0:        %{name}-%{version}.tar.zst
Source99:       polari-rpmlintrc

BuildRequires:  desktop-file-utils
BuildRequires:  gjs >= 1.57.3
BuildRequires:  json-glib-devel
BuildRequires:  meson >= 1.1.0
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-2.0) >= 2.85.1
BuildRequires:  pkgconfig(girepository-2.0) >= 2.85.1
BuildRequires:  pkgconfig(gjs-1.0) >= 1.85.1
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(telepathy-glib)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
Requires:       gjs >= 1.69.2
Requires:       telepathy-idle
Requires:       telepathy-mission-control
# Dependency not detected by the dep scanner - boo#1122687
Requires:       typelib(Gspell)
Recommends:     telepathy-logger
# typelib-1_0-Polari-1_0 was merged into the main package, as it's in a private library directory
Obsoletes:      typelib-1_0-Polari-1_0 < %{version}

%description
Polari is an IRC client that is designed to integrate seamlessly
with GNOME 3.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%check
%meson_test

%files
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}
%{_bindir}/polari
%{_datadir}/applications/org.gnome.Polari.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Polari.service
%{_datadir}/dbus-1/services/org.gnome.Polari.service
%{_datadir}/glib-2.0/schemas/org.gnome.Polari.gschema.xml
%{_datadir}/metainfo/org.gnome.Polari.metainfo.xml
%{_datadir}/polari/
%dir %{_datadir}/telepathy
%dir %{_datadir}/telepathy/clients
%{_datadir}/telepathy/clients/Polari.client
%{_datadir}/icons/hicolor/
%dir %{_libdir}/polari
%{_libdir}/polari/libpolari-1.0.so
%dir %{_libdir}/polari/girepository-1.0
%{_libdir}/polari/girepository-1.0/Polari-1.0.typelib

%files lang -f %{name}.lang

%changelog
