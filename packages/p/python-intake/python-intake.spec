#
# spec file for package python-intake
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
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-intake%{psuffix}
Version:        2.0.5
Release:        0
Summary:        Data loading and cataloging system
License:        BSD-2-Clause
URL:            https://github.com/intake/intake
Source:         https://github.com/intake/intake/archive/refs/tags/%{version}.tar.gz#/intake-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 64}
BuildRequires:  %{python_module setuptools_scm >= 8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-appdirs
Requires:       python-fsspec >= 2023
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module dask-all}
BuildRequires:  %{python_module hvplot}
BuildRequires:  %{python_module intake = %{version}}
# strictly a test req, but not a runtime requirement, not available in openSUSE
#BuildRequires:  %%{python_module intake-parquet}
BuildRequires:  %{python_module msgpack-numpy}
BuildRequires:  %{python_module notebook}
BuildRequires:  %{python_module numpy < 2}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module panel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module xarray}
BuildRequires:  %{python_module zarr}
%endif
%python_subpackages

%description
A python package for describing, loading and processing data

Intake is an open-source package to:
 * describe your data declaratively
 * gather data sets into catalogs
 * search catalogs and services to find the right data you need
 * load, transform and output data in many formats
 * work with third party remote storage and compute platforms

%prep
%autosetup -p1 -n intake-%{version}

%build
%if !%{with test}
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# upstream currently only tests the readers subdir. The rest seems to still expect v1
# See .github/workflows/main.yaml
%pytest -rsfE intake/readers
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/intake
%{python_sitelib}/intake-%{version}.dist-info
%endif

%changelog
