#
# spec file for package flint
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


Name:           flint
%define lname	libflint18
Version:        3.0.0
Release:        0
Summary:        C library for doing number theory
License:        LGPL-2.1-or-later
Group:          Productivity/Scientific/Math
URL:            https://flintlib.org/

#Git-Clone:     https://github.com/flintlib/flint
Source:         https://github.com/flintlib/flint/archive/v%version.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel >= 5
BuildRequires:  libtool
BuildRequires:  mpfr-devel >= 3
BuildRequires:  ntl-devel
BuildRequires:  xz

%description
FLINT (Fast Library for Number Theory) is a C library in support of
computations in number theory. It is also a research project into
algorithms in number theory. At this stage, FLINT consists mainly of
fast integer and polynomial arithmetic and linear algebra.

%package -n %lname
Summary:        C library for doing number theory
Group:          System/Libraries

%description -n %lname
FLINT (Fast Library for Number Theory) is a C library in support of
computations in number theory. It is also a research project into
algorithms in number theory. At this stage, FLINT consists mainly of
fast integer and polynomial arithmetic and linear algebra.

%package devel
Summary:        Development files for flint
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       gmp-devel
Requires:       mpfr-devel
Requires:       ntl-devel
Conflicts:      antic-devel
Conflicts:      arb-devel
Conflicts:      calcium-devel

%description devel
FLINT (Fast Library for Number Theory) is a C library in support of
computations in number theory. It is also a research project into
algorithms in number theory. At this stage, FLINT consists mainly of
fast integer and polynomial arithmetic and linear algebra.

This subpackage contains the include files and library links for
developing against the FLINT library.

%prep
%autosetup -p1

%build
if test ! -e configure; then
	./bootstrap.sh
fi
%configure \
%if 0%{?suse_version} < 1590
	--enable-gmp-internals=no \
%endif
	--disable-static --enable-reentrant --with-ntl
%make_build

%install
%make_install
b="%buildroot"
rm -f "$b/%_libdir"/*.la
ln -s libflint.so "$b/%_libdir/libarb.so"
ln -s libflint.so "$b/%_libdir/libantic.so"
ln -s libflint.so "$b/%_libdir/libcalcium.so"
# a little bit of compat (hence Conflicts, not Obsoletes used in subpackage)
mkdir -p "$b/%_includedir/antic" "$b/%_includedir/calcium"
for i in nf.h nf_elem.h qfb.h; do
	ln -s "../flint/$i" "$b/%_includedir/antic/"
done
for i in ca.h ca_ext.h ca_field.h ca_mat.h ca_poly.h ca_vec.h calcium.h \
    fexpr.h fexpr_builtin.h fmpz_mpoly_q.h qqbar.h; do
	ln -s "../flint/$i" "$b/%_includedir/calcium/"
done
ln -s ../flint/fmpz_mpoly.h "$b/%_includedir/calcium/utils_flint.h"
%fdupes %buildroot/%_prefix

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libflint.so.*
%license LICENSE

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%doc doc/source/history.rst

%changelog
