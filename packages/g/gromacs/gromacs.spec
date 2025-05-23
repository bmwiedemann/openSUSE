#
# spec file for package gromacs
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2015-2019 Christoph Junghans <junghans@votca.org>
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

# Section 32-bit archs officially unsupported
# https://gitlab.com/gromacs/gromacs/-/merge_requests/2453
ExcludeArch:    %{ix86} %{arm}
# /Section

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%endif

%if "%flavor" == "openmpi"
%{bcond_without mpi}
%else
%{bcond_with    mpi}
%endif

%if %{with mpi}
%define libname_gromacs libgromacs_mpi10
%define libname_gmxapi libgmxapi_mpi0
%else
%define libname_gromacs libgromacs10
%define libname_gmxapi libgmxapi0
%endif
%define libname_nblib_gmx libnblib_gmx0

%ifarch x86_64
%bcond_without opencl
%else
%bcond_with    opencl
%endif

%bcond_with    tinyxml2
%bcond_without tests

Name:           gromacs%{?with_mpi:-openmpi}
Version:        2025.1
Release:        0
%define uversion %{version}
Summary:        Molecular Dynamics Package
License:        Apache-2.0 AND LGPL-2.1-or-later AND BSD-3-Clause
Group:          Productivity/Scientific/Chemistry
URL:            https://www.gromacs.org
Source0:        ftp://ftp.gromacs.org/pub/gromacs/gromacs-%{uversion}.tar.gz
Source1:        ftp://ftp.gromacs.org/pub/manual/manual-%{uversion}.pdf
Source2:        ftp://ftp.gromacs.org/regressiontests/regressiontests-%{uversion}.tar.gz
BuildRequires:  cmake >= 3.13.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 9
BuildRequires:  lapack-devel
%if %{with opencl}
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
%endif
%if %{with mpi}
BuildRequires:  openmpi-devel
BuildRequires:  openmpi-macros-devel
%endif
BuildRequires:  pkg-config
BuildRequires:  cmake(GTest)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(muparser)
BuildRequires:  pkgconfig(zlib)
%if %{with tinyxml2}
BuildRequires:  (pkgconfig(tinyxml2) > 3.0 with pkgconfig(tinyxml2) < 7)
%endif
Requires:       gromacs-data = %{version}
%if %{with mpi}
# MPI communication fails on 32bit architectures
ExcludeArch:    %{ix86} %{arm} ppc
%endif

%description
GROMACS is a package to perform molecular dynamics computer
simulations and subsequent trajectory analysis. It is developed for
biomolecules like proteins, but it can be used in several other field
like polymer chemistry and solid state physics.

%package devel
Summary:        Molecular dynamics package
Group:          Development/Libraries/C and C++
Requires:       %{libname_gmxapi} = %{version}-%{release}
Requires:       %{libname_gromacs} = %{version}-%{release}
Requires:       %{libname_nblib_gmx} = %{version}-%{release}
# cmake files refer to /usr/bin/gmx, too
Requires:       %{name} = %{version}-%{release}

%description devel
GROMACS is a package to perform molecular dynamics computer
simulations.

This package contains development libraries and header for GROMACS

%package -n %{libname_gromacs}
Summary:        Libraries for Gromacs
Group:          System/Libraries

%description -n %{libname_gromacs}
GROMACS is a package to perform molecular dynamics computer
simulations.

This package contains libraries for Gromacs

%package -n %{libname_gmxapi}
Summary:        Libraries for Gromacs
Group:          System/Libraries

%description -n %{libname_gmxapi}
GROMACS is a package to perform molecular dynamics computer
simulations.

This package contains libraries for Gromacs.

%package -n %{libname_nblib_gmx}
Summary:        Libraries for Gromacs
Group:          System/Libraries

%description -n %{libname_nblib_gmx}
GROMACS is a package to perform molecular dynamics computer
simulations.

This package contains libraries for Gromacs.

%package bash-completion
Summary:        Bash completion for Gromacs
Group:          Productivity/Other
Supplements:    (bash-completion and gromacs)
Supplements:    (bash-completion and gromacs-openmpi)
BuildArch:      noarch
Provides:       %{name}-bash = %{version}
Obsoletes:      %{name}-bash < %{version}

%description bash-completion
GROMACS is a package to perform molecular dynamics computer
simulations.

This package contains bash completion support for gromacs.

%package doc
Summary:        Documentation for Gromacs
Group:          Productivity/Scientific/Chemistry
BuildArch:      noarch

%description doc
GROMACS is a package to perform molecular dynamics computer
simulations.

This package contains documentation for gromacs.

%package data
Summary:        Data files for Gromacs
Group:          Productivity/Scientific/Chemistry
# Package split
Provides:       gromacs:%{_datadir}/gromacs/README.tutor
Conflicts:      gromacs < %{version}-%{release}
BuildArch:      noarch

%description data
GROMACS is a package to perform molecular dynamics computer
simulations.

This package contains data files for gromacs.

%prep
%autosetup -n gromacs-%{uversion} -p1
tar -xzf %{S:2}
# Force same behavior on 32 and 64 bit archs
sed -i -e '/set(CMAKE_BUILD_WITH_INSTALL_RPATH/ s@.*@# \0@' CMakeLists.txt

%build
%if %{with mpi}
%setup_openmpi
%endif

%global acce None
%ifarch %x86 x86_64
#increase to SSE4.1, AVX_128_FMA, AVX_256 when possible
%global acce SSE2
%endif
%ifarch aarch64
%global simd ARM_NEON_ASIMD
%endif

# Avoid oversubscription, some tests run with 2 Ranks locally
export MAX_TEST_THREADS=$(( %{?_smp_build_ncpus}%{!?_smp_build_ncpus:2} / 2 ))
%cmake \
  -DGMX_VERSION_STRING_OF_FORK=openSUSE \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DCMAKE_VERBOSE_MAKEFILE=TRUE \
  -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags} -fno-strict-aliasing" \
  -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=ON \
  -DGMX_BUILD_UNITTESTS:BOOL=ON \
  -DGMX_EXTERNAL_TINYXML2:BOOL=%{?with_tinyxml:ON}%{!?with_tinyxml:OFF} \
  -DGMX_EXTERNAL_ZLIB:BOOL=ON \
  -DGMX_USE_MUPARSER=EXTERNAL \
  -DGMX_SIMD=%{acce} \
%if %{with mpi}
  -DGMX_MPI=ON \
%else
  -DGMX_MPI=OFF \
  -DGMX_THREAD_MPI=ON \
%endif
%if %{with opencl}
  -DGMX_GPU=OpenCL \
%endif
  -DGMX_OPENMP=ON \
  -DGMX_INSTALL_LEGACY_API=ON \
  -DREGRESSIONTEST_PATH="%{_builddir}/gromacs-%{uversion}/regressiontests-%{uversion}" \
  -DGMX_TEST_NUMBER_PROCS=${MAX_TEST_THREADS} \
  %{nil}
%cmake_build
%cmake_build tests

%install
%cmake_install

# fix shebang
sed -i '1s@env @@' %{buildroot}/%{_bindir}/*.pl

#no need when installed in /usr
rm -f %{buildroot}%{_bindir}/GMXRC*

%if %{without mpi}
# Move bash completion file to correct location
mkdir -p %{buildroot}%{_datadir}/bash_completion.d
#concatenate all gmx-completion*, starting with gmx-completion.bash (fct defs)
cat %{buildroot}%{_bindir}/gmx-completion{,?*}.bash > %{buildroot}%{_datadir}/bash_completion.d/gromacs

cp %{S:1} %{buildroot}%{_datadir}/gromacs

%else
rm -f %{buildroot}%{_bindir}/*.pl
rm -Rf %{buildroot}%{_datadir}/gromacs/*
# nblib_gmx is the same for MPI and non-MPI builds
rm -f %{buildroot}%{_libdir}/libnblib_gmx*
rm -f %{buildroot}%{_mandir}/man1/*
# TODO: Some parts of the devel files are MPI dependent
rm -Rf %{buildroot}%{_datadir}/cmake
rm -Rf %{buildroot}%{_includedir}/*
rm -f %{buildroot}%{_libdir}/*.so
rm -Rf %{buildroot}%{_libdir}/pkgconfig/*
rm -Rf %{buildroot}%{_datadir}/gromacs/opencl
%endif

rm -f %{buildroot}%{_bindir}/gmx-completion*

%fdupes %{buildroot}%{_datadir}/gromacs

%check
%if %{with tests}
# parallel test are broken, gl#gromacs/gromacs#4975
%ctest
%endif

%post   -n %{libname_gromacs} -p /sbin/ldconfig
%postun -n %{libname_gromacs} -p /sbin/ldconfig
%post   -n %{libname_gmxapi} -p /sbin/ldconfig
%postun -n %{libname_gmxapi} -p /sbin/ldconfig
%post   -n %{libname_nblib_gmx} -p /sbin/ldconfig
%postun -n %{libname_nblib_gmx} -p /sbin/ldconfig

%files
%if %{without mpi}
%{_bindir}/gmx
%{_bindir}/*.pl
%else
%{_bindir}/gmx_mpi
%endif

%files -n %{libname_gromacs}
%{_libdir}/libgromacs*.so.*

%files -n %{libname_gmxapi}
%{_libdir}/libgmxapi*.so.*

%if %{without mpi}
%files -n %{libname_nblib_gmx}
%{_libdir}/libnblib_gmx.so.*

%files data
%dir %{_datadir}/gromacs
%{_datadir}/gromacs/top
%doc %{_mandir}/man1/*

%files doc
%dir %{_datadir}/gromacs
%doc %{_datadir}/gromacs/*.pdf
%doc %{_datadir}/gromacs/README*
%doc %{_datadir}/gromacs/COPYING

%files devel
%{_datadir}/gromacs/template
%{_datadir}/cmake
%{_includedir}/gromacs/
%{_includedir}/gmxapi/
%{_includedir}/nblib/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%if %{with opencl}
%dir %{_datadir}/gromacs/opencl
%{_datadir}/gromacs/opencl/gromacs
%endif

%files bash-completion
%dir %{_datadir}/bash_completion.d
%{_datadir}/bash_completion.d/gromacs
%endif

%changelog
