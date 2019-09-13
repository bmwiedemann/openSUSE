#
# spec file for package libXbgi
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libXbgi
%define lname	libXbgi1
Version:        364
Release:        0
Summary:        BGI-compatible 2D graphics C library with X11 backend
License:        MIT and GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            http://libXbgi.sf.net/

#Freecode-URL:	http://freecode.com/projects/libxbgi/
Source:         http://libxbgi.sf.net/xbgi-%version.tar.gz
Patch1:         xbgi-automake.diff
Patch2:         xbgi-getpixel.diff
Patch3:		xbgi-sequence.diff
Patch4:		xbgi-grapherrormsg.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
Group:          System/Libraries
License:        MIT

%description -n %lname
libXbgi is a Borland Graphics Interface (BGI) emulation library for
X11. This library strictly emulates most BGI functions, making it
possible to compile X11 versions of programs written for
Turbo/Borland C. RGB extensions and basic mouse support are also
implemented.

%package devel
Summary:        Development files for the XBGI library
Group:          Development/Libraries/C and C++
License:        MIT
Requires:       %lname = %version
Requires:	libX11-devel, xorg-x11-proto-devel

%description devel
libXbgi is a Borland Graphics Interface (BGI) emulation library for
X11. This library strictly emulates most BGI functions, making it
possible to compile X11 versions of programs written for
Turbo/Borland C. RGB extensions and basic mouse support are also
implemented.

This package contains the development headers for the library found
in %lname.

%prep
%setup -qn xbgi-%version
%patch -P 1 -P 2 -P 3 -P 4 -p1

%build
autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags} V=1;

%install
make install DESTDIR="%buildroot";
rm -f "%buildroot/%_libdir"/*.la;

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc License.txt
%_libdir/libXbgi.so.1*

%files devel
%defattr(-,root,root)
%_includedir/graphics.h
%_libdir/libXbgi.so
%doc Functions.txt Using.txt README TODO.txt

%changelog
