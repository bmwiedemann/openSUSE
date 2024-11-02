#
# spec file for package cm
#
# Copyright (c) 2024 SUSE LLC
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
Version:        0.4.3
Release:        0
Summary:        Class polynomial computation via floating point approximations
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.multiprecision.org/cm/
#Git-Clone:     https://gitlab.inria.fr/enge/cm
Source:         http://www.multiprecision.org/downloads/%name-%version.tar.gz
Source2:        http://www.multiprecision.org/downloads/%name-%version.tar.gz.asc
Source3:        %name.keyring
Patch1:         0001-Include-standard-header-file.patch
BuildRequires:  flint-devel >= 3
BuildRequires:  gmp-devel >= 4.3.2
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  mpc-devel >= 1
BuildRequires:  mpfr-devel >= 3
BuildRequires:  mpfrcx-devel >= 0.6.3
BuildRequires:  pari-devel >= 2.11
BuildRequires:  zlib-devel

%description
The CM software implements the construction of ring class fields of
imaginary quadratic number fields and of elliptic curves with complex
multiplication via floating point approximations.

%package devel
Summary:        Development files for the CM computation software
Group:          Development/Libraries/C and C++
Requires:       libcm1 = %version-%release
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

%prep
%autosetup -p1

%build
autoreconf -fi
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

%ldconfig_scriptlets -n libcm1

%post
%install_info --info-dir="%_infodir" "%_infodir/cm.info.gz"

%postun
%install_info_delete --info-dir="%_infodir" "%_infodir/cm.info.gz"

%files
%_bindir/classpol
%_bindir/cm
%_bindir/ecpp*
%_datadir/cm/
%_infodir/cm.info*

%files devel
%_includedir/cm*.h
%_libdir/libcm*.so

%files -n libcm1
%_libdir/libcm.so.1*

%changelog
