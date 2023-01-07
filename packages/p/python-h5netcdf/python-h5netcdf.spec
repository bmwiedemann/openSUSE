#
# spec file for package python-h5netcdf
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
%define         skip_python36 1
Name:           python-h5netcdf
Version:        1.1.0
Release:        0
Summary:        A Python library to use netCDF4 files via h5py
License:        BSD-3-Clause
URL:            https://github.com/h5netcdf/h5netcdf
Source:         https://files.pythonhosted.org/packages/source/h/h5netcdf/h5netcdf-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-h5py
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module netCDF4}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A Python interface for the netCDF4 file-format that reads and writes
local or remote HDF5 files directly via h5py or h5pyd, without
relying on the Unidata netCDF library.

%prep
%autosetup -p1 -n h5netcdf-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -rs

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/h5netcdf
%{python_sitelib}/h5netcdf-%{version}*-info

%changelog
