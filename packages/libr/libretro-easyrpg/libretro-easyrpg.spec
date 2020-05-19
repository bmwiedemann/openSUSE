#
# spec file for package libretro-easyrpg
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


Name:           libretro-easyrpg
Version:        0~git20200510
Release:        0
Summary:        EasyRPG libretro core
License:        GPL-3.0-only
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(liblcf)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libxmp)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(vorbis)

%description
EasyRPG is a community project to create a free, open source, role playing game
creation tool, compatible with RPG Maker 2000/2003 games.

This package is for RetroArch/Libretro front-end.

%prep
%setup -q

%build
%cmake -DPLAYER_TARGET_PLATFORM=libretro -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp build/easyrpg_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/easyrpg_libretro.so

%changelog
