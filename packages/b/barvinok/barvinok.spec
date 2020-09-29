#
# spec file for package barvinok
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


%define lname	libbarvinok23
Name:           barvinok
Version:        0.41.3
Release:        0
Summary:        Library for computing homotopy continuation of roots
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://barvinok.gforge.inria.fr/
Source:         http://barvinok.gforge.inria.fr/%name-%version.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  glpk-devel
BuildRequires:  ntl-devel
BuildRequires:  pkgconfig(gmpxx)
BuildRequires:  pkgconfig(isl)
BuildRequires:  pkgconfig(polylibgmp)
Provides:       bundled(4ti2) = 1.3.1

%description
This is a library for computing homotopy continuation of a given root
of one dimensional sections of bivariate complex polynomials.

%package -n %lname
Summary:        Library for computing homotopy continuation of roots
Group:          System/Libraries

%description -n %lname
This is a library for computing homotopy continuation of a given root
of one dimensional sections of bivariate complex polynomials.

%package devel
Summary:        Development files for PolyLib
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
This is a library for computing homotopy continuation of a given root of one
dimensional sections of bivariate complex polynomials.

The output is a piecewise linear approximation of the path followed
by the root, with the property that there is a tubular neighborhood,
with square transversal section, that contains the actual path, and
there is a three times thicker tubular neighborhood guaranted to
contain no other root of the polynomial. This second property ensures
that the piecewise linear approximation computed from all roots of a
polynomial form a topologically correct deformation of the actual
braid, since the inner tubular neighborhoods cannot intersect.

This subpackage contains the include files and library links for
developing with PolyLib.

%prep
%autosetup -p1

%build
%configure --disable-static --enable-shared-barvinok \
	--with-isl=system --with-ntl=system --with-polylib=system
%make_build

%install
%make_install
find %buildroot -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_bindir/barvinok_*
%_bindir/iscc
%_bindir/polytope_scan

%files -n %lname
%_libdir/libbarvinok.so.23*

%files devel
%_includedir/barvinok/
%_libdir/libbarvinok.so
%_libdir/pkgconfig/*.pc
%license LICENSE

%changelog
