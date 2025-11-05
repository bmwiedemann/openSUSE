#
# spec file for package lua-luautf8
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


%define flavor @BUILD_FLAVOR@
%define mod_name luautf8
%define rock_version 0.1.5-2
%ifarch %{ix86}
 %define luarock_arch x86
%else
 %ifarch s390x
  %define luarock_arch s390
 %else
  %define luarock_arch %{_arch}
 %endif
%endif
Version:        0.1.6
Release:        0
Summary:        A utf-8 support module for Lua and LuaJIT
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/starwing/luautf8
# Source:         %%{mod_name}-%%{version}.tar.zst
Source:         https://github.com/starwing/luautf8/archive/refs/tags/%{version}.tar.gz
# PATCH-{FIX|FEATURE}-{OPENSUSE|SLE|UPSTREAM} name-of-file.patch bsc#[0-9]+ mcepl@suse.com
# this patch makes things totally awesome
Patch0:         warnings-away.patch
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-luarocks
BuildRequires:  lua-macros
BuildRequires:  zstd
Requires:       %{flavor}
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
This module adds UTF-8 support to Lua. It use data extracted from
Unicode Character Database, and tested on Lua 5.2.3, Lua 5.3.0 and LuaJIT.
parseucd.lua is a pure Lua script generate unidata.h, to support convert
characters and check characters' category. It mainly used to compatible
with Lua's own string module, it passed all string and pattern matching
test in lua test suite2.

%prep
%autosetup -n %{mod_name}-%{version}

%build
%__cc %{optflags} -fPIC %(pkgconf --cflags lua) -c lutf8lib.c -o lutf8lib.o
%__cc  -shared %{?build_ldflags} %(pkgconf --libs lua) -o lua-utf8.so lutf8lib.o

%install
install -dD %{buildroot}%{lua_archdir}
install -p -m 755 lua-utf8.so %{buildroot}%{lua_archdir}

%check
for testf in test*.lua
do
lua $testf
done

%files
%{lua_archdir}
%license LICENSE

%changelog
