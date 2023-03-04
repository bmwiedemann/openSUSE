#
# spec file for package hitori
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


Name:           hitori
Version:        44.0
Release:        0
Summary:        Original puzzle of Nikoli
License:        GPL-3.0-or-later
Group:          Amusements/Games/Logic
URL:            https://gitlab.gnome.org/GNOME/hitori
Source0:        https://download.gnome.org/sources/hitori/44/%{name}-%{version}.tar.xz

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo) >= 1.4
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.15.0

%description
Hitori is played with a grid of squares or cells, and each cell contains a number.
The objective is to eliminate numbers by filling in the squares such that remaining cells do not
contain numbers that appear more than once in either a given row or column.

Filled-in cells cannot be horizontally or vertically adjacent, although they can be diagonally
adjacent. The remaining un-filled cells must form a single component connected horizontally
and vertically.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}
%fdupes %{buildroot}%{_prefix}

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Hitori.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.Hitori*
%{_datadir}/glib-2.0/schemas/org.gnome.hitori.gschema.xml
%{_datadir}/metainfo/org.gnome.Hitori.appdata.xml

%files lang -f %{name}.lang

%changelog
