#
# spec file for package python-phply
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-phply
Version:        1.2.6
Release:        0
Summary:        Lexer and parser for PHP source implemented using PLY
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/viraptor/phply
Source:         https://files.pythonhosted.org/packages/source/p/phply/phply-%{version}.tar.gz
BuildRequires:  %{python_module ply}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ply
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
phply is a parser for the PHP programming language written using PLY, a Lex/YACC-style parser generator toolkit for Python.

%prep
%autosetup -p1 -n phply-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/phpparse
%python_clone -a %{buildroot}%{_bindir}/phplex
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests

%check
%pytest

%post
%python_install_alternative phpparse
%python_install_alternative phplex

%postun
%python_uninstall_alternative phpparse
%python_uninstall_alternative phplex

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/phplex
%python_alternative %{_bindir}/phpparse
%{python_sitelib}/*

%changelog
