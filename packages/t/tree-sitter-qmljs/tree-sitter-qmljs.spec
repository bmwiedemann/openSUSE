#
# spec file for package tree-sitter-qmljs
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


%define         _name qmljs
Name:           tree-sitter-qmljs
Version:        0.2.0
Release:        0
Summary:        QML grammar for tree-sitter
License:        MIT
URL:            https://github.com/yuja/tree-sitter-qmljs
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  tree-sitter
BuildRequires:  treesitter_grammar_src(tree-sitter-typescript)
%treesitter_grammars %{_name}

%description
%{summary}.

%prep
%autosetup

%build
%treesitter_configure
%treesitter_build

%install
%treesitter_install

%files
%license LICENSE
%treesitter_files

%changelog
