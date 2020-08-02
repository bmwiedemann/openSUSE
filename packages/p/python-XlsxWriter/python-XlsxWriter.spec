#
# spec file for package python-XlsxWriter
#
# Copyright (c) 2020 SUSE LLC
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
%define         oldpython python
Name:           python-XlsxWriter
Version:        1.2.9
Release:        0
Summary:        Python module for writing OOXML spreadsheet files
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jmcnamara/XlsxWriter
Source:         https://github.com/jmcnamara/XlsxWriter/archive/RELEASE_%{version}.tar.gz#/XlsxWriter-RELEASE_%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
# python-xlsxwriter was last used in openSUSE Leap 42.1.
Provides:       %{oldpython}-xlsxwriter = %{version}
Obsoletes:      %{oldpython}-xlsxwriter < %{version}
%endif
%ifpython3
# python3-xlsxwriter was last used in openSUSE Leap 42.1.
Provides:       python3-xlsxwriter = %{version}
Obsoletes:      python3-xlsxwriter < %{version}
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
%python_build

%install
%{python_expand %$python_install && \
  mv %{buildroot}%{_bindir}/vba_extract.py \
   %{buildroot}%{_bindir}/vba_extract-%$python_bin_suffix}

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%prepare_alternative vba_extract

%post
%python_install_alternative vba_extract

%postun
%python_uninstall_alternative vba_extract

%check
%pytest

%files %{python_files}
%doc Changes README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/vba_extract
%{python_sitelib}/xlsxwriter/
%{python_sitelib}/XlsxWriter-%{version}-py*.egg-info

%changelog
