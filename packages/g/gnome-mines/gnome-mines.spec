#
# spec file for package gnome-mines
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


Name:           gnome-mines
Version:        48.1
Release:        0
Summary:        Minesweeper Game for GNOME
License:        GPL-3.0-or-later
Group:          Amusements/Games/Board/Other
URL:            https://wiki.gnome.org/Mines
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.37.1
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libgnome-games-support-2)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:  pkgconfig(vapigen)

%description
This is the popular logic puzzle minesweeper, which includes avoiding
mines while receiving clues for the location of the mines.

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
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/org.gnome.Mines.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Mines.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Mines*
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/metainfo/org.gnome.Mines.metainfo.xml
%{_datadir}/dbus-1/services/org.gnome.Mines.service

%files lang -f %{name}.lang

%changelog
