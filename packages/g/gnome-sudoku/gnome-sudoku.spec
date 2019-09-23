#
# spec file for package gnome-sudoku
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gnome-sudoku
Version:        3.32.0
Release:        0
Summary:        Sudoku Game for GNOME
License:        GPL-3.0-or-later
Group:          Amusements/Games/Logic
URL:            https://wiki.gnome.org/Apps/Sudoku
Source0:        https://download.gnome.org/sources/gnome-sudoku/3.32/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gcc-c++
# Needed for typelib() requires generator.
BuildRequires:  gobject-introspection
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.35.7.24
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.40.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.19.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(qqwing) >= 1.3.4

%description
Sudoku is a logic puzzle game, in which one must fill a 9 by 9 square
with the correct digits.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes -s %{buildroot}/%{_datadir}
%fdupes -s %{buildroot}/%{_libexecdir}

%files
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}/
%{_datadir}/applications/org.gnome.Sudoku.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Sudoku.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/org.gnome.Sudoku.appdata.xml
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_bindir}/%{name}

%files lang -f %{name}.lang

%changelog
