#
# spec file for package python-xlwt
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


%bcond_without tests

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-xlwt
Version:        1.3.0
Release:        0
Url:            https://secure.simplistix.co.uk/svn/xlwt/trunk
Summary:        Library to Create Spreadsheet Files Compatible With MS Excel 97/2000/XP/2003
License:        BSD-4-Clause and BSD-3-Clause and LGPL-2.1+
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/x/xlwt/xlwt-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python3-Sphinx
BuildRequires:  python3-pkginfo
%if %{with tests}
BuildRequires:  %{python_module nose}
%endif
BuildArch:      noarch
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

%build
%python_build
cd docs && make html && rm _build/html/.buildinfo

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with tests}
%check
nosetests
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%doc docs/_build/html/
%doc examples/
%{python_sitelib}/*

%changelog
