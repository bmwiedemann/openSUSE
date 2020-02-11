#
# spec file for package libretro-ppsspp
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


Name:           libretro-ppsspp
Version:        0~git20191015
Release:        0
Summary:        PPSSPP libretro core for PSP emulation
License:        GPL-2.0
Group:          System/Emulators/Other
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  Mesa-devel

%description
A PSP emulator for Android, Windows, Mac and Linux, written in C++.

This package is for RetroArch/libretro front-end.

%prep
%setup -q

%build
mkdir build
cd build
cmake .. -DLIBRETRO=ON -DCMAKE_BUILD_TYPE=Release
make

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp build/lib/ppsspp_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/ppsspp_libretro.so

%changelog
