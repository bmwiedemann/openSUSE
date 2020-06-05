#
# spec file for package python-pyparsing
#
# Copyright (c) 2020 SUSE LLC
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


%define modname pyparsing
%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%bcond_without python2
Name:           python-pyparsing%{psuffix}
Version:        2.4.7
Release:        0
Summary:        Grammar Parser Library for Python
License:        MIT AND GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://github.com/pyparsing/pyparsing/
Source:         https://files.pythonhosted.org/packages/source/p/pyparsing/pyparsing-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
%ifpython2
Provides:       %{oldpython}-parsing = %{version}
Obsoletes:      %{oldpython}-parsing < %{version}
%endif
%python_subpackages

%description
The pyparsing module is an alternative approach to creating and executing
simple grammars, vs. the traditional lex/yacc approach, or the use of regular
expressions. The pyparsing module provides a library of classes that client
code uses to construct the grammar directly in Python code.

%prep
%setup -q -n %{modname}-%{version}
# do not require setuptools
# https://github.com/pyparsing/pyparsing/pull/133
sed -i -e 's:from setuptools :from distutils.core :g' setup.py

%build
%python_build

%install
%if ! %{with test}
%python_install
# ensure egg-info is a directory
%{python_expand rm -rf %{buildroot}%{$python_sitelib}/*.egg-info
cp -r pyparsing.egg-info %{buildroot}%{$python_sitelib}/pyparsing-%{version}-py%{$python_version}.egg-info
}
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if ! %{with test}
%files %{python_files}
%license LICENSE
%doc CHANGES README.rst
%{python_sitelib}/pyparsing.py*
%pycache_only %{python_sitelib}/__pycache__/*
%{python_sitelib}/pyparsing-%{version}-py*.egg-info/
%endif

%changelog
