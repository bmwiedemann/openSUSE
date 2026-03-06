#
# spec file for package tree-sitter-tcl
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


%define         _name tcl
Name:           tree-sitter-tcl
Version:        0+20241105.98015eb
Release:        0
Summary:        TCL grammar for tree-sitter
License:        MIT
URL:            https://github.com/tree-sitter-grammars/tree-sitter-tcl
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  tree-sitter
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
%treesitter_devel_install

%files
%license LICENSE
%treesitter_files

%treesitter_devel_package

%changelog
