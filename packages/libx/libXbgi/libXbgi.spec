#
# spec file for package libXbgi
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


Name:           libXbgi
%define lname	libXbgi1
Version:        365
Release:        0
Summary:        BGI-compatible 2D graphics C library with X11 backend
License:        MIT AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://libXbgi.sf.net/

#Freecode-URL:	http://freecode.com/projects/libxbgi/
Source:         https://downloads.sf.net/libxbgi/xbgi-%version.tar.gz
Patch1:         xbgi-automake.diff
Patch2:         xbgi-getpixel.diff
Patch3:         xbgi-sequence.diff
Patch4:         xbgi-grapherrormsg.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)

%description
libXbgi is a Borland Graphics Interface (BGI) emulation library for
X11. This library strictly emulates most BGI functions, making it
possible to compile X11 versions of programs written for
Turbo/Borland C. RGB extensions and basic mouse support are also
implemented.

%package -n %lname
Summary:        BGI-compatible 2D graphics C library
License:        MIT
Group:          System/Libraries

%description -n %lname
libXbgi is a Borland Graphics Interface (BGI) emulation library for
X11. This library strictly emulates most BGI functions, making it
possible to compile X11 versions of programs written for
Turbo/Borland C. RGB extensions and basic mouse support are also
implemented.

%package devel
Summary:        Development files for the XBGI library
License:        MIT
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       libX11-devel
Requires:       xorg-x11-proto-devel

%description devel
libXbgi is a Borland Graphics Interface (BGI) emulation library for
X11. This library strictly emulates most BGI functions, making it
possible to compile X11 versions of programs written for
Turbo/Borland C. RGB extensions and basic mouse support are also
implemented.

This package contains the development headers for the library found
in %lname.

%prep
%autosetup -n xbgi-%version -p1

%build
autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%doc License.txt
%_libdir/libXbgi.so.1*

%files devel
%_includedir/graphics.h
%_libdir/libXbgi.so
%doc Functions.txt Using.txt README TODO.txt

%changelog
