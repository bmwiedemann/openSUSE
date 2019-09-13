#
# spec file for package python-gast
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define srcname gast
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-gast
Version:        0.3.0
Release:        0
Summary:        Python AST that abstracts the underlying Python version
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/serge-sans-paille/gast/
Source:         https://github.com/serge-sans-paille/gast/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module astunparse}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description

A generic AST to represent Python2 and Python3's Abstract Syntax Tree(AST).

GAST provides a compatibility layer between the AST of various Python versions,
as produced by ``ast.parse`` from the standard ``ast`` module.

%prep
%setup -q -n gast-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%{python_sitelib}/*
%doc README.rst
%license LICENSE

%changelog
