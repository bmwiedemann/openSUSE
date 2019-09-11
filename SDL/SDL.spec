#
# spec file for package SDL
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


%define aalib   0

Name:           SDL
%define lname	libSDL-1_2-0
Version:        1.2.15
Release:        0
Summary:        Simple DirectMedia Layer Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/X11
Url:            http://libsdl.org/

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
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%if 0%{?aalib} == 1
BuildRequires:  aalib-devel
%endif
%if 0%{?suse_version} < 1120
BuildRequires:  arts-devel
%endif

%description
This is the "Simple DirectMedia Layer" library. It provides a generic
API for access to audio, keyboard, mouse, and display framebuffer
across multiple platforms.

%package -n %lname
Summary:        Simple DirectMedia Layer Library
# SDL was used last in 11.1
Group:          System/Libraries
Provides:       SDL = %version
Obsoletes:      SDL < %version
# bnc437293
%ifarch ppc64
Obsoletes:      SDL-64bit
%endif

%description -n %lname
This is the "Simple DirectMedia Layer" library. It provides a generic
API for access to audio, keyboard, mouse, and display framebuffer
across multiple platforms.

%package -n libSDL-devel
Summary:        SDL Library Developer Files
# SDL-devel was used last in 11.1
Group:          Development/Libraries/X11
Provides:       SDL-devel = %version
Obsoletes:      SDL-devel < %version
# bnc437293
%ifarch ppc64
Obsoletes:      SDL-devel-64bit
%endif
Requires:       %lname = %version
Requires:       c_compiler
Requires:       pkgconfig
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xproto)

%description -n libSDL-devel
This package contains files needed for development with the SDL
library.

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
%if 0%{?aalib}
    --enable-video-aalib \
%endif
    --disable-video-svga \
    --disable-video-ps3 \
    --with-pic
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la
rm "%buildroot/%_libdir"/libSDLmain.a
sed -i -e '/^Libs.private/d' "%buildroot/%_libdir/pkgconfig/sdl.pc"

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc BUGS COPYING CREDITS README README-SDL.txt
%_libdir/libSDL-1*.so.*

%files -n libSDL-devel
%defattr(-,root,root)
%doc docs.html README.HG TODO WhatsNew
%doc docs/index.html docs/html/ docs/images/
%_bindir/sdl-config
%_libdir/libSDL.so
%_includedir/SDL/
%_datadir/aclocal/
%_mandir/man3/*.3*
%_libdir/pkgconfig/sdl.pc

%changelog
