#
# spec file for package lua-shell-games
#
# Copyright (c) 2022 SUSE LLC
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
%define mod_name shell-games
Version:        1.1.0
Release:        0
Summary:        Lua library to help execute shell commands
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/GUI/lua-shell-games
Source:         https://github.com/GUI/lua-shell-games/archive/v%{version}.tar.gz#/lua-%{mod_name}-%{version}.tar.gz
Patch1:         Fix-capture_combined_spec-with-new-shell.patch
BuildRequires:  %{flavor}-busted
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-luacheck
BuildRequires:  %{flavor}-luarocks
BuildRequires:  lua-macros
Requires:       %{flavor}
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
A Lua library to help execute shell commands more easily and safely.

* Easily execute shell commands, while capturing the command's output and exit
code. Includes compatibility across versions of Lua, LuaJIT, and OpenResty
where io.popen may not return exit codes (pre Lua 5.2 behavior).
* Utilities to quote and escape shell arguments for safer, less error-prone
execution.

When executing shell commands, shell-games wraps either os.execute or io.popen
(depending on whether the output is being captured).

%prep
%autosetup -p1 -n lua-%{mod_name}-%{version}

%build

%install
install -m 0755 -p -d %{buildroot}%{lua_noarchdir}
install -v -D -m 0644 -p -t %{buildroot}%{lua_noarchdir} lib/%{mod_name}.lua

%check
ln -sfv lib/%{mod_name}.lua .
%if "%{flavor}" == "lua51"
REFUTE_LUA52_BEHAVIOR=true \
%endif
EXPECTED_LUA_VERSION="Lua %{lua_version}" %make_build test

%files
%license LICENSE.txt
%doc README.md CHANGELOG.md
%{lua_noarchdir}/%{mod_name}*

%changelog
