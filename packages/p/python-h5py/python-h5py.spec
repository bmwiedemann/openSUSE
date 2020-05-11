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
Name:           python-h5py
Version:        2.10.0
Release:        0
Summary:        Python interface to the Hierarchical Data Format library
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/h5py/h5py
Source:         https://files.pythonhosted.org/packages/source/h/h5py/h5py-%{version}.tar.gz
#PATCH-FIX-OPENSUSE no_include_opt.patch -- Don't include /opt/ directory.
Patch0:         no_include_opt.patch
#PATCH-FIX-OPENSUSE remove_unittest2.patch mcepl@suse.cz -- remove dependency unittest2
Patch1:         remove_unittest2.patch
BuildRequires:  %{python_module Cython >= 0.23}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.7}
BuildRequires:  %{python_module pkgconfig}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  hdf5-devel
BuildRequires:  python-rpm-macros
Requires:       hdf5
Requires:       python-numpy >= 1.7
Requires:       python-six
%requires_eq    libhdf5_hl100
%python_subpackages

%description
H5py provides a simple, robust read/write interface to HDF5 data from Python.
Existing Python and Numpy concepts are used for the interface; for example,
datasets on disk are represented by a proxy class that supports slicing, and
has dtype and shape attributes. HDF5 groups are presented using a dictionary
metaphor, indexed by name.

%prep
%setup -q -n h5py-%{version}
%autopatch -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export PYTHONDONTWRITEBYTECODE=1
# test_float_round_tripping -- overflows on 32bit
# py3 only code must be skipped
%pytest_arch %{buildroot}%{$python_sitearch}/h5py/tests/ -k 'not (test_highlevel_access or test_deprecation_available_ftypes or test_read_uncompressed_offsets or test_read_write_chunk or test_float_round_tripping)'

%files %{python_files}
%license lzf/LICENSE.txt
%doc ANN.rst README.rst lzf/README.txt examples licenses/*
%{python_sitearch}/h5py/
%{python_sitearch}/h5py-%{version}-py*.egg-info

%changelog
