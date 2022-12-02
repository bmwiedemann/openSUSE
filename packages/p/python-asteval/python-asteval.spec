#
# spec file for package python-asteval
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-asteval
Version:        0.9.28
Release:        0
Summary:        Safe, minimalistic evaluator of python expression using ast module
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/newville/asteval
Source:         https://files.pythonhosted.org/packages/source/a/asteval/asteval-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
# /SECTION
%python_subpackages

%description
ASTEVAL provides a numpy-aware, safe(ish) 'eval' function

Emphasis is on mathematical expressions, and so numpy ufuncs
are used if available.  Symbols are held in the Interpreter
symbol table 'symtable':  a simple dictionary supporting a
simple, flat namespace.

Expressions can be compiled into ast node for later evaluation,
using the values in the symbol table current at evaluation time.

%prep
%setup -q -n asteval-%{version}
sed -i -e '/^#!\//, 1d' asteval/asteval.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
