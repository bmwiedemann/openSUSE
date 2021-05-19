#
# spec file for package python-clint
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
%bcond_without test
Name:           python-clint
Version:        0.5.1
Release:        0
Summary:        Python Command Line Interface Tools
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/kennethreitz/clint
# pypi release misses docs and tests
Source:         https://github.com/kennethreitz/clint/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module args}
BuildRequires:  %{python_module pytest}
%endif
Requires:       python-args
BuildArch:      noarch

%python_subpackages

%description
Clint is a module filled with a set of tools for developing
commandline applications. It supports colors, and custom email-style
quotes. It has a nestable indentation context manager, and a column
printer with optional auto-expanding columns with autodetection of
console size, wrapping your words properly to fit the column size.

%prep
%setup -q -n clint-%{version}

%build
sed -i '1s/^#!.*//' examples/*.py clint/packages/appdirs.py examples/unicode.sh
%python_build

%install
%python_install

%if %{with test}
%check
export LANG=en_US.utf8
%pytest
%endif

%files %{python_files}
%doc AUTHORS HISTORY.rst README.rst docs examples
%%license LICENSE
%{python_sitelib}/*

%changelog
