#
# spec file for package tree-sitter-hcl
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


%define         _name hcl
Name:           tree-sitter-hcl
Version:        1.2.0
Release:        0
Summary:        HCL and Terraform grammars for tree-sitter
License:        Apache-2.0
URL:            https://github.com/tree-sitter-grammars/tree-sitter-hcl
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        binding.gyp
BuildRequires:  tree-sitter
%treesitter_grammars %{_name}=src terraform=dialects

%description
%{summary}.

%prep
%autosetup -p1
cp %{SOURCE1} binding.gyp

%build
%treesitter_set_flags
tree-sitter generate
(cd dialects/terraform; tree-sitter generate)
%treesitter_build

%install
%treesitter_install

%files
%license LICENSE
%treesitter_files

%changelog
