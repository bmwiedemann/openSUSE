#
# spec file for package python-h5py
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%if "%{flavor}" == "openmpi4"
%global mpi_flavor openmpi
%define mpi_vers 4
%endif
%if "%{flavor}" == "openmpi5"
%global mpi_flavor openmpi
%define mpi_vers 5
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
Version:        3.15.1
Release:        0
Summary:        Python interface to the Hierarchical Data Format library
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/h5py/h5py
Source:         https://files.pythonhosted.org/packages/source/h/h5py/h5py-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 3 with %python-Cython < 4}
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module numpy-devel >= 2.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pkgconfig >= 1.5.5}
BuildRequires:  %{python_module pytest >= 8.2.2}
BuildRequires:  %{python_module setuptools >= 77.0.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  hdf5%{?my_suffix}-devel >= 1.11.5
BuildRequires:  python-rpm-macros
# Work around requires_eq not finding the capability libhdf5. Need the Requires before the macro for the python subpackage rewriter
Requires:       %(rpm -q --requires hdf5%{?my_suffix}-devel | grep 'libhdf5.* = ' | head -n 1)
Requires:       python-numpy >= 1.21.2
%if %{with mpi}
BuildRequires:  %{mpi_flavor}%{mpi_vers}-devel
BuildRequires:  %{python_module mpi4py >= 3.1.2}
BuildRequires:  %{python_module pytest-mpi >= 0.6}
Requires:       python-mpi4py >= 3.1.2
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
donttest="dummytest"
%ifarch %{ix86} %{arm}
# overflow
donttest="test_float_round_tripping or test_register_filter"
%endif
# Disable test for ppc64le because of Insufficient precision
%ifarch ppc64le
donttest+=" or test_complex256 or test_long_double or test_custom_float_promotion"
%endif
%{python_expand #
%if %{with mpi}
source %{my_bindir}/mpivars.sh
%endif
export LD_LIBRARY_PATH=%{my_libdir}
export PYTHONPATH=%{buildroot}%{my_sitearch_in_expand}
export PYTHONDONTWRITEBYTECODE=1
pytest-%{$python_bin_suffix} %{buildroot}%{my_sitearch_in_expand}/h5py/ \
%{?with_mpi:-k "not ($donttest)" -m 'not mpi_skip'}%{!?with_mpi:-k "not (TestMPI or $donttest)"}
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
