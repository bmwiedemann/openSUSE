#
# spec file for package lapack
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


%global flavor @BUILD_FLAVOR@%{nil}
%global pname lapack
%if "%{flavor}" == "static"
%define psuffix -static
%bcond_with shared
# Generate man files for the static flavour to avoid additional deps/build time
# for main flavour
%bcond_without man
%else
%define psuffix %{nil}
%bcond_without shared
%bcond_with man
%endif
%define __builder ninja
%define so_ver 3
%bcond_without tmg

# For Leap 15.X, we do not need arch dependent symlink names because no baselibs are generated
%if 0%{?suse_version} >= 1500
%define a_x _%{_arch}
%endif
Name:           %{pname}%{?psuffix}
Version:        3.12.0
Release:        0
Summary:        Linear Algebra PACKage
License:        BSD-3-Clause
URL:            https://www.netlib.org/lapack/
Source0:        https://github.com/Reference-LAPACK/lapack/archive/v%{version}.tar.gz#/%{pname}-%{version}.tar.gz
Source98:       lapack.rpmlintrc
Source99:       baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base
# SECTION Requirements for MAN files
%if %{with man}
BuildRequires:  doxygen
BuildRequires:  graphviz
%endif
# /SECTION

%description
LAPACK provides routines for solving systems of simultaneous linear
equations, least-squares solutions of linear systems of equations,
eigenvalue problems, and singular value problems. The associated matrix
factorizations (LU, Cholesky, QR, SVD, Schur, generalized Schur) are
also provided, as are related computations such as reordering of the
Schur factorizations and estimating condition numbers. Dense and banded
matrices are handled, but not general sparse matrices. In all areas,
similar functionality is provided for real and complex matrices, in
both single and double precision.


# LAPACK
%package     -n liblapack%{so_ver}
Summary:        Linear Algebra PACKage: Shared Library
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description -n liblapack%{so_ver}
LAPACK provides routines for solving systems of simultaneous linear
equations, least-squares solutions of linear systems of equations,
eigenvalue problems, and singular value problems. The associated matrix
factorizations (LU, Cholesky, QR, SVD, Schur, generalized Schur) are
also provided, as are related computations such as reordering of the
Schur factorizations and estimating condition numbers. Dense and banded
matrices are handled, but not general sparse matrices. In all areas,
similar functionality is provided for real and complex matrices, in
both single and double precision.

This package provides the shared library for LAPACK.

%package -n %{pname}-devel
Summary:        Linear Algebra PACKage: headers and source files for development
Requires:       blas-devel = %{version}
Requires:       liblapack%{so_ver} = %{version}
Recommends:     lapack-man = %{version}
Provides:       lapack = %{version}
Obsoletes:      lapack < %{version}

%description -n %{pname}-devel
LAPACK provides routines for solving systems of simultaneous linear
equations, least-squares solutions of linear systems of equations,
eigenvalue problems, and singular value problems. The associated matrix
factorizations (LU, Cholesky, QR, SVD, Schur, generalized Schur) are
also provided, as are related computations such as reordering of the
Schur factorizations and estimating condition numbers. Dense and banded
matrices are handled, but not general sparse matrices. In all areas,
similar functionality is provided for real and complex matrices, in
both single and double precision.

%package -n %{pname}-devel-static
Summary:        Linear Algebra PACKage - static libraries
Requires:       lapack-devel = %{version}

%description -n %{pname}-devel-static
LAPACK provides routines for solving systems of simultaneous linear
equations, least-squares solutions of linear systems of equations,
eigenvalue problems, and singular value problems. The associated matrix
factorizations (LU, Cholesky, QR, SVD, Schur, generalized Schur) are
also provided, as are related computations such as reordering of the
Schur factorizations and estimating condition numbers. Dense and banded
matrices are handled, but not general sparse matrices. In all areas,
similar functionality is provided for real and complex matrices, in
both single and double precision.

This package provides the static library for LAPACK.


# BLAS
%package     -n libblas%{so_ver}
Summary:        Basic Linear Algebra Subprograms: Shared Library
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description -n libblas%{so_ver}
BLAS (Basic Linear Algebra Subprograms) is a standard library for
numerical algebra.  BLAS provides a number of basic algorithms for
linear algebra.

This package provides the shared library for BLAS.

%package     -n blas-devel
Summary:        Basic Linear Algebra Subprograms: headers and sources for development
Requires:       libblas%{so_ver} = %{version}
Recommends:     lapack-man = %{version}
Provides:       blas = %{version}
Obsoletes:      blas < %{version}

%description -n blas-devel
BLAS (Basic Linear Algebra Subprograms) is a standard library for
numerical algebra. BLAS provides a number of basic algorithms for
linear algebra. BLAS is fast and well-tested, was written in FORTRAN 77
and built with gfortran. BLAS manual pages are available in the
blas-man package.

%package     -n blas-devel-static
Summary:        Basic Linear Algebra Subprograms: static library
Requires:       blas-devel = %{version}

%description -n blas-devel-static
BLAS (Basic Linear Algebra Subprograms) is a standard library for
numerical algebra. BLAS provides a number of basic algorithms for
linear algebra. BLAS is fast and well-tested, was written in FORTRAN 77
and built with gfortran. BLAS manual pages are available in the
blas-man package.

This package provides the static library for BLAS.


# LAPACKE
%package     -n liblapacke%{so_ver}
Summary:        Native C Interface to LAPACK: shared library
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description -n liblapacke%{so_ver}
This library provides a native C interface to LAPACK routines available
at www.netlib.org/lapack to facilitate usage of LAPACK functionality
for C programmers.

%package     -n lapacke-devel
Summary:        Native C Interface to LAPACK: headers and sources for development
Requires:       liblapacke%{so_ver} = %{version}
Recommends:     lapack-man = %{version}
Provides:       lapacke = %{version}

%description -n lapacke-devel
LAPACKE provides a native C interface to LAPACK routines available
at www.netlib.org/lapack to facilitate usage of LAPACK functionality
for C programmers.

This package provides LAPACKE headers and development files.

%package     -n lapacke-devel-static
Summary:        Native C Interface to LAPACK: static library
Requires:       lapacke-devel = %{version}

%description -n lapacke-devel-static
LAPACKE provides a native C interface to LAPACK routines available
at www.netlib.org/lapack to facilitate usage of LAPACK functionality
for C programmers.

This package provides the static library for LAPACKE.


# CBLAS
%package     -n libcblas%{so_ver}
Summary:        Native C interface to BLAS: Shared Library
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description -n libcblas%{so_ver}
This library provides a native C interface to BLAS routines available
at www.netlib.org/blas to facilitate usage of BLAS functionality
for C programmers.

%package     -n cblas-devel
Summary:        Native C interface to BLAS: headers and sources for development
Requires:       libcblas%{so_ver} = %{version}
Recommends:     lapack-man = %{version}
Provides:       cblas = %{version}

%description -n cblas-devel
This library provides a native C interface to BLAS routines available
at www.netlib.org/blas to facilitate usage of BLAS functionality
for C programmers.

This package provides the cblas headers and development files.

%package     -n cblas-devel-static
Summary:        Native C interface to BLAS: static library
Requires:       cblas-devel = %{version}

%description -n cblas-devel-static
This library provides a native C interface to BLAS routines available
at www.netlib.org/blas to facilitate usage of BLAS functionality
for C programmers.

This package contains the CBLAS static libraries.


# TMGLIB
%package -n libtmglib%{so_ver}
Summary:        Test Matrix Generator Library: shared library

%description -n libtmglib%{so_ver}
This package provides the shared library for tmglib, the Test Matrix Generator
Library.

%package -n tmglib-devel
Summary:        Test Matrix Generator Library: headers and sources for development
Requires:       libtmglib%{so_ver} = %{version}

%description -n tmglib-devel
This package provides the headers and sources needed to develop against tmglib,
the Test Matrix Generator Library.

%package -n tmglib-devel-static
Summary:        Test Matrix Generator Library: static library
Requires:       tmglib-devel

%description -n tmglib-devel-static
This package provides the headers and sources needed to develop against the
tmglib as a static library.


# MAN Pages
%package -n lapack-man
Summary:        Man pages for BLAS, CBLAS, and LAPACK

%description -n lapack-man
This package provides the man pages for BLAS, CBLAS, and LAPACK.

%prep
%autosetup -p1 -n %{pname}-%{version}
sed -i -E '1{s@#!/usr/bin/env python[0-9]*@#!%{_bindir}/python%{python3_version}@}' lapack_testing.py

%build
%ifarch %{ix86}
%if 0%{?sle_version:%sle_version} >= 150000
%global precflags "-mfpmath=sse"
%global test_precflags %{precflags}
%else
%global test_precflags "-ffloat-store"
%endif
%endif

%if %{without shared}
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%endif
%global optflags_f %{optflags}

%cmake \
  -DBUILD_SHARED_LIBS=%{?with_shared:ON}%{!?with_shared:OFF} \
  -DBLAS++=OFF \
  -DLAPACK++=OFF \
  -DCBLAS=ON \
  -DLAPACKE=ON \
  -DLAPACKE_WITH_TMG=%{?with_tmglib:ON}%{!?with_tmglib:OFF} \
  -DBUILD_DEPRECATED=ON \
  -DBUILD_MAN_DOCUMENTATION=%{?with_man:ON}%{!?with_man:OFF} \
  -DBUILD_TESTING=ON \
  %{nil}
%cmake_build

%if %{with man}
doxygen Doxyfile.man
%endif

%install
%cmake_install

%if %{with shared}
# Prepare for update-alternatives
install -d %{buildroot}%{_sysconfdir}/alternatives
install -d %{buildroot}%{_libdir}/{lapack,blas}
mv %{buildroot}%{_libdir}/liblapack{,e}.so.* %{buildroot}%{_libdir}/lapack/
mv %{buildroot}%{_libdir}/lib{,c}blas.so.* %{buildroot}%{_libdir}/blas/

# Create the symlinks
for t in blas cblas lapack lapacke
do
  ln -s %{_sysconfdir}/alternatives/lib${t}.so.%{so_ver}%{?a_x} %{buildroot}%{_libdir}/lib${t}.so.%{so_ver}
done

%else
# Remove headers and script files for static flavour to avoid file conflicts
rm -fr %{buildroot}%{_includedir}/*.h \
       %{buildroot}%{_libdir}/cmake \
       %{buildroot}%{_libdir}/pkgconfig
%endif

%if %{with man}
# Delete weirdly named man files
rm %{__builddir}/DOCS/man/man3/_*_.3
# Rename isnan to avoid conflict with libm's isnan man file (package man-pages)
mv %{__builddir}/DOCS/man/man3/isnan{,-lapack}.3
# Install man pages
mkdir -p %{buildroot}%{_mandir}
cp -r %{__builddir}/DOCS/man/man3 %{buildroot}%{_mandir}/
%endif

%check
%ctest

%if %{with shared}
%ldconfig_scriptlets -n libtmglib%{so_ver}

# BLAS
%post -n libblas%{so_ver}
%{_sbindir}/update-alternatives --install \
  %{_libdir}/libblas.so.%{so_ver} libblas.so.%{so_ver}%{?a_x} %{_libdir}/blas/libblas.so.%{so_ver}  50
/sbin/ldconfig

%postun -n libblas%{so_ver}
/sbin/ldconfig
if [ ! %{_libdir}/blas/libblas.so.%{so_ver} ] ; then
  %{_sbindir}/update-alternatives --remove libblas.so.%{so_ver}%{?a_x}  %{_libdir}/blas/libblas.so.%{so_ver}
fi
# /BLAS

# LAPACK
%post -n liblapack%{so_ver}
%{_sbindir}/update-alternatives --install \
  %{_libdir}/liblapack.so.%{so_ver} liblapack.so.%{so_ver}%{?a_x} %{_libdir}/lapack/liblapack.so.%{so_ver}  50
/sbin/ldconfig

%postun -n liblapack%{so_ver}
/sbin/ldconfig
if [ ! -f  %{_libdir}/lapack/liblapack.so.%{so_ver} ] ; then
  %{_sbindir}/update-alternatives --remove liblapack.so.%{so_ver}%{?a_x} %{_libdir}/lapack/liblapack.so.%{so_ver}
fi
# /LAPACK

# CBLAS
%post -n libcblas%{so_ver}
%{_sbindir}/update-alternatives --install \
  %{_libdir}/libcblas.so.%{so_ver} libcblas.so.%{so_ver}%{?a_x} %{_libdir}/blas/libcblas.so.%{so_ver}  50
/sbin/ldconfig

%postun -n libcblas%{so_ver}
/sbin/ldconfig
if [ ! -f %{_libdir}/blas/libcblas.so.%{so_ver} ] ; then
  %{_sbindir}/update-alternatives --remove libcblas.so.%{so_ver}%{?a_x}  %{_libdir}/blas/libcblas.so.%{so_ver}
fi
# /CBLAS

# LAPACKE
%post -n liblapacke%{so_ver}
%{_sbindir}/update-alternatives --install \
  %{_libdir}/liblapacke.so.%{so_ver} liblapacke.so.%{so_ver}%{?a_x} %{_libdir}/lapack/liblapacke.so.%{so_ver}  50
/sbin/ldconfig

%postun -n liblapacke%{so_ver}
/sbin/ldconfig
if [ ! -f %{_libdir}/lapack/liblapacke.so.%{so_ver} ] ; then
  %{_sbindir}/update-alternatives --remove liblapacke.so.%{so_ver}%{?a_x} %{_libdir}/lapack/liblapacke.so.%{so_ver}
fi
# /LAPACKE
%endif

# SECTION main vs static flavour packages
%if %{with shared}
%files -n liblapack%{so_ver}
%doc README.md
%license LICENSE
%dir %{_libdir}/lapack
%{_libdir}/lapack/liblapack.so.*
%ghost %{_libdir}/liblapack.so.%{so_ver}
%ghost %{_sysconfdir}/alternatives/liblapack.so.%{so_ver}%{?a_x}

%files -n libblas%{so_ver}
%doc README.md
%license LICENSE
%dir %{_libdir}/blas
%{_libdir}/blas/libblas.so.*
%ghost %{_libdir}/libblas.so.%{so_ver}
%ghost %{_sysconfdir}/alternatives/libblas.so.%{so_ver}%{?a_x}

%files -n liblapacke%{so_ver}
%dir %{_libdir}/lapack
%{_libdir}/lapack/liblapacke.so.*
%ghost %{_libdir}/liblapacke.so.%{so_ver}
%ghost %{_sysconfdir}/alternatives/liblapacke.so.%{so_ver}%{?a_x}

%files -n libcblas%{so_ver}
%doc README.md
%license LICENSE
%dir %{_libdir}/blas
%{_libdir}/blas/libcblas.so.*
%ghost %{_libdir}/libcblas.so.%{so_ver}
%ghost %{_sysconfdir}/alternatives/libcblas.so.%{so_ver}%{?a_x}

%files -n libtmglib%{so_ver}
%license LICENSE
%{_libdir}/libtmglib.so.%{so_ver}*

%files -n tmglib-devel
%license LICENSE
%{_libdir}/libtmglib.so

%files -n %{pname}-devel
%{_libdir}/liblapack.so
%{_includedir}/lapack.h
%{_libdir}/cmake/lapack-%{version}/
%{_libdir}/pkgconfig/lapack.pc

%files -n blas-devel
%{_libdir}/libblas.so
%{_libdir}/pkgconfig/blas.pc

%files -n lapacke-devel
%doc LAPACKE/README
%license LAPACKE/LICENSE
%{_libdir}/liblapacke.so
%{_includedir}/lapacke*.h
%{_libdir}/cmake/lapacke-%{version}/
%{_libdir}/pkgconfig/lapacke.pc

%files -n cblas-devel
%doc CBLAS/README
%{_libdir}/libcblas.so
%{_includedir}/cblas*.h
%{_libdir}/cmake/cblas-%{version}/
%{_libdir}/pkgconfig/cblas.pc

# End of packages built for main flavour
%else

# Start of static flavour
%files -n %{pname}-devel-static
%license LICENSE
%{_libdir}/liblapack.a

%files -n cblas-devel-static
%license LICENSE
%{_libdir}/libcblas.a

%files -n blas-devel-static
%license LICENSE
%{_libdir}/libblas.a

%files -n lapacke-devel-static
%license LICENSE
%{_libdir}/liblapacke.a

%files -n tmglib-devel-static
%license LICENSE
%{_libdir}/libtmglib.a

%endif
# /SECTION main vs static flavour pkgs

%if %{with man}
%files -n lapack-man
%{_mandir}/man3/*.3%{?ext_man}
%endif

%changelog
