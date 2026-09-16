#
# spec file for package tree-sitter-fsharp
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


%define         _name fsharp
Name:           tree-sitter-fsharp
Version:        0.3.12
Release:        0
Summary:        F# grammars for tree-sitter
License:        MIT
URL:            https://github.com/ionide/tree-sitter-fsharp
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  lld
BuildRequires:  tree-sitter
BuildRequires:  wasi-libc
%treesitter_grammars %{_name} %{_name}_signature
# No Python subpackage: upstream's binding exports language() and
# language_signature(), which %%treesitter_python_install cannot emit.

%description
The tree-sitter grammars for F# implementation files (fsharp) and
signature files (fsharp_signature), as shared libraries, WebAssembly
modules and the grammars' own queries.

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

%files
%license LICENSE
%doc README.md
%treesitter_files

%treesitter_wasm_package

%treesitter_queries_package

%treesitter_devel_package

%changelog
