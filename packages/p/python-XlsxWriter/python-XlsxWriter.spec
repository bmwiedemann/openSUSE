#
# spec file for package python-XlsxWriter
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


%{?sle15_python_module_pythons}
%define         oldpython python
Name:           python-XlsxWriter
Version:        3.2.9
Release:        0
Summary:        Python module for writing OOXML spreadsheet files
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jmcnamara/XlsxWriter
Source:         https://github.com/jmcnamara/XlsxWriter/archive/RELEASE_%{version}.tar.gz#/XlsxWriter-RELEASE_%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python3-xlsxwriter = %{version}
Obsoletes:      python3-xlsxwriter < %{version}
BuildArch:      noarch
%ifpython2
# python-xlsxwriter was last used in openSUSE Leap 42.1.
Provides:       %{oldpython}-xlsxwriter = %{version}
Obsoletes:      %{oldpython}-xlsxwriter < %{version}
%endif
%python_subpackages

%description
XlsxWriter is a Python module for writing files in the Microsoft
Office Open XML spreadsheet format. It can be used to write text,
numbers, formulas and hyperlinks to multiple worksheets and it
supports features such as formatting and many more.

%prep
%setup -q -n XlsxWriter-RELEASE_%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/vba_extract.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative vba_extract.py

%postun
%python_uninstall_alternative vba_extract.py

%check
%pytest

%files %{python_files}
%doc Changes README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/vba_extract.py
%{python_sitelib}/xlsxwriter
%{python_sitelib}/[Xx]lsx[Ww]riter-%{version}*-info

%changelog
