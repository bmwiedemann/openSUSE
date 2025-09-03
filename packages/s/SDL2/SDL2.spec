#
# spec file for package SDL2
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           SDL2
Version:        2.32.10
Release:        0
Summary:        Simple DirectMedia Layer Library
License:        Zlib
Group:          Development/Libraries/X11
URL:            https://libsdl.org/
#Git-Clone:     https://github.com/libsdl-org/SDL
Source:         https://libsdl.org/release/%name-%version.tar.gz
Source2:        https://libsdl.org/release/%name-%version.tar.gz.sig
Source3:        %name.keyring
Patch1:         sdl2-symvers.patch
Patch2:         alsa-sig.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libdecor-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(alsa) >= 1.0.11
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv1_cm)
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
%define __global_provides_exclude_from %_libdir/SDL2

%description
This is the "Simple DirectMedia Layer" library. It provides a generic
API for access to audio, keyboard, mouse, and display framebuffer
across multiple platforms.

This package is provided for corner cases when sdl2_compat is
insufficient. To use original SDL2, exercise with the
LD_LIBRARY_PATH="%_libdir/SDL2" mechanism.

SDL2 uses dlopen, so if you experience problems under X11, check
again that libXrandr2 and libXi6 are in fact installed.

%prep
%autosetup -p1
perl -i -pe 's{\r\n}{\n}g' *.txt README.md

%build
%global _lto_cflags %_lto_cflags -ffat-lto-objects
# In this instance, we do want --with-pic because of libSDL2main.a.
%configure --with-pic --disable-alsa-shared --disable-video-directfb \
	--enable-video-kmsdrm --enable-video-wayland \
	--disable-fcitx \
%ifarch ix86
	--enable-sse2=no \
%endif
	--enable-sse3=no --disable-rpath --disable-3dnow
%make_build

%install
%make_install
b="%buildroot"
mkdir -pv "$b/%_libdir/SDL2"
mv -v "$b/%_libdir"/libSDL2-2.0.so.* "$b/%_libdir/SDL2/"
rm -Rf "$b/%_bindir" "$b/%_datadir" "$b/%_includedir" "$b/%_libdir/pkgconfig" \
	"$b/%_libdir"/lib* "$b/%_libdir/cmake"

%files
%license LICENSE.txt
%_libdir/SDL2/

%changelog
