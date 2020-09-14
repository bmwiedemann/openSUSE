#
# spec file for package zn_poly
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


Name:           zn_poly
%define abiversion 0.9
%define lname	libzn_poly-0_9
Version:        0.9.2
Release:        0
Summary:        Library for polynomial arithmetic in Z/nZ[x]
License:        BSD-2-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Scientific/Math
URL:            https://gitlab.com/sagemath/zn_poly/
Source:         https://gitlab.com/sagemath/zn_poly/-/archive/%version/%name-%version.tar.bz2
Patch1:         znpoly-automake.diff
BuildRequires:  gmp-devel
BuildRequires:  libtool

%description
zn_poly is a C library for polynomial arithmetic in Z/nZ[x], where n
is any modulus that fits into an unsigned long.

%package -n %lname
Summary:        Library for polynomial arithmetic in Z/nZ[x]
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n %lname
zn_poly is a C library for polynomial arithmetic in Z/nZ[x], where n
is any modulus that fits into an unsigned long.

%package devel
Summary:        Development files for the zn_poly library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++

%description devel
zn_poly is a C library for polynomial arithmetic in Z/nZ[x], where n
is any modulus that fits into an unsigned long.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-static
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libzn_poly-%abiversion.so
%license COPYING

%files devel
%_libdir/libzn_poly.so
%_includedir/%name/

%changelog
