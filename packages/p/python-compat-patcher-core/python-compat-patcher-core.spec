#
# spec file for package python-compat-patcher-core
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-compat-patcher-core
Version:        1.0
Release:        0
Summary:        Python patcher system
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pakal/compat-patcher-core
Source:         https://files.pythonhosted.org/packages/source/c/compat-patcher-core/compat-patcher-core-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  cookiecutter > 1.6.0
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
Python patcher system to allow easy and lasting API compatibility.

%prep
%setup -q -n compat-patcher-core-%{version}
sed -i 's/python setup/python3 setup/' tests/*.py
dos2unix CHANGELOG
# Depends on pytest-cookies, and the recipe isnt part of the core package
rm tests/test_cookiecutter_recipe.py
rm pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%doc AUTHORS CHANGELOG README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
