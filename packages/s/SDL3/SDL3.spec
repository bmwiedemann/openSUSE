#
# spec file for package SDL3
#
# Copyright (c) 2024 SUSE LLC
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


%define sle_version 0
Name:           SDL3
%define lname   libSDL3-0
Version:        3.1.6
Release:        0
Summary:        Simple DirectMedia Layer Library
License:        Zlib
Group:          Development/Libraries/X11
URL:            https://libsdl.org/
#Git-Clone:     https://github.com/libsdl-org/SDL
Source:         https://github.com/libsdl-org/SDL/releases/download/preview-%version/SDL3-%version.tar.gz
Source3:        %name.keyring
Source4:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libdecor-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(alsa) >= 1.0.11
BuildRequires:  pkgconfig(dbus-1)
%if !0%{?sle_version}
BuildRequires:  pkgconfig(fcitx)
%endif
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(ice)
# KMS/DRM driver needs libdrm and libgbm
BuildRequires:  pkgconfig(gbm) >= 11.1.0
BuildRequires:  pkgconfig(libdrm) >= 2.4.82
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.20
BuildRequires:  pkgconfig(libpulse-simple) >= 0.9
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(wayland-client) >= 1.18
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xxf86vm)

%description
This is the "Simple DirectMedia Layer" library. It provides a generic
API for access to audio, keyboard, mouse, and display framebuffer
across multiple platforms.

%package -n %lname
Summary:        Simple DirectMedia Layer Library
Group:          System/Libraries

%description -n %lname
This is the "Simple DirectMedia Layer" library. It provides a generic
API for access to audio, keyboard, mouse, and display framebuffer
across multiple platforms.

SDL uses dlopen, so if you experience problems under X11, check
again that libXrandr2 and libXi6 are in fact installed.

%package devel
Summary:        SDL3 Library Developer Files
Group:          Development/Libraries/X11
Requires:       %lname = %version-%release
Requires:       c_compiler
Requires:       pkgconfig
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glesv1_cm)
Requires:       pkgconfig(glesv2)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xproto)

%description devel
This package contains files needed for development with the SDL
library.

%package devel-doc
Summary:        Manual pages for the SDL3 API
Group:          Documentation/Man
BuildArch:      noarch

%description devel-doc
This package contains manual pages (in troff format) for the
SDL3 C API.

%prep
%autosetup -p1

%build
%global _lto_cflags %_lto_cflags -ffat-lto-objects
# SDL_*_SHARED=false -> link to libs rather than dlopen.
%cmake \
%ifarch %ix86
	-DSDL_MMX:BOOL=OFF -DSDL_SSE:BOOL=OFF -DSDL_SSE2:BOOL=OFF \
%endif
	-DSDL_SSE3:BOOL=OFF -DSDL_3DNOW:BOOL=OFF \
	-DSDL_ALSA_SHARED:BOOL=OFF -DSDL_LIBSAMPLERATE_SHARED:BOOL=OFF \
	-DSDL_PIPEWIRE_SHARED:BOOL=OFF -DSDL_PULSEAUDIO_SHARED:BOOL=OFF \
	-DSDL_X11_SHARED:BOOL=OFF -DSDL_WAYLAND_SHARED:BOOL=OFF \
	-DSDL_KMSDRM_SHARED:BOOL=OFF \
	-DSDL_STATIC:BOOL=OFF -DSDL_STATIC_PIC:BOOL=ON -DSDL_RPATH:BOOL=OFF \
	-DSDL_TEST_LIBRARY:BOOL=OFF -DSDL_DISABLE_INSTALL_DOCS:BOOL=OFF

%cmake_build

%install
%cmake_install
rm -Rf "%buildroot/%_datadir/licenses" # we use %%license

%ldconfig_scriptlets -n %lname

%files -n %lname
%license LICENSE.txt
%_libdir/libSDL3.so.0*

%files devel
%_libdir/libSDL3.so
%_includedir/SDL3/
%_libdir/pkgconfig/sdl3.pc
%_libdir/cmake/SDL3/

%files devel-doc
%_mandir/man3/*.3*

%changelog
