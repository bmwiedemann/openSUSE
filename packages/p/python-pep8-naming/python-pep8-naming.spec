#
# spec file for package python-pep8-naming
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pep8-naming
Version:        0.13.3
Release:        0
Summary:        Flake8 plugin for checking PEP-8 naming conventions
License:        MIT
URL:            https://github.com/PyCQA/pep8-naming
Source:         https://files.pythonhosted.org/packages/source/p/pep8-naming/pep8-naming-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flake8 >= 5.0.0
Requires:       python-flake8-polyfill >= 1.0.2
Requires:       python-setuptools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module flake8 >= 5.0.0}
BuildRequires:  %{python_module flake8-polyfill >= 1.0.2}
# /SECTION
%python_subpackages

%description
Check the PEP-8 naming conventions.

This module provides a plugin for ``flake8``, the Python code checker.

(It replaces the plugin ``flint-naming`` for the ``flint`` checker.)

%prep
%autosetup -p1 -n pep8-naming-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -B run_tests.py
}

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/pep8ext_naming.py*
%pycache_only %{python_sitelib}/__pycache__/pep8ext_naming.*.py*
%{python_sitelib}/pep8_naming-%{version}*-info

%changelog
