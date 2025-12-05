#
# spec file for package sdl12_compat
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        1.2.72
Release:        0
Summary:        SDL-1.2 Compatibility Layer for Simple DirectMedia Layer 2.0
License:        MIT
Group:          Development/Libraries/X11
URL:            https://github.com/libsdl-org/sdl12-compat
Source:         https://github.com/libsdl-org/sdl12-compat/releases/download/release-%version/sdl12-compat-%version.tar.gz
Source2:        https://github.com/libsdl-org/sdl12-compat/releases/download/release-%version/sdl12-compat-%version.tar.gz.sig
Source7:        %name.keyring
Source8:        baselibs.conf
Source9:        %name-rpmlintrc
BuildRequires:  cmake
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xproto)

# A list of known apps/issues is at
# docs.google.com/spreadsheets/d/1u8Rq3LVQYYgu28sBuxrZ371QolbiZu5z_LjENc4ddZs/edit

%description
This is the "Simple DirectMedia Layer" library built from sdl12_compat.
it provides a binary and source compatible API for programs written
against SDL 1.2, but it uses SDL 2.0 behind the scenes.

%package -n %lname
Summary:        SDL Graphics Routines for Primitives and Other Support Functions
Group:          System/Libraries
%requires_eq libSDL2-2_0-0

%description -n %lname
This is the "Simple DirectMedia Layer" library built from sdl12_compat.
it provides a binary and source compatible API for programs written
against SDL 1.2, but it uses SDL 2.0 behind the scenes.

%package devel
Summary:        Libraries, includes and more to develop SDL-1.2 applications
Group:          Development/Libraries/X11
Requires:       %lname = %version
Requires:       pkgconfig(gl)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xproto)
Conflicts:      SDL-devel
Provides:       SDL-devel = %version-%release
Provides:       libSDL-devel = %version-%release

%description devel
This package contains files needed for development with the SDL
library.

%prep
%autosetup -p1 -n sdl12-compat-%version

%build
%cmake
%cmake_build

%install
%cmake_install
b="%buildroot"
%if 0%{?suse_version} < 1600
# pkgconfig 0.x does not know "Provides" lines; work around it.
ln -s sdl12_compat.pc "$b/%_libdir/pkgconfig/sdl.pc"
%endif
rm -v "$b/%_libdir"/*.a

%ldconfig_scriptlets -n %lname

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
