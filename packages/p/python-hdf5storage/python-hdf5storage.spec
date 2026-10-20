#
# spec file for package python-hdf5storage
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-hdf5storage
Version:        0.2.2
Release:        0
Summary:        Utilities to read/write HDF5 files, including MATLAB v7.3 MAT files
License:        BSD-3-Clause
URL:            https://github.com/jclds139/hdf5storage
Source:         https://github.com/jclds139/hdf5storage/archive/refs/tags/%{version}.tar.gz#/hdf5storage-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module h5py >= 3.9}
BuildRequires:  %{python_module numpy >= 1.26}
BuildRequires:  %{python_module pytest >= 6.0}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{pythons}
# /SECTION
Requires:       python-h5py >= 3.9
Requires:       python-numpy >= 1.26
Recommends:     python-scipy >= 1.14.0
BuildArch:      noarch
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license COPYING.txt
%{python_sitelib}/hdf5storage/
%{python_sitelib}/hdf5storage-%{version}.dist-info

%changelog
