#
# spec file for package python-dash-core-components
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
# Upstream cannot tag the release version, but we need the github archive for the test files
# https://github.com/plotly/dash-core-components/issues/886
%define commit 230997613c81ce927cf558720585a9632e3df192
Name:           python-dash-core-components%{psuffix}
Version:        1.14.1
Release:        0
Summary:        Core component suite for Dash
License:        MIT
URL:            https://github.com/plotly/dash-core-components
Source:         https://github.com/plotly/dash-core-components/archive/%{commit}.tar.gz#/dash-core-components-%{version}-gh.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module dash}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module selenium}
%endif
%python_subpackages

%description
Core component suite for Dash

%prep
%setup -q -n dash-core-components-%{commit}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# simplest integration tests as run in .circleci/
%pyunittest tests/test_dash_import.py -v
# fulls suite needs working selenium and chromedriver
# when fixed this should be enabled
#%%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/dash_core_components
%{python_sitelib}/dash_core_components-%{version}-py*.egg-info
%endif

%changelog
