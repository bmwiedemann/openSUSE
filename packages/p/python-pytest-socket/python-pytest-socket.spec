#
# spec file for package python-pytest-socket
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


%{?sle15_python_module_pythons}
Name:           python-pytest-socket
Version:        0.7.0
Release:        0
Summary:        Pytest Plugin to disable socket calls
License:        MIT
URL:            https://github.com/miketheman/pytest-socket
Source:         https://files.pythonhosted.org/packages/source/p/pytest-socket/pytest_socket-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 3.6.3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 3.6.3}
# /SECTION
%python_subpackages

%description
A plugin to use with Pytest to disable or restrict socket calls during
tests to ensure network calls are prevented.

%prep
%setup -q -n pytest_socket-%{version}
touch tests/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=$PWD/tests
# Most tests require a network connection, let's check basic function
%pytest -k 'test_disable_via or test_global_disable_via'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pytest_socket.py
%pycache_only %{python_sitelib}/__pycache__/pytest_socket*.pyc
%{python_sitelib}/pytest_socket-%{version}.dist-info

%changelog
