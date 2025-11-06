#
# spec file for package lua-inspect
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
%define mod_name inspect
Version:        3.1.3
Release:        0
Summary:        Library for printing Lua values
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/kikito/inspect.lua
Source:         https://github.com/kikito/inspect.lua/archive/v%{version}.tar.gz#/lua-%{mod_name}-%{version}.tar.gz
# # PATCH-FIX-UPSTREAM correct_assertion.patch gh#kikito/inspect.lua!75 mcepl@suse.com
# correct assertion for metatable with __metatable=nil
# seems that the patch fixes the issue with aarch64, but breaks everywhere else
# Patch0:         correct_assertion.patch
BuildRequires:  %{flavor}-busted
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-luacheck
BuildRequires:  lua-macros
Requires:       %{flavor}
BuildArch:      noarch
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
# see gh#kikito/inspect.lua!75
ExcludeArch:    aarch64
%endif

%description
This library transforms any Lua value into a human-readable representation. It is especially useful for debugging errors in tables.

The objective here is human understanding (i.e. for debugging), not serialization or compactness.

%prep
%autosetup -p1 -n %{mod_name}.lua-%{version}

%build
:

%install
install -v -D -m 0644 -p -t %{buildroot}%{lua_noarchdir} %{mod_name}.lua
cp -p -r spec/ %{buildroot}%{lua_noarchdir}

%check
export PATH="%{buildroot}%{_bindir}:%{_bindir}"
LUA_PATH="%{buildroot}%{lua_noarchdir}/?.lua;%{lua_noarchdir}/?.lua;"
export LUA_PATH="%{buildroot}%{lua_noarchdir}/?/init.lua;%{lua_noarchdir}/?/init.lua;${LUA_PATH}"
luacheck inspect.lua
busted

%files
%license MIT-LICENSE.txt
%doc README.md CHANGELOG.md
%{lua_noarchdir}/%{mod_name}*
%{lua_noarchdir}/spec

%changelog
