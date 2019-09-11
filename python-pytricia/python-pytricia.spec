#
# spec file for package python-pytricia
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytricia
Version:        1.0.0
Release:        0
Summary:        A library for IP address lookup in Python
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Url:            https://github.com/jsommers/pytricia
Source:         https://files.pythonhosted.org/packages/source/p/pytricia/pytricia-%{version}.tar.gz
# https://github.com/jsommers/pytricia/issues/25
Source1:        https://raw.githubusercontent.com/jsommers/pytricia/master/COPYING.LESSER
# shorthened https://raw.githubusercontent.com/jsommers/pytricia/master/test.py
# see https://github.com/jsommers/pytricia/issues/26
Source2:        test.py
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Pytricia is a python module to store IP prefixes in a patricia tree.
It's based on Dave Plonka's modified patricia tree code, and has three things
to recommend it over related modules (including py-radix and SubnetTree).

%prep
%setup -q -n pytricia-%{version}
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -m unittest discover

%files %{python_files}
%license COPYING.LESSER
%doc README.md
%{python_sitearch}/*

%changelog
