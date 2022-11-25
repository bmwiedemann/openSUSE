#
# spec file for package python-arviz
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


%define modname arviz
Name:           python-arviz
Version:        0.14.0
Release:        0
Summary:        Exploratory analysis of Bayesian models
License:        Apache-2.0
URL:            http://github.com/arviz-devs/arviz
Source:         https://github.com/arviz-devs/arviz/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module cloudpickle}
BuildRequires:  %{python_module matplotlib >= 3.5}
BuildRequires:  %{python_module netCDF4}
BuildRequires:  %{python_module numba}
BuildRequires:  %{python_module numpy >= 1.20.0}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pandas >= 1.4.0}
BuildRequires:  %{python_module pytest >= 0.23}
BuildRequires:  %{python_module scipy >= 1.8.0}
BuildRequires:  %{python_module setuptools >= 60.0.0}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module xarray >= 0.21.0}
BuildRequires:  %{python_module xarray-einstats >= 0.3}
# /SECTION
BuildRequires:  fdupes
Requires:       python-matplotlib >= 3.5
Requires:       python-netCDF4
Requires:       python-numpy >= 1.20.0
Requires:       python-packaging
Requires:       python-pandas >= 1.4.0
Requires:       python-scipy >= 1.8.0
Requires:       python-setuptools >= 60.0.0
Requires:       python-xarray >= 0.21.0
Recommends:     python-bokeh >= 1.4.0
Recommends:     python-numba
Recommends:     python-ujson
BuildArch:      noarch
%python_subpackages

%description
ArviZ is a Python package for exploratory analysis of Bayesian models. Includes
functions for posterior analysis, data storage, model checking, comparison and
diagnostics.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Delete pyjags test to avoid import errors when running pytest
rm arviz/tests/external_tests/test_data_pyjags.py
# Weird errors when pymc3 is not available, just skipping the tests does not work
rm arviz/tests/external_tests/test_data_pymc.py
# Matplotlib tests try to save results to non-writeable dir
%pytest -k 'not test_plots_matplotlib'

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
