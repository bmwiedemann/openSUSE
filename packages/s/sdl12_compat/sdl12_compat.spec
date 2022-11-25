#
# spec file for package sdl12_compat
#
# Copyright (c) 2022 SUSE LLC
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


Name:           sdl12_compat
%define lname libSDL-1_2-0
%global _lto_cflags %_lto_cflags -ffat-lto-objects
Version:        1.2.60
Release:        0
Summary:        SDL-1.2 Compatibility Layer for Simple DirectMedia Layer 2.0
License:        MIT
Group:          Development/Libraries/X11
URL:            https://github.com/libsdl-org/sdl12-compat
Source:         https://github.com/libsdl-org/sdl12-compat/archive/refs/tags/release-%version.tar.gz
Source8:        baselibs.conf
Source9:        %name-rpmlintrc
BuildRequires:  cmake
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(sdl2)

%description
This is the "Simple DirectMedia Layer" library built from sdl12_compat.
it provides a binary and source compatible API for programs written
against SDL 1.2, but it uses SDL 2.0 behind the scenes.

%package -n %lname
Summary:        SDL Graphics Routines for Primitives and Other Support Functions
Group:          System/Libraries
Conflicts:      libSDL-1_2-0
%requires_eq    %(rpm --qf "%%{name}" -qf $(readlink -f %{_libdir}/libSDL2.so))

%description -n %lname
This is the "Simple DirectMedia Layer" library built from sdl12_compat.
it provides a binary and source compatible API for programs written
against SDL 1.2, but it uses SDL 2.0 behind the scenes.

%package devel
Summary:        Libraries, includes and more to develop SDL-1.2 applications
Group:          Development/Libraries/X11
Requires:       %lname = %version
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xproto)
Conflicts:      SDL-devel
Provides:       SDL-devel = %version-%release
Provides:       libSDL-devel = %version-%release

%description devel
This package contains files needed for development with the SDL
library.

%prep
%autosetup -p1 -n sdl12-compat-release-%version

%build
%cmake
%cmake_build

%install
%cmake_install
b="%buildroot"
ln -s sdl12_compat.pc "$b/%_libdir/pkgconfig/sdl.pc"
rm -v "$b/%_libdir"/*.a

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license LICENSE.txt
%_libdir/libSDL-1.2.so.*

%files devel
%_bindir/sdl-config
%_includedir/SDL/
%_datadir/aclocal/
%_libdir/pkgconfig/*.pc
%_libdir/libSDL*so

%changelog
