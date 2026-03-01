#
# spec file for package python-PyPika
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-PyPika
Version:        0.51.1
Release:        0
Summary:        A SQL query builder API for Python
License:        Apache-2.0
Group:          Development/Libraries/Python
URL:            https://github.com/kayak/pypika
Source0:        https://files.pythonhosted.org/packages/source/p/pypika/pypika-%{version}.tar.gz
Source1:        https://github.com/kayak/pypika/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A SQL query builder API for Python. The motivation behind PyPika is to provide a simple interface for building SQL queries without limiting the flexibility of handwritten SQL. Designed with data analysis in mind, PyPika leverages the builder design pattern to construct queries to avoid messy string formatting and concatenation. It is also easily extended to take full advantage of specific features of SQL database vendors.

%prep
%autosetup -p1 -n pypika-%{version}
# tests are not included in the tarball from pypi
(cd ..; tar xf %{SOURCE1} pypika-%{version}/pypika/tests)

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest pypika/tests

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/pypika
%{python_sitelib}/pypika-%{version}.dist-info

%changelog
