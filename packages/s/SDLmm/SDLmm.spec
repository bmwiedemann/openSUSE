#
# spec file for package SDLmm
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


Name:           SDLmm
%define lname	libSDLmm-0_1-8
Version:        0.1.8
Release:        0
Summary:        C++ glue API for Simple DirectMedia Layer
License:        LGPL-2.1-or-later
Group:          Development/Libraries/X11
URL:            http://sdlmm.sf.net/

Source:         http://downloads.sf.net/sdlmm/%name-%version.tar.bz2
Patch:          %name-%version.patch
Patch1:         %name-%version-lib64.patch
Patch2:         %name-%version-autoheader.patch
Patch3:         %name-%version-m4.patch
Patch4:         %name-%version-makefile.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(sdl)

%description
SDLmm takes advantage of native C++ features like object oriented
programming while programming SDL.

%package -n %lname
Summary:        Simple DirectMedia Layer C++ glue library
Group:          System/Libraries

%description -n %lname
SDLmm takes advantage of native C++ features like object oriented
programming while programming SDL.

%package devel
Summary:        Development files for the SDL C++ API layer
Group:          Development/Libraries/X11
Requires:       %lname = %version
Requires:       libstdc++-devel
Requires:       pkgconfig(sdl)
Provides:       libSDLmm-devel = %version
Obsoletes:      libSDLmm-devel <= %version

%description devel
SDLmm takes advantage of native C++ features like object oriented
programming while programming SDL.

%prep
%autosetup -p0
rm -fv acconfig.h acinclude.m4

%build
autoreconf -fi
%configure --disable-static
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la docs/html/Makefil*

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING
%_libdir/*.so.*

%files devel
%doc AUTHORS NEWS README THANKS
%doc docs/html
%_bindir/sdlmm-config
%_includedir/SDLmm
%_libdir/*.so
%_mandir/man3/*
%_datadir/aclocal/*

%changelog
