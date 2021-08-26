#
# spec file for package opengreedy
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2021, Martin Hauke <mardnh@gmx.de>
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


Name:           opengreedy
Version:        0.6
Release:        0
Summary:        A Pacman clone
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://troel.net/opengreedy/
#Git-Clone:     https://github.com/atroel/open-greedy.git
Source:         %{name}-%{version}.tar.xz
Source1:        https://github.com/atroel/basics/archive/refs/heads/master.zip
Patch0:         fix-build.patch
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(libxmp)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
Recommends:     opengreedy-data

%description
Opengreedy is an open-source version of Edromel Studio's Greedy XP.
https://www.edromel.com/us/index.php?menu=1
Greedy is a remake from the famous arcade game : Pacman. It allows
many options, greater sound effects, nice graphics and more than 70
levels.

%prep
%setup -q
%patch0 -p1
unzip %{SOURCE1} && mv basics-master ../basics

%build
%make_build -C ../basics static
%make_build BUILD=SUSE

%install
install -D -m 0755 opt/greedy %{buildroot}%{_bindir}/opengreedy
install -D -m 0644 opengreedy.6 %{buildroot}%{_mandir}/man6/opengreedy.6
install -d %{buildroot}%{_datadir}/games/opengreedy

%files
%license COPYING
%doc README
%{_bindir}/opengreedy
%{_mandir}/man6/opengreedy.6%{?ext_man}
%{_datadir}/games/opengreedy

%changelog
