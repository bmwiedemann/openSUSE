#
# spec file for package python-pcodedmp
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
Name:           python-pcodedmp
Version:        1.2.6
Release:        0
Summary:        A VBA p-code disassembler
License:        GPL-3.0-only
URL:            https://github.com/bontchev/pcodedmp
Source:         https://files.pythonhosted.org/packages/source/p/pcodedmp/pcodedmp-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module oletools >= 0.54}
# /SECTION
BuildRequires:  fdupes
Requires:       python-oletools >= 0.54
Suggests:       python-win_unicode_console
BuildArch:      noarch
%python_subpackages

%description
Disassembler for p-code of VBA code in OLE2 documents.

It supports VBA5 (Office 97, MacOffice 98), VBA6 (Office 2000 to
Office 2009) and VBA7 (Office 2010 and higher).

%prep
%setup -q -n pcodedmp-%{version}
sed -i '1{/\/bin\/env python/d;}' pcodedmp/pcodedmp.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pcodedmp
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pcodedmp

%postun
%python_uninstall_alternative pcodedmp

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pcodedmp
%{python_sitelib}/*

%changelog
