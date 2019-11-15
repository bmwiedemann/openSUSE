#
# spec file for package libretro-bsnes
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


Name:           libretro-bsnes
Version:        0~git20191013
Release:        0
Summary:        The bsnes libretro core for SNES emulation
License:        GPL-3.0-only
Group:          System/Emulators/Other
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
Fork of bsnes, a Super Nintendo (Super Famicom) emulator.

This package is for RetroArch/libretro front-end.

%prep
%setup -q

%build
cd bsnes
make -f GNUmakefile compiler=g++ target=libretro binary=library local=false platform=linux

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp bsnes/out/bsnes_libretro.so %{buildroot}%{_libdir}/libretro

%files
%defattr(-,root,root)
%license LICENSE.txt
%dir %{_libdir}/libretro
%{_libdir}/libretro/bsnes_libretro.so

%changelog
