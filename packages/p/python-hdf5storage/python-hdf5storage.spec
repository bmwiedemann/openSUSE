#
# spec file for package python-hdf5storage
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%define skip_python36 1
Name:           python-hdf5storage
Version:        0.1.18
Release:        0
Summary:        Utilities to read/write HDF5 files, including MATLAB v7.3 MAT files
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/frejanordsiek/hdf5storage
Source:         https://files.pythonhosted.org/packages/source/h/hdf5storage/hdf5storage-%{version}.zip
# PATCH-FIX-UPSTREAM nose-to-pytest.patch gh#frejanordsiek/hdf5storage#96 mcepl@suse.com
# uses pytest instead of nose
Patch0:         nose-to-pytest.patch
BuildRequires:  %{python_module h5py >= 2.1}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
# SECTION test requirements
# next release will use pytest gh#frejanordsiek/hdf5storage#96
BuildRequires:  %{python_module pytest >= 5.0}
# I don't know how to do @pytest.mark.parametrize on class methods
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module scipy}
# /SECTION
Requires:       python-h5py >= 2.1
Requires:       python-numpy
Recommends:     python-scipy
# This pure python package uses ctypes only suited for 64-bit. The tests segfault on 32-bit in libc memmove
# gh#frejanordsiek/hdf5storage#109
ExcludeArch:    %ix86 %arm
%python_subpackages

%description
This Python package provides high level utilities to read/write a
variety of Python types to/from HDF5 (Heirarchal Data Format) formatted
files. This package also provides support for MATLAB MAT v7.3 formatted
files, which are just HDF5 files with a different extension and some
extra meta-data.

%prep
%autosetup -p1 -n hdf5storage-%{version}
# fix end-of-line encoding
sed -i 's/\r$//' COPYING.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license COPYING.txt
%{python_sitelib}/hdf5storage/
%{python_sitelib}/hdf5storage-%{version}-py*.egg-info

%changelog
