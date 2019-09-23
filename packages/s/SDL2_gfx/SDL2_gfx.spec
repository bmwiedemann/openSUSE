#
# spec file for package SDL2_gfx
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define lname	libSDL2_gfx-1_0-0
Name:           SDL2_gfx
Version:        1.0.4
Release:        0
Summary:        SDL2 Graphics Routines for Primitives and Other Support Functions
License:        Zlib
Group:          Development/Libraries/X11
URL:            http://www.ferzkopp.net/wordpress/2016/01/02/sdl_gfx-sdl2_gfx/
Source:         http://www.ferzkopp.net/Software/SDL2_gfx/%name-%version.tar.gz
Source2:        https://sourceforge.net/projects/sdl2gfx/files/%name-%version.tar.gz.asc
Source3:        baselibs.conf
# Key: 231D4B58E1DDB871, http://www.ferzkopp.net/wordpress/2016/01/02/sdl_gfx-sdl2_gfx/#comment-89
Source4:        %name.keyring
BuildRequires:  dos2unix
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(sdl2)

%description
Library containing 20+ graphics primitives (line, box, circle, polygon, etc.) for SDL2.

%package -n %lname
Summary:        SDL2 Graphics Routines for Primitives and Other Support Functions
Group:          System/Libraries
Provides:       SDL2_gfx = %version-%release

%description -n %lname
Library containing 20+ graphics primitives (line, box, circle, polygon, etc.) for SDL2.

%package -n libSDL2_gfx-devel
Summary:        Libraries, includes and more to develop SDL2_gfx applications
Group:          Development/Libraries/X11
Requires:       %lname = %version
Provides:       SDL2_gfx-devel = %version-%release

%description -n libSDL2_gfx-devel
Library containing 20+ graphics primitives (line, box, circle, polygon, etc.) for SDL2.

%prep
%setup -q

%build
%configure \
%ifnarch x86_64
	--disable-mmx \
%endif
	--disable-static
make %{?_smp_mflags}
dos2unix ChangeLog README
chmod 644 COPYING AUTHORS ChangeLog NEWS README

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%_libdir/lib*.so.*

%files -n libSDL2_gfx-devel
%_includedir/SDL2/
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc

%changelog
