#
# spec file for package python-xarray
#
# Copyright (c) 2021 SUSE LLC
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
# NEP 29: Numpy 1.20 dropped support for Python 3.6, python36-numpy is removed from Tumbleweed. xarray will follow on next release
%define         skip_python36 1
Name:           python-xarray
Version:        0.18.0
Release:        0
Summary:        N-D labeled arrays and datasets in Python
License:        Apache-2.0
URL:            https://github.com/pydata/xarray
Source:         https://files.pythonhosted.org/packages/source/x/xarray/xarray-%{version}.tar.gz
BuildRequires:  %{python_module numpy >= 1.15}
BuildRequires:  %{python_module numpy-devel >= 1.14}
BuildRequires:  %{python_module pandas >= 0.25}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.15
Requires:       python-pandas >= 0.25
Provides:       python-xray = %{version}
Obsoletes:      python-xray < %{version}
BuildArch:      noarch
Suggests:       python-dask-all
# SECTION extras accel
Recommends:     python-scipy >= 1.3
Recommends:     python-bottleneck
Recommends:     python-numbagg
# /SECTION
# SECTION extras viz
Suggests:       python-matplotlib
Suggests:       python-seaborn
Suggests:       python-nc-time-axis
#/SECTION
# SECTION extras io
Suggests:       python-netCDF4
Suggests:       python-h5netcdf
Suggests:       python-scipy
Suggests:       python-pydap
Suggests:       python-zarr
Suggests:       python-fsspec
Suggests:       python-cftime
Suggests:       python-rasterio
Suggests:       python-cfgrib
#/SECTION
# SECTION tests
BuildRequires:  %{python_module dask-dataframe}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
xarray (formerly xray) is a python-pandas-like and pandas-compatible
toolkit for analytics on multi-dimensional arrays. It provides
N-dimensional variants of the python-pandas labeled data structures,
rather than the tabular data that pandas uses.

The Common Data Model for self-describing scientific data is used.
The dataset is an in-memory representation of a netCDF file.

%prep
%autosetup -p1 -n xarray-%{version}
chmod -x xarray/util/print_versions.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
if [ $(getconf LONG_BIT) -eq 32 ]; then
  # precision errors on 32-bit
  donttest="(test_interpolate_chunk_advanced and linear)"
fi
%pytest -n auto ${donttest:+ -k "not ($donttest)"} xarray

%files %{python_files}
%doc README.rst
%license LICENSE licenses/
%{python_sitelib}/xarray
%{python_sitelib}/xarray-%{version}*-info

%changelog
