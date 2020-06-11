#
# spec file for package libretro-desmume
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


Name:           libretro-desmume
Version:        0~git20190902
Release:        0
Summary:        DeSmuME libretro core for Nintendo DS emulation
License:        GPL-2.0-only
Group:          System/Emulators/Other
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  Mesa-devel
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  make
# On Arm, only armv7 is supported
ExcludeArch:    aarch64 armv6l armv6hl

%description
DeSmuME is a Nintendo DS emulator. This package is for
RetroArch/libretro front-end.

%prep
%setup -q

%build
cd desmume/src/frontend/libretro
make \
%ifarch armv7l armv7hl
  platform=classic_armv7_a7 \
  LDFLAGS="$LDFLAGS -pthread " \
%endif
  -f Makefile.libretro

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp desmume/src/frontend/libretro/desmume_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/desmume_libretro.so

%changelog
