#
# spec file for package python-openpyxl
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-openpyxl
Version:        3.1.3
Release:        0
Summary:        A Python library to read/write Excel 2010 xlsx/xlsm files
License:        MIT AND Python-2.0
URL:            https://foss.heptapod.net/openpyxl/openpyxl
Source:         https://files.pythonhosted.org/packages/source/o/openpyxl/openpyxl-%{version}.tar.gz
BuildRequires:  %{python_module et_xmlfile}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-et_xmlfile
# for embedded image support
Recommends:     python-Pillow
BuildArch:      noarch
%python_subpackages

%description
openpyxl is a pure python reader and writer of Excel OpenXML files.
It is ported from the PHPExcel project

%prep
%setup -q -n openpyxl-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
mv LICENCE.rst LICENSE.rst

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE.rst
%{python_sitelib}/openpyxl
%{python_sitelib}/openpyxl-%{version}.dist-info

%changelog
