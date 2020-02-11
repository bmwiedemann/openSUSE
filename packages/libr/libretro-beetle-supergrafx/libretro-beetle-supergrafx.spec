#
# spec file for package libretro-beetle-supergrafx
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libretro-beetle-supergrafx
Version:        0~git20190911
Release:        0
Summary:        Mednafen PCE Fast libretro core for SuperGrafx TG-16 emulation
License:        GPL-2.0
Group:          System/Emulators/Other
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
Standalone port of Mednafen PCE Fast to libretro. This one only emulates a SuperGrafx TG-16.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp mednafen_supergrafx_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/mednafen_supergrafx_libretro.so

%changelog
