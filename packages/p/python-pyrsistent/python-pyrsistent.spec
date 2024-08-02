#
# spec file for package python-pyrsistent
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-pyrsistent
Version:        0.20.0
Release:        0
Summary:        Persistent, Functional, Immutable data structures
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/tobgu/pyrsistent/
Source:         https://files.pythonhosted.org/packages/source/p/pyrsistent/pyrsistent-%{version}.tar.gz
# PATCH-FIX-UPSTREAM - gh/tobgu/pyrsistent#284 - Replace _PyList_Extend with PyList_SetSlice
Patch:          https://patch-diff.githubusercontent.com/raw/tobgu/pyrsistent/pull/284.patch#/replace-private-function.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Pyrsistent is a number of persistent collections
(by some referred to as functional data structures).
Persistent in  the sense that they are immutable.

All methods on a data structure that would normally
mutate it instead return a new copy of the structure
containing the requested updates. The original structure
is left untouched.

%prep
%setup -q -n pyrsistent-%{version}
%patch -P0 -p1

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch -ra

%files %{python_files}
%license LICENSE.mit
%doc CHANGES.txt README.rst
%pycache_only %{python_sitearch}/__pycache__/_pyrsistent*
%{python_sitearch}/_pyrsistent*
%{python_sitearch}/pvectorc*
%{python_sitearch}/pyrsistent
%{python_sitearch}/pyrsistent-%{version}.dist-info

%changelog
