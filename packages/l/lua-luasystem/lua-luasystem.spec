#
# spec file for package lua-luasystem
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
%if "%{flavor}" == "test"
%define flavor lua54
%bcond_without test
%else
%bcond_with test
%endif
%define mod_name luasystem
Version:        0.6.3
Release:        0
Summary:        Platform independent system calls for Lua
License:        MIT
URL:            https://github.com/lunarmodules/luasystem
Source:         https://github.com/lunarmodules/luasystem/archive/v%{version}.tar.gz#/%{mod_name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM unused_variable.patch gh#lunarmodules/luasystem!78 mcepl@suse.com
# remove two unused-variable warnings
Patch0:         unused_variable.patch
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-luarocks
BuildRequires:  lua-macros
BuildRequires:  pkgconf
Requires:       %{flavor}
%lua_provides
%if "%{flavor}" == ""
Name:           lua-luasystem
ExclusiveArch:  do_not_build
%else
%if %{with test}
Name:           %{flavor}-luasystem-test
%else
Name:           %{flavor}-luasystem
%endif
%endif
%if %{with test}
BuildRequires:  %{flavor}-luasystem
BuildRequires:  %{flavor}-busted
%endif

%description
Adds a Lua API for making platform independent system calls.

%prep
%autosetup -p1 -n %{mod_name}-%{version}

%build
export CFLAGS="%{optflags} $(pkgconf --cflags lua)" \
	MYLDFLAGS="$(pkgconf --libs lua)"
%luarocks_build 

%install
%if %{without test}
export CWARNS="%{optflags}" \
	LUAINC_linux=%{lua_incdir} \
	LUAPREFIX_linux=%{_prefix} \
	CDIR_linux="%{_lib}/lua/%{lua_version}"
%luarocks_install ./*.rock
%endif

%check
%if %{with test}
busted || true
%endif

%if %{without test}
%files
%dir %{lua_archdir}/system
%{lua_archdir}/system/*
%dir %{lua_noarchdir}/system
%{lua_noarchdir}/system/*
%endif

%changelog
