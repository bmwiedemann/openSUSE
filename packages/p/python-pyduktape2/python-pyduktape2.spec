#
# spec file for package python-pyduktape2
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-pyduktape2
Version:        0.5.0
Release:        0
License:        GPL-2.0-only
Summary:        Python integration for the Duktape Javascript interpreter
URL:            https://github.com/phith0n/pyduktape2
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pyduktape2/pyduktape2-%{version}.tar.gz
Patch0:         pyduktape2-add_pyduktape2_pyx.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 18.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Cython}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Cython

%python_subpackages

%description
Python integration for the Duktape Javascript interpreter

%prep
%autosetup -p1 -n pyduktape2-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc README.rst
%{python_sitearch}/*

%changelog
