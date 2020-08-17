#
# spec file for package libretro-stella
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


Name:           libretro-stella
Version:        0~git20200804
Release:        0
Summary:        Stella libretro core for Atari 2600 emulation
License:        GPL-2.0-only
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
Stella is a multi-platform Atari 2600 VCS emulator which allows you to play all
of your favourite Atari 2600 games on your PC. This package is for RetroArch/
Libretro front-end.

%prep
%setup -q

%build
cd src/libretro
make

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp src/libretro/stella_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/stella_libretro.so

%changelog
