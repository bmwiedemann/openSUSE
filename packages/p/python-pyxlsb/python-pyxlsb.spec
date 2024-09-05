#
# spec file for package python-pyxlsb
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

%{?sle15_python_module_pythons}
Name:           python-pyxlsb
Version:        1.0.10
Release:        0
Summary:        Excel 2007-2010 Binary Workbook (xlsb) parser
License:        LGPL-3.0+
URL:            https://github.com/willtrnr/pyxlsb
Source:         https://files.pythonhosted.org/packages/source/p/pyxlsb/pyxlsb-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Excel 2007-2010 Binary Workbook (xlsb) parser

%prep
%autosetup -p1 -n pyxlsb-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license COPYING COPYING.LESSER
%{python_sitelib}/pyxlsb
%{python_sitelib}/pyxlsb-%{version}.dist-info

%changelog
