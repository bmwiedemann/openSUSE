#
# spec file for package python-license-expression
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-license-expression
Version:        30.1.0
Release:        0
Summary:        Library to parse, compare, simplify and normalize license expressions
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/nexB/license-expression
Source:         https://files.pythonhosted.org/packages/source/l/license-expression/license-expression-%{version}.tar.gz
BuildRequires:  %{python_module boolean.py >= 4.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-boolean.py >= 4.0
BuildArch:      noarch
%python_subpackages

%description
This module defines a mini language to parse, validate, simplify, normalize and
compare license expressions using a boolean logic engine.

This supports SPDX license expressions and also accepts other license naming
conventions and license identifiers aliases to resolve and normalize licenses.

Using boolean logic, license expressions can be tested for equality,
containment, equivalence and can be normalized or simplified.

%prep
%setup -q -n license-expression-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%license apache-2.0.LICENSE NOTICE
%doc README.rst
%{python_sitelib}/license[_-]expression*

%changelog
