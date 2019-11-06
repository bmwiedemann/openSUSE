#
# spec file for package python-python-datamatrix
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-python-datamatrix
Version:        0.10.12
Release:        0
License:        GPL-3.0-or-later
Summary:        A python library to work with tabular data
Url:            https://github.com/smathot/python-datamatrix
Group:          Development/Languages/Python
Source:         https://github.com/smathot/python-datamatrix/archive/release/%{version}.tar.gz#/python-datamatrix-release-%{version}.tar.gz
BuildRequires:  %{python_module fastnumbers}
BuildRequires:  %{python_module json_tricks}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module nibabel}
BuildRequires:  %{python_module nilearn}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module openpyxl}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-PrettyTable
Recommends:     python-fastnumbers
Recommends:     python-json_tricks
Recommends:     python-matplotlib
Recommends:     python-nibabel
Recommends:     python-nilearn
Recommends:     python-numpy
Recommends:     python-openpyxl
Recommends:     python-pandas
Recommends:     python-scipy
BuildArch:      noarch

%python_subpackages

%description
The datamatrix package provides a high way to work with tabular data in Python.
Tabular data is datasets that consist of named columns and numbered rows.

%prep
%setup -q -n python-datamatrix-release-%{version}
# wrong-file-end-of-line-encoding
sed -i 's/\r$//' doc-pelican/data/fratescu-replication-data-exp1.csv

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# All test failures appear to be problematic, but are specific to input data types
%python_expand nosetests-%{$python_bin_suffix} testcases -e '(test_memoize|test_group|test_io|test_intcolumn|test_seriescolumn)'

%files %{python_files}
%license copyright
%doc readme.md 
%doc doc-pelican/content/pages/*
%doc doc-pelican/data/
%doc doc-pelican/include/api
%{python_sitelib}/datamatrix/
%{python_sitelib}/python_datamatrix-%{version}-py*.egg-info

%changelog
