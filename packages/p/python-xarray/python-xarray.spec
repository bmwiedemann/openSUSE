#
# spec file for package python-xarray
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
%define skip_python2 1
Name:           python-xarray
Version:        0.12.3
Release:        0
Summary:        N-D labeled arrays and datasets in Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://github.com/pydata/xarray
Source:         https://files.pythonhosted.org/packages/source/x/xarray/xarray-%{version}.tar.gz
BuildRequires:  %{python_module numpy-devel >= 1.12}
BuildRequires:  %{python_module pandas >= 0.19.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.12
Requires:       python-pandas >= 0.19.2
Recommends:     python-scipy
Provides:       python-xray = %{version}
Obsoletes:      python-xray < %{version}
BuildArch:      noarch
# SECTION tests
# dask tests currently failing
# BuildRequires:  %%{python_module dask-dataframe}
BuildRequires:  %{python_module pytest >= 2.7.1}
BuildRequires:  %{python_module scipy}
BuildRequires:  python2-mock
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests are xfail on aarch64: gh#pydata/xarray#2334
%pytest -k "not test_datetime_reduce and not test_roundtrip_numpy_datetime_data and not test_download_from_github"

%files %{python_files}
%doc README.rst
%license LICENSE licenses/
%{python_sitelib}/xarray*

%changelog
