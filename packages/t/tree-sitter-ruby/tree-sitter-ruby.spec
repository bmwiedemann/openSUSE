#
# spec file for package tree-sitter-ruby
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


%define _name ruby
Summary:        Ruby grammar for tree-sitter
Name:           tree-sitter-%{_name}
Version:        0.20.1
Release:        0
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/tree-sitter/tree-sitter-ruby
Source0:        %{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 0001-fix-escape-braces-in-regex.patch
# -- unescaped curly brace in regex and invert query precedence for test
# Fix build against new tree-sitter based taken from master branch
Patch1:         0001-fix-escape-braces-in-regex.patch
BuildRequires:  tree-sitter
%treesitter_grammars %{_name}

%description

%prep
%autosetup -p1

%build
%treesitter_configure
%treesitter_build

%install
%treesitter_install

%files
%{treesitter_files}

%changelog
