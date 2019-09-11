#
# spec file for package SDL_gfx
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define lname	libSDL_gfx15
Name:           SDL_gfx
Version:        2.0.26
Release:        0
Summary:        SDL Graphics Routines for Primitives and Other Support Functions
License:        Zlib
Group:          Development/Libraries/X11
URL:            http://www.ferzkopp.net/wordpress/2016/01/02/sdl_gfx-sdl2_gfx/
Source:         http://www.ferzkopp.net/Software/SDL_gfx-2.0/%name-%version.tar.gz
Source2:        baselibs.conf
BuildRequires:  dos2unix
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sdl)

%description
The SDL_gfx library evolved out of the SDL_gfxPrimitives code which
provided basic drawing routines such as lines, circles or polygons and
SDL_rotozoom which implemented a interpolating rotozoomer for SDL
surfaces.

%package -n %lname
Summary:        SDL Graphics Routines for Primitives and Other Support Functions
Group:          System/Libraries
Provides:       SDL_gfx = %version-%release
Obsoletes:      SDL_gfx < %version-%release

%description -n %lname
The SDL_gfx library evolved out of the SDL_gfxPrimitives code which
provided basic drawing routines such as lines, circles or polygons and
SDL_rotozoom which implemented a interpolating rotozoomer for SDL
surfaces.

%package -n libSDL_gfx-devel
Summary:        Libraries, includes and more to develop SDL_gfx applications
Group:          Development/Libraries/X11
Requires:       %lname = %version
Provides:       SDL_gfx-devel = %{version}
Obsoletes:      SDL_gfx-devel < %{version}

%description -n libSDL_gfx-devel
The SDL_gfx library evolved out of the SDL_gfxPrimitives code which
provided basic drawing routines such as lines, circles or polygons and
SDL_rotozoom which implemented a interpolating rotozoomer for SDL
surfaces. The current components of the SDL_gfx library are:

- Graphic Primitives (SDL_gfxPrimitves.h)

- Rotozoomer (SDL_rotozoom.h)

- Framerate control (SDL_framerate.h)

- MMX image filters (SDL_imageFilter.h)

The library is backwards compatible to the above mentioned code. It is
written in plain C and can be used in C++ code.

%prep
%setup -q

%build
# MMX code has a problem with uninitialized variables; we would only turn it
# on for x86_64 anyway - but that one can use SSE instead.
%configure --disable-static --disable-mmx
make %{?_smp_mflags}
dos2unix README
chmod 644 LICENSE AUTHORS ChangeLog NEWS README

%install
%make_install
find %buildroot -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license LICENSE
%doc AUTHORS ChangeLog NEWS README
%_libdir/libSDL_gfx.so.15*

%files -n libSDL_gfx-devel
%_includedir/SDL/
%_libdir/lib*.so
%_libdir/pkgconfig/SDL_gfx.pc

%changelog
