#
# spec file for package python-pytest-click
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
Name:           python-pytest-click
Version:        1.1.0
Release:        0
Summary:        Pytest plugin for Click
License:        MIT
URL:            https://github.com/Stranger6667/pytest-click
Source:         https://github.com/Stranger6667/pytest-click/archive/v%{version}.tar.gz#/pytest-click-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 6.0
Requires:       python-pytest >= 3.6.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click >= 6.0}
BuildRequires:  %{python_module pytest >= 5.0}
# /SECTION
%python_subpackages

%description
Py.test plugin for Click.

%prep
%setup -q -n pytest-click-%{version}
sed -i "s/'pytest-cov>=[0-9.]*'//;s/==/>=/g" setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=C.UTF-8
%pytest

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%{python_sitelib}/pytest_click
%{python_sitelib}/pytest_click-%{version}.dist-info

%changelog
