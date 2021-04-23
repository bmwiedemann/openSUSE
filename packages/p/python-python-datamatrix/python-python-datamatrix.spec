#
# spec file for package python-python-datamatrix
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-python-datamatrix
Version:        0.11.1
Release:        0
Summary:        A python library to work with tabular data
License:        GPL-3.0-or-later
URL:            https://github.com/open-cogsci/python-datamatrix
Source:         https://github.com/open-cogsci/python-datamatrix/archive/release/%{version}.tar.gz#/python-datamatrix-release-%{version}.tar.gz
BuildRequires:  %{python_module fastnumbers}
BuildRequires:  %{python_module openpyxl}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module json_tricks if (%python-base without python36-base)}
BuildRequires:  %{python_module matplotlib if (%python-base without python36-base)}
BuildRequires:  %{python_module nibabel if (%python-base without python36-base)}
BuildRequires:  %{python_module nilearn if (%python-base without python36-base)}
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
BuildRequires:  %{python_module pandas if (%python-base without python36-base)}
BuildRequires:  %{python_module scipy if (%python-base without python36-base)}
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
# all tests fail on collection or init, because they assume the presence of optional dependencies such as numpy
python36_donttest="-V"
# 32-bit datatype and precision errors
if [ $(getconf LONG_BIT) -eq 32 ]; then
  donttest="or test_intcolumn or test_seriescolumn"
fi
%pytest ${$python_donttest} ${donttest:+ -k "not (${donttest:4})"}

%files %{python_files}
%license copyright
%doc readme.md
%doc doc-pelican/content/pages/*
%doc doc-pelican/data/
%doc doc-pelican/include/api
%{python_sitelib}/datamatrix/
%{python_sitelib}/python_datamatrix-%{version}*-info

%changelog
