#
# spec file for package nvim-lspconfig
#
# Copyright (c) 2025 SUSE LLC
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


Name:           nvim-lspconfig
Version:        1.7.0
Release:        0
Summary:        Quickstart configs for Nvim LSP
License:        Apache-2.0
URL:            https://github.com/neovim/nvim-lspconfig
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  neovim
Requires:       neovim
BuildArch:      noarch

%description
default Nvim LSP client configurations for various LSP servers

%package doc
Summary:        Documentation for %{name}

%description doc
%{summary}.

%prep
%autosetup
%fdupes -s doc

%build
nvim -u NONE -i NONE -e --headless -c "helptags doc" -c quit

%install
install -d %{buildroot}%{_datadir}/nvim/runtime/
cp -r lua plugin %{buildroot}%{_datadir}/nvim/runtime/

%files
%license LICENSE.md
%doc CONTRIBUTING.md README.md
%{_datadir}/nvim/runtime/lua/lspconfig
%{_datadir}/nvim/runtime/lua/lspconfig.lua
%{_datadir}/nvim/runtime/plugin/lspconfig.lua

%files doc
%doc doc

%changelog
