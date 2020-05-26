#
# spec file for package SDL_bgi
#
# Copyright (c) 2020 SUSE LLC
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


Name:           SDL_bgi
%define lname	libSDL_bgi-suse3
Version:        2.4.0
Release:        0
Summary:        BGI-compatible 2D graphics C library with SDL backend
License:        Zlib AND GPL-2.0-or-later
Group:          Development/Libraries/X11
URL:            http://libXbgi.sf.net/

#Git-Web:       https://github.com/genpfault/sdl-bgi
Source:         http://downloads.sf.net/libxbgi/%name-%version.tar.gz
Source9:        %name-rpmlintrc
Patch1:         sdlbgi-cmake.diff
BuildRequires:  cmake
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(sdl2)

%description
SDL_bgi is largely compatible with BGI, the Borland Graphics
Interface that was a standard in PC graphics back in the DOS days.
SDL_bgi also provides extensions for RGB colors and mouse support.

%package -n %lname
Summary:        SDL Graphics Routines for Primitives and Other Support Functions
Group:          System/Libraries

%description -n %lname
SDL_bgi is a Borland Graphics Interface (BGI) emulation library for
SDL. It provides extensions for RGB colors and mouse support.

%package -n libSDL_bgi-devel
Summary:        Libraries, includes and more to develop SDL_bgi applications
Group:          Development/Libraries/X11
Requires:       %lname = %version
Provides:       SDL_bgi-devel = %version-%release

%description -n libSDL_bgi-devel
SDL_bgi is a Borland Graphics Interface (BGI) emulation library for
SDL. It provides extensions for RGB colors and mouse support.

Unlike other BGI-compatible libraries, the purpose of SDL_bgi is not
full compatibility with BGI. Rather, it is meant to be an
introduction to SDL-based graphics: SDL and BGI commands can be mixed
together.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%cmake_install
b="%buildroot"
mkdir -p "$b/%_defaultdocdir"
mv "$b/%_datadir/doc/%name" "$b/%_defaultdocdir/"
# just a forwarder and conflicts with xbgi
rm -v "%buildroot/%_includedir/graphics.h"

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license LICENSE
%_libdir/libSDL_bgi.so.suse3

%files -n libSDL_bgi-devel
%_defaultdocdir/%name/
%_includedir/*
%_libdir/libSDL_bgi.so

%changelog
