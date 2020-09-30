#
# spec file for package python-xarray
#
# Copyright (c) 2020 SUSE LLC
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
%define         skip_python2 1
Name:           python-xarray
Version:        0.16.1
Release:        0
Summary:        N-D labeled arrays and datasets in Python
License:        Apache-2.0
URL:            https://github.com/pydata/xarray
Source:         https://files.pythonhosted.org/packages/source/x/xarray/xarray-%{version}.tar.gz
BuildRequires:  %{python_module numpy >= 1.15}
BuildRequires:  %{python_module numpy-devel >= 1.14}
BuildRequires:  %{python_module pandas >= 0.25}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.15
Requires:       python-pandas >= 0.25
Recommends:     python-scipy >= 1.3
Suggests:       python-dask >= 2.2
Provides:       python-xray = %{version}
Obsoletes:      python-xray < %{version}
BuildArch:      noarch
# SECTION tests
# dask tests currently failing
# BuildRequires:  %%{python_module dask-dataframe}
BuildRequires:  %{python_module pytest >= 2.7.1}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
xarray (formerly xray) is a python-pandas-like and pandas-compatible
toolkit for analytics on multi-dimensional arrays. It provides
N-dimensional variants of the python-pandas labeled data structures,
rather than the tabular data that pandas uses.

The Common Data Model for self-describing scientific data is used.
The dataset is an in-memory representation of a netCDF file.

%prep
%setup -q -n xarray-%{version}
chmod -x xarray/util/print_versions.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_no_warning_from_dask_effective_get fails due to upstream scipy warning
%pytest -k "not test_download_from_github and not test_no_warning_from_dask_effective_get" xarray

%files %{python_files}
%doc README.rst
%license LICENSE licenses/
%{python_sitelib}/xarray*

%changelog
