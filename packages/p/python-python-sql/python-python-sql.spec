#
# spec file
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


%if 0%{?suse_version} >= 1550
%define pythons python3
%define mypython python3
%define mysitelib %python3_sitelib
%else
%{?sle15_python_module_pythons}
%define mypython %pythons
%define mysitelib %{expand:%%%{mypython}_sitelib}
%endif

%define base_name python-sql
Name:           python-%{base_name}
Version:        1.4.3
Release:        0
Summary:        Library to write SQL queries
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://pypi.io/project/python-sql
Source:         https://pypi.io/packages/source/p/%{base_name}/%{base_name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
python-sql is a library to write SQL queries in a pythonic way.

%prep
%setup -q -n %{base_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
mv sql sql_hide
%pyunittest discover -v
mv sql_hide sql

%files %{python_files}
%license COPYRIGHT
%doc README.rst
%{mysitelib}/sql
%{mysitelib}/python_sql-%{version}.dist-info

%changelog
