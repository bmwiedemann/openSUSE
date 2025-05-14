#
# spec file for package python-xlwt
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


%bcond_without tests
%{?sle15_python_module_pythons}
Name:           python-xlwt
Version:        1.3.0
Release:        0
Summary:        Library to Create Spreadsheet Files Compatible With MS Excel 97/2000/XP/2003
License:        BSD-3-Clause AND BSD-4-Clause AND LGPL-2.1-or-later
URL:            https://github.com/python-excel/xlwt
Source0:        https://files.pythonhosted.org/packages/source/x/xlwt/xlwt-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/python-excel/xlwt/refs/heads/master/LICENSE
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-pkginfo
BuildArch:      noarch
%if %{with tests}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
xlwt is a library for generating spreadsheet files that are compatible
with Excel 97/2000/XP/2003, OpenOffice.org Calc, and Gnumeric. xlwt has
full support for Unicode. Excel spreadsheets can be generated on any
platform without needing Excel or a COM server. The only requirement is
Python 2.3 to 2.6. xlwt is a fork of pyExcelerator.

%prep
%setup -q -n xlwt-%{version}
# fix end of line encoding
sed -i 's/\r$//' examples/{numbers_demo.py,panes2.py,image_chg_col_wid.py,zoom_magnification.py}
cp %{SOURCE1} .

%build
%pyproject_wheel
cd docs && make html && rm _build/html/.buildinfo

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with tests}
%check
%pytest
%endif

%files %{python_files}
%doc README.rst
%doc docs/_build/html/
%doc examples/
%license LICENSE
%{python_sitelib}/xlwt
%{python_sitelib}/xlwt-%{version}.dist-info

%changelog
