#
# spec file for package SDL_net
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


Name:           SDL_net
%define lname	libSDL_net-1_2-0
Version:        1.2.8
Release:        0
Summary:        SDL networking library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://libsdl.org/projects/SDL_net/release-1.2.html

# removed VisualC, Xcode, Xcode-iOS and Watcom-OS2.zip from the upstream tarball [bnc#508084]
Source:         %name-%version-repack.tar.bz2
Source2:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(sdl)

%description
This is a small cross-platform networking library for use with SDL.

%package -n %lname
Summary:        Simple DirectMedia Layer – Networking library
Group:          System/Libraries
Provides:       SDL_net = %version
Obsoletes:      SDL_net <= %version

%description -n %lname
This is a small cross-platform networking library for use with SDL.

%package -n libSDL_net-devel
Summary:        Development files for the SDL networking library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Provides:       SDL_net-devel = %version
Obsoletes:      SDL_net-devel <= %version

%description -n libSDL_net-devel
This is a small cross-platform networking library for use with SDL.

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
%_libdir/libSDL_net-1*.so.*

%files -n libSDL_net-devel
%defattr(-,root,root)
%_includedir/SDL/
%_libdir/libSDL_net.so
%_libdir/pkgconfig/SDL_net.pc

%changelog
