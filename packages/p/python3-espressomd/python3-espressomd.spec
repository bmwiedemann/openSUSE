#
# spec file for package python3-espressomd
#
# Copyright (c) 2020 SUSE LLC
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

%define pkgname espresso
%define modname %{pkgname}md
Name:           python3-%{modname}
Version:        4.1.4
Release:        0
Summary:        Parallel simulation software for soft matter research
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Chemistry
URL:            http://espressomd.org
Source:         https://github.com/%{modname}/%{pkgname}/releases/download/%{version}/%{pkgname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM boost-1.74.patch gh#espressomd/espresso#3864
Patch0:         boost-1.74.patch
BuildRequires:  cmake
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
# Currently libboost_mpi-devel and hdf5 use different mpi versions
# BuildRequires:  hdf5-devel
BuildRequires:  %{mpiver}-devel
BuildRequires:  gsl-devel
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_mpi-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  hdf5-%{mpiver}-devel
BuildRequires:  zlib-devel
BuildRequires:  python3-h5py
%else
BuildRequires:  boost-devel
%endif
Obsoletes:      libEspresso4 < 4.1
Requires:       python3-numpy
Requires:       python3-h5py
# make sure rpm pulls in the right dependency
Requires:       libhdf5-%{mpiver}

%description
ESPResSo is a highly versatile software package for performing and analyzing
scientific Molecular Dynamics many-particle simulations of coarse-grained
atomistic or bead-spring models as they are used in soft-matter research in
physics, chemistry and molecular biology. It can be used to simulate systems
such as polymers, liquid crystals, colloids, ferrofluids and biological
systems, for example DNA and lipid membranes.

%prep
%setup -q -n %{pkgname}
%patch0 -p1

%build
source %{_libdir}/mpi/gcc/%{mpiver}/bin/mpivars.sh
# gh#espressomd/espresso#3396
%define _lto_cflags %{nil}

#force usage of shared hdf5
export HDF5_USE_SHLIB=yes
# overwrite .so linker flags on SUSE distros: drop --no-undefined
# we don't install {i,}pypresso scripts as they aren't needed when installing in /usr
%cmake \
  -DCMAKE_SHARED_LINKER_FLAGS='-Wl,--as-needed -Wl,-z,now' \
  -DLIBDIR=%{_lib} \
  -DPYTHON_EXECUTABLE=%{_bindir}/python3 \
  -DINSTALL_PYPRESSO=OFF
%make_jobs

%install
%cmake_install

# no devel package
rm -f %{buildroot}%{_libdir}/lib*.so

%check
# gh#espressomd/espresso#3315
%ifarch i586
%define testargs ARGS='-E collision_detection'
%endif
LD_LIBRARY_PATH='%{buildroot}/%{python3_sitearch}/espressomd::%{_libdir}/mpi/gcc/%{mpiver}/%{_lib}' make -C build check CTEST_OUTPUT_ON_FAILURE=1 %{?testargs:%{testargs}}

%files
%license COPYING
%doc README AUTHORS NEWS ChangeLog
%{python3_sitearch}/espressomd

%changelog
