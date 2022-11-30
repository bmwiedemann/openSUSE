#
# spec file for package python-pytest-flake8
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


Name:           python-pytest-flake8
Version:        1.1.1
Release:        0
Summary:        Plugin for pytest to check FLAKE8 requirements
License:        BSD-2-Clause
URL:            https://github.com/tholo/pytest-flake8
Source:         https://files.pythonhosted.org/packages/source/p/pytest-flake8/pytest-flake8-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Support flake8 >= 5.0 gh#tholo/pytest-flake8#88
Patch0:         support-flake8-5.patch
BuildRequires:  %{python_module flake8 >= 5.0}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flake8 >= 5.0
Requires:       python-py
Requires:       python-pytest >= 3.5
BuildArch:      noarch
%python_subpackages

%description
Plugin for py.test for efficiently checking PEP8 compliance.

%prep
%autosetup -p1 -n pytest-flake8-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG README.rst
%pycache_only %{python_sitelib}/__pycache__/*.pyc
%{python_sitelib}/pytest_flake8.py
%{python_sitelib}/pytest_flake8-%{version}*-info

%changelog
