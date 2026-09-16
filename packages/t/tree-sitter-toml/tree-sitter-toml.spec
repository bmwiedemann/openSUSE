#
# spec file for package tree-sitter-toml
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


%define         _name toml
Name:           tree-sitter-toml
Version:        0.7.0
Release:        0
Summary:        TOML grammar for tree-sitter
License:        MIT
URL:            https://github.com/tree-sitter-grammars/tree-sitter-toml
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  clang
BuildRequires:  lld
BuildRequires:  tree-sitter
BuildRequires:  wasi-libc
%treesitter_grammars %{_name}

%description
%{summary}.

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
%treesitter_files

%treesitter_wasm_package

%treesitter_queries_package
%treesitter_devel_package

%changelog
