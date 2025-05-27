#
# spec file for package python-flake8-docstrings
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


%{?sle15_python_module_pythons}
Name:           python-flake8-docstrings
Version:        1.7.0
Release:        0
Summary:        Extension for flake8 which uses pydocstyle to check docstrings
License:        MIT
URL:            https://gitlab.com/pycqa/flake8-docstrings
Source:         https://files.pythonhosted.org/packages/source/f/flake8_docstrings/flake8_docstrings-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flake8 >= 3
Requires:       python-flake8-polyfill
Requires:       python-pydocstyle >= 2.1.0
BuildArch:      noarch
%python_subpackages

%description
A module that adds an extension for the pydocstyle tool to flake8.

%prep
%setup -q -n flake8_docstrings-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/flake8_docstrings.*
%{python_sitelib}/flake8_docstrings-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__

%changelog
