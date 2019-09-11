#
# spec file for package cblas
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cblas
Version:        20110120
Release:        0
# original tarball unversioned, last modification date used as version
# http://icl.cs.utk.edu/lapack-forum/archives/lapack/msg00659.html
Summary:        A standard C language APIs for BLAS
License:        BSD-3-Clause
Group:          System/Libraries
Url:            http://www.netlib.org/blas/
Source0:        cblas.tgz
# http://www.netlib.org/blas/blast-forum/cblas.tgz
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-fortran
# blas is needed for tests only
BuildRequires:  blas-devel
BuildRequires:  update-alternatives

%description
This library provides a native C interface to BLAS routines available
at www.netlib.org/blas to facilitate usage of BLAS functionality 
for C programmers.

%package     -n libcblas3
Summary:        CBLAS development files
Group:          Development/Libraries/C and C++
Requires(post): update-alternatives
Requires(preun): update-alternatives

%description -n libcblas3
This library provides a native C interface to BLAS routines available
at www.netlib.org/blas to facilitate usage of BLAS functionality 
for C programmers.

%package        devel
Requires:       libcblas3 = %{version}
Provides:       cblas = %{version}
Summary:        CBLAS development files
Group:          Development/Libraries/C and C++

%description    devel
cblas headers and development files.

%package        devel-static
Summary:        CBLAS development files for -static linking
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description    devel-static
The cblas-devel-static package contains the CBLAS static libraries
for -static linking. You do not need these, unless you link
statically, which is highly discouraged.

%prep
%setup -q -n CBLAS
cp Makefile.LINUX Makefile.in

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
make %{?_smp_mflags} alllib CFLAGS="%{optflags} -fPIC -DADD_" \
	FFLAGS="%{optflags} -fPIC" LOADER=gfortran
mv lib/cblas_LINUX.a ./libcblas_pic.a

mkdir tmp
( cd tmp; ar x ../libcblas_pic.a )
gfortran -shared -Wl,-soname=libcblas.so.3 -o libcblas.so.%version tmp/*.o

# build static version
make clean
make alllib CFLAGS="%{optflags} -DADD_" FFLAGS="%{optflags}"
mv lib/cblas_LINUX.a ./libcblas.a

%install
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_libdir}/blas
install -d %{buildroot}%{_includedir}
install -d %{buildroot}%{_sysconfdir}/alternatives
install -m 644 include/*.h %{buildroot}%{_includedir}
install -m 644 libcblas*.a %{buildroot}%{_libdir}
install -m 755 libcblas.so.%{version} %{buildroot}%{_libdir}/blas
ln -s libcblas.so.%{version} %{buildroot}/%{_libdir}/blas/libcblas.so.3
ln -s blas/libcblas.so.3 %{buildroot}/%{_libdir}/libcblas.so
# dummy target for update-alternatives
ln -s blas/libcblas.so.3 %{buildroot}/%{_libdir}/libcblas.so.3
ln -s libcblas.so.3 %{buildroot}/%{_sysconfdir}/alternatives/libcblas.so.3

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH
make alltst runtst \
     BLLIB=%{_libdir}/libblas.so \
     CBLIB=%{buildroot}%{_libdir}/libcblas.so \
     CFLAGS="%{optflags} -DADD_" FFLAGS="%{optflags} -O0"

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

%files -n libcblas3
%defattr(-,root,root,-)
%{_libdir}/blas/libcblas.so.%{version}
%{_libdir}/blas/libcblas.so.3
%dir %{_libdir}/blas
%ghost %{_libdir}/libcblas.so.3
%ghost %{_sysconfdir}/alternatives/libcblas.so.3

%files devel
%defattr(-,root,root,-)
%doc README
%{_libdir}/libcblas.so
%{_includedir}/*

%files devel-static
%defattr(-,root,root)
%_libdir/libcblas.a
%_libdir/libcblas_pic.a

%changelog
