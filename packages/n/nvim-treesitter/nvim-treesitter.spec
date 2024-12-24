#
# spec file for package nvim-treesitter
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed upon.
# The license for this file, and modifications and additions to the file, is the
# same license as for the pristine package itself (unless the license for the
# pristine package is not an Open Source License, in which case the license is
# the MIT License). An "Open Source License" is a license that conforms to the
# Open Source Definition (Version 1.9) published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           nvim-treesitter
Version:        0.9.3
Release:        0
Summary:        Nvim Treesitter configurations and abstraction layer
License:        Apache-2.0
URL:            https://github.com/nvim-treesitter/nvim-treesitter
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  neovim
BuildRequires:  lua-macros
Requires:       neovim
BuildArch:      noarch

%description
The goal of nvim-treesitter is both to provide a simple and easy way to use the
interface for tree-sitter in Neovim and to provide some basic functionality such
as highlighting based on it.


%prep
%autosetup

%build

%install
export INST_LUADIR=%{buildroot}%{_datadir}/lua/%{lua_version}
%make_install install

%files 
%license LICENSE
%doc README.md
%{_datadir}/lua/%{lua_version}/%{name}
%{_datadir}/lua/%{lua_version}/%{name}.lua

%changelog
