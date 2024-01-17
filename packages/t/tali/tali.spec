#
# spec file for package tali
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


Name:           tali
Version:        40.9
Release:        0
Summary:        Yahtzee Game for GNOME
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Other
URL:            https://live.gnome.org/Tali
Source0:        https://download.gnome.org/sources/tali/40/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(libgnome-games-support-1)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.32.0

%description
Tali is like Yahtzee, or like poker with dice. The player rolls dice
to try to make the best possible combinations, like 4 of a kind, small
straight, and full house. The player is allowed 3 rolls per turn and
can hold certain dice with each roll.

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
%suse_update_desktop_file org.gnome.Tali
%fdupes %{buildroot}/%{_prefix}

%files
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/org.gnome.Tali.appdata.xml
%{_datadir}/applications/org.gnome.Tali.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Tali.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Tali*
%{_mandir}/man6/%{name}.6%{?ext_man}

%files lang -f %{name}.lang

%changelog
