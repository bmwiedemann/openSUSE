#
# spec file for package lua-luacheck
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2012 Togan Muftuoglu toganm@opensuse.org
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
%define mod_name luacheck
# Remove file dependency on the interpreter
%global __requires_exclude ^%{_bindir}/lua(5\\.[1-9]|jit)?$
%if "%{flavor}" == "luajit"
%define lua_value  52
%else
%define lua_value  %(echo "%{flavor}" |sed -e 's:lua::')
%endif
Version:        1.1.0
Release:        0
Summary:        Command-line tool for linting and static analysis of Lua code
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/lunarmodules/luacheck
Source:         https://github.com/lunarmodules/luacheck/archive/v%{version}.tar.gz#/%{mod_name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE - silence rpmlint
Patch0:         env.patch
BuildRequires:  %{flavor}
BuildRequires:  %{flavor}-argparse
BuildRequires:  %{flavor}-luafilesystem
BuildRequires:  lua-macros
Requires:       %{flavor}
Requires:       %{flavor}-argparse
Requires:       %{flavor}-luafilesystem
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       luacheck
Obsoletes:      luacheck < %{version}
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

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
%autosetup -n %{mod_name}-%{version} -p1

%build

%install
mkdir -p %{buildroot}%{lua_noarchdir}
mkdir -p %{buildroot}%{_bindir}
cp -v bin/luacheck.lua %{buildroot}%{_bindir}/luacheck-%{flavor}
cp -rv src/luacheck %{buildroot}%{lua_noarchdir}
chmod +x %{buildroot}%{_bindir}/luacheck-%{flavor}
sed -i -e 's,# *\!%{_bindir}/.*lua,#!%{_bindir}/lua,' %{buildroot}%{_bindir}/luacheck-%{flavor}

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/luacheck
ln -sf %{_sysconfdir}/alternatives/luacheck %{buildroot}%{_bindir}/luacheck

%check
LUA_PATH='%{lua_noarchdir}/?.lua;%{lua_noarchdir}/?/init.lua'
export LUA_PATH="%{buildroot}%{lua_noarchdir}/?.lua;%{buildroot}%{lua_noarchdir}/?/init.lua;${LUA_PATH}"
lua %{buildroot}%{_bindir}/luacheck-%{flavor} src/

%post
%{_sbindir}/update-alternatives --install %{_bindir}/luacheck luacheck %{_bindir}/luacheck-%{flavor} %{lua_value}

%postun
if [ "$1" = 0 ] ; then
	%{_sbindir}/update-alternatives --remove luacheck %{_bindir}/luacheck-%{flavor}
fi

%files
%doc README.md CHANGELOG.md docsrc/*.rst
%license LICENSE
%ghost %{_sysconfdir}/alternatives/luacheck
%{_bindir}/luacheck
%{_bindir}/luacheck-%{flavor}
%{lua_noarchdir}/luacheck/

%changelog
