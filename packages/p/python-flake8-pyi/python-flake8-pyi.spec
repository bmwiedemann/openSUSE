#
# spec file for package python-flake8-pyi
#
# Copyright (c) 2020 SUSE LLC
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-flake8-pyi
Version:        20.5.0
Release:        0
Summary:        A plugin for flake8 to enable linting .pyi files
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ambv/flake8-pyi
Source:         https://files.pythonhosted.org/packages/source/f/flake8-pyi/flake8-pyi-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/ambv/flake8-pyi/master/LICENSE
BuildRequires:  %{python_module base >= 3.6.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module flake8 >= 3.2.1}
BuildRequires:  %{python_module pyflakes >= 2.1.1}
# Use pytest directly to bypass setup.py test dependencies
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing}
# /SECTION
BuildRequires:  fdupes
Requires:       python-attrs
Requires:       python-base >= 3.6.0
Requires:       python-flake8 >= 3.2.1
Requires:       python-pyflakes >= 2.1.1
Requires:       python-typing
BuildArch:      noarch

%python_subpackages

%description
A plugin for Flake8 that provides specializations for type hinting stub
files. Especially interesting for linting typeshed.

%prep
%setup -q -n flake8-pyi-%{version}
sed -i '1{\,^#!%{_bindir}/env python,d}' pyi.py
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -v tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/pyi.py*
%{pycache_only %{python_sitelib}/__pycache__/pyi.*.py*}
%{python_sitelib}/flake8_pyi-%{version}-*.egg-info

%changelog
