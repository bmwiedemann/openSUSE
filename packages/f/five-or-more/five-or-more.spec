#
# spec file for package five-or-more
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


Name:           five-or-more
Version:        3.32.0
Release:        0
Summary:        "Five or More" Game for GNOME
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Puzzle
URL:            https://wiki.gnome.org/Apps/Five_or_more
Source0:        https://download.gnome.org/sources/five-or-more/3.32/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  libxml2-tools
BuildRequires:  meson >= 0.43
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.32
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(libgnome-games-support-1)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.32.0
Recommends:     %{name}-doc

%description
Five or More is a game where one must align colored pieces as the
board gets filled with randomly placed pieces. When five or more
pieces of the same color get lined up, they disappear. The game ends
when the board gets filled up all the way.

This package provides the binary, manual and data files for Five or More.

%package doc
Summary:        Documentation for the "Five or More" GNOME game
Group:          Documentation/Other
BuildArch:      noarch

%description doc
Five or More is a game where one must align colored pieces as the
board gets filled with randomly placed pieces. When five or more
pieces of the same color get lined up, they disappear. The game ends
when the board gets filled up all the way.

This package contains the help documentation for Five or More.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_datadir}

%files
%license COPYING
%doc NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/org.gnome.five-or-more.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.five-or-more.gschema.xml
%{_datadir}/icons/hicolor/
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/metainfo/org.gnome.five-or-more.appdata.xml

%files doc
%doc %{_datadir}/help/C/%{name}/

%files lang -f %{name}.lang

%changelog
