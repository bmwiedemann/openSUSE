#
# spec file for package python-gast
#
# Copyright (c) 2024 SUSE LLC
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
%define srcname gast
Name:           python-gast
# only update when python-pythran is compatible
Version:        0.5.4
Release:        0
Summary:        Python AST that abstracts the underlying Python version
License:        BSD-3-Clause
URL:            https://github.com/serge-sans-paille/gast/
Source:         https://github.com/serge-sans-paille/gast/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description

A generic AST to represent Python2 and Python3's Abstract Syntax Tree(AST).

GAST provides a compatibility layer between the AST of various Python versions,
as produced by ``ast.parse`` from the standard ``ast`` module.

%prep
%autosetup -p1 -n gast-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v tests

%files %{python_files}
%{python_sitelib}/gast
%{python_sitelib}/gast-%{version}*-info
%doc README.rst
%license LICENSE

%changelog
