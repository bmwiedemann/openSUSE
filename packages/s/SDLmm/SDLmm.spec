#
# spec file for package SDLmm
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


Name:           SDLmm
%define lname	libSDLmm-0_1-8
Version:        0.1.8
Release:        0
Summary:        C++ glue API for Simple DirectMedia Layer
License:        LGPL-2.1+
Group:          Development/Libraries/X11
Url:            http://sdlmm.sf.net/

Source:         http://downloads.sf.net/sdlmm/%name-%version.tar.bz2
Source2:        baselibs.conf
Patch:          %name-%version.patch
Patch1:         %name-%version-lib64.patch
Patch2:         %name-%version-autoheader.patch
Patch3:         %name-%version-m4.patch
Patch4:         %name-%version-makefile.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(sdl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SDLmm aims to stay as close as possible to the C API while taking
advantage of native C++ features like object oriented programming. It
also aims to be as platform independent as possible. In other words, it
tries to support every platform that SDL supports.

%package -n %lname
Summary:        Simple DirectMedia Layer C++ glue library
Group:          System/Libraries
Provides:       SDLmm = %version
Obsoletes:      SDLmm <= %version

%description -n %lname
SDLmm aims to stay as close as possible to the C API while taking
advantage of native C++ features like object oriented programming. It
also aims to be as platform independent as possible. In other words, it
tries to support every platform that SDL supports.

%package -n libSDLmm-devel
Summary:        Development files for the SDL C++ API layer
Group:          Development/Libraries/X11
Requires:       %lname = %version
Requires:       libSDL-devel
Requires:       libstdc++-devel
Provides:       SDLmm-devel = %version
Obsoletes:      SDLmm-devel <= %version

%description -n libSDLmm-devel
SDLmm aims to stay as close as possible to the C API while taking
advantage of native C++ features like object orientation. We will also
aim at being platform independent as much as possible. I.e we'll try to
support ever platform supported by SDL.

%prep
%setup -q
%patch
%patch1
%patch2
%patch3
%patch4
rm acconfig.h
rm acinclude.m4

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la docs/html/Makefil*

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README THANKS
%_libdir/*.so.*

%files -n libSDLmm-devel
%defattr(-,root,root)
%doc docs/html
%_bindir/sdlmm-config
%_includedir/SDLmm
%_libdir/*.so
%_mandir/man3/*
%_datadir/aclocal/*

%changelog
