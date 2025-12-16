#
# spec file for package python-pytest-flake8
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


Name:           python-pytest-flake8
Version:        1.3.0
Release:        0
Summary:        Pytest plugin to check flake8 requirements
License:        MIT
URL:            https://github.com/coherent-oss/pytest-flake8
Source:         https://files.pythonhosted.org/packages/source/p/pytest-flake8/pytest_flake8-1.3.0.tar.gz
Patch0:         support-pytest-9.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
# SECTION test requirements
BuildRequires:  %{python_module flake8 >= 4.0}
BuildRequires:  %{python_module pytest >= 7.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-flake8 >= 4.0
Requires:       python-pytest >= 7.0
Suggests:       python-sphinx >= 3.5
Suggests:       python-jaraco.packaging >= 9.3
Suggests:       python-rst.linker >= 1.9
Suggests:       python-furo
Suggests:       python-sphinx-lint
Suggests:       python-pytest-checkdocs >= 2.4
Suggests:       python-pytest-ruff >= 0.2.1
Suggests:       python-pytest-cov
Suggests:       python-pytest-enabler >= 2.2
Suggests:       python-pytest-mypy
BuildArch:      noarch
%python_subpackages

%description
pytest plugin to check FLAKE8 requirements

%prep
%autosetup -p1 -n pytest_flake8-%{version}

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
%{python_sitelib}/pytest_flake8.py
%pycache_only %{python_sitelib}/__pycache__/pytest_flake8*.pyc
%{python_sitelib}/pytest_flake8-%{version}.dist-info

%changelog
