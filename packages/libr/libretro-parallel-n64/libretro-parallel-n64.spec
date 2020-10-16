#
# spec file for package libretro-parallel-n64
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


Name:           libretro-parallel-n64
Version:        0~git20201011
Release:        0
Summary:        Parallel N64 libretro core for Nintendo 64 emulation
License:        GPL-3.0-only
Group:          System/Emulators/Other
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  Mesa-devel
BuildRequires:  gcc-c++
BuildRequires:  make

ExcludeArch:    armv6l armv6hl

%description
Optimized/rewritten Nintendo 64 emulator made specifically for Libretro.
Originally based on Mupen64 Plus.

%prep
%setup -q

%build
sed -i "s#aarch64-linux-gnu-##" Makefile
# https://github.com/libretro/libretro-super/blob/master/recipes/linux
%ifarch x86_64
    make WITH_DYNAREC=x86_64 HAVE_PARALLEL_RSP=1 HAVE_THR_AL=1
%endif
%ifarch %ix86
    make WITH_DYNAREC=x86 HAVE_PARALLEL_RSP=1 HAVE_THR_AL=1
%endif
%ifarch %arm
    make WITH_DYNAREC=arm HAVE_THR_AL=1 platform=classic_armv7_a7
%endif
%ifarch aarch64
    make WITH_DYNAREC=aarch64 HAVE_THR_AL=1 platform=armv8
%endif

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp parallel_n64_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/parallel_n64_libretro.so

%changelog
