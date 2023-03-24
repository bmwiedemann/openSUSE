#
# spec file for package atomix
#
# Copyright (c) 2023 SUSE LLC
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


Name:           atomix
Version:        44.0
Release:        0
Summary:        A puzzle game where you move atoms to build a molecule
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Other
URL:            https://wiki.gnome.org/Apps/Atomix
Source0:        https://download.gnome.org/sources/atomix/44/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.0.5
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
BuildRequires:  pkgconfig(libgnome-games-support-1)

%description
You start the game with the map filled with walls and a few atoms, which you can
move in any direction. However, the atoms won't stop until they hit a wall or
another atom.

You can see a preview of what molecule you have to build, and you have to do your
best to find where to build the molecule, and move the atoms there.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/atomix.appdata.xml
%{_datadir}/applications/atomix.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*

%files lang -f %{name}.lang

%changelog
