#
# spec file for package python-xlrd
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


%{?sle15_python_module_pythons}
Name:           python-xlrd
Version:        2.0.1
Release:        0
Summary:        Python module for extracting data from .xls Excel spreadsheet files
License:        BSD-3-Clause
URL:            https://www.python-excel.org/
Source:         https://github.com/python-excel/xlrd/archive/refs/tags/%{version}.tar.gz#/xlread-%{version}-gh.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A library for reading data and formatting information from Excel files
in the historical .xls format.

%prep
%setup -q -n xlrd-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
mv %{buildroot}%{_bindir}/runxlrd.py %{buildroot}%{_bindir}/runxlrd
%python_clone -a %{buildroot}%{_bindir}/runxlrd

%post
%python_install_alternative runxlrd

%postun
%python_uninstall_alternative runxlrd

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/runxlrd
%{python_sitelib}/xlrd
%{python_sitelib}/xlrd-%{version}.dist-info

%changelog
