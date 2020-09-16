#
# spec file for package zmusic
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


Name:           zmusic
Version:        1.1.2
Release:        0
Summary:        ZDoom component library for music handling
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://zdoom.org/

#Git-Clone:     https://github.com/coelckers/ZMusic
Source:         https://github.com/coelckers/ZMusic/archive/%version.tar.gz
Patch1:         system-gme.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(zlib)
Suggests:       fluid-soundfont-gm
Suggests:       fluid-soundfont-gs
Suggests:       timidity
Suggests:       timidity-eawpats
# DUMB is modified to read OggVorbis samples
Provides:       bundled(dumb) = 0.9.3

%description
This is the music playback code from gzdoom, which was separated into its own
code repository starting with gzdoom-4.4.0.

%package -n libzmusic1
Summary:        ZDoom component library for music handling
Group:          System/Libraries

%description -n libzmusic1
This is the music playback code from gzdoom, which was separated into its own
code repository starting with gzdoom-4.4.0.

%package devel
Summary:        Headers for the ZMusic library
Group:          Development/Libraries/C and C++
Requires:       libzmusic1 = %version

%description devel
This subpackage contains the headers for the zmusic library, which is ZDoom's
music component library.

%prep
%autosetup -p1 -n ZMusic-%version

%build
# There is handcrafted assembler, which LTO does not play nice with.
%define _lto_cflags %nil

%ifarch %ix86
# Allow sw to use intrinsics (functions like _mm_set_sd).
# Guarded by cpuid calls by sw.
export CFLAGS="%optflags -msse -msse2"
export CXXFLAGS="%optflags -msse -msse2"
%endif
%cmake -DNO_STRIP=1 \
	-DCMAKE_SHARED_LINKER_FLAGS="" \
	-DCMAKE_EXE_LINKER_FLAGS="" -DCMAKE_MODULE_LINKER_FLAGS="" \
	-DINSTALL_DOCS_PATH="%_defaultdocdir/%name" \
	-DDYN_FLUIDSYNTH=OFF \
	-DDYN_SNDFILE=OFF -DDYN_MPG123=OFF
make %{?_smp_mflags}

%install
%cmake_install
b="%buildroot"
# Won't need lite (a subset with no GPL code) in openSUSE.
rm -f "$b/%_libdir"/libzmusiclite*

%post   -n libzmusic1 -p /sbin/ldconfig
%postun -n libzmusic1 -p /sbin/ldconfig

%files -n libzmusic1
%_libdir/libzmusic.so.1*
%license licenses/*

%files devel
%_includedir/*
%_libdir/libzmusic.so

%changelog
