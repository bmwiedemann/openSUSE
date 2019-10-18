#
# spec file for package gnome-klotski
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


Name:           gnome-klotski
Version:        3.34.0
Release:        0
Summary:        Klotski Game for GNOME
License:        GPL-3.0-or-later
Group:          Amusements/Games/Board/Puzzle
URL:            https://live.gnome.org/Klotski
Source0:        https://download.gnome.org/sources/gnome-klotski/3.34/%{name}-%{version}.tar.xz

BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.19.0
BuildRequires:  pkgconfig(libgnome-games-support-1)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:  pkgconfig(vapigen)
Recommends:     %{name}-lang

%description
Klotski is a puzzle game of which the objective is to get the
patterned block to the marker, which is done by moving the blocks in
its way.

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
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Klotski.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Klotski.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Klotski*
%{_datadir}/metainfo/org.gnome.Klotski.appdata.xml
%{_mandir}/man6/%{name}.6%{?ext_man}

%files lang -f %{name}.lang

%changelog
