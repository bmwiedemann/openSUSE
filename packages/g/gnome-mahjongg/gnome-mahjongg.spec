#
# spec file for package gnome-mahjongg
#
# Copyright (c) 2025 SUSE LLC
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


Name:           gnome-mahjongg
Version:        47.1
Release:        0
Summary:        Mahjong Solitaire Game for GNOME
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Puzzle
URL:            https://live.gnome.org/GnomeMahongg
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.24.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.46.0
# Package was renamed to gnome-mahjongg, following upstreams name change during 3.6 development.
Obsoletes:      mahjongg < %{version}
Provides:       mahjongg = %{version}

%description
Mahjongg is a solitaire version of the classic Eastern tile game. It
involves clearing as much of the board as possible by matching
corresponding tiles and taking them out of play.

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

%check
%meson_test

%files
%license COPYING
%doc NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/org.gnome.Mahjongg.metainfo.xml
%{_datadir}/applications/org.gnome.Mahjongg.desktop
%{_datadir}/dbus-1/services/org.gnome.Mahjongg.service
%{_datadir}/glib-2.0/schemas/org.gnome.Mahjongg.gschema.xml
%{_datadir}/help/C/%{name}/
%{_datadir}/icons/hicolor/*/apps/org.gnome.Mahjongg*
%{_mandir}/man6/%{name}.6%{?ext_man}

%files lang -f %{name}.lang

%changelog
