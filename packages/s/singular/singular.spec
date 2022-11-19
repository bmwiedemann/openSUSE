#
# spec file for package singular
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           singular
Version:        4.3.1
Release:        0
%define verud	4_3_1
Summary:        Singular CAS
License:        GPL-2.0 and GPL-3.0 and LGPL-2.1 and BSD-3-Clause
Group:          Productivity/Scientific/Math
URL:            https://www.singular.uni-kl.de/

#Git-Clone:	https://github.com/Singular/Sources
Source:         https://github.com/Singular/Singular/archive/refs/tags/Release-4-3-1.tar.gz
Source9:        %name-rpmlintrc
Patch1:         0001-src-resolve-strict-aliasing-violation-in-ndbm.cc.patch
Patch2:         0001-src-remove-__DATE__-__TIME__.patch
BuildRequires:  autoconf >= 2.62
BuildRequires:  automake
BuildRequires:  bison >= 1.2.2
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  flex >= 2.4
BuildRequires:  flint-devel >= 2.4
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel >= 4.2
BuildRequires:  latex2html
BuildRequires:  libtool
BuildRequires:  mpfr-devel >= 3
BuildRequires:  ncurses-devel
BuildRequires:  ntl-devel >= 5
BuildRequires:  perl >= 5
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  sharutils
BuildRequires:  xz
Recommends:     gfan

%description
Singular is a computer algebra system for polynomial computations,
with special emphasis on commutative and non-commutative algebra,
algebraic geometry, and singularity theory.

Its main computational objects are ideals, modules and matrices over
a large number of baserings. These include

* polynomial rings over various ground fields and some rings
  (including the integers),
* localizations of the above,
* a general class of non-commutative algebras (including the exterior
  algebra and the Weyl algebra),
* quotient rings of the above,
* tensor products of the above.

Singular's core algorithms handle

* Gröbner resp. standard bases and free resolutions,
* polynomial factorization,
* resultants, characteristic sets, and numerical root finding.

%package -n libfactory-%verud
Summary:        Singular's factorization library
Group:          Productivity/Scientific/Math
Recommends:     libfactory-gftables = %version

%description -n libfactory-%verud
Factory is a C++ class library that implements a recursive
representation of multivariate polynomial data. Factory handles
sparse multivariate polynomials over different coefficient domains,
such as Z, Q and GF(q), as well as algebraic extensions over Q and
GF(q) in an efficient way. Factory includes algorithms for computing
univariate and multivariate gcds, resultants, chinese remainders, and
several algorithms to factorize univariate polynomials over the
integers and over finite fields.

%package -n libfactory-gftables
Summary:        G_F tables for Singular/libfactory
Group:          Productivity/Scientific/Math
BuildArch:      noarch

%description -n libfactory-gftables
Factory is a C++ class library that implements a recursive
representation of multivariate polynomial data.

This package contains the G_F tables.

%package -n libfactory-devel
Summary:        Development files for Singular's factorization library
Group:          Development/Libraries/C and C++
Requires:       libfactory-%verud = %version-%release

%description -n libfactory-devel
Factory is a C++ class library that implements a recursive
representation of multivariate polynomial data. Factory handles
sparse multivariate polynomials over different coefficient domains,
such as Z, Q and GF(q), as well as algebraic extensions over Q and
GF(q) in an efficient way. Factory includes algorithms for computing
univariate and multivariate gcds, resultants, chinese remainders, and
several algorithms to factorize univariate polynomials over the
integers and over finite fields.

This package contains the include and library files.

%package -n libomalloc-%verud
Summary:        The omalloc memory allocator library
Group:          System/Libraries

%description -n libomalloc-%verud
(Upstream has not provided any description.)

%package -n libomalloc-devel
Summary:        Development files for the omalloc memory allocator library
Group:          Development/Libraries/C and C++
Requires:       libomalloc-%verud = %version-%release

%description -n libomalloc-devel
(Upstream has not provided any description.)

%package -n libpolys-%verud
Summary:        Singular's POLYS library
Group:          System/Libraries

%description -n libpolys-%verud
(Upstream has not provided any description.)

%package -n libpolys-devel
Summary:        Development files for Singular's POLYS library
Group:          Development/Libraries/C and C++
Requires:       libSingular-devel = %version-%release
Requires:       libpolys-%verud = %version-%release

%description -n libpolys-devel
(Upstream has not provided any description.)

%package -n libSingular-%verud
Summary:        Singular's Singular library
Group:          Productivity/Scientific/Math

%description -n libSingular-%verud
(Upstream has not provided any description.)

%package -n libSingular-devel
Summary:        Development files for Singular's "Singular" library
Group:          Development/Libraries/C and C++
Requires:       libSingular-%verud = %version-%release
Requires:       mpfr-devel

%description -n libSingular-devel
(Upstream has not provided any description.)

%package -n libsingular_resources-%verud
Summary:        Singular's "Singular" library
Group:          Productivity/Scientific/Math

%description -n libsingular_resources-%verud
(Upstream has not provided any description.)

%package -n libsingular_resources-devel
Summary:        Development files for Singular's "Singular" library
Group:          Development/Libraries/C and C++
Requires:       libsingular_resources-%verud = %version-%release

%description -n libsingular_resources-devel
(Upstream has not provided any description.)

%prep
%autosetup -n Singular-Release-4-3-1 -p1

%build
./autogen.sh
%configure --disable-static --bindir=%_libexecdir/%name
%make_build PACKAGE_VERSION="%version"

%install
b="%buildroot"
%make_install PACKAGE_VERSION="%version"
rm -f "$b/%_libdir"/*.la
find "$b" -type f -name "*.la" -exec perl -i -pe \
	's(^(libdir|dependency_libs)=\x27(.*)\x27)
	  ("$1=\x27".&{sub{$_=pop;s(-L\s*\S+)()g;$_}}($2)."\x27")e' \
	"{}" "+"
mkdir -p "$b/%_bindir"
blen="${#b}"
for i in "$b/%_libexecdir/%name"/*Singular; do
	ln -s "${i:$blen}" "$b/%_bindir/"
done
%if 0%{?fdupes:1}
%fdupes %buildroot/%_prefix
%endif

%post   -n libfactory-%verud -p /sbin/ldconfig
%postun -n libfactory-%verud -p /sbin/ldconfig
%post   -n libomalloc-%verud -p /sbin/ldconfig
%postun -n libomalloc-%verud -p /sbin/ldconfig
%post   -n libpolys-%verud -p /sbin/ldconfig
%postun -n libpolys-%verud -p /sbin/ldconfig
%post   -n libSingular-%verud -p /sbin/ldconfig
%postun -n libSingular-%verud -p /sbin/ldconfig
%post   -n libsingular_resources-%verud -p /sbin/ldconfig
%postun -n libsingular_resources-%verud -p /sbin/ldconfig

%files
%_bindir/*Singular
%_libexecdir/singular/
%_datadir/applications/*
%_datadir/icons/*
%_datadir/man/man1/*
%_datadir/ml_*/
%_datadir/singular/
%license COPYING GPL2 GPL3

%files -n libfactory-%verud
%_libdir/libfactory-%version.so

%files -n libfactory-gftables
%_datadir/factory/

%files -n libfactory-devel
%_includedir/factory/
%_libdir/libfactory.so
%_libdir/pkgconfig/factory.pc

%files -n libomalloc-%verud
%_libdir/libomalloc-%version.so

%files -n libomalloc-devel
%_includedir/omalloc/
%_libdir/libomalloc.so
%_libdir/pkgconfig/omalloc.pc

%files -n libpolys-%verud
%_libdir/libpolys-%version.so

%files -n libpolys-devel
%_libdir/libpolys.so
%_libdir/pkgconfig/libpolys.pc

%files -n libSingular-%verud
%_libdir/libSingular-%version.so

%files -n libSingular-devel
%_includedir/singular/
%_libdir/libSingular.so
%_libdir/pkgconfig/Singular.pc

%files -n libsingular_resources-%verud
%_libdir/libsingular_resources-%version.so

%files -n libsingular_resources-devel
%_includedir/resources/
%_libdir/libsingular_resources.so
%_libdir/pkgconfig/singular_resources.pc

%changelog
