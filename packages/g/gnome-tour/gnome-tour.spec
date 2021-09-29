#
# spec file for package gnome-tour
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


Name:           gnome-tour
Version:        41.rc
Release:        0
Summary:        GNOME Tour & Greeter
License:        GPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/gnome-tour
Source0:        https://download.gnome.org/sources/gnome-tour/41/%{name}-%{version}.tar.xz

BuildRequires:  cargo
BuildRequires:  meson
BuildRequires:  rust
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0) >= 2.56
BuildRequires:  pkgconfig(glib-2.0) >= 2.64
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16
BuildRequires:  pkgconfig(libhandy-1) >= 1

%description
A guided tour and greeter for GNOME.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/gnome-tour
%{_datadir}/applications/org.gnome.Tour.desktop
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/icons/hicolor/symbolic/apps/*
%{_datadir}/metainfo/org.gnome.Tour.metainfo.xml

%files lang -f %{name}.lang

%changelog
