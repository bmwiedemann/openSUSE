#
# spec file for package SDL3_image
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


Name:           SDL3_image
%define lname	libSDL3_image0
Version:        3.2.0
Release:        0
Summary:        Simple DirectMedia Layer image loading library
License:        Zlib
Group:          Development/Libraries/X11
URL:            https://github.com/libsdl-org/SDL_image
Source:         https://github.com/libsdl-org/SDL_image/releases/download/release-%version/SDL3_image-%version.tar.gz
Source2:        https://github.com/libsdl-org/SDL_image/releases/download/release-%version/SDL3_image-%version.tar.gz.sig
Source9:        %name.keyring
BuildRequires:  cmake
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(sdl3)

%description
This is a library to load images of various formats as SDL
surfaces. This library supports the BMP, PPM, PCX, GIF, JPEG, PNG,
TIFF and WEBP formats.

%package -n %lname
Summary:        Simple DirectMedia Layer image loading library
Group:          System/Libraries
Provides:       SDL2_image = %version-%release

%description -n %lname
This is a library to load images of various formats as SDL
surfaces. This library supports the BMP, PPM, PCX, GIF, JPEG, PNG,
TIFF and WEBP formats.

%package devel
Summary:        Development files for the SDL3 image loader library
Group:          Development/Libraries/X11
Requires:       %lname = %version

%description devel
This is a library to load images of various formats as SDL
surfaces. This library supports the BMP, PPM, PCX, GIF, JPEG, PNG,
TIFF and WEBP formats.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
rm -Rf "%buildroot/%_datadir/licenses" # done via rpm %%license instead

%ldconfig_scriptlets -n %lname

%files -n %lname
%license LICENSE.txt
%_libdir/libSDL3_image.so.*

%files devel
%_includedir/SDL*
%_libdir/cmake/
%_libdir/pkgconfig/*.pc
%_libdir/libSDL3_image.so

%changelog
