#
# spec file for package cmh
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


Name:           cmh
%define lname   libcmh0
Version:        1.1.1
Release:        0
Summary:        Igusa (genus 2) class polynomial computation
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://www.multiprecision.org/cmh/
Source:         http://www.multiprecision.org/downloads/%name-%version.tar.gz
#Source2:        http://www.multiprecision.org/downloads/name-version.tar.gz.asc http 500
Source3:        %name.keyring
BuildRequires:  automake
BuildRequires:  fplll-devel >= 4
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel >= 5
BuildRequires:  libtool
BuildRequires:  mpc-devel >= 1
BuildRequires:  mpfr-devel >= 3
BuildRequires:  mpfrcx-devel >= 0.4.2
BuildRequires:  pari-devel >= 2.9
BuildRequires:  pari-gp
BuildRequires:  xz

%description
This software package computes Igusa (genus 2) class polynomials,
which parameterise the CM points in the moduli space of 2-dimensional
abelian varieties, i.e. Jacobians of hyperelliptic curves.

This program is also able to compute theta constants at arbitrary
precision.

%package -n %lname
Summary:        Igusa (genus 2) class polynomial computation library
Group:          System/Libraries

%description -n %lname
This library package computes Igusa (genus 2) class polynomials,
which parameterise the CM points in the moduli space of 2-dimensional
abelian varieties, i.e. Jacobians of hyperelliptic curves.

It includes libraries that can be called from within a C program.
This subpackage provides the development headers for CM.

%package devel
Summary:        Development files for the cmh library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       mpc-devel

%description devel
This software package computes Igusa (genus 2) class polynomials,
which parameterise the CM points in the moduli space of 2-dimensional
abelian varieties, i.e. Jacobians of hyperelliptic curves.

This subpackage provides the development headers for libcmh.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-static
%make_build

%install
%make_install
chmod a-x "%buildroot/%_datadir/cmh"/*.gp
rm -f "%buildroot/%_libdir"/*.la

%check
%make_build check

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_bindir/cm*
%_datadir/%name/
# plugins which are dlopened
%_libdir/cmh/

%files devel
%_includedir/cmh.h
%_libdir/libcmh.so

%files -n %lname
%_libdir/libcmh.so.0*

%changelog
