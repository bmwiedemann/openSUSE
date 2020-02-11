#
# spec file for package libretro-easyrpg
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


Name:           libretro-easyrpg
Version:        0~git20191105
Release:        0
Summary:        EasyRPG libretro core
License:        GPL-3.0
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake

%description
EasyRPG is a community project to create a free, open source, role playing game
creation tool, compatible with RPG Maker 2000/2003 games.

This package is for RetroArch/Libretro front-end.

%prep
%setup -q

%build
cd builds/libretro
make -f Makefile.libretro

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp builds/libretro/easyrpg_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/easyrpg_libretro.so

%changelog
