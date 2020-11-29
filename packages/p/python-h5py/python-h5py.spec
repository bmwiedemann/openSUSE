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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-h5py
Version:        3.1.0
Release:        0
Summary:        Python interface to the Hierarchical Data Format library
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/h5py/h5py
Source:         https://files.pythonhosted.org/packages/source/h/h5py/h5py-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE python-h5py-relax-dependency-versions.patch badshah400@gmail.com -- Build against newer version of numpy
Patch0:         python-h5py-relax-dependency-versions.patch
BuildRequires:  %{python_module Cython >= 0.23}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.12}
BuildRequires:  %{python_module pkgconfig}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  hdf5-devel
BuildRequires:  python-rpm-macros
Requires:       hdf5
Requires:       python-numpy >= 1.12
Requires:       python-six
%requires_eq    libhdf5
%if 0%{?suse_version} <= 1500
BuildRequires:  %{python_module cached-property}
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
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Offset test fails on 32-bit and we don't build against mpi-hdf5
%ifarch %{ix86}
%pytest_arch %{buildroot}%{$python_sitearch}/h5py/tests/ -k 'not (TestMPI or test_float_round_tripping)'
%else
%pytest_arch %{buildroot}%{$python_sitearch}/h5py/tests/ -k 'not TestMPI'
%endif

%files %{python_files}
%license lzf/LICENSE.txt
%doc README.rst lzf/README.txt examples licenses/*
%{python_sitearch}/h5py/
%{python_sitearch}/h5py-%{version}-py*.egg-info

%changelog
