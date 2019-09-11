#
# spec file for package lapack
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


Name:           lapack
Version:        3.8.0
Release:        0
Summary:        Linear Algebra Package
License:        BSD-3-Clause
Group:          Development/Libraries/Parallel
Url:            http://www.netlib.org/lapack/
Source0:        http://www.netlib.org/lapack/%{name}-%{version}.tar.gz
Source1:        lapack_testing.py
Source99:       baselibs.conf
Patch1:         lapack-3.2.2.patch
BuildRequires:  gcc-fortran
BuildRequires:  python3
BuildRequires:  update-alternatives
Requires(pre):  update-alternatives
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%if 0%{?suse_version} >= 1120
Requires(pre):  update-alternatives
%endif

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
%if 0%{?suse_version} >= 1120
Requires(pre):  update-alternatives
%endif

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
Provides:       lapacke-devel-static = %{version}

%description -n lapacke-devel
LAPACKE headers and development files.

%package     -n lapacke-devel-static
Summary:        LAPACKE development files - static libraries
Group:          Development/Libraries/C and C++
Requires:       lapacke-devel = %{version}

%description -n lapacke-devel-static
LAPACKE development files  - static libraries.

%prep
%setup -q
%patch1

%build
case "$RPM_ARCH" in
    i[0-9]86) PRECFLAGS="-ffloat-store" ;;
    *)        PRECFLAGS="" ;;
esac
export PRECFLAGS
cp make.inc.example make.inc
make cleanlib %{?_smp_mflags}
make %{?_smp_mflags} blaslib \
  OPTS="%{optflags} -fPIC" \
  NOOPT="%{optflags} -O0 -fPIC"
mv librefblas.a libblas_pic.a
mkdir tmp
( cd tmp; ar x ../libblas_pic.a )
gfortran -shared -Wl,-soname=libblas.so.3 -o libblas.so.%{version} tmp/*.o
ln -s libblas.so.%{version} libblas.so
rm -rf tmp
make cleanlib %{?_smp_mflags}
make %{?_smp_mflags} blaslib \
  OPTS="%{optflags}" \
  NOOPT="%{optflags} -O0"
make blas_testing \
  OPTS="%{optflags} $PRECFLAGS" \
  NOOPT="%{optflags} $PRECFLAGS -O0"
if grep -B15 -A15 FAIL BLAS/*.out; then
  echo
  echo "blas_testing FAILED"
  echo
  false
else
  true  # No failures
fi
mv librefblas.a libblas.a
make cleanlib %{?_smp_mflags}
make %{?_smp_mflags} lapacklib \
  OPTS="%{optflags} -fPIC" \
  NOOPT="%{optflags} -O0 -fPIC"
mv liblapack.a liblapack_pic.a
mkdir tmp
( cd tmp; ar x ../liblapack_pic.a )
gfortran -shared -Wl,-soname=liblapack.so.3 -o liblapack.so.%{version} tmp/*.o -L. -lblas
ln -s liblapack.so.%{version} liblapack.so
rm -rf tmp
make cleanlib %{?_smp_mflags}
make %{?_smp_mflags} lapacklib \
  OPTS="%{optflags}" \
  NOOPT="%{optflags} -O0"
ln -s libblas.a librefblas.a
cd LAPACKE
make %{?_smp_mflags} lapacke \
  CFLAGS="%{optflags} -fPIC -DADD_ -DHAVE_LAPACK_CONFIG_H -DLAPACK_COMPLEX_STRUCTURE" \
  LINKER=gfortran
mv ../liblapacke.a liblapacke_pic.a
mkdir tmp
( cd tmp; ar x ../liblapacke_pic.a )
gfortran -shared -Wl,-soname=liblapacke.so.3 -o liblapacke.so.%{version} tmp/*.o
ln -s liblapacke.so.%{version} liblapacke.so
rm -rf tmp
make cleanlib %{?_smp_mflags}
make %{?_smp_mflags} lapacke \
  CFLAGS="%{optflags} -DADD_ -DHAVE_LAPACK_CONFIG_H -DLAPACK_COMPLEX_STRUCTURE"
mv ../liblapacke.a liblapacke.a
# fix wrong end of line
sed -i 's/\r//' LICENSE
cd ..
cp %{SOURCE1} .
make lapack_testing \
  OPTS="%{optflags} $PRECFLAGS" \
  NOOPT="%{optflags} $PRECFLAGS -O0"
if grep -B15 -A15 FAIL TESTING/*.out; then
  echo
  echo "lapack_testing FAILED"
  echo
  false
else
  true  # No failures
fi

%install
install -d %{buildroot}/%{_libdir}
install -d %{buildroot}/%{_sysconfdir}/alternatives
## BLAS
install -d %{buildroot}/%{_libdir}/blas
install -m 644 libblas.a %{buildroot}/%{_libdir}
install -m 755 libblas.so.%{version} %{buildroot}/%{_libdir}/blas
ln -s libblas.so.%{version} %{buildroot}/%{_libdir}/blas/libblas.so.3
ln -s blas/libblas.so.%{version} %{buildroot}/%{_libdir}/libblas.so
# dummy target for update-alternatives
ln -s blas/libblas.so.%{version} %{buildroot}/%{_libdir}/libblas.so.3
ln -s libblas.so.%{version} %{buildroot}/%{_sysconfdir}/alternatives/libblas.so.3
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
install -d %{buildroot}/%{_includedir}
cd LAPACKE
install -m 644 include/*.h %{buildroot}/%{_includedir}
install -m 644 liblapacke.a %{buildroot}/%{_libdir}
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

%post -n liblapacke3 -p /sbin/ldconfig

%postun -n liblapacke3 -p /sbin/ldconfig

%files -n liblapack3
%defattr(-,root,root)
%doc README.md
%license LICENSE
%dir %{_libdir}/lapack
%{_libdir}/lapack/liblapack.so.%{version}
%{_libdir}/lapack/liblapack.so.3
%if 0%{?suse_version} >= 1120
%ghost %{_libdir}/liblapack.so.3
%ghost %{_sysconfdir}/alternatives/liblapack.so.3
%else
%{_libdir}/liblapack.so.3
%{_sysconfdir}/alternatives/liblapack.so.3
%endif

%files -n libblas3
%defattr(-,root,root)
%doc README.md
%license LICENSE
%dir %{_libdir}/blas
%{_libdir}/blas/libblas.so.%{version}
%{_libdir}/blas/libblas.so.3
%if 0%{?suse_version} >= 1120
%ghost %{_libdir}/libblas.so.3
%ghost %{_sysconfdir}/alternatives/libblas.so.3
%else
%{_libdir}/libblas.so.3
%{_sysconfdir}/alternatives/libblas.so.3
%endif

%files devel
%defattr(-,root,root)
%{_libdir}/liblapack.so

%files devel-static
%defattr(-,root,root)
%{_libdir}/liblapack.a

%files -n blas-devel
%defattr(-,root,root)
%{_libdir}/libblas.so

%files -n blas-devel-static
%defattr(-,root,root)
%{_libdir}/libblas.a

%files -n liblapacke3
%defattr(-,root,root,-)
%{_libdir}/liblapacke.so.%{version}
%{_libdir}/liblapacke.so.3

%files -n lapacke-devel
%defattr(-,root,root,-)
%doc LAPACKE/LICENSE LAPACKE/README
%{_libdir}/liblapacke.so
%{_includedir}/*.h

%files -n lapacke-devel-static
%defattr(-,root,root,-)
%{_libdir}/liblapacke.a

%changelog
