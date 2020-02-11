#
# spec file for package libretro-parallel-n64
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


Name:           libretro-parallel-n64
Version:        0~git20190917
Release:        0
Summary:        Parallel N64 libretro core for Nintendo 64 emulation
License:        GPL-3.0-only
Group:          System/Emulators/Other
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  Mesa-devel

%description
Optimized/rewritten Nintendo 64 emulator made specifically for Libretro.
Originally based on Mupen64 Plus.

%prep
%setup -q

%build
# https://github.com/libretro/libretro-super/blob/master/recipes/linux
%ifarch x86_64 amd64
    make WITH_DYNAREC=x86_64
%else
    %ifarch %ix86
        make WITH_DYNAREC=x86
    %else
        %ifarch %arm
            make WITH_DYNAREC=arm
        %else
            make
        %endif
    %endif
%endif

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp parallel_n64_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/parallel_n64_libretro.so

%changelog
