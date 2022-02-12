#
# spec file for package gnome-2048
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


Name:           gnome-2048
Version:        3.38.2
Release:        0
Summary:        Sliding block puzzle game
License:        GPL-3.0-or-later
Group:          Amusements/Games/Board/Puzzle
URL:            https://wiki.gnome.org/Apps/2048
Source0:        https://download.gnome.org/sources/gnome-2048/3.38/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM 21.patch -- Fix build with meson 0.61 and newer
Patch0:         https://gitlab.gnome.org/GNOME/gnome-2048/-/merge_requests/21.patch

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.24.0
BuildRequires:  pkgconfig(clutter-1.0) >= 1.12.0
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.6.0
BuildRequires:  pkgconfig(gee-0.8) >= 0.14.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(libgnome-games-support-1) >= 1.7.1

%description
2048 is a single-player sliding block puzzle game, in which the
objective is to slide and merge same-numbered tiles on a grid to
reach higher numbers.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
%meson_test

%files
%license COPYING
%{_bindir}/gnome-2048
%{_datadir}/metainfo/org.gnome.TwentyFortyEight.appdata.xml
%{_datadir}/applications/org.gnome.TwentyFortyEight.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.TwentyFortyEight.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.TwentyFortyEight*
%{_mandir}/man6/gnome-2048.6%{?ext_man}

%files lang -f %{name}.lang

%changelog
