#
# spec file for package python-arviz
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


%{?sle15_python_module_pythons}
Name:           python-arviz
Version:        0.23.0
Release:        0
Summary:        Exploratory analysis of Bayesian models
License:        Apache-2.0
URL:            http://github.com/arviz-devs/arviz
Source:         https://github.com/arviz-devs/arviz/archive/v%{version}.tar.gz#/arviz-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 60.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module cloudpickle}
BuildRequires:  %{python_module bokeh >= 3}
BuildRequires:  %{python_module dash}
BuildRequires:  %{python_module dask-distributed}
BuildRequires:  %{python_module dask}
BuildRequires:  %{python_module dm-tree >= 0.1.8}
BuildRequires:  %{python_module h5netcdf >= 1.0.2}
BuildRequires:  %{python_module matplotlib >= 3.5}
BuildRequires:  %{python_module netCDF4}
BuildRequires:  %{python_module numba}
BuildRequires:  %{python_module numpy >= 1.26.0}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pandas >= 2.1.0}
BuildRequires:  %{python_module pytest >= 0.23}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module scipy >= 1.11.0}
BuildRequires:  %{python_module typing_extensions >= 4.1.0}
BuildRequires:  %{python_module ujson}
BuildRequires:  %{python_module xarray >= 2023.7}
BuildRequires:  %{python_module xarray-einstats >= 0.3}
# Zarr is being updated to v3, arviz v1 will be compatible
## BuildRequires:  %%{python_module zarr >= 2.5 with %%python-zarr < 3}
# /SECTION
Requires:       python-h5netcdf >= 1.0.2
Requires:       python-matplotlib >= 3.8
Requires:       python-numpy >= 1.26.0
Requires:       python-packaging
Requires:       python-pandas >= 2.1.0
Requires:       python-scipy >= 1.11.0
Requires:       python-setuptools >= 60.0.0
Requires:       python-typing_extensions >= 4.1.0
Requires:       python-xarray >= 2023.7
Requires:       python-xarray-einstats >= 0.3
Recommends:     python-bokeh >= 3
Recommends:     python-dask-distributed
Recommends:     python-dm-tree >= 0.1.8
Recommends:     python-netCDF4
Recommends:     python-numba
Recommends:     python-ujson
Recommends:     (python-zarr >= 2.5.0 with python-zarr < 3)
BuildArch:      noarch
%python_subpackages

%description
ArviZ is a Python package for exploratory analysis of Bayesian models. Includes
functions for posterior analysis, data storage, model checking, comparison and
diagnostics.

%prep
%setup -q -n arviz-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Matplotlib tests try to save results to non-writeable dir
donttest="test_plots_matplotlib"
# Tries to connect to external server for arviz data
donttest="$donttest or test_plot_separation"
%pytest -n auto -k "not ($donttest)"

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/arviz
%{python_sitelib}/arviz-%{version}.dist-info

%changelog
