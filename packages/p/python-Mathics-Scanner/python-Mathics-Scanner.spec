#
# spec file for package python-Mathics-Scanner
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


%define skip_python2 1
%define modname mathics_scanner
Name:           python-Mathics-Scanner
Version:        1.4.1
Release:        0
Summary:        Character Tables and Tokenizer for Mathics and the Wolfram Language
License:        GPL-3.0-only
URL:            https://mathics.org/
Source:         https://files.pythonhosted.org/packages/source/M/Mathics-Scanner/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyYAML
Requires:       python-chardet
Requires:       python-click
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-ujson
BuildArch:      noarch
%python_subpackages

%description
Character Tables and Tokenizer for Mathics and the Wolfram Language.

%prep
%setup -q -n %{modname}-%{version}
# Fix shbang
sed -i "s|/usr/bin/env python|/usr/bin/python3|" mathics_scanner/generate/build_{,operator_}tables.py
sed -i "s|/usr/bin/env python3|/usr/bin/python3|" mathics_scanner/generate/rl_inputrc.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mathics3-generate-json-table
%python_clone -a %{buildroot}%{_bindir}/mathics3-generate-operator-json-table
%python_clone -a %{buildroot}%{_bindir}/mathics3-tokens
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# Should be executable
%python_expand chmod 0755 %{buildroot}%{$python_sitelib}/mathics_scanner/generate/{build_tables,build_operator_tables,rl_inputrc}.py

%check
%pytest

%post
%python_install_alternative mathics3-generate-json-table
%python_install_alternative mathics3-generate-operator-json-table
%python_install_alternative mathics3-tokens

%postun
%python_uninstall_alternative mathics3-generate-json-table
%python_uninstall_alternative mathics3-generate-operator-json-table
%python_uninstall_alternative mathics3-tokens

%files %{python_files}
%python_alternative %{_bindir}/mathics3-generate-json-table
%python_alternative %{_bindir}/mathics3-generate-operator-json-table
%python_alternative %{_bindir}/mathics3-tokens
%{python_sitelib}/%{modname}/
%{python_sitelib}/Mathics_Scanner-%{version}*.*-info/

%changelog
