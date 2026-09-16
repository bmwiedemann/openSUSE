#
# spec file for package tree-sitter-ocaml
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


%define python_subpackage_only 1
%define         _name ocaml
Name:           tree-sitter-ocaml
Version:        0.26.0
Release:        0
Summary:        OCaml grammars for tree-sitter
License:        MIT
URL:            https://github.com/tree-sitter/tree-sitter-ocaml
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  clang
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  lld
BuildRequires:  python-rpm-macros
BuildRequires:  tree-sitter
BuildRequires:  wasi-libc
%treesitter_grammars %{_name}=grammars/%{_name} %{_name}_interface=grammars/interface %{_name}_type=grammars/type
%python_subpackages

%description
The tree-sitter grammars for OCaml implementations (ocaml), interfaces
(ocaml_interface) and type expressions (ocaml_type), as shared
libraries, WebAssembly modules and the grammars' own queries.

%package -n python-%{name}
Summary:        Python binding for the %{name} grammar
Requires:       %{name} = %{version}-%{release}
Suggests:       python-tree-sitter >= 0.24

%description -n python-%{name}
The tree_sitter_* Python module for the %{name} grammar, loadable
with the Language()/Parser() API from python-tree-sitter.

%prep
%autosetup

%build
%treesitter_configure
%treesitter_build
%treesitter_wasm_build

%install
%treesitter_install
%treesitter_wasm_install
%treesitter_queries_install
%treesitter_devel_install
%treesitter_python_install ocaml ocaml ocaml_interface ocaml_type

%files
%license LICENSE
%doc README.md
%treesitter_files

%treesitter_wasm_package

%treesitter_queries_package

%treesitter_devel_package

%files %{python_files %{name}}
%license LICENSE
%{python_sitearch}/tree_sitter_*

%changelog
