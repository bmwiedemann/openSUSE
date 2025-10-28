#
# spec file for package gnome-usage
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2017 Bjørn Lie, Bryne, Norway.
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


Name:           gnome-usage
Version:        48.0
Release:        0
Summary:        System resources viewer for GNOME
License:        GPL-3.0-only
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/Usage
Source:         %{name}-%{version}.tar.zst

BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.74
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.38
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk4) >= 4.12
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(tinysparql-3.0)

%description
GNOME Usage is a program to view information about the use of system
resources, like memory and disk space.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Usage.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Usage.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Usage.svg
%{_datadir}/metainfo/org.gnome.Usage.metainfo.xml

%files lang -f %{name}.lang

%changelog
