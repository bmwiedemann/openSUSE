#
# spec file for package python-oletools
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
Name:           python-oletools
Version:        0.56.2
Release:        0
Summary:        Tools to analyze security characteristics of MS Office and OLE files
License:        BSD-2-Clause AND MIT
URL:            http://www.decalage.info/python/oletools
Source:         https://files.pythonhosted.org/packages/source/o/oletools/oletools-%{version}.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module colorclass}
BuildRequires:  %{python_module easygui}
BuildRequires:  %{python_module msoffcrypto-tool}
BuildRequires:  %{python_module olefile >= 0.46}
BuildRequires:  %{python_module pyparsing >= 2.1.0}
BuildRequires:  %{python_module pytest-runner}
# /SECTION
BuildRequires:  unzip
BuildRequires:  fdupes
Requires:       python-colorclass
Requires:       python-easygui
Requires:       python-msoffcrypto-tool
Requires:       python-olefile >= 0.46
Recommends:     python-pcodedmp >= 1.2.5
Requires:       python-pyparsing >= 2.1.0
BuildArch:      noarch
%python_subpackages

%description
Python tools to analyze security characteristics of MS Office and OLE files (also called Structured Storage, Compound File Binary Format or Compound Document File Format), for Malware Analysis and Incident Response (DFIR)

%prep
%setup -q -n oletools-%{version}
find oletools -name "*.py" -exec sed -i '1{/\/bin\/env python/d;}' {} \+
find oletools -name "*.py" -exec sed -i 's/\r\n/\n/' {} \+

%build
%python_build

%install
%python_install
# remove actually optional dependency from requires
sed -i '1{/pcodedmp/d;}' %{buildroot}%{python_sitelib}/oletools-*.egg-info/requires.txt
%python_clone -a %{buildroot}%{_bindir}/ezhexviewer
%python_clone -a %{buildroot}%{_bindir}/mraptor
%python_clone -a %{buildroot}%{_bindir}/mraptor3
%python_clone -a %{buildroot}%{_bindir}/olebrowse
%python_clone -a %{buildroot}%{_bindir}/oledir
%python_clone -a %{buildroot}%{_bindir}/oleid
%python_clone -a %{buildroot}%{_bindir}/olemap
%python_clone -a %{buildroot}%{_bindir}/olemeta
%python_clone -a %{buildroot}%{_bindir}/oletimes
%python_clone -a %{buildroot}%{_bindir}/olevba
%python_clone -a %{buildroot}%{_bindir}/olevba3
%python_clone -a %{buildroot}%{_bindir}/pyxswf
%python_clone -a %{buildroot}%{_bindir}/rtfobj
%python_clone -a %{buildroot}%{_bindir}/oleobj
%python_clone -a %{buildroot}%{_bindir}/msodde
%python_clone -a %{buildroot}%{_bindir}/olefile
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_rough_doctype and not test_encrypted and not test_crypt_return'

%post
%python_install_alternative ezhexviewer mraptor mraptor3 olebrowse oledir oleid olemap olemeta oletimes olevba olevba3 pyxswf rtfobj oleobj msodde olefile

%postun
%python_uninstall_alternative ezhexviewer

%files %{python_files}
%doc README.md
%license oletools/LICENSE.txt
%python_alternative %{_bindir}/ezhexviewer
%python_alternative %{_bindir}/mraptor
%python_alternative %{_bindir}/mraptor3
%python_alternative %{_bindir}/olebrowse
%python_alternative %{_bindir}/oledir
%python_alternative %{_bindir}/oleid
%python_alternative %{_bindir}/olemap
%python_alternative %{_bindir}/olemeta
%python_alternative %{_bindir}/oletimes
%python_alternative %{_bindir}/olevba
%python_alternative %{_bindir}/olevba3
%python_alternative %{_bindir}/pyxswf
%python_alternative %{_bindir}/rtfobj
%python_alternative %{_bindir}/oleobj
%python_alternative %{_bindir}/msodde
%python_alternative %{_bindir}/olefile
%{python_sitelib}/*

%changelog
