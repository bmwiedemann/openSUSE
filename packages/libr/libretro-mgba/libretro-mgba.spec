#
# spec file for package libretro-mgba
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


Name:           libretro-mgba
Version:        0~git20200206
Release:        0
Summary:        The mGBA libretro core for GameBoy Advance emulation
License:        MPL-2.0
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
mGBA is an emulator for running Game Boy Advance games. It aims to be faster and
more accurate than many existing Game Boy Advance emulators, as well as adding
features that other emulators lack. It also supports Game Boy and Game Boy Color
games. This package is for RetroArch/Libretro front-end.

%prep
%setup -q

%build
make -f Makefile.libretro

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp mgba_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/mgba_libretro.so

%changelog
