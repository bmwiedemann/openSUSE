#
# spec file for package cm
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


Name:           cm
Version:        0.3.1
Release:        0
Summary:        Class polynomial computation via floating point approximations
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://www.multiprecision.org/cm/
#Git-Clone:     https://gitlab.inria.fr/enge/cm
Source:         http://www.multiprecision.org/downloads/%name-%version.tar.gz
Source2:        http://www.multiprecision.org/downloads/%name-%version.tar.gz.asc
Source3:        %name.keyring
BuildRequires:  gmp-devel >= 4.3.2
BuildRequires:  mpc-devel >= 1
BuildRequires:  mpfr-devel >= 3
BuildRequires:  mpfrcx-devel >= 0.4
BuildRequires:  pari-devel >= 2.7
BuildRequires:  zlib-devel

%description
The CM software implements the construction of ring class fields of
imaginary quadratic number fields and of elliptic curves with complex
multiplication via floating point approximations.

%package devel
Summary:        Development files for the CM computation software
Group:          Development/Libraries/C and C++
Requires:       libcm1 = %version
Requires:       mpc-devel
Requires:       mpfrcx-devel
Requires:       zlib-devel

%description devel
The CM software implements the construction of ring class fields of
imaginary quadratic number fields and of elliptic curves with complex
multiplication via floating point approximations.

This subpackage provides the development headers for it.

%package -n libcm1
Summary:        Multi-precision floating-point interval arithmetic computation library
Group:          System/Libraries

%description -n libcm1
The CM software implements the construction of ring class fields of
imaginary quadratic number fields and of elliptic curves with complex
multiplication via floating point approximations.

It includes libraries that can be called from within a C program.

%package -n libmpfpx0
Summary:        Multi-precision floating-point polynomial library
Group:          System/Libraries

%description -n libmpfpx0
MPFPX is a GMP-based library for working with polynomials.

%package -n mpfpx-devel
Summary:        Header files for the multi-precision floating-point polynomial library
Group:          System/Libraries
Requires:       gmp-devel
Requires:       libmpfpx0 = %version

%description -n mpfpx-devel
MPFPX is a GMP-based library for working with polynomials.

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
if ! %make_build check; then
	cat tests/test-suite.log
	exit 1
fi

%post   -n libcm1 -p /sbin/ldconfig
%postun -n libcm1 -p /sbin/ldconfig
%post   -n libmpfpx0 -p /sbin/ldconfig
%postun -n libmpfpx0 -p /sbin/ldconfig

%post
%install_info --info-dir="%_infodir" "%_infodir/cm.info.gz"

%postun
%install_info_delete --info-dir="%_infodir" "%_infodir/cm.info.gz"

%files
%_bindir/classpol
%_bindir/cm
%_datadir/cm/
%_infodir/cm.info*

%files devel
%_includedir/cm_*.h
%_libdir/libcm*.so

%files -n libcm1
%_libdir/libcm_*.so.1*

%files -n libmpfpx0
%_libdir/libmpfpx.so.0*

%files -n mpfpx-devel
%_includedir/mpfpx.h
%_libdir/libmpfpx.so

%changelog
