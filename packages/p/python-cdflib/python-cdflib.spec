#
# spec file for package python-cdflib
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


%{?!python_module:%define python_module() python3-%{**}}
Name:           python-cdflib
Version:        0.3.20
Release:        0
Summary:        A python CDF reader toolkit
License:        MIT
URL:            https://github.com/MAVENSDC/cdflib
# Tests only included in github archive
Source:         https://github.com/MAVENSDC/cdflib/archive/refs/tags/%{version}.tar.gz#/cdflib-%{version}-gh.tar.gz
# Test datafile, Public domain, not packaged
Source1:        https://helios-data.ssl.berkeley.edu/data/E1_experiment/New_proton_corefit_data_2017/cdf/helios1/1974/h1_1974_346_corefit.cdf
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.2.0
Requires:       python-numpy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module astropy}
# /SECTION
%python_subpackages

%description
A python module to read/write CDF (Common Data Format .cdf) files without needing to install the CDF NASA library.

%prep
%setup -q -n cdflib-%{version}
sed -i '/addopts/ d' setup.cfg
cp %{SOURCE1} helios.cdf

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/cdflib
%{python_sitelib}/cdflib-%{version}*-info

%changelog
