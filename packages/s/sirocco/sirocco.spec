#
# spec file for package sirocco
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


%define lname	libsirocco0
Name:           sirocco
Version:        2.0.2
Release:        0
Summary:        Library for computing homotopy continuation of roots
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/miguelmarco/SIROCCO2
Source:         https://github.com/miguelmarco/SIROCCO2/releases/download/%version/libsirocco-%version.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  mpfr-devel

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
Summary:        Development files for sirocco, a math library
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
developing with the sirocco library.

%prep
%autosetup -p1 -n libsirocco-%version

%build
%configure --disable-static
%make_build

%install
%make_install
find %buildroot -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libsirocco.so.0*

%files devel
%license LICENSE
%_includedir/*
%_libdir/libsirocco.so

%changelog
