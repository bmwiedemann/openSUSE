#
# spec file for package 7kaa
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


%define base_version 2.15
Name:           7kaa
Version:        %{base_version}.6
Release:        0
Summary:        Seven Kingdoms: Ancient Adversaries
License:        GPL-2.0-only
Group:          Amusements/Games/Strategy/Real Time
URL:            https://7kfans.com/
Source0:        https://github.com/the3dfxdude/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.png
Source2:        %{name}.desktop
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  curl-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2) >= 2.24.0
Recommends:     %{name}-music >= %{base_version}

%description
Seven Kingdoms made departures from the traditional real-time strategy models
of "gather resources, build a base and army, and attack". The economic model
bears more resemblance to a turn-based strategy game. It features an espionage
system that allows players to train and control spies individually, who each
have a spying skill that increases over time. The player is also responsible
for catching spies in their own kingdom. Inns built within the game allow
players to hire mercenaries of various occupations, skill levels, and races.
Skilled spies of enemy races are essential to a well-conducted espionage
program, and the player can bolster his forces by grabbing a skilled fighter
or give ones own factories, mines, and towers of science, a boost by hiring a
skilled professional.

Enlight Software decided to release the game to the Open Source community
in August 2009. At that time everything, but the music, was released under
the GPL v2.

%prep
%setup -q

%build
autoreconf -if
./autogen.sh
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
%configure --docdir=%{_docdir}/%{name}
%make_build

%install
%make_install

# install icon
install -Dm 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install Desktop file
install -Dm 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop

%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}%{_prefix}
%find_lang %{name}

# remove duplicate COPYING file
rm -f %{buildroot}%{_docdir}/7kaa/COPYING

%files -f %{name}.lang
%license COPYING
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
