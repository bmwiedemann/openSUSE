#
# spec file for package normaliz
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           normaliz
Version:        3.6.3
Release:        0
Summary:        Tools for computations in affine monoids and rational cones
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
Url:            https://www.normaliz.uni-osnabrueck.de/

Source:         https://github.com/Normaliz/Normaliz/releases/download/v%version/%name-%version.tar.gz
BuildRequires:  boost-devel
BuildRequires:  cmake >= 2.6
#maybe with flint-devel later on
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Normaliz is an open source tool for computations in affine monoids,
vector configurations, lattice polytopes, and rational cones.

Computation goals

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

%package -n libnormaliz0
Summary:        C++ API for Normaliz, a tool for computation of rotational cones
Group:          System/Libraries

%description -n libnormaliz0
Normaliz is an open source tool for computations in affine monoids,
vector configurations, lattice polytopes, and rational cones.

Normaliz offers an API - libnormaliz - that allows the user to access
the Normaliz computations from any C++ program.

%package devel
Summary:        Development files for Normaliz, a tool for computation of rotational cones
Group:          Development/Libraries/C and C++
Requires:       boost-devel
Requires:       gmp-devel
Requires:       libnormaliz0 = %version

%description devel
Normaliz is an open source tool for computations in affine monoids,
vector configurations, lattice polytopes, and rational cones.

Normaliz offers an API - libnormaliz - that allows the user to access
the Normaliz computations from any C++ program.

%prep
%setup -q

%build
pushd source/
%cmake
make %{?_smp_mflags}
popd

%install
pushd source/
%cmake_install
popd

%post   -n libnormaliz0 -p /sbin/ldconfig
%postun -n libnormaliz0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%_bindir/normaliz
%license COPYING

%files -n libnormaliz0
%defattr(-,root,root)
%_libdir/libnormaliz.so.*

%files devel
%defattr(-,root,root)
%_includedir/libnormaliz/
%_libdir/libnormaliz.so

%changelog
