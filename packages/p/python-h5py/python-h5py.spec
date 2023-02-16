#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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
%define my_sitearch_in_expand %{my_libdir}/python%{$python_version}/site-packages
%else
%define my_prefix  %{_prefix}
%define my_bindir  %{_bindir}
%define my_libdir  %{_libdir}
%define my_incdir  %{_includedir}
%define my_datadir %{_datadir}
%define my_sitearch_in_expand %{$python_sitearch}
%endif
# /SECTION MPI DEFINITIONS
Name:           %{pname}%{?my_suffix}
Version:        3.8.0
Release:        0
Summary:        Python interface to the Hierarchical Data Format library
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/h5py/h5py
Source:         https://files.pythonhosted.org/packages/source/h/h5py/h5py-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.29}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module numpy-devel >= 1.14.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pkgconfig}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  hdf5%{?my_suffix}-devel
BuildRequires:  python-rpm-macros
%requires_eq    hdf5%{?my_suffix}
%requires_eq    libhdf5%{?my_suffix}
Requires:       python-numpy >= 1.14.5
%if %{with mpi}
BuildRequires:  %{mpi_flavor}%{mpi_vers}-devel
BuildRequires:  %{python_module mpi4py >= 3.0.2}
BuildRequires:  %{python_module pytest-mpi}
Requires:       python-mpi4py >= 3.0.2
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
%pyproject_wheel

%install
%if %{with mpi}
%pyproject_install --prefix %{my_prefix}
%else
%pyproject_install
%endif
%python_expand %fdupes %{buildroot}%{my_sitearch_in_expand}/h5py/

%check
%{python_expand # Offset test fails on 32-bit
%if %{with mpi}
source %{my_bindir}/mpivars.sh
%endif
export LD_LIBRARY_PATH=%{my_libdir}
export PYTHONPATH=%{buildroot}%{my_sitearch_in_expand}
export PYTHONDONTWRITEBYTECODE=1
pytest-%{$python_bin_suffix} %{buildroot}%{my_sitearch_in_expand}/h5py/ \
%ifarch %{ix86}
        %{?with_mpi:-k 'not test_float_round_tripping' -m 'not mpi_skip'}%{!?with_mpi:-k 'not (TestMPI or test_float_round_tripping)'}
%else
        %{?with_mpi:-m 'not mpi_skip'}%{!?with_mpi:-k 'not TestMPI'}
%endif
}

%files %{python_files}
%license lzf/LICENSE.txt
%doc README.rst lzf/README.txt examples licenses/*
%if %{with mpi}
%dir %{my_libdir}/python%{python_version}
%dir %{my_libdir}/python%{python_version}/site-packages
%{my_libdir}/python%{python_version}/site-packages/h5py
%{my_libdir}/python%{python_version}/site-packages/h5py-%{version}*-info
%else
%{python_sitearch}/h5py/
%{python_sitearch}/h5py-%{version}*-info
%endif

%changelog
