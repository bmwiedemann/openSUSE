#
# spec file for package netpanzer
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


# use GCC 13 for Leap 15.x
%if 0%{?suse_version} < 1600
%global force_gcc_version 13
%endif
Name:           netpanzer
Version:        0.9.1
Release:        0
Summary:        An Online Multiplayer Tactical Warfare Game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Strategy/Real Time
URL:            https://netpanzer.io/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  gettext
BuildRequires:  lua51
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(physfs)
BuildRequires:  pkgconfig(sdl2)

%description
netPanzer is an online multiplayer tactical warfare game designed for FAST
ACTION combat. Gameplay concentrates on the core -- no resource management is
needed. The game is based on quick tactical action and unit management in
real-time. Battles progress quickly and constantly as destroyed players respawn
with a set of new units. Players can join or leave multiplayer games at any
time.

%lang_package

%prep
%autosetup -n %{name}-%{version}

%build
%if 0%{?force_gcc_version}
export CXX="g++-%{force_gcc_version}"
%endif

%meson \
	-Ddocdir=%{_docdir}/%{name} \
	--buildtype=release \
	-Dstrip=true \
	-Db_sanitize=none \
	-Dbuild_tests=false
%meson_build

%install
%meson_install

%find_lang %{name}

# Remove bundled license files if they exist in docs (duplicate with %license)
rm -f %{buildroot}%{_docdir}/%{name}/COPYING.txt

# Install desktop item
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 support/win32/%{name}.desktop %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 %{name}.png %{buildroot}%{_datadir}/pixmaps
find %{buildroot}%{_datadir}/%{name} -type f -exec chmod 644 {} \;

%fdupes %{buildroot}%{_datadir}/%{name}

%files
%license COPYING.txt
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files lang -f %{name}.lang

%changelog
