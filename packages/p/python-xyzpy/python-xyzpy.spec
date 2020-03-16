#
# spec file for package python-xyzpy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-xyzpy
Version:        0.3.1
Release:        0
Summary:        Package to generate large parameter space data
License:        MIT
URL:            https://github.com/jcmgray/xyzpy
Source0:        https://github.com/jcmgray/xyzpy/archive/%{version}.tar.gz#/xyzpy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-bokeh >= 0.12.3
Requires:       python-cytoolz >= 0.8
Requires:       python-dask-all >= 0.11.1
Requires:       python-h5netcdf >= 0.2.2
Requires:       python-h5py >= 2.6.0
Requires:       python-joblib >= 0.12
Requires:       python-matplotlib >= 2.2.0
Requires:       python-numpy >= 1.10.0
Requires:       python-scipy
Requires:       python-tqdm >= 4.7.6
Requires:       python-xarray >= 0.9.0
Requires:       python-netCDF4
Recommends:     python-numba
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module bokeh >= 0.12.3}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module cytoolz >= 0.8}
BuildRequires:  %{python_module dask-all >= 0.11.1}
BuildRequires:  %{python_module h5netcdf >= 0.2.2}
BuildRequires:  %{python_module h5py >= 2.6.0}
BuildRequires:  %{python_module joblib >= 0.12}
BuildRequires:  %{python_module jupyter_ipython}
BuildRequires:  %{python_module matplotlib >= 2.2.0}
BuildRequires:  %{python_module netCDF4}
BuildRequires:  %{python_module numba}
BuildRequires:  %{python_module numpy >= 1.10.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module tqdm >= 4.7.6}
BuildRequires:  %{python_module xarray >= 0.9.0}
# /SECTION
%python_subpackages

%description
XYZPY is python library for generating, manipulating and plotting
data with a lot of dimensions, of the type that often occurs in
numerical simulations.

%prep
%setup -q -n xyzpy-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
