#
# spec file for package SDL2_ttf
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


Name:           SDL2_ttf
%define lname	libSDL2_ttf-2_0-0
Version:        2.0.15
Release:        0
Summary:        Simple DirectMedia Layer 2 Truetype library
License:        Zlib
Group:          Development/Libraries/X11
URL:            https://libsdl.org/projects/SDL_ttf/

#Hg-Clone:	https://hg.libsdl.org/SDL_ttf/
Source:         https://libsdl.org/projects/SDL_ttf/release/%name-%version.tar.gz
Source2:        baselibs.conf
BuildRequires:  dos2unix
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(sdl2)

%description
This is a sample library that allows you to use TrueType fonts in your
SDL applications.

%package -n %lname
Summary:        Simple DirectMedia Layer 2 Truetype library
Group:          System/Libraries
Provides:       SDL2_ttf = %version

%description -n %lname
This is a sample library that allows you to use TrueType fonts in your
SDL applications.

%package -n libSDL2_ttf-devel
Summary:        Header files for the Simple DirectMedia Layer 2 Truetype library
Group:          Development/Libraries/X11
Requires:       %lname = %version
Provides:       SDL2_ttf-devel = %version

%description -n libSDL2_ttf-devel
This is a sample library that allows you to use TrueType fonts in your
SDL applications.

%prep
%autosetup -p1
dos2unix *.txt

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING.txt
%_libdir/libSDL2_ttf-2*.so.*

%files -n libSDL2_ttf-devel
%doc CHANGES.txt README.txt
%_includedir/SDL2/
%_libdir/libSDL2_ttf.so
%_libdir/pkgconfig/SDL2_ttf.pc

%changelog
