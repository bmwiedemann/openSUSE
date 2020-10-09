#
# spec file for package iagno
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


Name:           iagno
Version:        3.36.7
Release:        0
Summary:        Reversi Game for GNOME
License:        GPL-3.0-or-later
Group:          Amusements/Games/Board/Other
URL:            https://wiki.gnome.org/Apps/Iagno
Source0:        https://download.gnome.org/sources/iagno/3.36/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0) >= 2.42.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.42.0
BuildRequires:  pkgconfig(gsound) >= 1.0.2
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.32.0

%description
Iagno is the two player strategy game of Othello, which is also known
as Reversi and is similar to Go. The pieces are tiles that are black
on one side and white on the other and the objective is for the player
to flip his/her opponent's tiles to his/her color, while keeping the
opponent from doing the same. Once the board is filled with tiles, the
winner is the player with the most of his/her color tiles on the
board.

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
%fdupes %{buildroot}/%{_datadir}

%files
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/org.gnome.Reversi.appdata.xml
%{_datadir}/applications/org.gnome.Reversi.desktop
%{_datadir}/dbus-1/services/org.gnome.Reversi.service
%{_datadir}/glib-2.0/schemas/org.gnome.Reversi.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man6/%{name}.6%{?ext_man}

%files lang -f %{name}.lang

%changelog
