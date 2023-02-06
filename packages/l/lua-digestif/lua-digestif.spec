#
# spec file
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


%define flavor @BUILD_FLAVOR@
%define lua_value  %(echo "%{flavor}" |sed -e 's:lua::')
%define mod_name digestif
%define rock_version dev-1
Version:        0.5.1
Release:        0
Summary:        Language server for TeX and friends
License:        GPL-3.0-or-later AND LPPL-1.3c
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://github.com/astoff/digestif
Source:         https://github.com/astoff/digestif/archive/refs/tags/v%{version}.tar.gz#/lua-%{mod_name}-%{version}.tar.gz
BuildRequires:  lua-macros
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do-not-build
%else
Name:           %{flavor}-%{mod_name}
Requires:       %{flavor}
BuildRequires:  %{flavor}-busted
BuildRequires:  %{flavor}-cjson
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-lpeg
BuildRequires:  %{flavor}-luarocks
%endif
Requires(post): update-alternatives
Requires(postun):update-alternatives

%description
Digestif is a code analyzer, and a language server, for LaTeX, ConTeXt et caterva.
It provides context-sensitive completion, documentation, code navigation, and related
functionality to any text editor that speaks the LSP protocol.

%prep
%autosetup -n %{mod_name}-%{version}

%build
%luarocks_build

%install
%luarocks_install %{mod_name}-dev-1.all.rock

# Wrapper script based on
# https://github.com/astoff/digestif/blob/main/INSTALL.md#standard-packaging
cat > %{buildroot}%{_bindir}/%{mod_name} <<-SH
#!/usr/bin/lua%{lua_version}
require "digestif.config".data_dirs = { "%{luarocks_treedir}/%{mod_name}/dev-1/data" }
require "digestif.langserver".main(arg)
SH

cat > %{buildroot}%{luarocks_treedir}/%{mod_name}/dev-1/bin/%{mod_name} <<-SH
#!/usr/bin/lua%{lua_version}
require "digestif.config".data_dirs = { "%{luarocks_treedir}/%{mod_name}/dev-1/data" }
require "digestif.langserver".main(arg)
SH

# in preparation for update alternatives
mv %{buildroot}%{_bindir}/%{mod_name}{,-lua%{lua_version}}

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/%{mod_name}
ln -sfv %{_sysconfdir}/alternatives/%{mod_name} %{buildroot}%{_bindir}/%{mod_name}
cp -v %{buildroot}%{luarocks_treedir}/%{mod_name}/%{rock_version}/bin/%{mod_name}{,-lua%{lua_version}}
ln -sfv %{luarocks_treedir}/%{mod_name}/%{rock_version}/bin/%{mod_name} \
  %{buildroot}%{luarocks_treedir}/%{mod_name}/%{rock_version}/bin/%{mod_name}-lua%{lua_version}

%post
%{_sbindir}/update-alternatives --install %{_bindir}/%{mod_name} digestif %{_bindir}/%{mod_name}-lua%{lua_version} %{lua_value}

%postun
if [ "$1" = 0 ]; then
  %{_sbindir}/update-alternatives --remove digestif %{_bindir}/%{mod_name}-lua%{lua_version}
fi

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{mod_name}*
%{luarocks_treedir}/*
%{lua_noarchdir}/%{mod_name}*
%ghost %{_sysconfdir}/alternatives/%{mod_name}

%changelog
