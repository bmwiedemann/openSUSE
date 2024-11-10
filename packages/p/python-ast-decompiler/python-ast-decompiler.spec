#
# spec file for package python-ast_decompiler
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


Name:           python-ast-decompiler
Version:        0.8.0
Release:        0
Summary:        Python module to decompile AST to Python code
License:        Apache-2.0
URL:            https://github.com/JelleZijlstra/ast_decompiler
Source:         https://files.pythonhosted.org/packages/source/a/ast-decompiler/ast_decompiler-%{version}.tar.gz
# PATCH-FIX-UPSTREAM no-relative-imports.patch gh#JelleZijlstra/ast_decompiler#52 mcepl@suse.com
# Fix erroring tests
Patch0:         no-relative-imports.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Python module to decompile AST to Python code

%prep
%autosetup -p1 -n ast_decompiler-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/

%files %{python_files}
%{python_sitelib}/ast_decompiler
%{python_sitelib}/ast_decompiler-%{version}*-info

%changelog
