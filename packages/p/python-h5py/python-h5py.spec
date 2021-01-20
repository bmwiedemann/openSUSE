#
# spec file for package python-h5py
#
# Copyright (c) 2020 SUSE LLC
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

%define pname python-h5py

# SECTION MPI DEFINITIONS
%if "%{flavor}" == "openmpi1"
%global mpi_flavor openmpi
%if 0%{?suse_version} <= 1500
%define mpi_vers %{nil}
%else
%define mpi_vers 1
%endif
%endif

%if "%{flavor}" == "openmpi2"
%global mpi_flavor openmpi
%define mpi_vers 2
%endif

%if "%{flavor}" == "openmpi3"
%global mpi_flavor openmpi
%define mpi_vers 3
%endif

%if "%{flavor}" == "openmpi4"
%global mpi_flavor openmpi
%define mpi_vers 4
%endif

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}
%{?with_mpi:%{!?mpi_flavor:error "No MPI family specified!"}}

%if %{with mpi}
%define my_prefix  %{_libdir}/mpi/gcc/%{mpi_flavor}%{?mpi_vers}
%define my_bindir  %{my_prefix}/bin
%define my_libdir  %{my_prefix}/%{_lib}
%define my_incdir  %{my_prefix}/include
%define my_suffix  -%{mpi_flavor}%{?mpi_vers}
%else
%define my_prefix  %{_prefix}
%define my_bindir  %{_bindir}
%define my_libdir  %{_libdir}
%define my_incdir  %{_includedir}
%define my_datadir %{_datadir}
%endif
# /SECTION MPI DEFINITIONS

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           %{pname}%{?my_suffix}
Version:        3.1.0
Release:        0
Summary:        Python interface to the Hierarchical Data Format library
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/h5py/h5py
Source:         https://files.pythonhosted.org/packages/source/h/h5py/h5py-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE python-h5py-relax-dependency-versions.patch badshah400@gmail.com -- Build against newer version of numpy
Patch0:         python-h5py-relax-dependency-versions.patch
BuildRequires:  %{python_module cached-property}
BuildRequires:  %{python_module Cython >= 0.23}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.12}
BuildRequires:  %{python_module pkgconfig}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  hdf5%{?my_suffix}-devel
BuildRequires:  python-rpm-macros
Requires:       hdf5%{?my_suffix}
Requires:       python-numpy >= 1.12
Requires:       python-six
%requires_eq    libhdf5%{?my_suffix}
%if %python_version_nodots < 38
Requires:       python-cached-property
%endif
%if %{with mpi}
BuildRequires:  %{mpi_flavor}%{mpi_vers}-devel
BuildRequires:  %{python_module mpi4py}
BuildRequires:  %{python_module pytest-mpi}
%endif
%python_subpackages

%description
H5py provides a simple, robust read/write interface to HDF5 data from Python.
Existing Python and Numpy concepts are used for the interface; for example,
datasets on disk are represented by a proxy class that supports slicing, and
has dtype and shape attributes. HDF5 groups are presented using a dictionary
metaphor, indexed by name.

%prep
%autosetup -p1 -n h5py-%{version}

%build
%if %{with mpi}
source %{my_bindir}/mpivars.sh
export CC=mpicc
export HDF5_MPI="ON"
export HDF5_LIBDIR=%{my_libdir}
export HDF5_INCLUDEDIR=%{my_incdir}
%endif
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%if %{with mpi}
%python_exec setup.py install -O1 --skip-build --force --root %{buildroot} --prefix %{my_prefix}
%else
%python_install
%endif
%python_expand %fdupes %{buildroot}%{my_libdir}/python%{python_version}/site-packages/h5py/

%check
# Offset test fails on 32-bit
%if %{with mpi}
source %{my_bindir}/mpivars.sh
%endif
export LD_LIBRARY_PATH=%{my_libdir}
export PYTHONPATH=%{buildroot}%{my_libdir}/python%{python_version}/site-packages
export PYTHONDONTWRITEBYTECODE=1
%ifarch %{ix86}
pytest-%{python_version} %{buildroot}%{my_libdir}/python%{python_version}/site-packages/h5py/ %{?with_mpi:-k 'not test_float_round_tripping'}%{!?with_mpi:-k 'not (TestMPI or test_float_round_tripping)'}
%else
pytest-%{python_version} %{buildroot}%{my_libdir}/python%{python_version}/site-packages/h5py/ %{!?with_mpi:-k 'not TestMPI'}
%endif

%files %{python_files}
%license lzf/LICENSE.txt
%doc README.rst lzf/README.txt examples licenses/*
%if %{with mpi}
%dir %{my_libdir}/python%{python_version}
%dir %{my_libdir}/python%{python_version}/site-packages
%endif
%{my_libdir}/python%{python_version}/site-packages/h5py/
%{my_libdir}/python%{python_version}/site-packages/h5py-%{version}-py*.egg-info

%changelog
