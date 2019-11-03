#
# spec file for package lammps
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2019 Christoph Junghans
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

# Build with OpenMPI
%if 0%{?sle_version} == 0
%define mpiver  openmpi2
%else
%if 0%{?sle_version} <= 120300
%define mpiver  openmpi
%else
  %if 0%{?sle_version} <= 150000
  %define mpiver  openmpi2
  %else
  %define mpiver  openmpi3
  %endif
%endif
%endif

Name:           lammps
Version:        20180807
%define         uversion stable_7Aug2019
Release:        0
Summary:        Molecular Dynamics Simulator
License:        GPL-2.0 and GPL-3.0+
Group:          Productivity/Scientific/Chemistry
Url:            http://lammps.sandia.gov
Source0:        https://github.com/lammps/lammps/archive/%{uversion}.tar.gz#/%{name}-%{uversion}.tar.gz
%define         tversion d0394a77fa2b4b2d545a73ea092cf6de7616aac8
Source1:        https://github.com/lammps/lammps-testing/archive/%{tversion}.tar.gz#/%{name}-testing-%{tversion}.tar.gz
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  %{mpiver}
BuildRequires:  %{mpiver}-devel
BuildRequires:  python-devel
BuildRequires:  fftw3-devel
BuildRequires:  voro++-devel
BuildRequires:  zlib-devel
BuildRequires:  gsl-devel
BuildRequires:  kim-api-devel >= 2.1
BuildRequires:  cmake
BuildRequires:  opencl-headers
BuildRequires:  ocl-icd-devel
Requires:       %{name}-data
BuildRoot:      %{_tmppath}/%{name}-%{version}-build


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

%package -n liblammps0
Summary:        LAMMPS library
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
Summary:    Development headers and libraries for LAMMPS
Group:      Development/Libraries/C and C++
Requires:   liblammps0 = %{version}
Requires:   %{name} = %{version}

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

%package -n python-%{name}
Summary:    LAMMPS python module
Group:      Development/Languages/Python
Requires:   liblammps0 = %{version}

%description -n python-%{name}
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
Summary:    LAMMPS data
Group:      Productivity/Scientific/Chemistry
BuildArch:  noarch

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
%setup -a 1 -q -n %{name}-%{uversion}

%build
source %{_libdir}/mpi/gcc/%{mpiver}/bin/mpivars.sh

%{cmake} \
  -C ../cmake/presets/all_on.cmake \
  -C ../cmake/presets/nolib.cmake \
  -DBUILD_TOOLS=ON \
  -DBUILD_LIB=ON -DBUILD_MPI=ON -DPKG_PYTHON=ON \
  -DPKG_KIM=ON -DENABLE_TESTING=ON -DPKG_VORONOI=ON \
  -DPKG_GPU=ON -DGPU_API=OpenCL -DFFT=FFTW3 \
  -DPYTHON_INSTDIR=%{python_sitearch} -DCMAKE_INSTALL_SYSCONFDIR=/etc \
%ifnarch x86_64 i586
  -DPKG_USER-INTEL=OFF \
%endif  
  -DLAMMPS_TESTING_SOURCE_DIR=$(echo $PWD/../lammps-testing-*) ../cmake
%make_jobs

%install
%cmake_install

%check
LD_LIBRARY_PATH='%{buildroot}/%{_libdir}:%{_libdir}/mpi/gcc/%{mpiver}/%{_lib}' make -C build %{?_smp_mflags} test CTEST_OUTPUT_ON_FAILURE=1

%post -n liblammps0 -p /sbin/ldconfig
%postun -n liblammps0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README
%license LICENSE
%{_bindir}/lmp
%{_mandir}/man1/lmp.1.*
%{_bindir}/msi2lmp
%{_mandir}/man1/msi2lmp.1.*
%{_bindir}/binary2txt

%files -n liblammps0
%defattr(-,root,root,-)
%{_libdir}/liblammps.so.*

%files devel
%defattr(-,root,root)
%license LICENSE
%{_includedir}/%{name}
%{_libdir}/liblammps.so
%{_libdir}/pkgconfig/liblammps.pc
%dir %{_datadir}/cmake/Modules
%{_datadir}/cmake/Modules/FindLAMMPS.cmake

%files -n python-%{name}
%defattr(-,root,root,-)
%{python_sitearch}/%{name}.py

%files data
%defattr(-,root,root,-)
%license LICENSE
%{_datadir}/%{name}
%config %{_sysconfdir}/profile.d/lammps.*

%changelog
