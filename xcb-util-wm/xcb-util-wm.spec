#
# spec file for package xcb-util-wm
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xcb-util-wm
Version:        0.4.1
Release:        0
Summary:        XCB utility module for client- and WM-side ICCCM helpers
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xcb.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xcb/util-wm
#Git-Web:	http://cgit.freedesktop.org/xcb/util-wm/
Source:         http://xorg.freedesktop.org/releases/individual/xcb/%{name}-%{version}.tar.bz2
Source99:       baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.62, automake, libtool
BuildRequires:  m4
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb) >= 1.4
BuildRequires:  pkgconfig(xorg-macros) >= 1.6.0

%description
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

Included in this package is:

- icccm: Both client and window-manager helpers for ICCCM.

%package -n libxcb-ewmh2
Summary:        XCB utility module for client- and WM-side ICCCM helpers
Group:          System/Libraries

%description -n libxcb-ewmh2
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

Included in this package is:

- icccm: Both client and window-manager helpers for ICCCM.

%package -n libxcb-icccm4
Summary:        XCB utility module for client- and WM-side ICCCM helpers
Group:          System/Libraries

%description -n libxcb-icccm4
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

Included in this package is:

- icccm: Both client and window-manager helpers for ICCCM.

%package devel
Summary:        Development files for the XCB EWMH/ICCCM utility modules
Group:          Development/Libraries/C and C++
Requires:       libxcb-ewmh2 = %version
Requires:       libxcb-icccm4 = %version

%description devel
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

This package contains the development headers for the library found
in libxcb-ewmh2, libxcb-icccm4.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la

%post   -n libxcb-ewmh2 -p /sbin/ldconfig
%postun -n libxcb-ewmh2 -p /sbin/ldconfig
%post   -n libxcb-icccm4 -p /sbin/ldconfig
%postun -n libxcb-icccm4 -p /sbin/ldconfig

%files -n libxcb-ewmh2
%defattr(-,root,root)
%_libdir/libxcb-ewmh.so.2*

%files -n libxcb-icccm4
%defattr(-,root,root)
%_libdir/libxcb-icccm.so.4*

%files devel
%defattr(-,root,root)
%_includedir/xcb
%_libdir/libxcb-ewmh.so
%_libdir/libxcb-icccm.so
%_libdir/pkgconfig/xcb-ewmh.pc
%_libdir/pkgconfig/xcb-icccm.pc

%changelog
