#
# spec file for package libretro-blastem
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


Name:           libretro-blastem
Version:        0~git20190620
Release:        0
Summary:        BlastEm libretro core for Sega Genesis emulation
License:        GPL-3.0-only
Group:          System/Emulators/Other
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz
Patch0:         fix-enum-syntax.patch
ExclusiveArch:  x86_64 i586
BuildRequires:  gcc-c++
BuildRequires:  make

%description
BlastEm is an open source, higly accurate emulator for the Genesis/Megadrive
that runs on modest hardware. This package is for RetroArch/libretro front-end.

%prep
%setup -q
%patch0 -p1

%build
%ifarch x86_64
make -f Makefile.libretro
%endif
%ifarch %ix86
make -f Makefile.libretro ABI=i686
%endif

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp blastem_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/blastem_libretro.so

%changelog
