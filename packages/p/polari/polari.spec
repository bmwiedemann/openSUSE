#
# spec file for package polari
#
# Copyright (c) 2020 SUSE LLC
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
Version:        3.36.3
Release:        0
Summary:        An IRC Client for GNOME
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Networking/IRC
URL:            https://wiki.gnome.org/Apps/Polari
Source0:        https://download.gnome.org/sources/polari/3.36/%{name}-%{version}.tar.xz
Source99:       polari-rpmlintrc
# PATCH-FIX-UPSTREAM polari-fix-nb-translation.patch glgo#GNOME/polari!145 -- Fix Norwegian bokmål translation
Patch0:         polari-fix-nb-translation.patch

BuildRequires:  gjs >= 1.57.3
BuildRequires:  meson >= 0.43.0
BuildRequires:  mozjs60
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-2.0) >= 2.43.4
BuildRequires:  pkgconfig(gjs-1.0) >= 1.57.3
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.6
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.21.6
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(telepathy-glib)
BuildRequires:  pkgconfig(telepathy-logger-0.2)
Requires:       gjs >= 1.45.0
Requires:       telepathy-idle
Requires:       telepathy-logger
Requires:       telepathy-mission-control
# Dependency not detected by the dep scanner - boo#1122687
Requires:       typelib(Gspell)

%description
Polari is an IRC client that is designed to integrate seamlessly
with GNOME 3.

%package -n typelib-1_0-Polari-1_0
Summary:        Introspection bindings for Polari client library
Group:          System/Libraries

%description -n typelib-1_0-Polari-1_0
Polari is an IRC client that is designed to integrate seamlessly
with GNOME 3.
This package contains Introspection bindings.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS NEWS
%doc %{_datadir}/help/C/%{name}
%{_bindir}/polari
%{_datadir}/applications/org.gnome.Polari.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Polari.service
%{_datadir}/dbus-1/services/org.gnome.Polari.service
%{_datadir}/glib-2.0/schemas/org.gnome.Polari.gschema.xml
%{_datadir}/metainfo/org.gnome.Polari.appdata.xml
%{_datadir}/polari/
%dir %{_datadir}/telepathy
%dir %{_datadir}/telepathy/clients
%{_datadir}/telepathy/clients/Polari.client
%{_datadir}/icons/hicolor/*/apps/*
%{_libdir}/polari/libpolari-1.0.so

%files -n typelib-1_0-Polari-1_0
%dir %{_libdir}/polari
%dir %{_libdir}/polari/girepository-1.0
%{_libdir}/polari/girepository-1.0/Polari-1.0.typelib

%files lang -f %{name}.lang

%changelog
