#
# spec file for package tree-sitter-zig
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
%define         _name zig
Name:           tree-sitter-zig
Version:        1.1.2
Release:        0
Summary:        Zig grammar for tree-sitter
License:        MIT
URL:            https://github.com/tree-sitter-grammars/tree-sitter-zig
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module installer}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  tree-sitter
%treesitter_grammars %{_name}
%python_subpackages

%description
%{summary}.

%package -n python-%{name}
Summary:        Python binding for the %{name} grammar
Suggests:       python-tree-sitter

%description -n python-%{name}
The tree_sitter_* Python module for the %{name} grammar, loadable
with the Language()/Parser() API from python-tree-sitter.

%prep
%autosetup

%build
%treesitter_configure
%treesitter_build
%treesitter_python_build

%install
%treesitter_install
%treesitter_devel_install
%treesitter_python_install

%files
%license LICENSE
%treesitter_files

%treesitter_devel_package

%files %{python_files %{name}}
%license LICENSE
%{python_sitearch}/tree_sitter_*

%changelog
