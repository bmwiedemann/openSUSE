#
# spec file for package SDL2_net
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define lname	libSDL2_net-2_0-0
Name:           SDL2_net
Version:        2.4.0
Release:        0
Summary:        SDL2 networking library
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://github.com/libsdl-org/SDL_net
Source:         https://www.libsdl.org/projects/SDL_net/release/%name-%version.tar.gz
Source2:        baselibs.conf
Patch1:         sdl2-symvers.patch
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(sdl2)

%description
This is a networking library for use with SDL.

%package -n %lname
Summary:        Simple DirectMedia Layer 2 – Networking library
Group:          System/Libraries
Provides:       SDL2_net = %version

%description -n %lname
This is a networking library for use with SDL.

%package devel
Summary:        Development files for the SDL2 networking library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version-%release
Obsoletes:      libSDL2_net-devel < %version-%release
Provides:       libSDL2_net-devel = %version-%release

%description devel
This is a networking library for use with SDL.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure --disable-static
%make_build
dos2unix CHANGES.txt README.txt

%install
%make_install
find %buildroot -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %lname

%files -n %lname
%license LICENSE.txt
%_libdir/libSDL2_net-2*.so.*

%files devel
%doc CHANGES.txt README.txt
%_includedir/SDL2/
%_libdir/libSDL2_net.so
%_libdir/pkgconfig/SDL2_net.pc
%_libdir/cmake/

%changelog
