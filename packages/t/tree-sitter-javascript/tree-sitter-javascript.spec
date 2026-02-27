#
# spec file for package tree-sitter-javascript
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


%define         _name javascript
%define         python_subpackage_only 1
%define         python_libname tree_sitter_javascript
%{?sle15_python_module_pythons}
Name:           tree-sitter-javascript
Version:        0.23.1
Release:        0
Summary:        Javascript grammar for tree-sitter
License:        MIT
URL:            https://github.com/tree-sitter/tree-sitter-javascript
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       tree-sitter-javascript-rpmlintrc
BuildRequires:  tree-sitter
%treesitter_grammars %{_name}

%description
%{summary}.

%package -n python-tree-sitter-javascript
Summary:        Python bindings for JavaScript TS grammar
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
%python_subpackages

%description -n python-tree-sitter-javascript
Python bindings for the JavaScript grammar for tree-sitter.

%prep
%autosetup -p1

%build
%treesitter_configure
%treesitter_build
%pyproject_wheel

%install
%treesitter_install
%treesitter_devel_install
%pyproject_install


%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files
%license LICENSE
%treesitter_files

%treesitter_devel_package

%files %{python_files %{name}}
%dir %{python_sitearch}/%{python_libname}
%dir %{python_sitearch}/%{python_libname}/queries
%pycache_only %{python_sitearch}/%{python_libname}/__pycache__
%{python_sitearch}/%{python_libname}/__init__.py
%{python_sitearch}/%{python_libname}/__init__.pyi
%{python_sitearch}/%{python_libname}/_binding.abi3.so
%{python_sitearch}/%{python_libname}/binding.c
%{python_sitearch}/%{python_libname}/py.typed
%{python_sitearch}/%{python_libname}/queries/*.scm
%{python_sitearch}/%{python_libname}-%{version}.dist-info

%changelog
