#
# spec file for package python-python-datamatrix
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


Name:           python-python-datamatrix
Version:        1.0.16
Release:        0
Summary:        A python library to work with tabular data
License:        GPL-3.0-or-later
URL:            https://github.com/open-cogsci/python-datamatrix
Source:         https://github.com/open-cogsci/python-datamatrix/archive/release/%{version}.tar.gz#/python-datamatrix-release-%{version}.tar.gz
BuildRequires:  %{python_module PrettyTable}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module fastnumbers}
BuildRequires:  %{python_module flit-core >= 3.4}
BuildRequires:  %{python_module json_tricks}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module nibabel}
BuildRequires:  %{python_module nilearn}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module openpyxl}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module tomlkit}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PrettyTable
Requires:       python-json_tricks
Requires:       python-numpy
Requires:       python-openpyxl
Requires:       python-psutil
Requires:       python-scipy
Requires:       python-tomlkit
Recommends:     python-fastnumbers
Recommends:     python-matplotlib
Recommends:     python-nibabel
Recommends:     python-nilearn
Recommends:     python-pandas
BuildArch:      noarch
%python_subpackages

%description
The datamatrix package provides a high way to work with tabular data in Python.
Tabular data is datasets that consist of named columns and numbered rows.

%package -n %{name}-doc
Summary:        Documentation for %{name}
Provides:       %{python_module python-datamatrix-doc = %{version}}

%description -n %{name}-doc
Documentation and examples for %{name}.

%prep
%setup -q -n datamatrix-release-%{version}
# wrong-file-end-of-line-encoding
sed -i 's/\r$//' doc-pelican/data/fratescu-replication-data-exp1.csv

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# 32-bit datatype and precision errors
if [ $(getconf LONG_BIT) -eq 32 ]; then
  donttest="or test_intcolumn or test_seriescolumn"
fi
%pytest -p no:warnings ${$python_donttest} ${donttest:+ -k "not (${donttest:4})"}

%files %{python_files}
%license copyright
%doc readme.md
%{python_sitelib}/datamatrix/
%{python_sitelib}/datamatrix-%{version}.dist-info

%files -n %{name}-doc
%license copyright
%doc doc-pelican/content/pages/*
%doc doc-pelican/data/
%doc doc-pelican/include/api

%changelog
