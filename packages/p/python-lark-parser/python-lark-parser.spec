#
# spec file for package python-lark-parser
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-lark-parser
Version:        0.9.0
Release:        0
Summary:        A parsing library for Python
License:        MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/lark-parser
Source:         https://github.com/lark-parser/lark/archive/%{version}.tar.gz#/lark-%{version}.tar.gz
# extracted test gramars from nearley -> https://github.com/kach/nearley
Source1:        testdata.tar.gz
BuildRequires:  %{python_module Js2Py >= 0.68}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-regex
Suggests:       python-Js2Py >= 0.68
BuildArch:      noarch
%python_subpackages

%description
Lark is a general-purpose parsing library for Python.

With Lark, one can parse any context-free grammar with little code.

%prep
%setup -q -n lark-%{version} -a1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.md docs/*
%{python_sitelib}/*

%changelog
