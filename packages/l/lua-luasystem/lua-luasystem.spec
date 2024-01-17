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
%define mod_name luasystem
%define upversion 0.2.1
Version:        0.21
Release:        0
Summary:        Platform independent system calls for Lua
License:        MIT
URL:            https://github.com/o-lim/luasystem
Source:         https://github.com/o-lim/luasystem/archive/v%{upversion}.tar.gz#/%{mod_name}-%{upversion}.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  lua-macros
Requires:       %{flavor}
%lua_provides
%if "%{flavor}" == ""
Name:           lua-luasystem
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-luasystem
%endif

%description
Adds a Lua API for making platform independent system calls.

%prep
%setup -q -n %{mod_name}-%{upversion}

%build
make %{?_smp_mflags} \
	CWARNS="%{optflags}" \
        LUAINC_linux=%{lua_incdir} \
        CDIR_linux?=%{_lib}/lua/%{lua_version} \
        LUAPREFIX_linux?=%{_prefix} \
        linux

%install
%make_install \
        CWARNS="%{optflags}" \
        LUAINC_linux=%{lua_incdir} \
        LUAPREFIX_linux?=%{_prefix} \
        CDIR_linux?=%{_lib}/lua/%{lua_version} \
        linux
install -v -D -m0644 -p -t %{buildroot}%{lua_noarchdir}/system system/init.lua

%files
%dir %{lua_archdir}/system
%{lua_archdir}/system/*
%dir %{lua_noarchdir}/system
%{lua_noarchdir}/system/*

%changelog
