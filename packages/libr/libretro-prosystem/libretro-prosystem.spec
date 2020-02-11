#
# spec file for package libretro-prosystem
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libretro-prosystem
Version:        0~git20190914
Release:        0
Summary:        ProSystem libretro core for Atari 7800 emulation
License:        GPL-2.0
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
The ProSystem Emulator is an Atari 7800 emulator for the PC and Windows OS. The emulator was written in C++ using the Windows API and DirectX. It emulates the Atari 7800 NTSC and PAL TV standards.

This package is for RetroArch/Libretro front-end.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp prosystem_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/prosystem_libretro.so

%changelog
