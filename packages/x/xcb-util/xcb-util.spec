#
# spec file for package xcb-util
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


%define lname	libxcb-util1
Name:           xcb-util
Version:        0.4.1
Release:        0
Summary:        XCB utility modules
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://xcb.freedesktop.org/
#Git-Clone:	git://anongit.freedesktop.org/xcb/util
#Git-Web:	http://cgit.freedesktop.org/xcb/util/
Source:         https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
#git#BuildRequires:	autoconf >= 2.62, automake, libtool
BuildRequires:  gperf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb) >= 1.4
BuildRequires:  pkgconfig(xproto) >= 7.0.8

%description
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

Included in this package are:

- atom: Standard core X atom constants and atom caching.
- aux: Convenient access to connection setup and some core requests.
- event: Callback X event handling.

%package -n %{lname}
Summary:        XCB utility modules
Group:          System/Libraries

%description -n %{lname}
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

Included in this package are:

- atom: Standard core X atom constants and atom caching.
- aux: Convenient access to connection setup and some core requests.
- event: Callback X event handling.

%package devel
Summary:        Development files for the XCB utility modules
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

This package contains the development headers for the library found
in %{lname}.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/libxcb-util.so.1*

%files devel
%license COPYING
%doc README.md
%{_includedir}/xcb
%{_libdir}/libxcb-util.so
%{_libdir}/pkgconfig/xcb-*.pc

%changelog
