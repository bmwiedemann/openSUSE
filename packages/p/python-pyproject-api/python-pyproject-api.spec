#
# spec file for package python-pyproject-api
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


%{?sle15_python_module_pythons}
Name:           python-pyproject-api
Version:        1.5.1
Release:        0
Summary:        API to interact with the python pyproject.toml based projects
License:        MIT
URL:            https://github.com/tox-dev/pyproject-api
Source:         https://files.pythonhosted.org/packages/source/p/pyproject_api/pyproject_api-%{version}.tar.gz
BuildRequires:  %{python_module hatch >= 0.3}
BuildRequires:  %{python_module hatch-vcs >= 0.3}
BuildRequires:  %{python_module hatchling >= 1.12.2}
BuildRequires:  %{python_module importlib-metadata >= 6 if %python-base < 3.8}
BuildRequires:  %{python_module packaging >= 23}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module tomli >= 2.0.1 if %python-base < 3.11}
BuildRequires:  %{python_module wheel >= 0.38.4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildRequires:  (python36-importlib-metadata >= 6 if python36-base)
Requires:       python-packaging >= 23
Requires:       (python-importlib-metadata >= 6 if python3-base < 3.8)
Requires:       (python-tomli >= 2.0.1 if python3-base < 3.11)
BuildArch:      noarch
# SECTION testing=
# (except for pytest-cov and -randomly)
BuildRequires:  %{python_module covdefaults >= 2.2.2}
BuildRequires:  %{python_module pytest >= 7.2.0}
BuildRequires:  %{python_module pytest-mock >= 3.10.0}
BuildRequires:  %{python_module virtualenv >= 20.17.1}
# /SECTION
%python_subpackages

%description
pyproject-api aims to abstract away interaction with
pyproject.toml style projects in a flexible way.

%prep
%autosetup -p1 -n pyproject_api-%{version}

%build
export LANG=en_US.UTF8
%pyproject_wheel

%install
export LANG=en_US.UTF8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#tox-dev/pyproject-api#45
skip_tests="test_can_build_on_python_2"
# gh#tox-dev/pyproject-api#77
skip_tests="($skip_tests or test_setuptools_prepare_metadata_for_build_wheel)"
%pytest -k "not $skip_tests"

%files %{python_files}
%license LICENSE
%doc README.md docs/changelog.rst
%{python_sitelib}/pyproject_api-%{version}*-info
%{python_sitelib}/pyproject_api

%changelog
