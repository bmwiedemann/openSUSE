#
# spec file for package python-tree-sitter
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-tree-sitter
Version:        0.24.0
Release:        0
Summary:        Python bindings to the Tree-sitter parsing library
License:        MIT
URL:            https://github.com/tree-sitter/py-tree-sitter
Source:         https://files.pythonhosted.org/packages/source/t/tree-sitter/tree-sitter-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 43}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This module provides Python bindings to the tree-sitter parsing library.

%prep
%autosetup -p1 -n tree-sitter-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# test suite is not included in the distribution tarball,
# and it is not possible to build easily from GitHub checkout tarball
:

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/tree_sitter
%{python_sitearch}/tree_sitter-%{version}.dist-info

%changelog
