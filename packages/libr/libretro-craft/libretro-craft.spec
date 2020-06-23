#
# spec file for package libretro-craft
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


Name:           libretro-craft
Version:        1.0~git20200504
Release:        0
Summary:        Craft libretro core
License:        GPL-3.0-only
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz
Patch1:         tinycthread.patch

BuildRequires:  Mesa-devel
BuildRequires:  gcc
BuildRequires:  make

%description
Minecraft clone for Windows, Mac OS X and Linux. Just a few thousand lines of C using modern OpenGL (shaders). Online multiplayer support is included using a Python-based server.

This package is for RetroArch/libretro front-end.

%prep
%setup -q
%patch1 -p1

%build
make -f Makefile.libretro

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp craft_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/craft_libretro.so

%changelog
