#
# spec file for package python-pytricia
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
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-pytricia
Version:        1.0.2
Release:        0
Summary:        A library for IP address lookup in Python
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/jsommers/pytricia
Source:         https://files.pythonhosted.org/packages/source/p/pytricia/pytricia-%{version}.tar.gz
# https://github.com/jsommers/pytricia/issues/25
Source2:        https://raw.githubusercontent.com/jsommers/pytricia/master/test.py
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Pytricia is a python module to store IP prefixes in a patricia tree.
It's based on Dave Plonka's modified patricia tree code, and has three things
to recommend it over related modules (including py-radix and SubnetTree).

%prep
%setup -q -n pytricia-%{version}
cp %{SOURCE2} .

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install

%check
%pytest_arch test.py

%files %{python_files}
%license COPYING.LESSER
%doc README.md
%{python_sitearch}/*

%changelog
