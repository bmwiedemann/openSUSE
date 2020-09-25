#
# spec file for package arb
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


Name:           arb
%define lname   libarb2
Version:        2.18.1
Release:        0
Summary:        Arbitrary-precision floating-point ball arithmetic library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Scientific/Math
URL:            http://fredrikj.net/arb/
#Git-Clone:	https://github.com/fredrik-johansson/arb/
Source:         https://github.com/fredrik-johansson/arb/archive/%version.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  flint-devel
BuildRequires:  gcc-c++
BuildRequires:  libmpir-devel
BuildRequires:  libtool
BuildRequires:  mpfr-devel

%description
Arb is a C library for arbitrary-precision floating-point ball
(mid-rad interval) arithmetic. It supports complex numbers,
polynomials, matrices, and evaluation of special functions, with
error bounding.

%package -n %lname
Summary:        Arbitrary-precision floating-point ball arithmetic library
Group:          System/Libraries

%description -n %lname
Arb is a C library for arbitrary-precision floating-point ball
(mid-rad interval) arithmetic. It supports complex numbers,
polynomials, matrices, and evaluation of special functions, with
error bounding.

%package devel
Summary:        Development files for Arb, an Arbitrary-precision ball arithmetic library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Arb is a C library for arbitrary-precision floating-point ball
(mid-rad interval) arithmetic. It supports complex numbers,
polynomials, matrices, and evaluation of special functions, with
error bounding.

This subpackage contains libraries and header files for developing
applications that want to make use of Arb.

%prep
%autosetup -p1

%build
# Not autoconf
./configure --prefix="%_prefix" --disable-static CFLAGS="%optflags"
%make_build verbose

%install
%make_install LIBDIR="%_lib"

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libarb.so.2*

%files devel
%_includedir/*.h
%_libdir/libarb.so
%license LICENSE
%doc doc/source/history.rst

%changelog
