#
# spec file for package python-hdf5storage
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-hdf5storage
Version:        0.1.15
Release:        0
Summary:        Utilities to read/write HDF5 files, including MATLAB v7.3 MAT files
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/frejanordsiek/hdf5storage
Source:         https://files.pythonhosted.org/packages/source/h/hdf5storage/hdf5storage-%{version}.zip
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module h5py >= 2.1}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module scipy}
BuildRequires:  unzip
# SECTION test requirements
BuildRequires:  %{python_module nose}
# /SECTION
Requires:       python-h5py >= 2.1
Requires:       python-numpy
Requires:       python-scipy
BuildArch:      noarch
%python_subpackages

%description
This Python package provides high level utilities to read/write a
variety of Python types to/from HDF5 (Heirarchal Data Format) formatted
files. This package also provides support for MATLAB MAT v7.3 formatted
files, which are just HDF5 files with a different extension and some
extra meta-data.

%prep
%setup -q -n hdf5storage-%{version}
# fix end-of-line encoding
sed -i 's/\r$//' COPYING.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license COPYING.txt
%{python_sitelib}/hdf5storage/
%{python_sitelib}/hdf5storage-%{version}-py*.egg-info

%changelog
