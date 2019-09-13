#
# spec file for package libgme
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define soname 0
Name:           libgme
Version:        0.6.2
Release:        0
Summary:        Collection of video game music file emulators
License:        LGPL-2.1+
Group:          System/Libraries
Url:            https://bitbucket.org/mpyne/game-music-emu/wiki/Home
Source0:        https://bitbucket.org/mpyne/game-music-emu/downloads/game-music-emu-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Game_Music_Emu is a collection of video game music file emulators that support
the following formats and systems:
- AY: ZX Spectrum/Amstrad CPC
- GBS: Nintendo Game Boy
- GYM: Sega Genesis/Mega Drive
- HES: NEC TurboGrafx-16/PC Engine
- KSS: MSX Home Computer/other Z80 systems (doesn't support FM sound)
- NSF/NSFE: Nintendo NES/Famicom (with VRC 6, Namco 106, and FME-7 sound)
- SAP: Atari systems using POKEY sound chip
- SPC: Super Nintendo/Super Famicom
- VGM/VGZ: Sega Master System/Mark III, Sega Genesis/Mega Drive,BBC Micro

%package -n libgme%{soname}
Summary:        Collection of video game music file emulators
Group:          System/Libraries

%description -n libgme%{soname}
Game_Music_Emu is a collection of video game music file emulators that support
the following formats and systems:
- AY: ZX Spectrum/Amstrad CPC
- GBS: Nintendo Game Boy
- GYM: Sega Genesis/Mega Drive
- HES: NEC TurboGrafx-16/PC Engine
- KSS: MSX Home Computer/other Z80 systems (doesn't support FM sound)
- NSF/NSFE: Nintendo NES/Famicom (with VRC 6, Namco 106, and FME-7 sound)
- SAP: Atari systems using POKEY sound chip
- SPC: Super Nintendo/Super Famicom
- VGM/VGZ: Sega Master System/Mark III, Sega Genesis/Mega Drive,BBC Micro

%package devel
Summary:        Development libraries and headers for libgme
Group:          Development/Libraries/C and C++
Requires:       libgme%{soname} = %{version}

%description devel
The developmental files that must be installed in order to compile applications
which use libgme.

%prep
%setup -q -n game-music-emu-%{version}
sed -i 's/\r$//' changes.txt design.txt gme.txt license.txt readme.txt

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%post -n libgme%{soname} -p /sbin/ldconfig

%postun -n libgme%{soname} -p /sbin/ldconfig

%files -n libgme%{soname}
%defattr(0644, root, root, 0755)
%doc changes.txt gme.txt license.txt readme.txt
%{_libdir}/libgme.so.%{soname}*

%files devel
%defattr(0644, root, root, 0755)
%doc design.txt
%{_includedir}/gme
%{_libdir}/libgme.so
%{_libdir}/pkgconfig/libgme.pc

%changelog
