#
# spec file for package dunelegacy
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           dunelegacy
Version:        0.99.5
Release:        0
Summary:        A modern Dune II reimplementation
License:        GPL-2.0-or-later
Group:          Amusements/Games/Strategy/Real Time
URL:            https://dunelegacy.sourceforge.net/
Source:         %{name}-%{version}.tar.xz
# PATCH-FEATURE-UPSTREAM https://sourceforge.net/p/dunelegacy/patches/8/
Source8:        %{name}.appdata.xml
# PATCH-FEATURE-UPSTREAM https://sourceforge.net/p/dunelegacy/patches/7/
Source9:        %{name}.6
Patch0:         dunelegacy-fix-cmake.patch
BuildRequires:  cmake
BuildRequires:  discord-rpc-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(miniupnpc)
BuildRequires:  pkgconfig(sdl2)

%description
Lead one of three interplanetary houses, Atreides, Harkonnen or Ordos,
in an attempt to harvest the largest amount of spice from the sand
dunes. Exchange your spice stockpiles for credits through refinement
and build an army capable of thwarting attempts of the other houses to
stop your harvesting!

Dune Legacy is an effort by a handful of developers to revitalize the
first-ever real-time strategy game. The original game was the basis
for the hugely successful Command and Conquer series, and the gameplay
has been replicated an extended to a wide variety of storylines and
series.

NOTE: Original Dune 2 game files are needed.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
install -Dpm 0644 %{SOURCE8} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
install -Dpm 0644 %{SOURCE9} %{buildroot}%{_mandir}/man6/%{name}.6
rm %{buildroot}/usr/share/doc/packages/dunelegacy/{AUTHORS,COPYING,NEWS,Release_Notes.md}

%files
%license COPYING
%doc AUTHORS NEWS README ChangeLog release_notes/RELEASE_NOTES.md
%{_bindir}/dunelegacy
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/DuneLegacy
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
