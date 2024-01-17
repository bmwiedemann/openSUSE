#
# spec file for package nvimpager
#
# Copyright (c) 2023 SUSE LLC
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


Name:           nvimpager
Version:        0.12.0
Release:        0
Summary:        Use nvim as a pager
License:        BSD-2-Clause
Group:          Productivity/Text/Editors
URL:            https://github.com/lucc/nvimpager
Source:         https://github.com/lucc/nvimpager/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  scdoc
Requires:       lua54
Requires:       neovim >= 0.9
BuildArch:      noarch

%description
Using neovim as a pager to view man pages, git diffs, whatnot with neovim's syntax highlighting and mouse support.

%package zsh-completion
Summary:        Zsh completion for %{name}
Group:          Productivity/Text/Editors
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%setup -q
sed -i "s/#!\/usr\/bin\/env bash/#!\/bin\/bash/" nvimpager

%build

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/nvimpager
%{_mandir}/man1/nvimpager.1%{?ext_man}
%dir %{_datadir}/nvimpager
%dir %{_datadir}/nvimpager/runtime
%dir %{_datadir}/nvimpager/runtime/lua
%dir %{_datadir}/nvimpager/runtime/lua/nvimpager
%{_datadir}/nvimpager/runtime/lua/nvimpager/ansi2highlight.lua
%{_datadir}/nvimpager/runtime/lua/nvimpager/cat.lua
%{_datadir}/nvimpager/runtime/lua/nvimpager/init.lua
%{_datadir}/nvimpager/runtime/lua/nvimpager/options.lua
%{_datadir}/nvimpager/runtime/lua/nvimpager/pager.lua
%{_datadir}/nvimpager/runtime/lua/nvimpager/util.lua

%files zsh-completion
%license LICENSE
%{_datadir}/zsh

%changelog
