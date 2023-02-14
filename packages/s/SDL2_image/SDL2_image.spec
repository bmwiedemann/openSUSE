#
# spec file for package SDL2_image
#
# Copyright (c) 2023 SUSE LLC
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


Name:           SDL2_image
%define lname	libSDL2_image-2_0-0
Version:        2.6.3
Release:        0
Summary:        Simple DirectMedia Layer 2 image loading library
License:        Zlib
Group:          Development/Libraries/X11
URL:            https://libsdl.org/projects/SDL_image/

#Hg-Clone:	http://hg.libsdl.org/SDL_image/
Source:         https://github.com/libsdl-org/SDL_image/releases/download/release-%version/SDL2_image-%version.tar.gz
BuildRequires:  SDL2-devel >= 2.24
BuildRequires:  dos2unix
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)

%description
This is a simple library to load images of various formats as SDL
surfaces. This library supports the BMP, PPM, PCX, GIF, JPEG, PNG,
TIFF and WEBP formats.

%package -n %lname
Summary:        Simple DirectMedia Layer 2 image loading library
Group:          System/Libraries
Provides:       SDL2_image = %version-%release

%description -n %lname
This is a simple library to load images of various formats as SDL
surfaces. This library supports the BMP, PPM, PCX, GIF, JPEG, PNG,
TIFF and WEBP formats.

%package devel
Summary:        Development files for the SDL2 image loader library
Group:          Development/Libraries/X11
Requires:       %lname = %version
Obsoletes:      libSDL2_image-devel < %version-%release
Provides:       libSDL2_image-devel = %version-%release

%description devel
This is a simple library to load images of various formats as SDL
surfaces. This library supports the BMP, PPM, PCX, GIF, JPEG, PNG,
TIFF and WEBP formats.

%prep
%autosetup -p1
dos2unix *.txt
rm -rf external

%build
# --disable-*-shared: Link, rather than dlopen.
#
%configure --disable-stb-image --disable-png-shared --disable-jpg-shared \
	--disable-tif-shared --disable-webp-shared --disable-static
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license LICENSE.txt
%_libdir/libSDL2_image-2*.so.*

%files devel
%doc CHANGES.txt README.txt
%_includedir/SDL2/
%_libdir/libSDL2_image.so
%_libdir/cmake/
%_libdir/pkgconfig/*.pc

%changelog
