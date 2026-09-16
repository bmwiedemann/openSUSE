#
# spec file for package tree-sitter-nix
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


%define         _name nix
Name:           tree-sitter-nix
Version:        0.3.0
Release:        0
Summary:        Nix grammar for tree-sitter
License:        MIT
URL:            https://github.com/nix-community/tree-sitter-nix
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  lld
BuildRequires:  tree-sitter
BuildRequires:  wasi-libc
%treesitter_grammars %{_name}

%description
The tree-sitter grammar for the Nix language, as a shared library, a
WebAssembly module and the grammar's own queries.

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
