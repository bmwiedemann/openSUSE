#
# spec file for package tree-sitter-rpmspec
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


%define         _name rpmspec
Name:           tree-sitter-rpmspec
Version:        0+20260218.12ca618
Release:        0
Summary:        RPMspec grammar for tree-sitter
License:        MIT
URL:            https://gitlab.com/cryptomilk/tree-sitter-rpmspec
Source0:        %{name}-%{version}.tar.gz
Patch1:         0001-fix-binding.gyp-correctly-list-source-files.patch
# PATCH-FIX-UPSTREAM build-fix-bindings.patch gl#cryptomilk/tree-sitter-rpmspec!85 mcepl@suse.com
# multi-grammar support in language bindings
Patch2:         build-fix-bindings.patch
BuildRequires:  tree-sitter
# For rpmbash grammar
BuildRequires:  treesitter_grammar_src(tree-sitter-bash)
%treesitter_grammars %{_name} rpmbash

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
# Manual installation of queries as the macros don't handle them for sub-grammars
for grammar in %{_name} rpmbash; do
    install -d %{buildroot}%{_datadir}/tree-sitter/queries/$grammar
    install -m 0644 $grammar/queries/*.scm %{buildroot}%{_datadir}/tree-sitter/queries/$grammar/
done

%files
%license LICENSE
%treesitter_files
%dir %{_datadir}/tree-sitter
%{_datadir}/tree-sitter/queries/

%treesitter_devel_package

%changelog
