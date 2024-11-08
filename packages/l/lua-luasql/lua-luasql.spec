#
# spec file for package lua-luasql
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2014 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


%global flavor @BUILD_FLAVOR@%{nil}
%define flavor_dec $(c=%{flavor}; echo ${c:0:-1}.${c: -1})
%define flavor_ver %{lua:ver, ok = string.gsub(rpm.expand("%{flavor}"), "lua(%{d})(%{d})", "%{1}.%{2}"); print(ver)}
%define mod_name luasql
Version:        2.6.0+git.1724375068.d60f8b2
Release:        0
Summary:        Simple interface from Lua to a DBMS
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/lunarmodules/luasql
# Source0:        https://github.com/lunarmodules/luasql/archive/refs/tags/%%{version}/%%{mod_name}-%%{version}.tar.gz
Source0:        %{mod_name}-%{version}.tar.gz
BuildRequires:  %{flavor}-devel
BuildRequires:  libiodbc-devel
BuildRequires:  libmysqlclient-devel
BuildRequires:  lua-macros
BuildRequires:  pkgconf
BuildRequires:  postgresql-devel
BuildRequires:  sqlite3-devel
Requires:       %{flavor}
Requires:       libmariadb3
%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
A simple interface from Lua to a DBMS. It enables a Lua program to:
 - Connect to ODBC, ADO, Oracle, MySQL, SQLite and PostgreSQL databases;
 - Execute arbitrary SQL statements;
 - Retrieve results in a row-by-row cursor fashion.

%prep
%autosetup -p1 -n %{mod_name}-%{version}

%build
export OPTFLAGS="%{optflags}"
export LUA_INC="%{lua_incdir}"

# also oci8 firebird
%make_build \
    DRIVER_INCS="-I%{_includedir}" DRIVER_LIBS_sqlite3="-lsqlite3" sqlite3
%make_build \
    DRIVER_INCS="-I%{_includedir}/pgsql" DRIVER_LIBS_postgres="-lpq" postgres
%make_build \
    DRIVER_INCS="-I%{_includedir}/mysql" DRIVER_LIBS_mysql="-lmysqlclient -lz" mysql
%make_build \
    DRIVER_INCS="-I%{_includedir}" DRIVER_LIBS_odbc="-liodbc" odbc

%install
%make_install LUA_LIBDIR='$(DESTDIR)%{lua_archdir}' sqlite3
%make_install LUA_LIBDIR='$(DESTDIR)%{lua_archdir}' postgres
%make_install LUA_LIBDIR='$(DESTDIR)%{lua_archdir}' mysql
%make_install LUA_LIBDIR='$(DESTDIR)%{lua_archdir}' odbc

%check
export LUA_PATH='%{buildroot}%{lua_archdir}/?.lua;;'
export LUA_CPATH='%{buildroot}%{lua_archdir}/?.so'
lua%{lua_version} tests/test.lua sqlite3

%files
%doc doc/us/*
%dir %{lua_archdir}/luasql
%{lua_archdir}/luasql/
# TODO? Split to subpackages?
# /usr/lib64/lua/%%{lua_version}/luasql
# /usr/lib64/lua/%%{lua_version}/luasql/mysql.so
# /usr/lib64/lua/%%{lua_version}/luasql/postgres.so
# /usr/lib64/lua/%%{lua_version}/luasql/sqlite3.so

%changelog
