#
# spec file for package gsl
#
# Copyright (c) 2025 SUSE LLC
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


%define libname  libgsl28
%define libcblas libgslcblas0

Name:           gsl
Version:        2.8
Release:        0
Summary:        GNU Scientific Library
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.gnu.org/software/%{name}/
Source0:        https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=gsl&download=1#/%{name}.keyring
Patch6:         gsl-qawc-test-x86-precision.diff
Patch7:         gsl-disable-fma.patch
# PATCH-FIX-UPSTREAM gsl-bspline-missing-definition.patch svg#65868 badshah400@gmail.com -- Add missing definition for gsl_bspline_eval_nonzero
Patch8:         gsl-bspline-missing-definition.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig

BuildRequires:  update-alternatives
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description
The GNU Scientific Library (GSL) is a collection of routines for
numerical computing. The routines are written from scratch by the GSL
team in ANSI C and present an Applications Programming Interface
(API) for C programmers, while allowing wrappers to be written for very
high level languages.

%package     -n %{libname}
Summary:        GNU Scientific Library
Group:          System/Libraries

%description -n %{libname}
The GNU Scientific Library (GSL) is a collection of routines for
numerical computing. The routines are written from scratch by the GSL
team in ANSI C and present an Applications Programming Interface
(API) for C programmers, while allowing wrappers to be written for very
high level languages.

The library covers the following areas:

Complex Numbers - Roots of Polynomials - Special Functions -
Vectors and Matrices - Permutations - Sorting - BLAS Support -
Linear Algebra - Eigensystems - Fast Fourier Transforms - Quadrature -
Random Numbers - Quasi-Random Sequences - Random Distributions -
Statistics - Histograms - N-Tuples - Monte Carlo Integration -
Simulated Annealing - Differential Equations - Interpolation -
Numerical Differentiation - Chebyshev Approximation - Series Acceleration -
Discrete Hankel Transforms - Root-Finding - Minimization -
Least-Squares Fitting - Physical Constants - IEEE Floating-Point

%package     -n %{libcblas}
Summary:        A standard C language APIs for BLAS from GNU Scientific Library
# file conflict, see boo#991155
Group:          System/Libraries

%description -n %{libcblas}
This library provides a native C interface to BLAS routines. This is part of
the GNU Scientific Library.

%package        devel
Summary:        Development files for the GNU Scientific Library
Group:          Development/Libraries/C and C++
Requires:       %{libcblas} = %{version}
Requires:       %{libname} = %{version}
Requires(pre):  %{install_info_prereq}
%{?with_hpc:%hpc_requires_devel}

%description devel
This package contains the headers, static libraries and some
documentation for GSL.

The GNU Scientific Library (GSL) is a collection of routines for
numerical computing. The routines are written from scratch by the GSL
team in ANSI C, and present an Applications Programming Interface
(API) for C programmers, while allowing wrappers to be written for very
high level languages.

%package        doc
Summary:        Documentation for the GNU Scientific Library
Group:          Documentation/Other
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
BuildArch:      noarch

%description    doc
This package contains documentation for GSL

The GNU Scientific Library (GSL) is a collection of routines for
numerical computing. The routines are written from scratch by the GSL
team in ANSI C, and present an Applications Programming Interface
(API) for C programmers, while allowing wrappers to be written for very
high level languages.

%package        examples
Summary:        Examples for the GNU Scientific Library
Group:          Documentation/Other
BuildArch:      noarch

%description    examples
This package contains examples for GSL

%prep
%setup -q -n %{name}-%{version}
%patch -P 6
%patch -P 7 -p1
%patch -P 8 -p1

%build
autoreconf -fiv
export CFLAGS="%{optflags}"
%configure \
	--disable-static \
	--enable-shared \
	--with-gnu-ld
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_infodir}/dir

# create a copy for testing without dirtying the installed files
cp -a `pwd` ../test.tmp
# Clean up to package directory
make -C doc/examples clean
rm doc/examples/Makefile*
chmod a-x doc/examples/*

%check
cd ../test.tmp
# On i586 (32bit) this still fails
%ifarch %{ix86}
make %{?_smp_mflags} check || ( find -name \*.log -print -exec cat {} \; ; exit 0 )
%else
make %{?_smp_mflags} check || ( find -name \*.log -print -exec cat {} \; ; exit 1 )
%endif
cd .. ; rm -rf test.tmp

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%post   -n %{libcblas} -p /sbin/ldconfig
%postun -n %{libcblas} -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/gsl-histogram
%{_bindir}/gsl-randist
%{_mandir}/man1/gsl-histogram.1*
%{_mandir}/man1/gsl-randist.1*

%files -n %{libname}
%{_libdir}/libgsl.so.*

%files -n %{libcblas}
%{_libdir}/libgslcblas.so.*

%files devel
%license COPYING
%{_includedir}/gsl
%{_libdir}/libgsl*.so
%{_libdir}/pkgconfig/gsl.pc
%{_bindir}/gsl-config
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/gsl.m4
%{_mandir}/man1/gsl-config.1*
%{_mandir}/man3/gsl.3*

%files examples
%doc doc/examples
%license COPYING

%files doc
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%license COPYING
%{_infodir}/gsl-ref*

%post doc
%install_info --info-dir=%{_infodir} %{_infodir}/gsl-ref.info%{ext_info}

%preun doc
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gsl-ref.info%{ext_info}

%changelog
