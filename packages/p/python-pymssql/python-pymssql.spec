#
# spec file for package python-pymssql
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


Name:           python-pymssql
Version:        2.3.2
Release:        0
Summary:        A simple database interface to MS-SQL for Python
License:        LGPL-2.1-only
Group:          Development/Languages/Python
URL:            https://pymssql.org
Source:         https://files.pythonhosted.org/packages/source/p/pymssql/pymssql-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 3.0.11}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  freetds-devel
BuildRequires:  krb5-devel
BuildRequires:  openssl-devel
BuildRequires:  python-rpm-macros
%python_subpackages

%description
pymssql is the Python language extension module that provides access to
Microsoft SQL Servers from Python scripts. It is compliant with Python
DB-API 2.0 Specification and works on most popular operating systems.

%prep
%setup -q -n pymssql-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

### Tests need access to a MSSQL-server
#%%check
#%%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc ChangeLog.rst README.rst
%{python_sitearch}/pymssql
%{python_sitearch}/pymssql-%{version}*-info

%changelog
