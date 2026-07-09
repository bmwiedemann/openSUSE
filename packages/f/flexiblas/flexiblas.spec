#
# spec file for package flexiblas
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           flexiblas
Version:        3.5.0
Release:        0
Summary:        A BLAS/LAPACK wrapper library with runtime exchangeable backends
License:        LGPL-3.0 and BSD-3-Clause
URL:            https://www.mpi-magdeburg.mpg.de/projects/flexiblas
Source0:        https://github.com/mpimd-csc/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
#!BuildConflicts: update-alternatives
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-fortran
BuildRequires:  libopenblas_openmp-devel
BuildRequires:  libopenblas_pthreads-devel
BuildRequires:  libopenblas_serial-devel
BuildRequires:  ninja

%description
FlexiBLAS is a wrapper library that enables the exchange of the BLAS and LAPACK
implementation used by a program without recompiling or relinking it.

%package devel
Summary:        Development files for flexiblas
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
This package contains development files for flexiblas.

%package netlib
Summary:        FlexiBLAS NETLIB backend
Requires:       %{name} = %{version}-%{release}

%description netlib
This package provides the NETLIB backend for FlexiBLAS.

%package openblas-openmp
Summary:        FlexiBLAS OpenBLAS OpenMP backend
Requires:       %{name} = %{version}-%{release}
Requires:       libopenblas_openmp0

%description openblas-openmp
This package provides the OpenBLAS OpenMP backend for FlexiBLAS.

%package openblas-pthreads
Summary:        FlexiBLAS OpenBLAS pthreads backend
Requires:       %{name} = %{version}-%{release}
Requires:       libopenblas_pthreads0

%description openblas-pthreads
This package provides the OpenBLAS pthreads backend for FlexiBLAS.

%package openblas-serial
Summary:        FlexiBLAS OpenBLAS serial backend
Requires:       %{name} = %{version}-%{release}
Requires:       libopenblas_serial0

%description openblas-serial
This package provides the OpenBLAS serial backend for FlexiBLAS.

%package man
Summary:        Manual pages for flexiblas
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description man
Manual pages for flexiblas.

%prep
%autosetup

%build
rpm -E cmake \
%{nil}
%cmake \
  -DCMAKE_EXE_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now" \
  -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now" \
  -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
  -DSYSCONFDIR="%{_sysconfdir}" \
  -DDEBUG=ON \
  -DCBLAS=ON \
  -DABI=GNU \
  -DLTO=ON \
  %{nil}

%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README.md
%{_bindir}/flexiblas
%{_bindir}/flexiblas-config
%dir %{_sysconfdir}/flexiblasrc.d
%config(noreplace) %{_sysconfdir}/flexiblasrc
%{_libdir}/libflexiblas*.so.*
%dir %{_libdir}/flexiblas
%{_libdir}/flexiblas/libflexiblas_fallback_lapack.so
%{_libdir}/flexiblas/libflexiblas_hook_dummy.so
%{_libdir}/flexiblas/libflexiblas_hook_profile.so

%files netlib
%config(noreplace) %{_sysconfdir}/flexiblasrc.d/NETLIB.conf
%{_libdir}/flexiblas/libflexiblas_netlib.so

#%files openblas-openmp
#%config(noreplace) %{_sysconfdir}/flexiblasrc.d/OpenBLASOMP.conf
#%{_libdir}/flexiblas/libflexiblas_openblas-omp.so

%files openblas-pthreads
%config(noreplace) %{_sysconfdir}/flexiblasrc.d/OpenBLASPThread.conf
%{_libdir}/flexiblas/libflexiblas_openblaspthread.so

#%files openblas-serial
#%config(noreplace) %{_sysconfdir}/flexiblasrc.d/OpenBLASSerial.conf
#%{_libdir}/flexiblas/libflexiblas_openblas-serial.so

%files devel
%{_includedir}/flexiblas/
%{_libdir}/libflexiblas*.so
%{_libdir}/pkgconfig/flexiblas*.pc

%files man
%{_mandir}/man1/flexiblas.1%{?ext_man}
%{_mandir}/man3/flexiblas_*.3%{?ext_man}
%{_mandir}/man7/flexiblas-api.7%{?ext_man}

%changelog
