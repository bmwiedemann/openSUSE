#
# spec file for package python-xarray
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


Name:           python-xarray
Version:        2022.12.0
Release:        0
Summary:        N-D labeled arrays and datasets in Python
License:        Apache-2.0
URL:            https://github.com/pydata/xarray
Source:         https://files.pythonhosted.org/packages/source/x/xarray/xarray-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM local_dataset.patch gh#pydata/xarray#5377 mcepl@suse.com
# fix xr.tutorial.open_dataset to work with the preloaded cache.
Patch0:         local_dataset.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module numpy-devel >= 1.20}
BuildRequires:  %{python_module packaging >= 21.3}
BuildRequires:  %{python_module pandas >= 1.3}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.20
Requires:       python-packaging >= 21.3
Requires:       python-pandas >= 1.3
Provides:       python-xray = %{version}
Obsoletes:      python-xray < %{version}
BuildArch:      noarch
# SECTION extras accel
Recommends:     python-scipy
Recommends:     python-bottleneck
Recommends:     python-flox
Recommends:     python-numbagg
# /SECTION
# SECTION extras parallalel
Suggests:       python-dask-complete
# /SECTION
# SECTION extras viz
Suggests:       python-matplotlib
Suggests:       python-seaborn
Suggests:       python-nc-time-axis
#/SECTION
# SECTION extras io
Suggests:       python-netCDF4
Suggests:       python-h5netcdf
Suggests:       (python-pydap if python-base < 3.10)
Suggests:       python-zarr
Suggests:       python-fsspec
Suggests:       python-cftime
Suggests:       python-rasterio
Suggests:       python-cfgrib
Suggests:       python-pooch
#/SECTION
# SECTION tests
BuildRequires:  %{python_module Bottleneck}
BuildRequires:  %{python_module dask-dataframe}
BuildRequires:  %{python_module dask-diagnostics}
BuildRequires:  %{python_module h5netcdf}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module netCDF4}
BuildRequires:  %{python_module pooch}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module zarr}
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
# OOM crashes the whole vm or even the local host running osc: https://github.com/pydata/xarray/issues/6854
donttest="nczarr"
if [ $(getconf LONG_BIT) -eq 32 ]; then
  # https://github.com/pydata/xarray/issues/5341
  # https://github.com/pydata/xarray/issues/5375
  # still precision problems in 2022.11.0
  donttest="$donttest or (test_interpolate_chunk_advanced and linear)"
  # tests for 64bit types
  donttest="$donttest or TestZarrDictStore or TestZarrDirectoryStore"
fi
%pytest -n auto -rsEf -k "not ($donttest)" xarray

%files %{python_files}
%doc README.md
%license LICENSE licenses/
%{python_sitelib}/xarray
%exclude %{python_sitelib}/xarray/tests
%{python_sitelib}/xarray-%{version}*-info

%changelog
