#
# spec file for package fplll
#
# Copyright (c) 2023 SUSE LLC
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


Name:           fplll
%define lname   libfplll8
Version:        5.4.4
Release:        0
Summary:        Lenstra-Lovász Lattice Basis Reduction Algorithm Library
License:        LGPL-2.1-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/dstehle/fplll

#Git-Clone:	https://github.com/fplll/fplll
Source:         https://github.com/fplll/fplll/releases/download/%version/fplll-%version.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  memory-constraints
BuildRequires:  mpfr-devel
BuildRequires:  pkg-config

%description
fplll contains several algorithms on lattices that rely on
floating-point computations. This includes implementations of the
floating-point LLL reduction algorithm, offering different
speed/guarantees ratios. It also includes a rigorous floating-point
implementation of the Kannan-Fincke-Pohst algorithm that finds a
shortest non-zero lattice vector.

%package -n %lname
Summary:        Lenstra-Lovász Lattice Basis Reduction Algorithm Library
Group:          System/Libraries

%description -n %lname
fplll contains several algorithms on lattices that rely on
floating-point computations. This includes implementations of the
floating-point LLL reduction algorithm, offering different
speed/guarantees ratios. It also includes a rigorous floating-point
implementation of the Kannan-Fincke-Pohst algorithm that finds a
shortest non-zero lattice vector.

%package devel
Summary:        Development files for Lattice Basis Reduction with libfplll
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Obsoletes:      libfplll-devel < %version-%release
Provides:       libfplll-devel = %version-%release

%description devel
fplll contains several algorithms on lattices that rely on
floating-point computations. This includes implementations of the
floating-point LLL reduction algorithm, offering different
speed/guarantees ratios. It also includes a rigorous floating-point
implementation of the Kannan-Fincke-Pohst algorithm that finds a
shortest non-zero lattice vector.

This subpackage contains libraries and header files for developing
applications that want to make use of libfplll.

%prep
%autosetup

%build
%limit_build -m 1700
%configure --disable-static
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%doc NEWS README.md
%license COPYING
%_bindir/fplll
%_bindir/latticegen
%_datadir/fplll/

%files -n %lname
%_libdir/libfplll.so.*

%files devel
%_includedir/fplll*
%_libdir/libfplll.so
%_libdir/pkgconfig/*.pc

%changelog
