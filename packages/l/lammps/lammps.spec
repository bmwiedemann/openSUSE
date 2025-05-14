#
# spec file for package lammps
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2017-2020 Christoph Junghans
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


# kokkos >= 4.3.01 required
%bcond_with kokkos
%bcond_without test
%ifarch %ix86
# Missing openmpi-macros-devel on i586
%bcond_with mpi
%else
%bcond_without mpi
%endif
%define shlib lib%{name}0
%define pythons python3
%define __builder ninja
%define         uversion stable_29Aug2024_update2
Name:           lammps
Version:        20240829.02
Release:        0
Summary:        Molecular Dynamics Simulator
License:        GPL-2.0-only AND GPL-3.0-or-later
Group:          Productivity/Scientific/Chemistry
URL:            https://lammps.sandia.gov
Source0:        https://github.com/lammps/lammps/archive/refs/tags/%{uversion}.tar.gz#/%{name}-%{uversion}.tar.gz
# PATCH-FEATURE-OPENSUSE lammps-allow-system-gtest.patch badshah400@gmail.com -- Look for system installed gtest/gmock before trying to download
Patch0:         lammps-allow-system-gtest.patch
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gzip
BuildRequires:  kim-api-devel >= 2.1
BuildRequires:  python3-build
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  voro++-devel
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(OpenCL-CLHPP)
BuildRequires:  pkgconfig(OpenCL-Headers)
BuildRequires:  pkgconfig(clBLAS)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(lapack)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(ocl-icd)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(tbb)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-data
%if "%{?__builder}" == "ninja"
BuildRequires:  ninja
%endif
%if %{with kokkos}
BuildRequires:  kokkos-devel >= 3.2
%endif
%if %{with mpi}
BuildRequires:  openmpi-macros-devel
%endif
%if %{with test}
BuildRequires:  kim-api-examples
BuildRequires:  valgrind
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gmock_main)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gtest_main)
%endif

%description
LAMMPS is a classical molecular dynamics code, and an acronym for Large-scale
Atomic/Molecular Massively Parallel Simulator.

LAMMPS has potentials for soft materials (biomolecules, polymers) and
solid-state materials (metals, semiconductors) and coarse-grained or
mesoscopic systems. It can be used to model atoms or, more generically, as a
parallel particle simulator at the atomic, meso, or continuum scale.

LAMMPS runs on single processors or in parallel using message-passing
techniques and a spatial-decomposition of the simulation domain. The code is
designed to be easy to modify or extend with new functionality.

%package -n %{shlib}
Summary:        A molecular dynamics simulator library
Group:          System/Libraries

%description -n liblammps0
LAMMPS is a classical molecular dynamics code, and an acronym for Large-scale
Atomic/Molecular Massively Parallel Simulator.

LAMMPS has potentials for soft materials (biomolecules, polymers) and
solid-state materials (metals, semiconductors) and coarse-grained or
mesoscopic systems. It can be used to model atoms or, more generically, as a
parallel particle simulator at the atomic, meso, or continuum scale.

LAMMPS runs on single processors or in parallel using message-passing
techniques and a spatial-decomposition of the simulation domain. The code is
designed to be easy to modify or extend with new functionality.

This package contains the library of LAMMPS package.

%package devel
Summary:        Development headers and libraries for LAMMPS
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{shlib} = %{version}

%description devel
LAMMPS is a classical molecular dynamics code, and an acronym for Large-scale
Atomic/Molecular Massively Parallel Simulator.

LAMMPS has potentials for soft materials (biomolecules, polymers) and
solid-state materials (metals, semiconductors) and coarse-grained or
mesoscopic systems. It can be used to model atoms or, more generically, as a
parallel particle simulator at the atomic, meso, or continuum scale.

LAMMPS runs on single processors or in parallel using message-passing
techniques and a spatial-decomposition of the simulation domain. The code is
designed to be easy to modify or extend with new functionality.

This package contains development headers and libraries for LAMMPS.

%package -n %{pythons}-%{name}
Summary:        LAMMPS python module
Group:          Development/Languages/Python
Requires:       %{shlib} = %{version}
BuildArch:      noarch
# File conflict, old package contained python3 module
Conflicts:      python-%{name} <= %{version}
Provides:       python-%{name}:%{python3_sitearch}/%{name}.py

%description -n %{pythons}-%{name}
LAMMPS is a classical molecular dynamics code, and an acronym for Large-scale
Atomic/Molecular Massively Parallel Simulator.

LAMMPS has potentials for soft materials (biomolecules, polymers) and
solid-state materials (metals, semiconductors) and coarse-grained or
mesoscopic systems. It can be used to model atoms or, more generically, as a
parallel particle simulator at the atomic, meso, or continuum scale.

LAMMPS runs on single processors or in parallel using message-passing
techniques and a spatial-decomposition of the simulation domain. The code is
designed to be easy to modify or extend with new functionality.

This subpackage contains LAMMPS's Python module.

%package data
Summary:        LAMMPS data
Group:          Productivity/Scientific/Chemistry
BuildArch:      noarch

%description data
LAMMPS is a classical molecular dynamics code, and an acronym for Large-scale
Atomic/Molecular Massively Parallel Simulator.

LAMMPS has potentials for soft materials (biomolecules, polymers) and
solid-state materials (metals, semiconductors) and coarse-grained or
mesoscopic systems. It can be used to model atoms or, more generically, as a
parallel particle simulator at the atomic, meso, or continuum scale.

LAMMPS runs on single processors or in parallel using message-passing
techniques and a spatial-decomposition of the simulation domain. The code is
designed to be easy to modify or extend with new functionality.

This subpackage contains LAMMPS's potential files

%prep
%autosetup -p1 -n %{name}-%{uversion}

%build
%if %{with mpi}
%setup_openmpi
%endif

pushd cmake
%cmake \
  -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
  -DCMAKE_TUNE_FLAGS='%{?tune_flags}' \
  -DBUILD_TOOLS=ON \
  -DBUILD_LAMMPS_SHELL=$(pkg-config readline && echo ON) \
  -DBUILD_MPI=%{?with_mpi:ON}%{!?with_mpi:OFF} \
  -DBUILD_OMP=ON \
  -DDOWNLOAD_POTENTIALS=OFF \
  -DENABLE_TESTING:BOOL=%{?with_test:ON}%{!?with_test:OFF} \
  -DEXTERNAL_GTEST:BOOL=ON \
  -DFFT=FFTW3 \
  -DGPU_API=OpenCL \
  -DPKG_COMPRESS=ON \
  -DPKG_EXTRA-MOLECULE=ON \
  -DPKG_GPU=ON \
  -DPKG_KIM=ON \
  -DPKG_KSPACE=OFF \
  -DPKG_LEPTON=ON \
  -DPKG_MANYBODY=ON \
  -DPKG_MOLECULE=ON \
  -DPKG_PHONON=OFF \
  -DPKG_PYTHON=ON \
  -DPKG_VORONOI=ON \
  -DPYTHON_EXECUTABLE=%{_bindir}/python%{python3_version} \
  -DUSE_STATIC_OPENCL_LOADER=OFF \
  -DUSE_SPGLIB:BOOL=OFF \
  %{?with_kokkos:-DPKG_KOKKOS=ON -DEXTERNAL_KOKKOS=ON} \
%{nil}
%cmake_build
popd
cd python
%pyproject_wheel

%install
pushd cmake
%cmake_install
popd

pushd python
%pyproject_install
popd

%fdupes %{buildroot}%{_datadir}/%{name}/
%fdupes %{buildroot}%{python3_sitelib}/%{name}/

%if %{with test}
%check
%if %{with mpi}
%setup_openmpi
%endif

pushd cmake
# Do not cause failing tests on non-x86_64 archs to abort builds
# as these are due to minor numerical tolerance differences which
# upstream does not intend to fix. See, for instance,
# * https://github.com/lammps/lammps/issues/2383
# * https://github.com/lammps/lammps/issues/2978
%ifnarch x86_64
%ctest || true
%else
%ctest
%endif
popd

%endif

%ldconfig_scriptlets -n %{shlib}

%files
%doc README
%license LICENSE
%{_bindir}/l{mp,ammps}*
%{_mandir}/man1/lmp.1%{?ext_man}
%{_bindir}/msi2lmp
%{_mandir}/man1/msi2lmp.1%{?ext_man}
%{_bindir}/binary2txt
%{_bindir}/chain.x
%{_bindir}/micelle2d.x
%{_bindir}/phana
%{_bindir}/stl_bin2txt

%files -n %{shlib}
%{_libdir}/liblammps.so.*

%files devel
%license LICENSE
%{_includedir}/%{name}
%{_libdir}/liblammps.so
%{_libdir}/pkgconfig/liblammps.pc
%{_libdir}/cmake/LAMMPS

%files data
%license LICENSE
%{_datadir}/%{name}
%config %{_sysconfdir}/profile.d/lammps.*

%files -n %{pythons}-%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*.*-info

%changelog
