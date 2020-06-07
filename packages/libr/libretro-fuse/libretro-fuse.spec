#
# spec file for package libretro-fuse
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


Name:           libretro-fuse
Version:        0~git20200506
Release:        0
Summary:        Fuse libretro core for ZX Spectrum emulation
License:        GPL-3.0-only
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
Fuse (the Free Unix Spectrum Emulator) was originally, and somewhat unsurprisingly,
a ZX Spectrum emulator for Unix. However, it has now also been ported to Mac OS X,
which may or may not count as a Unix variant depending on your advocacy position.
It has also been ported to Windows, the Wii, AmigaOS and MorphOS, which are definitely
not Unix variants. This package is for RetroArch/Libretro front-end.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp fuse_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/fuse_libretro.so

%changelog
