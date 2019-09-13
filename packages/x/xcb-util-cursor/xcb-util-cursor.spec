#
# spec file for package xcb-util-cursor
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


%define lname   libxcb-cursor0
Name:           xcb-util-cursor
Version:        0.1.3
Release:        0
Summary:        XCB cursor library (libxcursor port)
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xcb.freedesktop.org/
#Git-Clone:	git://anongit.freedesktop.org/xcb/util-cursor
#Git-Web:	http://cgit.freedesktop.org/xcb/util-cursor/
Source:         http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gperf
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb) >= 1.4
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-proto) >= 1.6
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xorg-macros) >= 1.6.0

%description
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

Included in this package is:

- cursor: port of libxcursor

%package -n %{lname}
Summary:        XCB cursor library (libxcursor port)
Group:          System/Libraries

%description -n %{lname}
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

Included in this package is:

- cursor: port of libxcursor

%package devel
Summary:        Development files for the XCB cursor library (libxcursor port)
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

This package contains the development headers for the library found
in %{lname}.

%prep
%setup -q

%build
autoreconf -fiv
%configure \
  --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/libxcb-cursor.so.0*

%files devel
%{_includedir}/xcb
%{_libdir}/libxcb-cursor.so
%{_libdir}/pkgconfig/xcb-cursor.pc

%changelog
