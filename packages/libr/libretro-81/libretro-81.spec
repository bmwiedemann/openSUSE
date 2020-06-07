#
# spec file for package libretro-81
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


Name:           libretro-81
Version:        0~git20190918
Release:        0
Summary:        81 libretro core for ZX81 emulation
License:        GPL-3.0-only
Group:          System/Emulators/Other
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz
Patch0:         fix-multiple-definition-error.patch

BuildRequires:  gcc-c++
BuildRequires:  make

%description
A port of the EightyOne ZX81 Emulator to libretro

%prep
%setup -q
%patch0 -p1

%build
make

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp 81_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/81_libretro.so

%changelog
