#
# spec file for package gnome-characters
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


Name:           gnome-characters
Version:        43.1
Release:        0
Summary:        Character Map
License:        GPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Design/Apps/CharacterMap
Source0:        https://download.gnome.org/sources/gnome-characters/43/%{name}-%{version}.tar.xz

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  intltool >= 0.50.1
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gjs-1.0) >= 1.43.3
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.35.9
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.0
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangoft2)
# Ensure default sections are filled with content
Recommends:     noto-coloremoji-fonts

%description
A simple utility application to find and insert unusual characters.

%package -n gnome-shell-search-provider-gnome-characters
Summary:        GNOME Characters -- Search Provider for GNOME Shell
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Supplements:    (gnome-shell and %{name})
BuildArch:      noarch

%description -n gnome-shell-search-provider-gnome-characters
This package contains a search provider to enable GNOME Shell to get
search results from GNOME Characters.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D pangoft2=true \
	-D installed_tests=false \
	%{nil}
%meson_build

%install
%meson_install
%find_lang org.gnome.Characters %{name}.lang

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Characters.desktop
%meson_test

%files
%license COPYING
%{_bindir}/gnome-characters
%{_datadir}/metainfo/org.gnome.Characters.appdata.xml
%{_datadir}/org.gnome.Characters/
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/glib-2.0/schemas/org.gnome.Characters.gschema.xml
%{_datadir}/icons/hicolor/*
%{_datadir}/applications/org.gnome.Characters.desktop
%{_datadir}/dbus-1/services/org.gnome.Characters.service
%{_libdir}/org.gnome.Characters/

%files -n gnome-shell-search-provider-gnome-characters
%{_datadir}/gnome-shell/search-providers/org.gnome.Characters.search-provider.ini

%files lang -f %{name}.lang

%changelog
