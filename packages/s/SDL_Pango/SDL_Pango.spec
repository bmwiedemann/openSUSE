#
# spec file for package SDL_Pango
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


%define lname	libSDL_Pango1
Name:           SDL_Pango
Version:        0.1.2
Release:        0
Summary:        Programming Pango via SDL
License:        LGPL-2.1-or-later
Group:          Development/Libraries/X11
URL:            http://sdlpango.sourceforge.net/
#CVS-Clone:	-d:pserver:anonymous@sdlpango.cvs.sourceforge.net:/cvsroot/sdlpango co -P SDL_Pango
Source:         %name-%version.tar.bz2
Patch1:         %name-%version-API-adds.patch
BuildRequires:  dos2unix
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(sdl)

%description
Pango is the text rendering engine of GNOME 2.x. SDL_Pango connects the
engine to SDL.

%package -n %lname
Summary:        Programming Pango via SDL
Group:          System/Libraries

%description -n %lname
Pango is the text rendering engine of GNOME 2.x. SDL_Pango connects the
engine to SDL.

%package devel
Summary:        Headers for SDL_Pango development
Group:          Development/Libraries/X11
Requires:       %lname = %version
Requires:       pkgconfig(sdl)
Provides:       libSDL_Pango-devel = %version-%release
Obsoletes:      libSDL_Pango-devel < %version-%release

%description devel
This package contains the necessary include files and libraries needed
to develop applications that require SDL_Pango.

%prep
%autosetup -p1
dos2unix AUTHORS README

%build
autoreconf -fiv
%configure --disable-static
%make_build

%install
%make_install
find %buildroot -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING
%doc AUTHORS README
%_libdir/libSDL_Pango.so.*

%files devel
%_includedir/SDL_Pango.h
%_libdir/pkgconfig/SDL_Pango.pc
%_libdir/libSDL_Pango.so

%changelog
