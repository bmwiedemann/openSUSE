#
# spec file for package fftw3
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


%define bname fftw
%define BNAME FFTW

%bcond_with ringdisabled

%if !0%{?is_opensuse:1} && 0%{?sle_version:1} && 0%{?sle_version} < 150300
%define DisOMPI4 ExclusiveArch:  do_not_build
%endif
%if 0%{?sle_version:1} && 0%{?sle_version} < 160000
%define DisOMPI5 ExclusiveArch:  do_not_build
%endif

%ifnarch %{arm} %ix86 s390 s390x
%bcond_without mpi
%endif
%bcond_without system_packages

%define package_libname lib%{name}-3

Name:           fftw3
BuildRequires:  fdupes
BuildRequires:  pkgconfig
Version:        3.3.10
Release:        0
Summary:        Discrete Fourier Transform (DFT) C Subroutine Library
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://www.fftw.org
Source:         ftp://ftp.fftw.org/pub/fftw/fftw-%{version}%{?pl_ext:-%{pl_ext}}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
Requires:       %{name}-libs = %{version}
%if %{with mpi}
BuildRequires:  openmpi-macros-devel
%endif

%description
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %package_libname = %{version}-%{release}
Requires:       glibc-devel
Requires(post): %install_info_prereq
Requires(preun): %install_info_prereq
Provides:       fftw-devel

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package devel-static
Summary:        Static libraries for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel

%description devel-static
Libraries to build statically linked applications with fftw3.

%package -n %package_libname
Summary:        Discrete Fourier Transform (DFT) C Subroutine Library
# Remove Prov/Obs when appropriate; were added 2011-Nov-21 (post-openSUSE-12.1)
Group:          System/Libraries
Provides:       fftw3 = %{version}-%{release}
Obsoletes:      fftw3 < 3.3
%if %{with hpc}
%hpc_requires
%endif

%description -n %package_libname
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package -n libfftw3_threads3
Summary:        Discrete Fourier Transform (DFT) C subroutine library
Group:          Productivity/Scientific/Math
Provides:       fftw3-threads = %{version}-%{release}
Obsoletes:      fftw3-threads < 3.3
# libfftw3_threads.so does not have a DT_NEEDED entry for fftw symbols, since it
# may be used with either libfftw3.so or libfftw3f.so. Hence, manual Requires.
#Requires:       libfftw3-3 = %%{version}

%description -n libfftw3_threads3
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package threads-devel
Summary:        Discrete Fourier Transform (DFT) C subroutine library
Group:          Development/Libraries/C and C++
Requires:       fftw3-devel = %{version}-%{release}
Requires:       glibc-devel
Requires:       libfftw3_threads3 = %{version}-%{release}

%description threads-devel
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package -n libfftw3_omp3
Summary:        Discrete Fourier Transform (DFT) C subroutine library
Group:          Productivity/Scientific/Math
Provides:       fftw3-openmp = %{version}-%{release}
Obsoletes:      fftw3-openmp < 3.3
# Same as libfftw3_threads.so: manual Requires for fftw3 main lib
#Requires:       libfftw3-3 = %%{version}

%description -n libfftw3_omp3
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package openmp-devel
Summary:        Discrete Fourier Transform (DFT) C subroutine library
Group:          Development/Libraries/C and C++
Requires:       fftw3-devel = %{version}-%{release}
Requires:       glibc-devel
Requires:       libfftw3_omp3 = %{version}-%{release}

%description openmp-devel
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%if %{with mpi}
%package -n libfftw3_mpi3
Summary:        Discrete Fourier Transform (DFT) C subroutine library
Group:          Productivity/Scientific/Math
Provides:       fftw3-mpi = %{version}-%{release}
Obsoletes:      fftw3-mpi < 3.3
# Same as libfftw3_threads.so: manual Requires for fftw3 main lib
#Requires:       libfftw3-3 = %%{version}
#Requires:       openmpi

%description -n libfftw3_mpi3
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package mpi-devel
Summary:        Discrete Fourier Transform (DFT) C subroutine library
Group:          Development/Libraries/C and C++
Requires:       fftw3-devel = %{version}
Requires:       glibc-devel
Requires:       libfftw3_mpi3 = %{version}-%{release}
Requires:       openmpi-devel

%description mpi-devel
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.
%endif

%prep
%setup -q -n %{bname}-%{version}%{?pl_ext:-%{pl_ext}}

cat > %{_sourcedir}/baselibs.conf  <<EOF
%{package_libname}
lib%{name}_threads3
lib%{name}_omp3
lib%{name}_mpi3
EOF

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%if %{with mpi}
%setup_openmpi
%endif

%configure \
  --disable-static \
%if %{with mpi}
  --enable-mpi \
%endif
%ifarch %ix86 x86_64
  --enable-sse2 \
  --enable-avx \
%endif
  --enable-shared \
  --enable-threads \
  --enable-openmp

make %{?_smp_mflags}

%install
%makeinstall

# remove unneeded files
rm -f %{buildroot}%{_libdir}/lib*.*a

# hack to also compile/install single-precision version:
make distclean

%if %{with mpi}
%setup_openmpi
%endif

%configure \
	--enable-shared --enable-threads --enable-float --enable-openmp \
%if %{with mpi}
  --enable-mpi \
%endif
%ifarch %ix86 x86_64
  --enable-sse2 \
%endif
  --disable-static

make %{?_smp_mflags}
%makeinstall

# hack to also compile/install long-double-precision version:
make distclean

%if %{with mpi}
%setup_openmpi
%endif
%configure \
	--enable-shared --enable-threads --enable-long-double --enable-openmp \
%if %{with mpi}
  --enable-mpi \
%endif
  --disable-static

make %{?_smp_mflags}
%makeinstall

# remove unneeded files
rm -f %{buildroot}%{_libdir}/lib*.*a

gzip -9nf %{buildroot}%{_infodir}/*.info*

# remove Makefiles in doc directory at last
find doc -name 'Makefile*' | xargs rm

%fdupes -s doc

# cmake files are incomplete and useless when installed via auto-tools (bsc#1194728)
rm -rf %{buildroot}%{_libdir}/cmake

%preun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/fftw3.info.gz

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/fftw3.info.gz

%post -n %package_libname  -p /sbin/ldconfig

%postun -n %package_libname -p /sbin/ldconfig

%post -n libfftw3_threads3 -p /sbin/ldconfig

%postun -n libfftw3_threads3 -p /sbin/ldconfig

%post -n libfftw3_omp3 -p /sbin/ldconfig

%postun -n libfftw3_omp3 -p /sbin/ldconfig

%if %{with mpi}
%post -n libfftw3_mpi3 -p /sbin/ldconfig

%postun -n libfftw3_mpi3 -p /sbin/ldconfig
%endif

%files -n %package_libname
%{_libdir}/libfftw3.so.3*
%{_libdir}/libfftw3f.so.3*
%{_libdir}/libfftw3l.so.3*

%files -n libfftw3_threads3
%{_libdir}/libfftw3_threads.so.3*
%{_libdir}/libfftw3f_threads.so.3*
%{_libdir}/libfftw3l_threads.so.3*

%files -n libfftw3_omp3
%{_libdir}/libfftw3_omp.so.3*
%{_libdir}/libfftw3f_omp.so.3*
%{_libdir}/libfftw3l_omp.so.3*

%if %{with mpi}
%files -n libfftw3_mpi3
%{_libdir}/libfftw3_mpi.so.3*
%{_libdir}/libfftw3f_mpi.so.3*
%{_libdir}/libfftw3l_mpi.so.3*
%endif
# ENDIF FOR {with mpi}

%files devel
%license COPYING
%doc AUTHORS CONVENTIONS COPYRIGHT ChangeLog NEWS README TODO
%doc doc/*
%doc %{_mandir}/man?/*
%{_infodir}/*.info*
%{_includedir}/fftw3.*
%{_includedir}/fftw3q.f03
%{_includedir}/fftw3l.f03
%{_libdir}/libfftw3.so
%{_libdir}/libfftw3f.so
%{_libdir}/libfftw3l.so
%{_libdir}/pkgconfig/*.pc
%{_bindir}/*

%files threads-devel
%{_libdir}/libfftw3_threads.so
%{_libdir}/libfftw3f_threads.so
%{_libdir}/libfftw3l_threads.so

%files openmp-devel
%{_libdir}/libfftw3_omp.so
%{_libdir}/libfftw3f_omp.so
%{_libdir}/libfftw3l_omp.so

%if %{with mpi}
%files mpi-devel
%{_libdir}/libfftw3_mpi.so
%{_libdir}/libfftw3f_mpi.so
%{_libdir}/libfftw3l_mpi.so
%{_includedir}/fftw3-mpi.*
%{_includedir}/fftw3l-mpi.f03
%endif
# ENDIF FOR {with mpi}

%changelog
