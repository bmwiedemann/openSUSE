#
# spec file for package dunelegacy
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           dunelegacy
Version:        0.96.4
Release:        0
Summary:        A modern Dune II reimplementation
License:        GPL-2.0+
Group:          Amusements/Games/Strategy/Real Time
Url:            http://dunelegacy.sourceforge.net/
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.bz2
# PATCH-FEATURE-UPSTREAM https://sourceforge.net/p/dunelegacy/patches/8/
Source8:        %{name}.appdata.xml
# PATCH-FEATURE-UPSTREAM https://sourceforge.net/p/dunelegacy/patches/7/
Source9:        %{name}.6
# PATCH-FIX-OPENSUSE fix-build-with-SDL_mixer-2.0.2.patch wbauer@tmo.at -- fix build with SDL2_mixer 2.0.2 where MIX_INIT_FLUIDSYNTH has been renamed to MIX_INIT_MID
Patch:          fix-build-with-SDL_mixer-2.0.2.patch
BuildRequires:  cppunit-devel
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(sdl2)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%setup -q
%patch -p1
dos2unix ToDo.txt

%build
%configure
make V=1 %{?_smp_mflags}

%check
make V=1 %{?_smp_mflags} distclean
./runUnitTests.sh

%install
%make_install V=1

# Install .desktop file and icon
%suse_update_desktop_file -i %{name}
install -D -p -m 0644 %{name}-128x128.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# https://en.opensuse.org/openSUSE:AppStore
mkdir -p %{buildroot}%{_datadir}/appdata
cp %{SOURCE8} %{buildroot}%{_datadir}/appdata

# Install man page
mkdir -p %{buildroot}%{_mandir}/man6
cp %{SOURCE9} %{buildroot}%{_mandir}/man6

%files
%defattr(644,root,root,755)
%doc README ToDo.txt NEWS COPYING AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man?/%{name}.?.*
%{_datadir}/%{name}/
%attr(755,root,root) %{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
