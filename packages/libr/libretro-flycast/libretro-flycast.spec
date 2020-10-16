#
# spec file for package libretro-flycast
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


Name:           libretro-flycast
Version:        0~git20201013
Release:        0
Summary:        Flycast libretro core for Sega Dreamcast emulation
License:        GPL-3.0-only
Group:          System/Emulators/Other
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  Mesa-devel
BuildRequires:  gcc-c++
BuildRequires:  make
ExcludeArch:    armv6l armv6hl

%description
Flycast is a multi-platform Sega Dreamcast emulator. This package is for
RetroArch/libretro front-end.

%prep
%setup -q

%build
%ifarch aarch64
export platform=arm64
export CC_AS=gcc
%endif
%ifarch %arm
export ARCH=arm
export platform=classic_armv7_a7
%endif
make

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp flycast_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/flycast_libretro.so

%changelog
