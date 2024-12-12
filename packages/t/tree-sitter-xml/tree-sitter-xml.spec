#
# spec file for package tree-sitter-xml
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


%define         _name xml
Name:           tree-sitter-xml
Version:        0.7.0
Release:        0
Summary:        Xml grammar for tree-sitter
License:        MIT
URL:            https://github.com/tree-sitter-grammars/tree-sitter-xml
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  tree-sitter
%treesitter_grammars %{_name} dtd

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

#neovim stuff
install -d %{buildroot}%{_libdir}/tree_sitter
ln -s %{_libdir}/lib%{name}.so %{buildroot}%{_libdir}/tree_sitter/%{_name}.so
ln -s %{_libdir}/libtree-sitter-dtd.so %{buildroot}%{_libdir}/tree_sitter/dtd.so

%files
%license LICENSE
%treesitter_files
%{_libdir}/tree_sitter/%{_name}.so
%{_libdir}/tree_sitter/dtd.so
%if 0%{?suse_version} < 1600
%dir %{_libdir}/tree_sitter
%endif

%treesitter_devel_package

%changelog
