#
# spec file for package SDL_image
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


Name:           SDL_image
%define lname	libSDL_image-1_2-0
Version:        1.2.12+hg695
Release:        0
Summary:        SDL image loading library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/X11
URL:            https://libsdl.org/projects/SDL_image/release-1.2.html

#Hg-Clone:	http://hg.libsdl.org/SDL_image/
Source:         %name-%version.tar.xz
Source3:        baselibs.conf
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(sdl)

%description
This is a simple library to load images of various formats as SDL
surfaces. This library supports the BMP, PPM, PCX, GIF, JPEG, PNG,
TIFF and WEBP formats.

%package -n %lname
Summary:        Simple DirectMedia Layer – Image loading library
Group:          System/Libraries
Provides:       SDL_image = %version-%release
Obsoletes:      SDL_image < %version-%release

%description -n %lname
This is a simple library to load images of various formats as SDL
surfaces. This library supports the BMP, PPM, PCX, GIF, JPEG, PNG,
TIFF and WEBP formats.

%package -n libSDL_image-devel
Summary:        Libraries, includes and more to develop SDL_image applications
Group:          Development/Libraries/X11
Requires:       %lname = %{version}
Provides:       SDL_image-devel = %version-%release
Obsoletes:      SDL_image-devel < %version-%release

%description -n libSDL_image-devel
This is a simple library to load images of various formats as SDL
surfaces. This library supports the BMP, PPM, PCX, GIF, JPEG, PNG,
TIFF and WEBP formats.

%prep
%autosetup -p1

%build
%configure --disable-png-shared --disable-jpg-shared --disable-tif-shared \
	--disable-webp-shared --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING
%_libdir/libSDL_image-1*.so.*

%files -n libSDL_image-devel
%doc CHANGES README
%_includedir/SDL/
%_libdir/libSDL_image.so
%_libdir/pkgconfig/SDL_image.pc

%changelog
