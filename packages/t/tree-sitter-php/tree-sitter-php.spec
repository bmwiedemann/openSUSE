#
# spec file for package tree-sitter-php
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


%define python_subpackage_only 1
%define         _name php
Name:           tree-sitter-php
Version:        0.23.9
Release:        0
Summary:        PHP grammar for tree-sitter
License:        MIT
URL:            https://github.com/tree-sitter/tree-sitter-php
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  tree-sitter
BuildRequires:  %{python_module base}
%if 0%{?suse_version} >= 1699
# Only for the functional test in %%check; python-tree-sitter does not
# exist in Leap 16.0, and gating the test keeps that repo resolvable.
BuildRequires:  %{python_module tree-sitter}
%endif
%treesitter_grammars %{_name} php_only
%python_subpackages

%description
%{summary}.

%package -n python-%{name}
Summary:        Python binding for the %{_name} tree-sitter grammar
Requires:       %{name} = %{version}-%{release}
Suggests:       python-tree-sitter >= 0.22

%description -n python-%{name}
Pure-Python module tree_sitter_%{_name} that loads the grammar
libraries shipped in %{name} and exposes them to python-tree-sitter
via language_php() and language_php_only().

%prep
%autosetup

%build
%treesitter_configure
%treesitter_build

%install
%treesitter_install
# php/grammar.js and php_only/grammar.js require('../common/define-grammar.js').
%treesitter_devel_install common/define-grammar.js common/scanner.h common/common.mak
# Multi-language module: language_php() + language_php_only().
%treesitter_python_install php php php_only

%if 0%{?suse_version} >= 1699
%check
# The generated shim must point exactly at the libraries this package ships.
test -f %{buildroot}%{_treesitter_grammardir}/libtree-sitter-%{_name}.so
test -f %{buildroot}%{_treesitter_grammardir}/libtree-sitter-php_only.so
%{python_expand grep -Fq '%{_treesitter_grammardir}/libtree-sitter-%{_name}.so' %{buildroot}%{$python_sitearch}/tree_sitter_%{_name}/_binding.py}
%{python_expand grep -Fq '%{_treesitter_grammardir}/libtree-sitter-php_only.so' %{buildroot}%{$python_sitearch}/tree_sitter_%{_name}/_binding.py}
# Functional: parse real source through the shim. %%check runs unprivileged,
# so the library cannot be placed at its real path; redirect the directory
# constant to the build dir, where %%treesitter_build left the .so. -W error
# also proves the supported capsule path is taken - the deprecated int path
# would raise DeprecationWarning.
%{python_expand rm -rf _tspy_check ; mkdir _tspy_check ; cp -pr %{buildroot}%{$python_sitearch}/tree_sitter_%{_name} _tspy_check/ ; rm -rf _tspy_check/tree_sitter_%{_name}/__pycache__ ; sed -i "s|%{_treesitter_grammardir}|$PWD|" _tspy_check/tree_sitter_%{_name}/_binding.py ; PYTHONPATH=$PWD/_tspy_check $python -W error::DeprecationWarning -c "import tree_sitter_%{_name} as tsg; from tree_sitter import Language, Parser; lang = Language(tsg.language_php()); tree = Parser(lang).parse(b'<?php function f() { return 1; }\n'); assert tree.root_node.type == 'program', tree.root_node.type; lang = Language(tsg.language_php_only()); tree = Parser(lang).parse(b'function f() { return 1; }\n'); assert tree.root_node.type == 'program', tree.root_node.type"}
%endif

%files
%license LICENSE
%treesitter_files

%treesitter_devel_package

%files %{python_files %{name}}
%license LICENSE
%{python_sitearch}/tree_sitter_*

%changelog
