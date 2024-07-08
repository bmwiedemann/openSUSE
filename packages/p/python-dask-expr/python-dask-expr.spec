#
# spec file for package python-dask-expr
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


%define psuffix %{nil}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-dask-expr%{psuffix}
Version:        1.1.6
Release:        0
Summary:        High Level Expressions for Dask
License:        BSD-3-Clause
URL:            https://github.com/dask/dask-expr
Source0:        https://github.com/dask/dask-expr/archive/refs/tags/v%{version}.tar.gz#/dask_expr-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 62.6}
BuildRequires:  %{python_module versioneer-toml}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dask = 2024.6.2
Requires:       python-pandas >= 2
Requires:       python-pyarrow >= 7.0.0
Provides:       python-dask_expr = %{version}-%{release}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module dask-dataframe}
BuildRequires:  %{python_module dask-expr = %{version}}
BuildRequires:  %{python_module distributed}
BuildRequires:  %{python_module pandas >= 2}
BuildRequires:  %{python_module pyarrow >= 7.0.0}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Dask DataFrames with query optimization.
This is a rewrite of Dask DataFrame that includes query optimization
and generally improved organization.

%prep
%autosetup -p1 -n dask-expr-%{version}
sed -i 's/--color=yes//' pyproject.toml

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# https://github.com/dask/dask-expr/issues/789 (?)
donttest="test_groupby_index_array"
%pytest -k "not ($donttest)"
%endif

%if !%{with test}
%files %{python_files}
%{python_sitelib}/dask_expr
%{python_sitelib}/dask_expr-%{version}.dist-info
%endif

%changelog
