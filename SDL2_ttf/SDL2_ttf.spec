#
# spec file for package SDL2_ttf
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           SDL2_ttf
%define lname	libSDL2_ttf-2_0-0
Version:        2.0.14
Release:        0
Summary:        SDL2 TrueType library
License:        Zlib
Group:          Development/Libraries/X11
Url:            http://libsdl.org/projects/SDL_ttf/

#Hg-Clone:	http://hg.libsdl.org/SDL_ttf/
Source:         http://libsdl.org/projects/SDL_ttf/release/%name-%version.tar.gz
Source2:        baselibs.conf
BuildRequires:  dos2unix
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(sdl2)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a sample library that allows you to use TrueType fonts in your
SDL applications.

%package -n %lname
Summary:        Simple DirectMedia Layer 2 – Truetype Library
Group:          System/Libraries
Provides:       SDL2_ttf = %version

%description -n %lname
This is a sample library that allows you to use TrueType fonts in your
SDL applications.

%package -n libSDL2_ttf-devel
Summary:        Simple DirectMedia Layer - Truetype Library
Group:          Development/Libraries/X11
Requires:       %lname = %version
Provides:       SDL2_ttf-devel = %version

%description -n libSDL2_ttf-devel
This is a sample library that allows you to use TrueType fonts in your
SDL applications.

%prep
%setup -q
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
%defattr(-,root,root)
%doc CHANGES.txt COPYING.txt README.txt
%_libdir/libSDL2_ttf-2*.so.*

%files -n libSDL2_ttf-devel
%defattr(-,root,root)
%_includedir/SDL2/
%_libdir/libSDL2_ttf.so
%_libdir/pkgconfig/SDL2_ttf.pc

%changelog
