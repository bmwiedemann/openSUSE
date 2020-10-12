#
# spec file for package lapack
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


Name:           lapack
Version:        3.8.0
Release:        0
Summary:        Linear Algebra Package
License:        BSD-3-Clause
Group:          Development/Libraries/Parallel
URL:            http://www.netlib.org/lapack/
Source0:        http://www.netlib.org/lapack/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
Patch1:         lapack-3.2.2.patch
BuildRequires:  gcc-fortran
BuildRequires:  python3-base
BuildRequires:  update-alternatives
Requires(pre):  update-alternatives

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

%package     -n liblapack3
Summary:        LAPACK Shared Library
Group:          Development/Libraries/Parallel
Requires(pre):  update-alternatives

%description -n liblapack3
LAPACK provides routines for solving systems of simultaneous linear
equations, least-squares solutions of linear systems of equations,
eigenvalue problems, and singular value problems. The associated matrix
factorizations (LU, Cholesky, QR, SVD, Schur, generalized Schur) are
also provided, as are related computations such as reordering of the
Schur factorizations and estimating condition numbers. Dense and banded
matrices are handled, but not general sparse matrices. In all areas,
similar functionality is provided for real and complex matrices, in
both single and double precision.

%package     -n libblas3
Summary:        BLAS Shared Library
Group:          Development/Libraries/Parallel
Requires(pre):  update-alternatives

%description -n libblas3
BLAS (Basic Linear Algebra Subprograms) is a standard library for
numerical algebra.  BLAS provides a number of basic algorithms for
linear algebra.

%package        devel
Summary:        Linear Algebra Package
Group:          Development/Libraries/Parallel
Requires:       blas-devel = %{version}
Requires:       liblapack3 = %{version}
Provides:       lapack = %{version}
Obsoletes:      lapack < %{version}

%description    devel
LAPACK provides routines for solving systems of simultaneous linear
equations, least-squares solutions of linear systems of equations,
eigenvalue problems, and singular value problems. The associated matrix
factorizations (LU, Cholesky, QR, SVD, Schur, generalized Schur) are
also provided, as are related computations such as reordering of the
Schur factorizations and estimating condition numbers. Dense and banded
matrices are handled, but not general sparse matrices. In all areas,
similar functionality is provided for real and complex matrices, in
both single and double precision.

%package        devel-static
Summary:        Linear Algebra Package - static libraries
Group:          Development/Libraries/Parallel
Requires:       lapack-devel = %{version}

%description    devel-static
LAPACK provides routines for solving systems of simultaneous linear
equations, least-squares solutions of linear systems of equations,
eigenvalue problems, and singular value problems. The associated matrix
factorizations (LU, Cholesky, QR, SVD, Schur, generalized Schur) are
also provided, as are related computations such as reordering of the
Schur factorizations and estimating condition numbers. Dense and banded
matrices are handled, but not general sparse matrices. In all areas,
similar functionality is provided for real and complex matrices, in
both single and double precision.

%package     -n blas-devel
Summary:        Basic Linear Algebra Subprograms
Group:          Development/Libraries/Parallel
Requires:       libblas3 = %{version}
Provides:       blas = %{version}
Obsoletes:      blas < %{version}

%description -n blas-devel
BLAS (Basic Linear Algebra Subprograms) is a standard library for
numerical algebra. BLAS provides a number of basic algorithms for
linear algebra. BLAS is fast and well-tested, was written in FORTRAN 77
and built with gfortran. BLAS manual pages are available in the
blas-man package.

%package     -n blas-devel-static
Summary:        Basic Linear Algebra Subprograms
Group:          Development/Libraries/Parallel
Requires:       blas-devel = %{version}

%description -n blas-devel-static
BLAS (Basic Linear Algebra Subprograms) is a standard library for
numerical algebra. BLAS provides a number of basic algorithms for
linear algebra. BLAS is fast and well-tested, was written in FORTRAN 77
and built with gfortran. BLAS manual pages are available in the
blas-man package.

%package     -n liblapacke3
Summary:        LAPACKE development files
Group:          Development/Libraries/C and C++

%description -n liblapacke3
This library provides a native C interface to LAPACK routines available
at www.netlib.org/lapack to facilitate usage of LAPACK functionality
for C programmers.

This implementation introduces:
- row-major and column-major matrix layout controlled by the first function
  parameter;
- an implementation with working arrays (middle-level interface) as well as
  without working arrays (high-level interface);
- input scalars passed by value;
- error code as a return value instead of the INFO parameter.

%package     -n lapacke-devel
Summary:        LAPACKE development files
Group:          Development/Libraries/C and C++
Requires:       liblapacke3 = %{version}
Provides:       lapacke = %{version}

%description -n lapacke-devel
LAPACKE headers and development files.

%package     -n lapacke-devel-static
Summary:        LAPACKE static libraries
Group:          Development/Libraries/C and C++
Requires:       lapacke-devel = %{version}

%description -n lapacke-devel-static
LAPACKE development files - static libraries.

%package     -n libcblas3
Summary:        CBLAS Shared Library
Group:          Development/Libraries/C and C++
Requires(pre):  update-alternatives
# Only version ever packaged separately
Obsoletes:      libcblas3 == 20110120

%description -n libcblas3
This library provides a native C interface to BLAS routines available
at www.netlib.org/blas to facilitate usage of BLAS functionality 
for C programmers.

%package     -n cblas-devel
Summary:        CBLAS development files
Group:          Development/Libraries/C and C++
Requires:       libcblas3 = %{version}
Provides:       cblas = %{version}

%description -n cblas-devel
cblas headers and development files.

%package     -n cblas-devel-static
Summary:        CBLAS - static libraries
Group:          Development/Libraries/C and C++
Requires:       cblas-devel = %{version}

%description -n cblas-devel-static
The cblas-devel-static package contains the CBLAS static libraries
for -static linking. You do not need these, unless you link
statically, which is highly discouraged.


%prep
%setup -q
%patch1
sed -i -e '1 s@env python@python3@' lapack_testing.py

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%global optflags_f %{optflags} -std=legacy
case "$RPM_ARCH" in
    i[0-9]86) PRECFLAGS="-ffloat-store" ;;
    *)        PRECFLAGS="" ;;
esac
export PRECFLAGS
cp make.inc.example make.inc

make cleanlib %{?_smp_mflags}
make %{?_smp_mflags} blaslib \
  OPTS="%{optflags_f} -fPIC" \
  NOOPT="%{optflags_f} -O0 -fPIC"
mkdir tmp
( cd tmp; ar x ../librefblas.a )
gfortran -shared -Wl,-soname=libblas.so.3 -o libblas.so.%{version} tmp/*.o
ln -s libblas.so.%{version} libblas.so
rm -rf tmp

make blas_testing \
  OPTS="%{optflags_f} $PRECFLAGS" \
  NOOPT="%{optflags_f} $PRECFLAGS -O0"
if grep -B15 -A15 FAIL BLAS/*.out; then
  echo
  echo "blas_testing FAILED"
  false
fi
mv librefblas.a libblas.a

make %{?_smp_mflags} cblaslib \
  CFLAGS="%{optflags} -fPIC -DADD_ " \
  LINKER=gfortran
mkdir tmp
( cd tmp; ar x ../libcblas.a )
gfortran -shared -Wl,-soname=libcblas.so.3 -o libcblas.so.%{version} tmp/*.o -L. -lblas
ln -s libcblas.so.%{version} libcblas.so
rm -rf tmp
make %{?_smp_mflags} cblas_testing \
  CFLAGS="%{optflags} -fPIC" \
  LINKER=gfortran
grep -B15 -A15 FAIL TESTING/*.out && false

make %{?_smp_mflags} lapacklib \
  OPTS="%{optflags_f} -fPIC" \
  NOOPT="%{optflags_f} -O0 -fPIC"
mkdir tmp
( cd tmp; ar x ../liblapack.a )
gfortran -shared -Wl,-soname=liblapack.so.3 -o liblapack.so.%{version} tmp/*.o -L. -lblas
ln -s liblapack.so.%{version} liblapack.so
rm -rf tmp

cd LAPACKE
make %{?_smp_mflags} lapacke \
  CFLAGS="%{optflags} -fPIC -DADD_ -DHAVE_LAPACK_CONFIG_H -DLAPACK_COMPLEX_STRUCTURE" \
  LINKER=gfortran
mkdir tmp
( cd tmp; ar x ../../liblapacke.a )
gfortran -shared -Wl,-soname=liblapacke.so.3 -o liblapacke.so.%{version} tmp/*.o
ln -s liblapacke.so.%{version} liblapacke.so
rm -rf tmp
cd ..

make lapack_testing \
  OPTS="%{optflags_f} $PRECFLAGS" \
  NOOPT="%{optflags_f} $PRECFLAGS -O0"
if grep -B15 -A15 FAIL TESTING/*.out; then
  echo
  echo "lapack_testing FAILED"
  false
fi

%install
install -d %{buildroot}/%{_libdir}
install -d %{buildroot}/%{_sysconfdir}/alternatives
install -d %{buildroot}/%{_includedir}
## BLAS
install -d %{buildroot}/%{_libdir}/blas
install -m 644 libblas.a %{buildroot}/%{_libdir}
install -m 755 libblas.so.%{version} %{buildroot}/%{_libdir}/blas
ln -s libblas.so.%{version} %{buildroot}/%{_libdir}/blas/libblas.so.3
ln -s blas/libblas.so.%{version} %{buildroot}/%{_libdir}/libblas.so
# dummy target for update-alternatives
ln -s blas/libblas.so.%{version} %{buildroot}/%{_libdir}/libblas.so.3
ln -s libblas.so.%{version} %{buildroot}/%{_sysconfdir}/alternatives/libblas.so.3
## CBLAS
install -m 644 CBLAS/include/*.h %{buildroot}/%{_includedir}
install -m 644 libcblas.a %{buildroot}/%{_libdir}
install -m 755 libcblas.so.%{version} %{buildroot}/%{_libdir}/blas
ln -s libcblas.so.%{version} %{buildroot}/%{_libdir}/blas/libcblas.so.3
ln -s blas/libcblas.so.%{version} %{buildroot}/%{_libdir}/libcblas.so
# dummy target for update-alternatives
ln -s blas/libcblas.so.%{version} %{buildroot}/%{_libdir}/libcblas.so.3
ln -s libcblas.so.%{version} %{buildroot}/%{_sysconfdir}/alternatives/libcblas.so.3
## LAPACK
install -d %{buildroot}/%{_libdir}/lapack
install -m 644 liblapack.a %{buildroot}/%{_libdir}
install -m 755 liblapack.so.%{version} %{buildroot}/%{_libdir}/lapack
ln -s liblapack.so.%{version} %{buildroot}/%{_libdir}/lapack/liblapack.so.3
ln -s lapack/liblapack.so.%{version} %{buildroot}/%{_libdir}/liblapack.so
# dummy target for update-alternatives
ln -s lapack/liblapack.so.%{version} %{buildroot}/%{_libdir}/liblapack.so.3
ln -s liblapack.so.%{version} %{buildroot}/%{_sysconfdir}/alternatives/liblapack.so.3
## LAPACKE
cd LAPACKE
install -m 644 include/*.h %{buildroot}/%{_includedir}
install -m 644 ../liblapacke.a %{buildroot}/%{_libdir}
install -m 755 liblapacke.so.%{version} %{buildroot}/%{_libdir}
ln -s liblapacke.so.%{version} %{buildroot}/%{_libdir}/liblapacke.so.3
ln -s liblapacke.so.%{version} %{buildroot}/%{_libdir}/liblapacke.so
cd ..

%post -n libblas3
%{_sbindir}/update-alternatives --install \
   %{_libdir}/libblas.so.3 libblas.so.3 %{_libdir}/blas/libblas.so.3  50
/sbin/ldconfig

%preun -n libblas3
if [ "$1" = 0 ] ; then
   %{_sbindir}/update-alternatives --remove libblas.so.3  %{_libdir}/blas/libblas.so.3
fi

%postun -n libblas3 -p /sbin/ldconfig

%posttrans -n libblas3
if [ "$1" = 0 ] ; then
  if ! [ -f %{_libdir}/libblas.so.3 ] ; then
      "%{_sbindir}/update-alternatives" --auto libblas.so.3
  fi
fi

%post -n liblapack3
%{_sbindir}/update-alternatives --install \
   %{_libdir}/liblapack.so.3 liblapack.so.3 %{_libdir}/lapack/liblapack.so.3  50
/sbin/ldconfig

%preun -n liblapack3
if [ "$1" = 0 ] ; then
   %{_sbindir}/update-alternatives --remove liblapack.so.3 %{_libdir}/lapack/liblapack.so.3
fi

%postun -n liblapack3 -p /sbin/ldconfig

%posttrans -n liblapack3
if [ "$1" = 0 ] ; then
  if ! [ -f %{_libdir}/liblapack.so.3 ] ; then
      "%{_sbindir}/update-alternatives" --auto liblapack.so.3
  fi
fi

%post -n libcblas3
%{_sbindir}/update-alternatives --install \
   %{_libdir}/libcblas.so.3 libcblas.so.3 %{_libdir}/blas/libcblas.so.3  50
/sbin/ldconfig

%preun -n libcblas3
if [ "$1" = 0 ] ; then
   %{_sbindir}/update-alternatives --remove libcblas.so.3  %{_libdir}/blas/libcblas.so.3
fi

%postun -n libcblas3 -p /sbin/ldconfig

%posttrans -n libcblas3
if [ "$1" = 0 ] ; then
  if ! [ -f %{_libdir}/libcblas.so.3 ] ; then
      "%{_sbindir}/update-alternatives" --auto libcblas.so.3
  fi
fi

%post -n liblapacke3 -p /sbin/ldconfig

%postun -n liblapacke3 -p /sbin/ldconfig

%files -n liblapack3
%doc README.md
%license LICENSE
%dir %{_libdir}/lapack
%{_libdir}/lapack/liblapack.so.%{version}
%{_libdir}/lapack/liblapack.so.3
%ghost %{_libdir}/liblapack.so.3
%ghost %{_sysconfdir}/alternatives/liblapack.so.3

%files -n libblas3
%doc README.md
%license LICENSE
%dir %{_libdir}/blas
%{_libdir}/blas/libblas.so.%{version}
%{_libdir}/blas/libblas.so.3
%ghost %{_libdir}/libblas.so.3
%ghost %{_sysconfdir}/alternatives/libblas.so.3

%files devel
%{_libdir}/liblapack.so

%files devel-static
%{_libdir}/liblapack.a

%files -n blas-devel
%{_libdir}/libblas.so

%files -n blas-devel-static
%{_libdir}/libblas.a

%files -n liblapacke3
%{_libdir}/liblapacke.so.%{version}
%{_libdir}/liblapacke.so.3

%files -n lapacke-devel
%doc LAPACKE/README
%license LAPACKE/LICENSE
%{_libdir}/liblapacke.so
%{_includedir}/lapack*.h

%files -n lapacke-devel-static
%{_libdir}/liblapacke.a

%files -n libcblas3
%doc README.md
%license LICENSE
%dir %{_libdir}/blas
%{_libdir}/blas/libcblas.so.%{version}
%{_libdir}/blas/libcblas.so.3
%ghost %{_libdir}/libcblas.so.3
%ghost %{_sysconfdir}/alternatives/libcblas.so.3

%files -n cblas-devel
%doc CBLAS/README
%{_libdir}/libcblas.so
%{_includedir}/cblas*.h

%files -n cblas-devel-static
%{_libdir}/libcblas.a

%changelog
