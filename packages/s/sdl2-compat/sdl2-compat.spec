#
# spec file for package sdl2-compat
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


%define lname libSDL2-2_0-0
%global _lto_cflags %_lto_cflags -ffat-lto-objects
Name:           sdl2-compat
Version:        2.32.58
Release:        0
Summary:        SDL-2.0 Compatibility Layer for Simple DirectMedia Layer 3.0
License:        Zlib
Group:          Development/Libraries/X11
URL:            https://github.com/libsdl-org/sdl2-compat
Source:         https://github.com/libsdl-org/sdl2-compat/releases/download/release-%version/sdl2-compat-%version.tar.gz
Source2:        https://github.com/libsdl-org/sdl2-compat/releases/download/release-%version/sdl2-compat-%version.tar.gz.sig
Source3:        %name.keyring
Source8:        baselibs.conf
Source9:        %name-rpmlintrc
Patch1:         sdl2-symvers.patch
BuildRequires:  cmake
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(sdl3) >= 3.2.12

%description
This is the "Simple DirectMedia Layer" library built from sdl2-compat.
it provides a binary and source compatible API for programs written
against SDL 2.0, but it uses SDL 3.0 behind the scenes.

%package -n %lname
Summary:        SDL-2.0 Compatibility Layer for Simple DirectMedia Layer 3.0
Group:          System/Libraries
Requires:       libSDL3-0 >= 3.2.10
# "sdl2-compat 2.32.54: SDL3 library is too old (have 3.2.8, but
# need at least 3.2.10). Segmentation fault (core dumped)"

%description -n %lname
This is the "Simple DirectMedia Layer" library built from sdl2-compat.
it provides a binary and source compatible API for programs written
against SDL 2.0, but it uses SDL 3.0 behind the scenes.

%package devel
Summary:        Header and build system files for sdl2-compat
Group:          Development/Libraries/X11
Requires:       %lname = %version
Conflicts:      SDL2-devel
Provides:       SDL2-devel = %version-%release
# You should not add pkgconfig(x11) to sdl-devel; as far as SDL is concerned, it is optional.
# (Think outputting to Wayland, KMSDRM, or null.)
# https://github.com/libsdl-org/sdl2-compat/issues/405

%description devel
This package contains files needed for development with the SDL2
library.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
b="%buildroot"
%cmake_install
rm -Rf "$b/%_datadir/licenses" # using %%license instead
cd "$b/%_libdir/cmake/SDL2/"
%if 0%{?suse_version} < 1600
# pkgconfig 0.x does not know "Provides" lines; work around it.
ln -s sdl2-compat.pc "$b/%_libdir/pkgconfig/sdl2.pc"
%endif

%ldconfig_scriptlets -n %lname

%files -n %lname
%license LICENSE.txt
%_libdir/libSDL2-2.0.so.*

%files devel
%_bindir/sdl2-config
%_includedir/SDL2/
%_libdir/*SDL2*.a
%_libdir/*.so
%_libdir/cmake/
%_libdir/pkgconfig/*.pc
%_datadir/aclocal/

%changelog
