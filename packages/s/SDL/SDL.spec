#
# spec file for package SDL
#
# Copyright (c) 2025 SUSE LLC
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


Name:           SDL
%define lname	libSDL-1_2-0
Version:        1.2.15
Release:        0
Summary:        Simple DirectMedia Layer Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/X11
URL:            http://libsdl.org/

#DL-URL:	http://libsdl.org/download-1.2.php
Source:         http://libsdl.org/release/%name-%version.tar.gz
Source2:        http://libsdl.org/release/%name-%version.tar.gz.sig
Source3:        %name.keyring
Source4:        baselibs.conf
# PATCH-FIX-OPENSUSE SDL-1.2.13-x11-keytounicode.patch
Patch0:         SDL-1.2.13-x11-keytounicode.patch
Patch1:         SDL_sdl_endian.patch
Patch2:         sdl-lfs.patch
Patch3:         libsdl-1.2.15-resizing.patch
Patch4:         SDL-1.2.15-Use-system-glext.h.patch
Patch5:         CVE-2019-7577.patch
Patch6:         CVE-2019-7575.patch
Patch7:         CVE-2019-7574.patch
Patch8:         CVE-2019-7572.patch
Patch9:         CVE-2019-7578.patch
Patch10:        CVE-2019-7635.patch
Patch11:        CVE-2019-7636.patch
Patch12:        CVE-2019-7637.patch
Patch13:        CVE-2019-13616.patch
Patch14:        CVE-2021-33657.patch
Patch15:        gcc15.patch
BuildRequires:  autoconf
BuildRequires:  nasm
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(alsa) >= 0.9.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libpulse-simple) >= 0.9
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
%define __global_provides_exclude_from %_libdir/SDL1

%description
This is the "Simple DirectMedia Layer" library. It provides a generic
API for access to audio, keyboard, mouse, and display framebuffer
across multiple platforms.

This package is provided for corner cases when sdl12_compat is insufficient
(e.g. with the "tcd" package). To use original SDL1, exercise
with the LD_LIBRARY_PATH="%_libdir/SDL1" mechanism.

%prep
%autosetup -p1
# remove the file to provide sufficient evidence that we are
# not using this file during the build [bnc#508111]
rm -f src/joystick/darwin/10.3.9-FIX/IOHIDLib.h

%build
./autogen.sh
# --with-pic is for libSDLmain.a
%configure \
    --disable-static \
    --disable-rpath \
    --disable-alsa-shared \
    --disable-x11-shared \
    --disable-pulseaudio-shared \
    --disable-esd-shared \
    --disable-osmesa-shared \
    --disable-video-svga \
    --disable-video-ps3 \
    --with-pic
%make_build

%install
# libtool can perform relink on install,
# so the .spec should not copy build/.libs/ manually
%make_install

b="%buildroot"
mkdir -p "$b/%_libdir/SDL1"
mv "$b/%_libdir"/libSDL-1.2.so.* "$b/%_libdir/SDL1"
rm -Rf "$b/%_bindir" "$b/%_datadir" "$b/%_includedir" "$b/%_libdir/pkgconfig" \
	"$b/%_libdir"/lib*

%files
%license COPYING
%_libdir/SDL1/

%changelog
