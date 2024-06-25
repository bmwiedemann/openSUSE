#
# spec file for package tree-sitter-vimdoc
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


%define         _name vimdoc
Name:           tree-sitter-%{_name}
Version:        2.5.1
Release:        0
Summary:        Tree-sitter parser for Vim help files
License:        Apache-2.0
URL:            https://github.com/neovim/tree-sitter-vimdoc
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  tree-sitter
%treesitter_grammars %{_name}

%description
This grammar implements the vimdoc "spec". Predictable results are the primary
goal, so that output formats (e.g. HTML) are well-formed; the input (vimdoc) is
secondary. The first step should always be to try to fix the input rather than
insist on a grammar that handles vimdoc's endless quirks.

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
%doc README.md
%{treesitter_files}
%treesitter_devel_package

%changelog
