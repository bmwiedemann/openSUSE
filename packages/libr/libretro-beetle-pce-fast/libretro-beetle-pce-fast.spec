#
# spec file for package libretro-beetle-pce-fast
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


Name:           libretro-beetle-pce-fast
Version:        0~git20200523
Release:        0
Summary:        Mednafen PCE Fast libretro core for TurboGrafx-16/PC Engine emulation
License:        GPL-2.0-only
Group:          System/Emulators/Other
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

Provides:       libretro-mednafen-pce-fast
Obsoletes:      libretro-mednafen-pce-fast

%description
Standalone port of Mednafen PCE Fast to libretro.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp mednafen_pce_fast_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/mednafen_pce_fast_libretro.so

%changelog
