#
# spec file for package python-typed-ast
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


%{?sle15_python_module_pythons}
Name:           python-typed-ast
Version:        1.5.4
Release:        0
Summary:        A fork of Python 2 and 3 ast modules with type comment support
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/python/typed_ast
Source0:        https://files.pythonhosted.org/packages/source/t/typed_ast/typed_ast-%{version}.tar.gz
# PATCH-FIX-UPSTREAM use-PyUnicode_DecodeUnicodeEscape.patch gh#python/typed_ast#172 mcepl@suse.com
# Use PyUnicode_DecodeUnicodeEscape directly
Patch0:         use-PyUnicode_DecodeUnicodeEscape.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
typed_ast is a Python 3 package that provides a Python 2.7 and Python 3
parser similar to the standard ast library. Unlike ast, the parsers in
typed_ast include PEP 484 type comments and are independent of the version of
Python under which they are run. The typed_ast parsers produce the standard
Python AST (plus type comments), and are both fast and correct, as they are
based on the CPython 2.7 and 3.6 parsers.

%prep
%setup -q -n typed_ast-%{version}
%autopatch -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/*

%changelog
