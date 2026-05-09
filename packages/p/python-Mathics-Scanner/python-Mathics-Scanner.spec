#
# spec file for package python-Mathics-Scanner
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


%define modname mathics3_scanner
Name:           python-Mathics-Scanner
Version:        10.0.0
Release:        0
Summary:        Character Tables and Tokenizer for Mathics and the Wolfram Language
License:        GPL-3.0-only
URL:            https://mathics.org/
Source0:        https://files.pythonhosted.org/packages/source/M/Mathics3-Scanner/%{modname}-%{version}.tar.gz
# Manually include missed file
Source1:        https://raw.githubusercontent.com/Mathics3/Mathics3-scanner/refs/tags/10.0.0/mathics_scanner/data/grouping-characters.yml
BuildRequires:  %{python_module base >= 3.10}
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
Provides:       python-Mathics3-Scanner = %{version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-ujson
BuildArch:      noarch
%python_subpackages

%description
Character Tables and Tokenizer for Mathics and the Wolfram Language.

%prep
%autosetup -n %{modname}-%{version}
cp %{SOURCE1} ./mathics_scanner/data/
chmod -x ./mathics_scanner/generate/*.py
sed -Ei "1{\@^#!/usr/bin/env@d}" ./mathics_scanner/generate/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mathics3-codeparser-tokenize
%python_clone -a %{buildroot}%{_bindir}/mathics3-make-boxing-character-json
%python_clone -a %{buildroot}%{_bindir}/mathics3-make-named-character-json
%python_clone -a %{buildroot}%{_bindir}/mathics3-make-operator-json
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative mathics3-codeparser-tokenize
%python_install_alternative mathics3-make-boxing-character-json
%python_install_alternative mathics3-make-named-character-json
%python_install_alternative mathics3-make-operator-json

%postun
%python_uninstall_alternative mathics3-codeparser-tokenize
%python_uninstall_alternative mathics3-make-boxing-character-json
%python_uninstall_alternative mathics3-make-named-character-json
%python_uninstall_alternative mathics3-make-operator-json

%files %{python_files}
%python_alternative %{_bindir}/mathics3-codeparser-tokenize
%python_alternative %{_bindir}/mathics3-make-boxing-character-json
%python_alternative %{_bindir}/mathics3-make-named-character-json
%python_alternative %{_bindir}/mathics3-make-operator-json
%{python_sitelib}/mathics_scanner/
%{python_sitelib}/%{modname}-%{version}*.*-info/

%changelog
