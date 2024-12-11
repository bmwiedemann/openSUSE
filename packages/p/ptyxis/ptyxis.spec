#
# spec file for package ptyxis
#
# Copyright (c) 2024 SUSE LLC
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


Name:           ptyxis
Version:        47.6
Release:        0
Summary:        A terminal for GNOME with first-class support for containers
License:        GPL-3.0-or-later
URL:            https://www.gnome.org
Source:         %{name}-%{version}.tar.zst
BuildRequires:  desktop-file-utils
BuildRequires:  meson >= 0.64.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.80
BuildRequires:  pkgconfig(gtk4) >= 4.14
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.6
BuildRequires:  pkgconfig(libadwaita-1) >= 1.6
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(vte-2.91-gtk4) >= 0.76

%description
Ptyxis is a terminal for GNOME with first-class support for containers.

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
%{_bindir}/ptyxis
%{_mandir}/man1/ptyxis.1%{?ext_man}
%{_libexecdir}/ptyxis-agent
%{_datadir}/applications/org.gnome.Ptyxis.desktop
%{_datadir}/dbus-1/services/org.gnome.Ptyxis.service
%{_datadir}/glib-2.0/schemas/org.gnome.Ptyxis.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/org.gnome.Ptyxis.metainfo.xml

%files lang -f %{name}.lang

%changelog
