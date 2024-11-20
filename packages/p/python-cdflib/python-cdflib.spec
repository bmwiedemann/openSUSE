#
# spec file for package python-cdflib
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


Name:           python-cdflib
Version:        1.3.2
Release:        0
Summary:        A python CDF reader toolkit
License:        MIT
URL:            https://github.com/MAVENSDC/cdflib
# Tests only included in github archive
Source:         https://github.com/MAVENSDC/cdflib/archive/refs/tags/%{version}.tar.gz#/cdflib-%{version}-gh.tar.gz
# Test datafile, Public domain, not packaged
Source1:        https://helios-data.ssl.berkeley.edu/data/E1_experiment/New_proton_corefit_data_2017/cdf/helios1/1974/h1_1974_346_corefit.cdf
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 45}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.21
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 1.21}
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module h5netcdf}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module netCDF4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module xarray}
# /SECTION
%python_subpackages

%description
A python module to read/write CDF (Common Data Format .cdf) files without needing to install the CDF NASA library.

%prep
%setup -q -n cdflib-%{version}
sed -i '/addopts/ d' setup.cfg
# don't install benchmarks and tests gh#MAVENSDC/cdflib#274
sed -i 's/packages = find:$/packages = cdflib/' setup.cfg
cp %{SOURCE1} helios.cdf

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -m "not remote_data"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/cdflib
%{python_sitelib}/cdflib-%{version}.dist-info

%changelog
