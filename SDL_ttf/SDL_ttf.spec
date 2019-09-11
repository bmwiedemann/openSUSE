#
# spec file for package SDL_ttf
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


Name:           SDL_ttf
%define lname	libSDL_ttf-2_0-0
#Note: thankfully no overlap with SDL2, which is libSDL2_ttf-2_0-0.
Version:        2.0.11
Release:        0
Summary:        SDL TrueType library
License:        Zlib
Group:          Development/Libraries/X11
Url:            http://libsdl.org/projects/SDL_ttf/release-1.2.html

# removed VisualC dir, Watcom-Win32.zip, Xcode and Xcode-iOS dirs from upstream tarball [bnc#508180]
Source:         %name-%version-repack.tar.bz2
Source2:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(sdl)

%description
This is a sample library that allows you to use TrueType fonts in your
SDL applications.

%package -n %lname
Summary:        Simple DirectMedia Layer – Truetype library
Group:          System/Libraries
Provides:       SDL_ttf = %version-%release
Obsoletes:      SDL_ttf < %version-%release

%description -n %lname
This is a sample library that allows you to use TrueType fonts in your
SDL applications.

%package -n libSDL_ttf-devel
Summary:        Development files for the SDL TrueType library
Group:          Development/Libraries/X11
Requires:       %lname = %version
Provides:       SDL_ttf-devel = %version-%release
Obsoletes:      SDL_ttf-devel < %version-%release

%description -n libSDL_ttf-devel
This is a sample library that allows you to use TrueType fonts in your
SDL applications.

%prep
%setup -q

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
%doc CHANGES COPYING README
%_libdir/libSDL_ttf-2*.so.*

%files -n libSDL_ttf-devel
%defattr(-,root,root)
%_includedir/SDL/
%_libdir/libSDL_ttf.so
%_libdir/pkgconfig/SDL_ttf.pc

%changelog
