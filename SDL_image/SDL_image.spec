#
# spec file for package SDL_image
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           SDL_image
%define lname	libSDL_image-1_2-0
Version:        1.2.12
Release:        0
Summary:        SDL image loading library
License:        LGPL-2.1+
Group:          Development/Libraries/X11
Url:            http://libsdl.org/projects/SDL_image/release-1.2.html

# removed VisualC.zip, VisualCE.zip, Watcom-OS2.zip, Xcode.tar.gz, Xcode_iPhone.tar.gz from upstream tarball [bnc#508084]
Source:         %name-%version-repack.tar.bz2
Source3:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkg-config
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
%setup -q

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
%defattr(-,root,root)
%doc CHANGES COPYING README
%_libdir/libSDL_image-1*.so.*

%files -n libSDL_image-devel
%defattr(-,root,root)
%_includedir/SDL/
%_libdir/libSDL_image.so
%_libdir/pkgconfig/SDL_image.pc

%changelog
