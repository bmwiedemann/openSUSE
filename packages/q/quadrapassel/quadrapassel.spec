#
# spec file for package quadrapassel
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


Name:           quadrapassel
Version:        3.32.0
Release:        0
Summary:        Tetris Game for GNOME
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Other
URL:            https://live.gnome.org/Quadrapassel
Source0:        https://download.gnome.org/sources/quadrapassel/3.32/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.24.0
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(clutter-1.0) >= 1.0.0
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 0.91.6
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:  pkgconfig(manette-0.2)
Recommends:     %{name}-lang

%description
Quadrapassel is a version of Tetris, the classic game of interlocking
four-piece blocks. As they fall from the top, the player must orient
them to fit the other blocks at the bottom so that they form a
complete horizontal line, in which case that line disappears and the
player gains points

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
%{_datadir}/metainfo/org.gnome.Quadrapassel.appdata.xml
%{_datadir}/applications/org.gnome.Quadrapassel.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Quadrapassel.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Quadrapassel*
%{_mandir}/man6/%{name}.6%{?ext_man}

%files lang -f %{name}.lang

%changelog
