#
# spec file for package luacheck
#
# Copyright (c) 2021 SUSE LLC
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


Name:           luacheck
Version:        0.24.0
Release:        0
Summary:        A a command-line tool for linting and static analysis of Lua code
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/luarocks/luacheck
Source:         https://github.com/luarocks/luacheck/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE - silence rpmlint
Patch0:         env.patch
BuildRequires:  lua-macros
BuildRequires:  lua53-luafilesystem
BuildRequires:  lua53-argparse
Requires:       lua53
Requires:       lua53-luafilesystem
Requires:       lua53-argparse
BuildArch:      noarch

%description
Luacheck is a static analyzer and a linter for Lua. Luacheck detects
various issues such as usage of undefined global variables, unused variables
and values, accessing uninitialized variables, unreachable code and more.
Most aspects of checking are configurable: there are options for defining
custom project-related globals, for selecting set of standard globals
(version of Lua standard library), for filtering warnings by type and name of
related variable, etc.
The options can be used on the command line, put into a config or directly into
checked files as Lua comments.

%prep
%setup -q
%patch0 -p1

%build

%install
mkdir -p %{buildroot}%{lua_noarchdir}
mkdir -p %{buildroot}%{_bindir}
cp bin/luacheck.lua %{buildroot}%{_bindir}/luacheck
cp -r src/luacheck %{buildroot}%{lua_noarchdir}
chmod +x %{buildroot}%{_bindir}/luacheck


%check
LUA_PATH='/usr/share/lua/%{lua_version}/?.lua'
LUA_PATH="%{buildroot}%{lua_noarchdir}/?/init.lua;${LUA_PATH}"
export LUA_PATH="%{buildroot}%{lua_noarchdir}/?.lua;${LUA_PATH}"
%{_bindir}/lua%{lua_version} %{buildroot}%{_bindir}/luacheck src/


%files
%doc README.md
%license LICENSE
%{_bindir}/luacheck
%{lua_noarchdir}/luacheck/

%changelog
