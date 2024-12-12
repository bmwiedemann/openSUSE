#
# spec file for package tree-sitter-typescript
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


%define         _name typescript
Name:           tree-sitter-typescript
Version:        0.23.2
Release:        0
Summary:        Typescript grammar for tree-sitter
License:        MIT
URL:            https://github.com/tree-sitter/tree-sitter-typescript
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  tree-sitter
BuildRequires:  treesitter_grammar_src(tree-sitter-javascript)
%treesitter_grammars %{_name} tsx

%description
%{summary}.

%prep
%autosetup

%build
%treesitter_configure
%treesitter_build

%install
%treesitter_install
%treesitter_devel_install common/define-grammar.js

#neovim stuff
install -d %{buildroot}%{_libdir}/tree_sitter
ln -s %{_libdir}/lib%{name}.so %{buildroot}%{_libdir}/tree_sitter/%{_name}.so
ln -s %{_libdir}/libtree-sitter-tsx.so %{buildroot}%{_libdir}/tree_sitter/tsx.so

%files
%license LICENSE
%treesitter_files
%{_libdir}/tree_sitter/%{_name}.so
%{_libdir}/tree_sitter/tsx.so
%if 0%{?suse_version} < 1600
%dir %{_libdir}/tree_sitter
%endif

%treesitter_devel_package

%changelog
