#
# spec file for package python-circuitbreaker
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


%define modname circuitbreaker
Name:           python-circuitbreaker
Version:        2.1.3
Release:        0
Summary:        Python implementation of the "Circuit Breaker" Pattern
License:        BSD-3-Clause
URL:            https://github.com/fabfuel/circuitbreaker
Source:         https://files.pythonhosted.org/packages/source/c/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-typing
BuildArch:      noarch
%python_subpackages

%description
Python implementation of the "Circuit Breaker" Pattern

%prep
%autosetup -p1 -n circuitbreaker-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTEST_ADDOPTS="--asyncio-mode=auto"
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.rst
%{python_sitelib}/circuitbreaker.py
%{python_sitelib}/circuitbreaker-%{version}.dist-info
%pycache_only %{python_sitelib}/__pycache__/circuitbreaker*

%changelog
