#
# spec file for package libgtpnl
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


Name:           libgtpnl
Version:        1.2.1
Release:        0
Summary:        GPRS tunnel configuration library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://osmocom.org/projects/linux-kernel-gtp-u/wiki

Source:         %name-%version.tar.xz
BuildRequires:  libtool >= 2
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(libmnl) >= 1.0.0

%description
libgtpnl wraps the genetlink-based GPRS tunnel configuration of the
Linux kernel into a C API.

%package -n libgtpnl0
Summary:        GPRS tunnel configuration library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libgtpnl0
libgtpnl wraps the genetlink-based GPRS tunnel configuration of the
Linux kernel into a C API.

%package devel
Summary:        Development files for the GPRS tunnel config library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libgtpnl0 = %version

%description devel
libgtpnl wraps the genetlink-based GPRS tunnel configuration of the
Linux kernel into a C API.

This subpackage contains libraries and header files for developing
applications that want to make use of libgtpnl.

%prep
%autosetup -p1

%build
echo "%version" >.tarball-version
autoreconf -fi
# bugzilla.opensuse.org/795968 for rationale
%configure --includedir="%_includedir/%name"
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%check
%make_build check

%post   -n libgtpnl0 -p /sbin/ldconfig
%postun -n libgtpnl0 -p /sbin/ldconfig

%files -n libgtpnl0
%_libdir/libgtpnl.so.0*

%files devel
%license COPYING
%_includedir/libgtpnl/
%_libdir/libgtpnl.so
%_libdir/pkgconfig/*.pc

%changelog
