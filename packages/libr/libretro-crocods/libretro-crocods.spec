#
# spec file for package libretro-crocods
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


Name:           libretro-crocods
Version:        0~git20200508
Release:        0
Summary:        CrocoDS libretro core for Amstrad emulation
License:        MIT
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
CrocoDS is the Amstrad emulator that boots fast and doesn't rely on keyboard.

This package is for RetroArch/libretro front-end.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp crocods_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/crocods_libretro.so

%changelog
