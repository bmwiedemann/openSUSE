#
# spec file for package SDL2
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


%define sle_version 0
Name:           SDL2
%define lname   libSDL2-2_0-0
Version:        2.0.10
Release:        0
Summary:        Simple DirectMedia Layer Library
License:        Zlib
Group:          Development/Libraries/X11
URL:            http://libsdl.org/

#DL-URL:        http://libsdl.org/download-2.0.php
Source:         http://libsdl.org/release/%name-%version.tar.gz
Source2:        http://libsdl.org/release/%name-%version.tar.gz.sig
Source3:        %name.keyring
Source4:        baselibs.conf
Patch1:         sdl2-symvers.patch
Patch2:         SDL2-endian.patch
Patch3:         CVE-2019-13616.patch
Patch4:         sdl2-khronos.patch
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  nasm
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(alsa) >= 0.9.0
BuildRequires:  pkgconfig(dbus-1)
%if !0%{?sle_version}
BuildRequires:  pkgconfig(fcitx)
%endif
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv1_cm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(ice)
# KMS/DRM driver needs libdrm and libgbm
BuildRequires:  pkgconfig(gbm) >= 9.0.0
BuildRequires:  pkgconfig(libdrm) >= 2.4.46
%if 0%{?suse_version} > 1220
BuildRequires:  pkgconfig(tslib)
%endif
BuildRequires:  pkgconfig(libpulse-simple) >= 0.9
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(wayland-client)
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
Provides:       SDL2 = %version-%release

%description -n %lname
This is the "Simple DirectMedia Layer" library. It provides a generic
API for access to audio, keyboard, mouse, and display framebuffer
across multiple platforms.

%package -n libSDL2-devel
Summary:        SDL2 Library Developer Files
Group:          Development/Libraries/X11
Requires:       %lname = %version
Requires:       c_compiler
Requires:       pkgconfig
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glesv1_cm)
Requires:       pkgconfig(glesv2)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xproto)
Provides:       SDL2-devel = %version-%release

%description -n libSDL2-devel
This package contains files needed for development with the SDL2
library.

%prep
%autosetup -p1
dos2unix WhatsNew.txt
dos2unix TODO.txt
dos2unix BUGS.txt
dos2unix README-SDL.txt
dos2unix README.txt
dos2unix CREDITS.txt
dos2unix COPYING.txt

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
# In this instance, we do want --with-pic because of libSDL2main.a.
%configure --with-pic --disable-alsa-shared --disable-video-directfb \
	--enable-video-kmsdrm --enable-video-wayland \
%if 0%{?sle_version}
	--disable-fcitx \
%endif
%ifarch ix86
	--enable-sse2=no \
%endif
	--enable-sse3=no --disable-rpath --disable-3dnow
make %{?_smp_mflags} V=1

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la
# We do not want static libs, but using --disable-static leads to make aborting
# halfway through %%build. Now it can be removed though.
rm -f "%buildroot/%_libdir/"*.a

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING.txt
%doc BUGS.txt CREDITS.txt README.txt README-SDL.txt
%_libdir/libSDL2-2*.so.*

%files -n libSDL2-devel
%doc TODO.txt WhatsNew.txt
%_bindir/sdl2-config
%_libdir/libSDL2.so
%_includedir/SDL2/
%_datadir/aclocal/sdl2.m4
%_libdir/pkgconfig/sdl2.pc
%_libdir/cmake/SDL2/

%changelog
