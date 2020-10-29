#
# spec file for package julius
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


Name:           julius
Version:        1.5.1
Release:        0
Summary:        An open source re-implementation of Caesar III
License:        GPL-3.0-only
Group:          Amusements/Games/Strategy/Other
URL:            https://github.com/bvschaik/julius
Source:         https://github.com/bvschaik/julius/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(sdl2)

%description
Julius is an open source re-implementation of Caesar III.

The aim of this project is to create an open-source version of
Caesar 3, with the same logic as the original, but with some UI
enhancements, that is able to be played on multiple platforms.

The same logic means that the saved games are 100% compatible,
and any gameplay bugs present in the original Caesar 3 game will
also be present in Julius.

UI enhancements include:

* Support for widescreen resolutions
* Windowed mode support for 32-bit desktops

Julius requires the original assets (graphics, sounds, etc) from
Caesar 3 to run.

%prep
%setup -q

%build
%cmake
%make_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.txt
%doc README.md 
%{_bindir}/julius
%{_datadir}/applications/com.github.bvschaik.julius.desktop
%{_datadir}/icons/hicolor/*/apps/com.github.bvschaik.julius.png
%{_datadir}/metainfo/com.github.bvschaik.julius.metainfo.xml

%changelog
