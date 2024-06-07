#
# spec file for package python-xarray
#
# Copyright (c) 2024 SUSE LLC
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
%if "%{flavor}" == "test"
%bcond_without test
%define psuffix -test
%else
%bcond_with test
%define psuffix %{nil}
%endif

%define ghversion 2024.05.0

%{?sle15_python_module_pythons}
Name:           python-xarray%{psuffix}
Version:        2024.5.0
Release:        0
Summary:        N-D labeled arrays and datasets in Python
License:        Apache-2.0
URL:            https://github.com/pydata/xarray
Source:         https://github.com/pydata/xarray/archive/refs/tags/v%{ghversion}.tar.gz#/xarray-%{ghversion}-gh.tar.gz
# PATCH-FEATURE-UPSTREAM local_dataset.patch gh#pydata/xarray#5377 mcepl@suse.com
# fix xr.tutorial.open_dataset to work with the preloaded cache.
Patch0:         local_dataset.patch
# PATCH-FIX-UPSTREAM xarray-pr8854-np2.patch gh#pydata/xarray#8854
Patch1:         xarray-pr8854-np2.patch
# PATCH-FIX-UPSTREAM xarray-pr9305-cftime.patch gh#pydata/xarray#9305
Patch2:         xarray-pr9305-cftime.patch
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.23
Requires:       python-packaging >= 23.1
Requires:       python-pandas >= 2
Obsoletes:      python-xray <= 0.7
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module xarray-complete = %{version}}
%endif
# /SECTION
%python_subpackages

%description
xarray (formerly xray) is a python-pandas-like and pandas-compatible
toolkit for analytics on multi-dimensional arrays. It provides
N-dimensional variants of the python-pandas labeled data structures,
rather than the tabular data that pandas uses.

The Common Data Model for self-describing scientific data is used.
The dataset is an in-memory representation of a netCDF file.

%package accel
# for minimum versions, check ci/requirements/min-all-deps.yml
Summary:        The python xarray[accel] extra
Requires:       python-Bottleneck >= 1.3
Requires:       python-opt-einsum
Requires:       python-scipy
Requires:       python-xarray = %{version}
# not available yet
Recommends:     python-flox >= 0.7
Recommends:     python-numbagg

%description accel
The [accel] extra for xarray, N-D labeled arrays and datasets in Python
Except flox and numbagg, because they are not packaged yet.
Use `pip-%{python_bin_suffix} --user install flox numbagg` to install from PyPI, if needed.

%package complete
Summary:        The python xarray[complete] extra
Requires:       python-xarray = %{version}
Requires:       python-xarray-accel = %{version}
Requires:       python-xarray-dev = %{version}
Requires:       python-xarray-io = %{version}
Requires:       python-xarray-parallel = %{version}
Requires:       python-xarray-viz = %{version}

%description complete
The [complete] extra for xarray, N-D labeled arrays and datasets in Python

%package dev
Summary:        The python xarray[dev] extra
Requires:       python-hypothesis
Requires:       python-pytest
Requires:       python-pytest-cov
Requires:       python-pytest-env
Requires:       python-pytest-timeout
Requires:       python-pytest-xdist
Requires:       python-ruff
Requires:       python-xarray = %{version}
Requires:       python-xarray-complete = %{version}
# Not available and not really useful for us
Recommends:     python-pre-commit

%description dev
The [dev] extra for xarray, N-D labeled arrays and datasets in Python
Except pre-commit, Use `pip-%{python_bin_suffix} --user install pre-commit` to install, if needed.

%package io
Summary:        The python xarray[io] extra
Requires:       python-cftime >= 1.6
Requires:       python-fsspec
Requires:       python-h5netcdf >= 1.1
Requires:       python-netCDF4 >= 1.6
Requires:       python-pooch
Requires:       python-scipy >= 1.10
Requires:       python-xarray = %{version}
Requires:       python-zarr >= 2.13

%description io
The [io] extra for xarray, N-D labeled arrays and datasets in Python

%package parallel
Summary:        The python xarray[parallel] extra
Requires:       python-dask-complete >= 2022.12
Requires:       python-xarray = %{version}

%description parallel
The [parallel] extra for xarray, N-D labeled arrays and datasets in Python

%package viz
Summary:        The python xarray[viz] extra
Requires:       python-matplotlib >= 3.6
Requires:       python-seaborn >= 0.12
Requires:       python-xarray = %{version}
# Not available yet
Recommends:     python-nc-time-axis

%description viz
The [viz] extra for xarray, N-D labeled arrays and datasets in Python

Except nc-time-axis, because it's not packaged yet.
Use `pip-%{python_bin_suffix} --user install nc-time-axis` to install from PyPI, if needed.

%prep
%autosetup -p1 -n xarray-%{ghversion}
chmod -x xarray/util/print_versions.py

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# obs file open race conditions?
donttest="(test_open_mfdataset_manyfiles and (h5netcdf or netCDF4))"
if [ $(getconf LONG_BIT) -eq 32 ]; then
  # https://github.com/pydata/xarray/issues/5341
  # https://github.com/pydata/xarray/issues/5375
  # still precision problems in 2022.11.0
  donttest="$donttest or (test_interpolate_chunk_advanced and linear)"
  # tests for 64bit types
  donttest="$donttest or TestZarrDictStore or TestZarrDirectoryStore or TestZarrWriteEmpty"
  donttest="$donttest or test_repr_multiindex or test_array_repr_dtypes_unix"
fi
# h5py was built without ROS3 support, can't use ros3 driver
donttest="$donttest or TestH5NetCDFDataRos3Driver"
# NetCDF4 fails with these unsupported drivers
donttest="$donttest or (TestNetCDF4 and test_compression_encoding and (szip or zstd or blosc_lz or blosc_zlib))"

%pytest -n auto -rsEf -k "not ($donttest)" xarray
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE licenses/
%{python_sitelib}/xarray
%{python_sitelib}/xarray-%{version}.dist-info

%files %{python_files accel}
%doc README.md
%license LICENSE

%files %{python_files complete}
%doc README.md
%license LICENSE

%files %{python_files dev}
%doc README.md
%license LICENSE

%files %{python_files io}
%doc README.md
%license LICENSE

%files %{python_files parallel}
%doc README.md
%license LICENSE

%files %{python_files viz}
%doc README.md
%license LICENSE
%endif

%changelog
