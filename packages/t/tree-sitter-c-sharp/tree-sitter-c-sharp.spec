#
# spec file for package tree-sitter-c-sharp
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


%define _name c-sharp
Summary:        C# grammar for tree-sitter
Name:           tree-sitter-%{_name}
Version:        0.21.2
Release:        0
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/tree-sitter/tree-sitter-c-sharp
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  tree-sitter
# Not enough memory for %%{ix86} and %%{arm32} to generate the grammar sources
ExcludeArch:    %{ix86} %{arm32}
%treesitter_grammars %{_name}

%description
%{summary}.

%prep
%autosetup -p1

%build
%treesitter_configure
%treesitter_build

%install
%treesitter_install

%check

%files
%{treesitter_files}
%license LICENSE

%changelog
