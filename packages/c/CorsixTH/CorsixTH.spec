#
# spec file for package CorsixTH
#
# Copyright (c) 2024 SUSE LLC
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


Name:           CorsixTH
Version:        0.68.0
Release:        0
Summary:        Theme Hospital clone
License:        MIT
Group:          Amusements/Games/Strategy/Other
URL:            http://corsixth.com
Source:         https://github.com/CorsixTH/CorsixTH/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(sdl2)
Requires:       lua-lpeg
Requires:       lua-luafilesystem
Recommends:     timidity

%description
This project aims to reimplement the game engine of Theme Hospital, and be
able to load the original game data files. This means that you will need a
purchased copy of Theme Hospital, or a copy of the demo, in order to use
CorsixTH. After most of the original engine has been reimplemented in open
source code, the project will serve as a base from which extensions and
improvements to the original game can be made.

%prep
%setup -q

%build
%cmake -DWITH_UPDATE_CHECK=OFF
%cmake_build

%install
%cmake_install
rm -f %{buildroot}/%{_datadir}/corsix-{th,TH}/LICENSE.txt
%fdupes %{buildroot}/%{_datadir}

%files
%license LICENSE.txt
%doc README.txt
%{_bindir}/corsix-th
%{_datadir}/corsix-th
%{_datadir}/icons/hicolor/scalable/apps/corsix-th.svg
%{_datadir}/metainfo/com.corsixth.corsixth.metainfo.xml
%{_datadir}/applications/com.corsixth.corsixth.desktop
%{_mandir}/man6/corsix-th.6%{?ext_man}

%changelog
