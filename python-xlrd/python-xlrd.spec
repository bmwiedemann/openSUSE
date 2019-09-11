#
# spec file for package python-xlrd
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-xlrd
Version:        1.2.0
Release:        0
Url:            http://www.lexicon.net/sjmachin/xlrd.htm
Summary:        Python module for extracting data from Excel spreadsheet files
License:        BSD-3-Clause
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/x/xlrd/xlrd-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module nose}
# /SECTION
Recommends:     python-defusedxml
BuildArch:      noarch
%python_subpackages

%description
Extract data from Excel spreadsheets
(.xls and .xlsx, versions 2.0 onwards).

%prep
%setup -q -n xlrd-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
mv %{buildroot}%{_bindir}/runxlrd.py %{buildroot}%{_bindir}/runxlrd

%check
%python_expand nosetests-%{$python_bin_suffix}

%files %{python_files}
%doc README.md
%license docs/licenses.rst
%python3_only %{_bindir}/runxlrd
%{python_sitelib}/*

%changelog
