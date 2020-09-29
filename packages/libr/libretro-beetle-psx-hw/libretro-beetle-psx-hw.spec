#
# spec file for package libretro-beetle-psx-hw
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


Name:           libretro-beetle-psx-hw
Version:        0~git20200921
Release:        0
Summary:        Mednafen PSX libretro core for Sony PlayStation emulation
License:        GPL-2.0-only
Group:          System/Emulators/Other
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  Mesa-devel
# GCC 4.8 bug only fixed in 4.9 https://gcc.gnu.org/bugzilla/show_bug.cgi?id=58016
BuildRequires:  gcc-c++ >= 4.9
BuildRequires:  make

%description
Standalone port/fork of Mednafen PSX to the Libretro API. This package supports
OpenGL or Vulkan hardware rendering.

%prep
%setup -q

%build
make HAVE_HW=1

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp mednafen_psx_hw_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/mednafen_psx_hw_libretro.so

%changelog
