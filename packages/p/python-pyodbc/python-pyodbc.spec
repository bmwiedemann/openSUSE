#
# spec file for package python-pyodbc
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
Name:           python-pyodbc
Version:        4.0.27
Release:        0
Summary:        Python ODBC API
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mkleehammer/pyodbc
Source:         https://files.pythonhosted.org/packages/source/p/pyodbc/pyodbc-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildRequires:  sqliteodbc
BuildRequires:  unixODBC-devel
%python_subpackages

%description
pyodbc is a Python 2.x and 3.x module that allows you to use ODBC
to connect to almost any database.

It implements the Python Database API Specification v2.0, but
additional features have been added to simplify database programming
even more.

%prep
%setup -q -n pyodbc-%{version}
mv tests2 tests-%{python2_bin_suffix}
mv tests3 tests-%{python3_bin_suffix}

%build
%python_build

%install
%python_install

%check
export PYTHONDONTWRITEBYTECODE=1
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python tests-%{$python_bin_suffix}/sqlitetests.py -v "Driver=SQLITE3;Database=sqlite.db"
}

%files %{python_files}
%{python_sitearch}/*
%license LICENSE.txt
%doc README.md

%changelog
