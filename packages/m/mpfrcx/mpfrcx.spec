#
# spec file for package mpfrcx
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


Name:           mpfrcx
%define lname	libmpfrcx1
Version:        0.6
Release:        0
Summary:        Multi-precision floating-point arithmetic of univariate polynomials
License:        LGPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://www.multiprecision.org/mpfrcx
Source:         http://www.multiprecision.org/downloads/%name-%version.tar.gz
Source2:        http://www.multiprecision.org/downloads/%name-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  gmp-devel >= 4.3.2
BuildRequires:  mpc-devel >= 1
BuildRequires:  mpfr-devel >= 2.4.2

%description
MPFRCX is a library for the arithmetic of univariate polynomials over
arbitrary precision real or complex numbers.

%package -n %lname
Summary:        Multi-precision floating-point interval arithmetic computation library
Group:          System/Libraries

%description -n %lname
MPFRCX is a library for the arithmetic of univariate polynomials over
arbitrary precision real or complex numbers, without control on the
rounding.

The motivation for the library is to have functionality available for
the floating-point approach to complex multiplication.
Asymptotically-fast routines such as Toom–Cook and the FFT for
multiplication of polynomials are available, as well as fast routines
for interpolation and evaluation based on trees of polynomials.

%package devel
Summary:        Development files for the MPFRCX arithmetic computation library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       gmp-devel
Requires:       mpc-devel
Requires:       mpfr-devel

%description devel
MPFRCX is a library for the arithmetic of univariate polynomials over
arbitrary precision real or complex numbers.

This subpackage provides the development headers for it.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%check
%make_build check

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%post devel
%install_info --info-dir="%_infodir" "%_infodir/mpfrcx.info.gz"

%postun devel
%install_info_delete --info-dir="%_infodir" "%_infodir/mpfrcx.info.gz"

%files -n %lname
%_libdir/libmpfrcx.so.1*

%files devel
%_includedir/mpfrcx.h
%_libdir/libmpfrcx.so
%_infodir/mpfrcx.info*
%license COPYING*
%doc NEWS

%changelog
