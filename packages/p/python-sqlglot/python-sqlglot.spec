#
# spec file for package python-sqlglot
#
# Copyright (c) 2022 SUSE LLC
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


%define modname sqlglot
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-sqlglot
Version:        7.0.0
Release:        0
Summary:        An easily customizable SQL parser and transpiler
License:        MIT
URL:            https://github.com/tobymao/sqlglot
# gh#tobymao/sqlglot#585
Source:         https://github.com/tobymao/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE missing-duckdb.patch mcepl@suse.com
# Skip over duckdb requiring tests until it is packaged
Patch0:         missing-duckdb.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# FOR TESTS
BuildRequires:  %{python_module pandas}
# END FOR TESTS
BuildArch:      noarch
%python_subpackages

%description
SQLGlot is a no dependency Python SQL parser, transpiler, and optimizer. It can be
used to format SQL or translate between different dialects like DuckDB, Presto,
Spark, Snowflake, and BigQuery. It aims to read a wide variety of SQL inputs and
output syntactically correct SQL in the targeted dialects.

It is a very comprehensive generic SQL parser with a robust test suite. It is also
quite performant while being written purely in Python. You can easily customize the
parser, analyze queries, traverse expression trees, and programmatically build SQL.
Syntax errors are highlighted and dialect incompatibilities can warn or raise
depending on configurations.

%prep
%autosetup -p1 -n sqlglot-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/sqlglot
%{python_sitelib}/sqlglot-%{version}*-info

%changelog
