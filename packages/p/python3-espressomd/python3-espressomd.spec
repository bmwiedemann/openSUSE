#
# spec file for package python3-espressomd
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Christoph Junghans
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


%define mpi_implem openmpi2
%ifarch ppc64
%define mpi_implem openmpi
%endif
%if  0%{?sle_version} == 120300 && 0%{?is_opensuse}
%define mpi_implem openmpi
%endif
%if 0%{?sle_version} == 120400 && !0%{?is_opensuse}
%define mpi_implem openmpi
%endif

%define pkgname espresso
%define modname %{pkgname}md
%define sonum 4
Name:           python3-%{modname}
Version:        4.0.2
Release:        0
Summary:        Parallel simulation software for soft matter research
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Chemistry
URL:            http://espressomd.org
Source:         https://github.com/%{modname}/%{pkgname}/releases/download/%{version}/%{pkgname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
# Currently libboost_mpi-devel and hdf5 use different mpi versions
# BuildRequires:  hdf5-devel
BuildRequires:  gsl-devel
BuildRequires:  %{mpi_implem}-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_mpi-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
%else
BuildRequires:  boost-devel
%endif

%description
ESPResSo is a highly versatile software package for performing and analyzing
scientific Molecular Dynamics many-particle simulations of coarse-grained
atomistic or bead-spring models as they are used in soft-matter research in
physics, chemistry and molecular biology. It can be used to simulate systems
such as polymers, liquid crystals, colloids, ferrofluids and biological
systems, for example DNA and lipid membranes.

%package -n libEspresso%{sonum}
Summary:        Shared libraries for ESPResSo
Group:          System/Libraries

%description -n libEspresso%{sonum}
This package provides shared libraries for ESPResSo.

%prep
%setup -q -n %{pkgname}

%build
source %{_libdir}/mpi/gcc/%{mpi_implem}/bin/mpivars.sh

# overwrite .so linker flags on SUSE distros: drop --no-undefined
# we don't install {i,}pypresso scripts as they aren't needed when installing in /usr
%cmake \
  '-DCMAKE_SHARED_LINKER_FLAGS=-Wl,--as-needed -Wl,-z,now' \
  -DLIBDIR=%{_lib} \
  -DPYTHON_EXECUTABLE=%{_bindir}/python3 \
  -DINSTALL_PYPRESSO=OFF
%make_jobs

%install
%cmake_install

#fix some permissions
find %{buildroot}%{_prefix} -name "*.so" -exec chmod +x {} \;
find %{buildroot}%{_prefix} -name "gen_pxiconfig" -exec chmod +x {} \;
# no devel package
rm -f %{buildroot}%{_libdir}/lib*.so

%check
LD_LIBRARY_PATH='%{buildroot}/%{_libdir}::%{_libdir}/mpi/gcc/%{mpi_implem}/%{_lib}' make -C build check CTEST_OUTPUT_ON_FAILURE=1 %{?testargs:%{testargs}}

%post -n libEspresso%{sonum} -p /sbin/ldconfig
%postun -n libEspresso%{sonum} -p /sbin/ldconfig

%files
%license COPYING
%doc README AUTHORS NEWS ChangeLog
%{python3_sitearch}/espressomd

%files -n libEspresso%{sonum}
%license COPYING
%{_libdir}/libEspressoCore.so.%{sonum}
%{_libdir}/libActor.so.%{sonum}
%{_libdir}/libImmersedBoundary.so.%{sonum}
%{_libdir}/libObjectInFluid.so.%{sonum}
%{_libdir}/libAccumulators.so.%{sonum}
%{_libdir}/libConstraints.so.%{sonum}
%{_libdir}/libEspressoConfig.so.%{sonum}
%{_libdir}/libEspressoScriptInterface.so.%{sonum}
%{_libdir}/libObservables.so.%{sonum}
%{_libdir}/libShapes.so.%{sonum}
%{_libdir}/libVirtualSites.so.%{sonum}
%{_libdir}/libcluster_analysis.so.%{sonum}

%changelog