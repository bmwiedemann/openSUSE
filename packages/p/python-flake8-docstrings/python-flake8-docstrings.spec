#
# spec file for package python-flake8-docstrings
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-flake8-docstrings
Version:        1.5.0
Release:        0
Summary:        Extension for flake8 which uses pydocstyle to check docstrings
License:        MIT
URL:            https://gitlab.com/pycqa/flake8-docstrings
Source:         https://files.pythonhosted.org/packages/source/f/flake8-docstrings/flake8-docstrings-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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
%setup -q -n flake8-docstrings-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/flake8_docstrings.*
%dir %{python_sitelib}/flake8_docstrings-%{version}-py*.egg-info
%{python_sitelib}/flake8_docstrings-%{version}-py*.egg-info/*
%pycache_only %{python_sitelib}/__pycache__

%changelog
