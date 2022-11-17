#
# spec file for package libXft
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


Name:           libXft
%define lname	libXft2
Version:        2.3.7
Release:        0
Summary:        X FreeType library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXft
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXft/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
# ft2build include. Positive sideeffect is that this patch makes it build with both freetype2 2.5.1, and older versions
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Source1:        baselibs.conf
BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig) >= 2.5.92
BuildRequires:  pkgconfig(freetype2) >= 2.1.6
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xrender) >= 0.8.2

%description
Xft is a library that connects X applications with the FreeType font
rasterization library. Xft uses fontconfig to locate fonts so it has
no configuration files.

%package -n %lname
Summary:        X FreeType library
Group:          System/Libraries

%description -n %lname
Xft is a library that connects X applications with the FreeType font
rasterization library. Xft uses fontconfig to locate fonts so it has
no configuration files.

%package devel
Summary:        Development files for the X FreeType library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Xft is a library that connects X applications with the FreeType font
rasterization library. Xft uses fontconfig to locate fonts so it has
no configuration files.

This package contains the development headers for the library found
in %lname.

%prep
%setup -q

%build
autoreconf -fi
%configure --disable-static
%make_build

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libXft.so.2*

%files devel
%defattr(-,root,root)
%_includedir/X11/Xft
%_libdir/libXft.so
%_libdir/pkgconfig/xft.pc
%_mandir/man3/*

%changelog
