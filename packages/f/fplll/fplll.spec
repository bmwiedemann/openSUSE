#
# spec file for package fplll
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


Name:           fplll
%define lname   libfplll7
Version:        5.4.0
Release:        0
Summary:        Lenstra-Lovász Lattice Basis Reduction Algorithm Library
License:        LGPL-2.1-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/dstehle/fplll

#Git-Clone:	https://github.com/fplll/fplll
Source:         https://github.com/fplll/fplll/releases/download/%version/fplll-%version.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
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

%description -n fplll-devel
fplll contains several algorithms on lattices that rely on
floating-point computations. This includes implementations of the
floating-point LLL reduction algorithm, offering different
speed/guarantees ratios. It also includes a rigorous floating-point
implementation of the Kannan-Fincke-Pohst algorithm that finds a
shortest non-zero lattice vector.

This subpackage contains libraries and header files for developing
applications that want to make use of libfplll.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%_bindir/fplll
%_bindir/latticegen
%_datadir/fplll/
%doc COPYING NEWS README.md

%files -n %lname
%defattr(-,root,root)
%_libdir/libfplll.so.*

%files -n fplll-devel
%defattr(-,root,root)
%_includedir/fplll*
%_libdir/libfplll.so
%_libdir/pkgconfig/*.pc

%changelog
