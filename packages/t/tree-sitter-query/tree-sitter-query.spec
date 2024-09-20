#
# spec file for package tree-sitter-query
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


%define         _name query
Name:           tree-sitter-%{_name}
Version:        0.4.0
Release:        0
Summary:        TS query grammar for tree-sitter
License:        Apache-2.0
URL:            https://github.com/tree-sitter-grammars/tree-sitter-query
Source:         %{name}-%{version}.tar.xz
BuildRequires:  tree-sitter
%treesitter_grammars %{_name}

%description
A tree-sitter parser for tree-sitter query files (scheme-like).

%prep
%autosetup -p1

%build
%treesitter_configure
%treesitter_build

%install
%treesitter_install

install -d %{buildroot}%{_libdir}/tree_sitter
ln -s %{_libdir}/lib%{name}.so %{buildroot}%{_libdir}/tree_sitter/%{_name}.so

%files
%license LICENSE
%doc README.md
%{treesitter_files}
%{_libdir}/tree_sitter/%{_name}.so
%if 0%{?suse_version} < 1600
%dir %{_libdir}/tree_sitter
%endif

%changelog
