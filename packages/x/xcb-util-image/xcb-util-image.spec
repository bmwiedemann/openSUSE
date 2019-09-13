#
# spec file for package xcb-util-image
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           xcb-util-image
%define lname	libxcb-image0
Version:        0.4.0
Release:        0
Summary:        XCB utility module for XImage/XShmImage-like functions
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xcb.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xcb/util-image
#Git-Web:	http://cgit.freedesktop.org/xcb/util-image/
Source:         %name-%version.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.59c, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb) >= 1.4
BuildRequires:  pkgconfig(xcb-proto) >= 1.6
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xorg-macros) >= 1.6.0
BuildRequires:  pkgconfig(xproto) >= 7.0.8

%description
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

Included in this package is:

- image: Port of Xlib's XImage and XShmImage functions.

%package -n %lname
Summary:        XCB utility module for XImage/XShmImage-like functions
Group:          System/Libraries

%description -n %lname
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

Included in this package is:

- image: Port of Xlib's XImage and XShmImage functions.

%package devel
Summary:        Development files for the XCB image utility module
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

This package contains the development headers for the library found
in %lname.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libxcb-image.so.0*

%files devel
%defattr(-,root,root)
%_includedir/xcb
%_libdir/libxcb-image.so
%_libdir/pkgconfig/xcb-image.pc

%changelog
