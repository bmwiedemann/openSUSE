#
# spec file for package python-lark
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-lark
Version:        1.1.4
Release:        0
Summary:        A parsing library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/lark-parser/lark
Source:         https://github.com/lark-parser/lark/archive/%{version}.tar.gz#/lark-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-regex
Suggests:       python-Js2Py
Suggests:       python-atomicwrites
# SECTION TEST
BuildRequires:  %{python_module regex}
BuildRequires:  %{python_module Js2Py}
BuildRequires:  %{python_module pytest >= 6}
# /SECTION
BuildArch:      noarch
# Upstream renamed the package with v0.12.0, SUSE had the old name until 1.1.2
Provides:       python-lark-parser = %{version}-%{release}
Obsoletes:      python-lark-parser <= 1.1.2
%python_subpackages

%description
Lark is a general-purpose parsing library for Python.

With Lark, one can parse any context-free grammar with little code.

%prep
%setup -q -n lark-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md docs/*
%{python_sitelib}/lark
%{python_sitelib}/lark-%{version}*-info

%changelog
