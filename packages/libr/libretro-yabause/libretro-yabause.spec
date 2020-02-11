#
# spec file for package libretro-yabause
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libretro-yabause
Version:        0~git20190825
Release:        0
Summary:        Yabause libretro core for Sega Saturn emulation
License:        GPL-3.0-only
Group:          System/Emulators/Other
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  Mesa-devel
BuildRequires:  glu-devel

%description
Yabause is a Sega Saturn emulator. This package is for RetroArch/libretro
front-end.

%prep
%setup -q

%build
cd libretro
make

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp libretro/yabause_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/yabause_libretro.so

%changelog
