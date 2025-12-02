#
# spec file for package python-lark
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-lark
Version:        1.3.1
Release:        0
Summary:        A parsing library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/lark-parser/lark
Source:         https://github.com/lark-parser/lark/archive/%{version}.tar.gz#/lark-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  %{python_module regex}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-Js2Py
Suggests:       python-atomicwrites
Suggests:       python-regex
# Upstream renamed the package with v0.12.0, SUSE had the old name until 1.1.2
Provides:       python-lark-parser = %{version}-%{release}
Obsoletes:      python-lark-parser <= 1.1.2
BuildArch:      noarch
%python_subpackages

%description
Lark is a general-purpose parsing library for Python.

With Lark, one can parse any context-free grammar with little code.

%prep
%autosetup -p1 -n lark-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md docs/*
%{python_sitelib}/lark
%{python_sitelib}/lark-%{version}*-info

%changelog
