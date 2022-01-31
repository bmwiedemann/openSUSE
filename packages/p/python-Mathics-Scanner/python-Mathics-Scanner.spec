#
# spec file for package python-Mathics-Scanner
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
%define skip_python2 1
Name:           python-Mathics-Scanner
Version:        1.2.4
Release:        0
Summary:        Character Tables and Tokenizer for Mathics and the Wolfram Language
License:        GPL-3.0-only
URL:            https://mathics.org/
Source:         https://files.pythonhosted.org/packages/source/M/Mathics-Scanner/Mathics_Scanner-%{version}.tar.gz
Patch0:         https://github.com/Mathics3/mathics-scanner/commit/9346764dfd22f011ec7bba9248497383f4b98a3a.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module PyYAML}
# /SECTION
BuildRequires:  fdupes
Requires:       python-chardet
Requires:       python-click
Requires:       python-PyYAML
Recommends:     python-ujson
BuildArch:      noarch
%python_subpackages

%description
Character Tables and Tokenizer for Mathics and the Wolfram Language.

%prep
%setup -q -n Mathics_Scanner-%{version}
%patch0 -p1
# Fix shbang
sed -i "s|/usr/bin/env python|/usr/bin/python|" mathics_scanner/generate/{build_tables,rl_inputrc}.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/mathics-generate-json-table
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# Should be executable
%python_expand chmod 0755 %{buildroot}%{$python_sitelib}/mathics_scanner/generate/{build_tables,rl_inputrc}.py

%check
%pytest

%post
%python_install_alternative mathics-generate-json-table

%postun
%python_uninstall_alternative mathics-generate-json-table

%files %{python_files}
%python_alternative %{_bindir}/mathics-generate-json-table
%{python_sitelib}/*

%changelog
