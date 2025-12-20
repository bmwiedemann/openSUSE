#
# spec file for package python-narwhals
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


Name:           python-narwhals
Version:        2.14.0
Release:        0
Summary:        Extremely lightweight compatibility layer between dataframe libraries
License:        MIT
URL:            https://github.com/narwhals-dev/narwhals
Source:         https://files.pythonhosted.org/packages/source/n/narwhals/narwhals-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module base >= 3.9}
# Test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-env}
BuildRequires:  %{python_module pytest-randomly}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pandas >= 1.1.3}
BuildRequires:  %{python_module dask >= 2024.8}
BuildRequires:  %{python_module dask-dataframe >= 2024.8}
BuildRequires:  %{python_module pyarrow >= 11.0.0}
# optional dependencies
Suggests:       python-pandas >= 1.1.3
Suggests:       python-dask >= 2024.8
Suggests:       python-dask-dataframe >= 2024.8
Suggests:       python-pyarrow >= 13.0.0

BuildArch:      noarch
%python_subpackages

%description
Extremely lightweight and extensible compatibility layer between
dataframe libraries!

%prep
%autosetup -p1 -n narwhals-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Dependencies not available in openSUSE
donttest="polars or ibis or duckdb or sqlframe"
%pytest -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/narwhals
%{python_sitelib}/narwhals-%{version}.dist-info

%changelog
