#
# spec file for package xcb-util-keysyms
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


Name:           xcb-util-keysyms
%define lname	libxcb-keysyms1
Version:        0.4.0
Release:        0
Summary:        XCB utility module for X keycode constants and conversions
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xcb.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xcb/util-keysyms
#Git-Web:	http://cgit.freedesktop.org/xcb/util-keysyms/
Source:         %name-%version.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.59c, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb) >= 1.4
BuildRequires:  pkgconfig(xcb-proto) >= 1.6
BuildRequires:  pkgconfig(xorg-macros) >= 1.6.0
BuildRequires:  pkgconfig(xproto) >= 7.0.8

%description
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

Included in this package is:

- keysyms: Standard X key constants and conversion to/from keycodes.

%package -n %lname
Summary:        XCB utility module for X keycode constants and conversions
Group:          System/Libraries

%description -n %lname
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

Included in this package is:

- keysyms: Standard X key constants and conversion to/from keycodes.

%package devel
Summary:        Development files for the XCB keysyms utility module
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
%_libdir/libxcb-keysyms.so.1*

%files devel
%defattr(-,root,root)
%_includedir/xcb
%_libdir/libxcb-keysyms.so
%_libdir/pkgconfig/xcb-keysyms.pc

%changelog
