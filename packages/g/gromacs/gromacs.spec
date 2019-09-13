#
# spec file for package gromacs
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%if 0%{?sle_version} <= 120300
%define mpiver  openmpi
%else
  %if 0%{?sle_version} <= 150000
  %define mpiver  openmpi2
  %else
  %define mpiver  openmpi3
  %endif
%endif

Name:           gromacs
Version:        2019.2
Release:        0
%define uversion %{version}
%define sover   4
Summary:        Molecular Dynamics Package
License:        GPL-2.0-or-later and Apache-2.0
Group:          Productivity/Scientific/Chemistry
Url:            http://www.gromacs.org
Source0:        ftp://ftp.gromacs.org/pub/gromacs/gromacs-%{uversion}.tar.gz
Source1:        ftp://ftp.gromacs.org/pub/manual/manual-%{uversion}.pdf
Source2:        http://gerrit.gromacs.org/download/regressiontests-%{uversion}.tar.gz

BuildRequires:  %{mpiver}
BuildRequires:  %{mpiver}-devel
BuildRequires:  cmake >= 2.8.8
BuildRequires:  fdupes
BuildRequires:  gcc-c++
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

%package bash
Summary:        Bash completion for Gromacs
Group:          Productivity/Other
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
BuildArch:      noarch

%description bash
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

%ifarch %x86 x86_64
#increse to SSE4.1, AVX_128_FMA, AVX_256 when possible
%define acce SSE2
%else
%define acce None
%endif
mkdir nompi
cd nompi
# note about rpath
# gromacs' cmake has too much rpath auto-magic, just
# force to skip it (CMAKE_SKIP_RPATH=1) and use 
# LD_LIBRARY_PATH for checks below

# regression are currently broken on i686, https://redmine.gromacs.org/issues/2584
# and cannot be used with GMX_BUILD_MDRUN_ONLY=ON
%{cmake} \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DCMAKE_VERBOSE_MAKEFILE=TRUE \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags} -fno-strict-aliasing" \
  -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags}" \
  -DCMAKE_SKIP_RPATH=1 \
  -DGMX_SIMD=%{acce} \
  -DGMX_MPI=OFF \
  -DGMX_THREAD_MPI=ON \
%ifarch x86_64
  -DGMX_GPU=ON -DGMX_USE_OPENCL=ON \
%endif
  -DGMX_SYMLINK_OLD_BINARY_NAMES=OFF \
  -DGMX_OPENMP=ON \
%ifnarch i586 %arm # regressiontest are not support on 32-bit archs: http://redmine.gromacs.org/issues/2584#note-35
  -DREGRESSIONTEST_PATH="$PWD/../../regressiontests-%{uversion}" \
%endif
  -DGMX_LIB_INSTALL_DIR=%{_lib} ../../
%make_jobs

cd ../..
mkdir %{mpiver}
cd %{mpiver}
%{cmake} \
  -DCMAKE_INSTALL_PREFIX=/usr \
  -DCMAKE_VERBOSE_MAKEFILE=TRUE \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags} -fno-strict-aliasing" \
  -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags}" \
  -DCMAKE_SKIP_RPATH=1 \
  -DGMX_SIMD=%{acce} \
  -DGMX_BUILD_MDRUN_ONLY=ON \
  -DBUILD_SHARED_LIBS=OFF \
  -DGMX_MPI=ON \
%ifarch x86_64
  -DGMX_GPU=ON -DGMX_USE_OPENCL=ON \
%endif
  -DGMX_SYMLINK_OLD_BINARY_NAMES=OFF \
  -DGMX_OPENMP=ON \
  -DGMX_LIB_INSTALL_DIR=%{_lib} ../../
%make_jobs

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
%ifnarch s390x
LD_LIBRARY_PATH=%{buildroot}/%{_libdir} make -C nompi/build %{?_smp_mflags} check
LD_LIBRARY_PATH='%{buildroot}/%{_libdir}::%{_libdir}/mpi/gcc/%{mpiver}/%{_lib}' make -C %{mpiver}/build %{?_smp_mflags} check
%endif

%post   -n libgromacs%sover -p /sbin/ldconfig
%postun -n libgromacs%sover -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
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
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*

%files doc
%defattr(-,root,root,-)
%doc %{_datadir}/gromacs/*.pdf
%doc %{_datadir}/gromacs/README*
%doc %{_datadir}/gromacs/COPYING

%files %{mpiver}
%defattr(-,root,root,-)
%{_bindir}/*_mpi

%files devel
%defattr(-,root,root)
%{_datadir}/gromacs/template
%{_datadir}/cmake
%{_includedir}/gromacs/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%ifarch x86_64
%dir %{_datadir}/gromacs/opencl
%{_datadir}/gromacs/opencl/gromacs/*/*.h
%{_datadir}/gromacs/opencl/gromacs/*/*/*.h
%endif

%files bash
%defattr(-,root,root,-)
%dir %{_datadir}/bash_completion.d
%{_datadir}/bash_completion.d/gromacs

%changelog
