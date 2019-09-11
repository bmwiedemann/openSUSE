#
# spec file for package gnome-tetravex
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


Name:           gnome-tetravex
Version:        3.32.0
Release:        0
Summary:        Tetravex Game for GNOME
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Puzzle
URL:            https://live.gnome.org/Tetravex
Source0:        https://download.gnome.org/sources/gnome-tetravex/3.32/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.13.2
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:  pkgconfig(vapigen) >= 0.24
Recommends:     %{name}-lang
# gnome-tetravex used to be called 'gnotravex' and was part of gnome-games until 3.7.x
Obsoletes:      gnotravex < %{version}
Obsoletes:      gnotravex-lang < %{version}

%description
Tetravex is a simple puzzle game in which pieces have numbers on each
side. The pieces must be positioned so that the same numbers touch
each other, during which you are being timed. The times are then
stored in a system-wide scoreboard.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/metainfo/org.gnome.Tetravex.appdata.xml
%{_datadir}/applications/org.gnome.Tetravex.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Tetravex.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man6/%{name}.6%{?ext_man}

%files lang -f %{name}.lang

%changelog
