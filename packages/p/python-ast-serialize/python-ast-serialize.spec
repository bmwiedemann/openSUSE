#
# spec file for package python-ast-serialize
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


Name:           python-ast-serialize
Version:        0.5.0
Release:        0
Summary:        Python bindings for mypy AST serialization
License:        MIT
URL:            https://github.com/mypyc/ast_serialize
Source:         https://files.pythonhosted.org/packages/source/a/ast-serialize/ast_serialize-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module maturin >= 1.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ast-serialize
%python_subpackages

%description
This is a fast Python extension for parsing Python files and serializing the
AST using the native binary format used by mypy. This will eventually replace
the current mypy parser, which uses the Python stdlib ``ast`` module for
parsing.

%prep
%autosetup -p1 -n ast_serialize-%{version} -a1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest_arch test_ast_serialize.py

%files %{python_files}
%license LICENSE
%{python_sitearch}/ast_serialize
%{python_sitearch}/ast_serialize-%{version}.dist-info

%changelog
