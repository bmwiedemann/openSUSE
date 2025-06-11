#
# spec file for package python-phply
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


%bcond_without libalternatives
Name:           python-phply
Version:        1.2.6
Release:        0
Summary:        Lexer and parser for PHP source implemented using PLY
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/viraptor/phply
Source:         https://files.pythonhosted.org/packages/source/p/phply/phply-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module ply}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-ply
BuildArch:      noarch
%python_subpackages

%description
phply is a parser for the PHP programming language written using PLY, a Lex/YACC-style parser generator toolkit for Python.

%prep
%autosetup -p1 -n phply-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/phpparse
%python_clone -a %{buildroot}%{_bindir}/phplex
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests

%check
%pytest

%pre
%python_libalternatives_reset_alternative phpparse
%python_libalternatives_reset_alternative phplex

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/phplex
%python_alternative %{_bindir}/phpparse
%{python_sitelib}/phply
%{python_sitelib}/phply-%{version}*-info
%{python_sitelib}/phply-%{version}*nspkg.pth

%changelog
