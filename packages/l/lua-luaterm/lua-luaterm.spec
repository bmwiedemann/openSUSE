#
# spec file for package lua-luaterm
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
%define mod_name luaterm
%define rname lua-term
Version:        0.07
Release:        0
Summary:        Terminal operations for Lua
License:        MIT
URL:            https://github.com/hoelzro/lua-term
Source:         https://github.com/hoelzro/lua-term/archive/%{version}.tar.gz#$/%{rname}-%{version}.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  lua-macros
Requires:       %{flavor}
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
This package provides terminal operations for Lua

%prep
%setup -q -n %{rname}-%{version}

%build
%make_build \
	CWARNS="%{optflags}" \
	LUA_INC=%{lua_incdir} \
	LUA_SHARE=%{lua_noarchdir}/term \
	LUA_LIBDIR=%{lua_archdir}/term

%install
%make_install \
        CWARNS="%{optflags}" \
        LUA_INC=%{lua_incdir} \
        LUA_SHARE=%{buildroot}%{lua_noarchdir}/term \
        LUA_LIBDIR=%{buildroot}%{lua_archdir}/term

%files
%dir %{lua_archdir}/term
%{lua_archdir}/term/core.so*
%dir %{lua_noarchdir}/term
%{lua_noarchdir}/term

%changelog
