#
# spec file for package python-python-sql
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
Name:           python-python-sql
Version:        1.5.1
Release:        0
Summary:        Library to write SQL queries
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://pypi.io/project/python-sql
## Source:         https://pypi.io/packages/source/p/python-sql/python-sql-%%{version}.tar.gz
## Naming scheme broken upsream
Source:         https://files.pythonhosted.org/packages/source/p/python_sql/python_sql-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
python-sql is a library to write SQL queries in a pythonic way.

%prep
%autosetup -n python_sql-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
mv sql sql_hide
%pyunittest discover -v
mv sql_hide sql

%files %{python_files}
%license COPYRIGHT
%doc README.rst
%{python_sitelib}/sql
%{python_sitelib}/python_sql-%{version}.dist-info

%changelog
