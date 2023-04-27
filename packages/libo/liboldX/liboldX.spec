#
# spec file for package liboldX
#
# Copyright (c) 2023 SUSE LLC
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


Name:           liboldX
%define lname	liboldX6
Version:        1.0.1
Release:        0
Summary:        X version 10 backwards compatibility library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://cgit.freedesktop.org/xorg/lib/liboldX/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/liboldX
Source:         http://xorg.freedesktop.org/releases/X11R7.0/src/lib/%{name}-X11R7.0-%{version}.tar.bz2
Source1:        baselibs.conf
#git#BuildRequires:	autoconf >= 2.57, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)

%description
X version 10 backwards compatibility for prehistoric X applications.

%package -n %lname
Summary:        X version 10 backwards compatibility library
Group:          System/Libraries

%description -n %lname
This interface provides backwards compatibility for apps from X
Version 10, which was the version of the X Window System from
November 1985, replaced by X11 in September 1987.

%package devel
Summary:        Development files for the X version 10 compatibility library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
X version 10 backwards compatibility for prehistoric X applications.

This package contains the development headers for the library found
in %lname.

%prep
%autosetup -n %name-X11R7.0-%version

%build
%configure --disable-static
%make_build

%install
%makeinstall
rm -f "%buildroot/%_libdir"/*.la

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/liboldX.so.6*

%files devel
%_includedir/X11/X10.h
%_libdir/liboldX.so
%_libdir/pkgconfig/oldx.pc

%changelog
