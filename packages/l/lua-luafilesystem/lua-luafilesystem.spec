#
# spec file for package lua-luafilesystem
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define flavor @BUILD_FLAVOR@
%define mod_name luafilesystem
%define pversion 1.7.0
%define _pversion 1_7_0_2
Version:        %pversion
Release:        0
Summary:        Filesystem support for Lua
License:        MIT
Group:          Development/Libraries/Other
Url:            http://keplerproject.github.io/luafilesystem/
Source:         https://github.com/keplerproject/luafilesystem/archive/v%{_pversion}.tar.gz#/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{flavor}-devel
Requires:       %{flavor}
%if "%{flavor}" == "lua53"
Provides:       lua-%{mod_name} = %{version}
Obsoletes:      lua-%{mod_name} < %{version}
%endif
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
LuaFileSystem is a Lua library developed to complement the set of functions
related to file systems offered by the standard Lua distribution.

LuaFileSystem offers a portable way to access the underlying directory
structure and file attributes.

%prep
%setup -q -n %{mod_name}-%{_pversion}

sed -i 's|@@VERSION@@|%{version}|g' Makefile

%build
make -j1 CFLAGS="%{optflags} -fPIC -I%{lua_incdir}"

%install
%make_install LUA_LIBDIR='$(DESTDIR)%{lua_archdir}'

%files
%doc doc/us/*
%{lua_archdir}/lfs.so

%changelog
