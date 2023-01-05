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
%define mod_name luafilesystem
%define pversion 1.8.0
%define _pversion 1_8_0

%if %{undefined lua_provides}
%define lua_provides \
Provides: lua-%{mod_name} = %{version}-%{release} \
Obsoletes: lua-%{mod_name} < %{version}-%{release}
%endif

Version:        %{pversion}
Release:        0
Summary:        Filesystem support for Lua
License:        MIT
Group:          Development/Libraries/Other
URL:            https://keplerproject.github.io/luafilesystem/
Source:         https://github.com/keplerproject/luafilesystem/archive/v%{_pversion}.tar.gz#/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{flavor}-devel
Requires:       %{flavor}
%lua_provides
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
%make_build -j1 CFLAGS="%{optflags} -fPIC -I%{lua_incdir}"

%install
%make_install LUA_LIBDIR='%{lua_archdir}'

%files
%doc doc/us/*
%{lua_archdir}/lfs.so

%changelog
