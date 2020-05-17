#
# spec file for package libretro-pcsx-rearmed
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


Name:           libretro-pcsx-rearmed
Version:        0~git20200507
Release:        0
Summary:        ARM optimized PCSX core for PlayStation emulation
License:        GPL-2.0-only
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

Provides:       libretro-pcsx_rearmed = %{version}
Obsoletes:      libretro-pcsx_rearmed < %{version}

%description
PCSX ReARMed is yet another PCSX fork based on the PCSX-Reloaded project, which
itself contains code from PCSX, PCSX-df and PCSX-Revolution. This version is ARM
architecture oriented and features MIPS->ARM recompiler by Ari64, NEON GTE code
and more performance improvements. It was created for Pandora handheld, but should
be usable on other devices after some code adjustments (N900, GPH Wiz/Caanoo,
PlayBook versions are also available).

PCSX ReARMed features ARM NEON GPU by Exophase, that in many cases produces pixel
perfect graphics at very high performance. There is also Una-i's GPU plugin from
PCSX4ALL project, and traditional P.E.Op.S. one.

This package is for RetroArch/Libretro front-end.

%prep
%setup -q

%build
make -f Makefile.libretro DYNAREC=lightrec

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp pcsx_rearmed_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/pcsx_rearmed_libretro.so

%changelog
