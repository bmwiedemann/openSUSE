#
# spec file for package libretro-dosbox
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


Name:           libretro-dosbox
Version:        0~git20190902
Release:        0
Summary:        DOSBOX libretro core for DOS emulation
License:        GPL-2.0
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
DOSBox is a DOS-emulator that uses the SDL-library which makes DOSBox very easy
to port to different platforms. DOSBox has already been ported to many different
platforms, such as Windows, BeOS, Linux, MacOS X...

This package is for RetroArch/Libretro front-end.

%prep
%setup -q

%build
make -f Makefile.libretro

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp dosbox_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/dosbox_libretro.so

%changelog
