#
# spec file for package tree-sitter-scheme
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


%define         _name scheme
%define         _upversion 0.24.7-1
Name:           tree-sitter-scheme
Version:        %(echo "%{_upversion}"|tr '-' '.')
Release:        0
Summary:        Lua grammar for tree-sitter
License:        MIT
URL:            https://github.com/6cdh/tree-sitter-scheme
Source0:        %{url}/archive/v%{_upversion}.tar.gz#/%{name}-%{_upversion}.tar.gz
BuildRequires:  tree-sitter >= 0.24.0
%treesitter_grammars %{_name}

%description
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{_upversion}

%build
%treesitter_configure
%treesitter_build

%install
%treesitter_install
%treesitter_devel_install

%files
%license LICENSE
%doc README.md
%treesitter_files

%treesitter_devel_package

%changelog
