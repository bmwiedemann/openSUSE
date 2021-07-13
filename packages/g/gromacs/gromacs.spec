#
# spec file for package gromacs
#
# Copyright (c) 2021 SUSE LLC
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


# Build with OpenMPI
%if 0%{?sle_version} == 0
%define mpiver  openmpi2
Obsoletes:      gromacs-openmpi < %{version}
%else
%if 0%{?sle_version} <= 120300
%define mpiver  openmpi
%else
Obsoletes:      gromacs-openmpi < %{version}
  %if 0%{?sle_version} <= 150000
  %define mpiver  openmpi2
  %else
  %define mpiver  openmpi3
  %endif
%endif
%endif

Name:           gromacs
Version:        2021.2
Release:        0
%define uversion %{version}
%define sover   4
Summary:        Molecular Dynamics Package
License:        Apache-2.0 AND GPL-2.0-or-later
Group:          Productivity/Scientific/Chemistry
URL:            http://www.gromacs.org
Source0:        ftp://ftp.gromacs.org/pub/gromacs/gromacs-%{uversion}.tar.gz
Source1:        ftp://ftp.gromacs.org/pub/manual/manual-%{uversion}.pdf
Source2:        ftp://ftp.gromacs.org/regressiontests/regressiontests-%{uversion}.tar.gz

BuildRequires:  %{mpiver}
BuildRequires:  %{mpiver}-devel
BuildRequires:  cmake >= 3.13.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  lapack-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fftw3)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

%package devel
Summary:        Molecular dynamics package
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains development libraries and header for GROMACS

%package -n libgromacs%sover
Summary:        Libraries for Gromacs
Group:          System/Libraries

%description -n libgromacs%sover
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains libraries for Gromacs

%package bash-completion
Summary:        Bash completion for Gromacs
Group:          Productivity/Other
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
BuildArch:      noarch
Provides:       %{name}-bash = %{version}
Obsoletes:      %{name}-bash < %{version}

%description bash-completion
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains bash completion support for gromacs.

%package doc
Summary:        Documentation for Gromacs
Group:          Productivity/Scientific/Chemistry
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains documentation for gromacs.

%package %{mpiver}
Summary:        Molecular dynamics package
Group:          Productivity/Scientific/Chemistry
Requires:       %{name} = %{version}

%description %{mpiver}
GROMACS is a versatile and extremely well optimized package to perform
molecular dynamics computer simulations and subsequent trajectory analysis.
It is developed for biomolecules like proteins, but the extremely high
performance means it is used also in several other field like polymer chemistry
and solid state physics.

This package contains the %{mpiver} version of GROMACS.

%prep
%setup -q -n %{name}-%{uversion}
tar -xzf %{S:2}

%build
source %{_libdir}/mpi/gcc/%{mpiver}/bin/mpivars.sh

# save some memory
%ifarch ppc64le
%global _smp_mflags -j1
%endif

%ifarch %x86 x86_64
#increse to SSE4.1, AVX_128_FMA, AVX_256 when possible
%define acce SSE2
%else
%define acce None
%endif
mkdir nompi
cd nompi

# regression are currently broken on i686, https://redmine.gromacs.org/issues/2584
# and cannot be used with GMX_BUILD_MDRUN_ONLY=ON
%cmake \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DCMAKE_VERBOSE_MAKEFILE=TRUE \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags} -fno-strict-aliasing" \
  -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=ON \
  -DGMX_SIMD=%{acce} \
  -DGMX_MPI=OFF \
  -DGMX_THREAD_MPI=ON \
%ifarch x86_64
  -DGMX_GPU=OpenCL \
%endif
  -DGMX_OPENMP=ON \
  -DGMX_INSTALL_LEGACY_API=ON \
%ifnarch i586 %arm # regressiontest are not support on 32-bit archs: http://redmine.gromacs.org/issues/2584#note-35
  -DREGRESSIONTEST_PATH="$PWD/../../regressiontests-%{uversion}" \
%endif
  ../../
%cmake_build

cd ../..
mkdir %{mpiver}
cd %{mpiver}
%{cmake} \
  -DCMAKE_INSTALL_PREFIX=/usr \
  -DCMAKE_VERBOSE_MAKEFILE=TRUE \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags} -fno-strict-aliasing" \
  -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=ON \
  -DGMX_SIMD=%{acce} \
  -DGMX_BUILD_MDRUN_ONLY=ON \
  -DBUILD_SHARED_LIBS=OFF \
  -DGMX_MPI=ON \
%ifarch x86_64
  -DGMX_GPU=OpenCL \
%endif
  -DGMX_OPENMP=ON \
  -DGMX_INSTALL_LEGACY_API=ON \
  ../../
%cmake_build

%install
cd nompi
%cmake_install
cd ../%{mpiver}
%cmake_install
cd ..

#no need when installed in /usr
rm -f %{buildroot}%{_bindir}/GMXRC*
# Move bash completion file to correct location
mkdir -p %{buildroot}%{_datadir}/bash_completion.d
#concatenate all gmx-completion*, starting with gmx-completion.bash (fct defs)
cat %{buildroot}%{_bindir}/gmx-completion{,?*}.bash > %{buildroot}%{_datadir}/bash_completion.d/gromacs
rm -f %{buildroot}%{_bindir}/gmx-completion*

cp %{S:1} %{buildroot}%{_datadir}/gromacs

%fdupes -s %{buildroot}

%check
#s390x is too slow for tests
# gmock based tests don't work on i586
%ifnarch s390x i586
%make_build -C nompi/build check
%make_build -C %{mpiver}/build check
%endif

%post   -n libgromacs%sover -p /sbin/ldconfig
%postun -n libgromacs%sover -p /sbin/ldconfig

%files
%{_bindir}/gmx
%{_bindir}/*.pl
%dir %{_datadir}/gromacs
%{_datadir}/gromacs/top
%ifarch x86_64
%{_datadir}/gromacs/opencl
%exclude %{_datadir}/gromacs/opencl/gromacs/*/*.h
%exclude %{_datadir}/gromacs/opencl/gromacs/*/*/*.h
%endif
%{_mandir}/man1/*

%files -n libgromacs%sover
%{_libdir}/lib*.so.*

%files doc
%doc %{_datadir}/gromacs/*.pdf
%doc %{_datadir}/gromacs/README*
%doc %{_datadir}/gromacs/COPYING

%files %{mpiver}
%{_bindir}/*_mpi

%files devel
%{_datadir}/gromacs/template
%{_datadir}/cmake
%{_includedir}/gromacs/
%{_includedir}/gmxapi/
%{_includedir}/nblib/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%ifarch x86_64
%dir %{_datadir}/gromacs/opencl
%{_datadir}/gromacs/opencl/gromacs/*/*.h
%{_datadir}/gromacs/opencl/gromacs/*/*/*.h
%endif

%files bash-completion
%dir %{_datadir}/bash_completion.d
%{_datadir}/bash_completion.d/gromacs

%changelog
