#
# spec file for package openxcom
#
# Copyright (c) 2020 SUSE LLC
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


Name:           openxcom
Version:        1.0.0.1615230250.adb97235b
Release:        0
Summary:        An open source reimplementation of the original X-Com game
License:        GPL-3.0-only
URL:            https://openxcom.org/
Source:         OpenXcom-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL_gfx)
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(yaml-cpp) >= 0.5
Obsoletes:      %{name}-doc

%description
OpenXcom is an open-source clone of the original UFO: Enemy Unknown
(X-Com: UFO Defense in USA), licensed under the GPL and written in C++ / SDL.

The goal of the project is to bring back the tried and true feel of the original
with none of the issues. All the same graphics, sound and gameplay with a brand
new codebase written from scratch.

User is required to have original gamedata (possible to obtain from e.g. Steam)
installed to ~/.local/share/openxcom/data/

%prep
%setup -q -n OpenXcom-%{version}
dos2unix *.txt

%build
%cmake
%cmake_build

%install
%cmake_install
rm %{buildroot}/usr/man/man6/openxcom.6

%files
%license LICENSE.txt
%doc README.md CHANGELOG.txt
%{_datadir}/applications/openxcom.desktop
%{_datadir}/icons/hicolor/*/apps/openxcom.*
%{_datadir}/%{name}/
%{_bindir}/%{name}

%changelog
