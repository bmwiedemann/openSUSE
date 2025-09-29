#
# spec file for package python-flake8-bugbear
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


%{?sle15_python_module_pythons}
Name:           python-flake8-bugbear
Version:        24.12.12
Release:        0
Summary:        A plugin for flake8 finding likely bugs and design problems in your program
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/PyCQA/flake8-bugbear
Source:         https://files.pythonhosted.org/packages/source/f/flake8-bugbear/flake8_bugbear-%{version}.tar.gz
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module flake8 >= 6.0.0}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module hypothesmith}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.2.0
Requires:       python-flake8 >= 6.0.0
BuildArch:      noarch
%python_subpackages

%description
A plugin for Flake8 finding likely bugs and design problems in your
program.  Contains warnings that don't belong in pyflakes and
pycodestyle.

%prep
%setup -q -n flake8_bugbear-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Fuzz testing needs fast machine for quick enough data responses
%pytest -k 'not TestFuzz'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/bugbear.py
%{python_sitelib}/flake8[-_]bugbear-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/bugbear*

%changelog
