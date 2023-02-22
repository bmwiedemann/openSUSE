#
# spec file for package pt2-clone
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


Name:           pt2-clone
Version:        1.57
Release:        0
Summary:        ProTracker 2 clone
License:        BSD-3-Clause AND CC-BY-NC-SA-4.0
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://16-bits.org/pt2.php
#Git-Clone:     https://github.com/8bitbubsy/pt2-clone.git
Source:         https://github.com/8bitbubsy/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sdl2)

%description
Multi-platform clone of the classic music making software
ProTracker 2.3D.

%prep
%setup -q
# HACK: fix icon
sed 's|Icon=ProTracker 2 clone|Icon=pt2-clone|g' \
 -i "release/other/Freedesktop.org Resources/ProTracker 2 clone.desktop"

%build
%cmake
%cmake_build

%install
%cmake_install
install -Dpm 0644 "release/other/Freedesktop.org Resources/ProTracker 2 clone.desktop" %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dpm 0644 "release/other/Freedesktop.org Resources/ProTracker 2 clone.png" %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%license LICENSE LICENSES.txt
%doc README.md release/{effects.txt,help.txt,keybindings.txt}
%doc release/other/protracker.ini
%{_bindir}/pt2-clone
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
