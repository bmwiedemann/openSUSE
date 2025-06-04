#
# spec file for package python-pretend
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
Name:           python-pretend
Version:        1.0.9
Release:        0
Summary:        A library for stubbing in Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/alex/pretend
Source:         https://files.pythonhosted.org/packages/source/p/pretend/pretend-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/alex/pretend/master/test_pretend.py
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Pretend is a library to make stubbing with Python easier.

%prep
%setup -q -n pretend-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files %{python_files}
%license LICENSE.rst
%doc README.rst
%{python_sitelib}/pretend*
%{python_sitelib}/__pycache__/*

%changelog
