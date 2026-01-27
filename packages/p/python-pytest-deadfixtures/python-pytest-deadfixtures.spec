#
# spec file for package python-pytest-deadfixtures
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-pytest-deadfixtures
Version:        3.1.0
Release:        0
Summary:        A simple plugin to list unused fixtures in pytest
License:        MIT
URL:            https://github.com/jllorencetti/pytest-deadfixtures
Source:         https://github.com/jllorencetti/pytest-deadfixtures/archive/refs/tags/%{version}.tar.gz#/pytest_deadfixtures-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 7.0.0}
BuildRequires:  %{python_module pytest-cov}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest >= 7.0.0
BuildArch:      noarch
%python_subpackages

%description
A simple plugin to list unused fixtures in pytest

%prep
%autosetup -p1 -n pytest-deadfixtures-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pytest_deadfixtures.py
%pycache_only %{python_sitelib}/__pycache__/pytest_deadfixtures*.pyc
%{python_sitelib}/pytest_deadfixtures-%{version}.dist-info

%changelog
