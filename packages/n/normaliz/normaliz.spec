#
# spec file for package normaliz
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


Name:           normaliz
%define lname	libnormaliz3
Version:        3.8.9
Release:        0
Summary:        Tools for computations in affine monoids and rational cones
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.normaliz.uni-osnabrueck.de/

Source:         https://github.com/Normaliz/Normaliz/releases/download/v%version/%name-%version.tar.gz
BuildRequires:  flint-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  mpfr-devel

%description
Normaliz is a tool for computations in affine monoids, vector configurations,
lattice polytopes, and rational cones. It supports,

* convex hulls and dual cones
* conversion from generators to constraints and vice versa
* triangulations, disjoint decompositions and Stanley decompositions
* Hilbert basis of rational, not necessarily pointed cones
* normalization of affine monoids
* lattice points of rational polytopes and (unbounded) polyhedra
* Hilbert (or Ehrhart) series and (quasi) polynomials under
  Z-gradings (for example, for rational polytopes)
* generalized (or weighted) Ehrhart series and Lebesgue integrals of
  polynomials over rational polytopes via NmzIntegrate

%package -n %lname
Summary:        C++ API for Normaliz, a tool for computation of rotational cones
Group:          System/Libraries

%description -n %lname
Normaliz is a tool for computations in affine monoids, vector configurations,
lattice polytopes, and rational cones.

Normaliz offers an API, libnormaliz, that allows the user to access
the Normaliz computations from C++ programs.

%package devel
Summary:        Development files for Normaliz, a tool for computation of rotational cones
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       gmp-devel

%description devel
Normaliz is a tool for computations in affine monoids, vector configurations,
lattice polytopes, and rational cones.

Normaliz offers an API, libnormaliz, that allows the user to access
the Normaliz computations from C++ programs.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_bindir/normaliz
%license COPYING

%files -n %lname
%_libdir/libnormaliz.so.3*

%files devel
%_includedir/libnormaliz/
%_libdir/libnormaliz.so

%changelog
