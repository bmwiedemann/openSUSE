#
# spec file for package python-databases
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-databases
Version:        0.9.0
Release:        0
Summary:        Async database support for Python
License:        BSD-3-Clause
URL:            https://github.com/encode/databases
Source:         https://github.com/encode/databases/archive/%{version}.tar.gz#/databases-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-sqlalchemy >= 2.0.7
Suggests:       python-aiomysql
Suggests:       python-aiopg
Suggests:       python-aiosqlite
Suggests:       python-asyncpg
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiosqlite}
BuildRequires:  %{python_module asyncpg}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module sqlalchemy >= 2.0.7}
# /SECTION
%python_subpackages

%description
Async database support for Python.

%prep
%autosetup -p1 -n databases-%{version}

# tests/test_integration.py depends on starlette
rm tests/test_integration.py

# Remove test dependencies aiopg, aiomysql and asyncmy
sed -Ei 's/from .*(aiopg|mysql|asyncmy).* import .*/pass/' tests/test_connection_options.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export TEST_DATABASE_URLS=sqlite:///mytestdb
export PYTHONPATH=${PWD}
%pytest -k 'not (aiopg or mysql or asyncmy)'

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/databases
%{python_sitelib}/databases-%{version}.dist-info

%changelog
