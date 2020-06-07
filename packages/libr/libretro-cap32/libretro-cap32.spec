#
# spec file for package libretro-cap32
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


Name:           libretro-cap32
Version:        0~git20200508
Release:        0
Summary:        Caprice32 libretro core for Amstrad CPC emulation
License:        GPL-2.0-only
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
Caprice32 is a software emulator of the Amstrad CPC 8bit home computer series
running on Linux and Windows. The emulator faithfully imitates the CPC464,
CPC664, and CPC6128 models. By recreating the operations of all hardware
components at a low level, the emulator achieves a high degree of compatibility
\with original CPC software. These programs or games can be run unmodified at
real-time or higher speeds, depending on the emulator host environment.

This package is for RetroArch/libretro front-end.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp cap32_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/cap32_libretro.so

%changelog
