#
# spec file for package tree-sitter-luau
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


%define         _name luau
Name:           tree-sitter-luau
Version:        1.2.0
Release:        0
Summary:        Luau grammar for tree-sitter
License:        MIT
URL:            https://github.com/tree-sitter-grammars/tree-sitter-luau
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE require-correct-lua.patch mcepl@suse.com
# Use the openSUSE-installed module path (tree-sitter-lua) instead of
# the npm scoped package name (@muniftanjim/tree-sitter-lua), and
# handle ESM default export from tree-sitter-lua grammar
Patch0:         require-correct-lua.patch
BuildRequires:  tree-sitter
BuildRequires:  treesitter_grammar_src(tree-sitter-lua)
%treesitter_grammars %{_name}

%description
%{summary}.

%prep
%autosetup -p1

%build
%treesitter_configure
%treesitter_build

%install
%treesitter_install
%treesitter_devel_install

%files
%license LICENSE
%treesitter_files

%treesitter_devel_package

%changelog
