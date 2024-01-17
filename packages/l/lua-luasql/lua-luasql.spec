#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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
%define flavor_ver %{lua:ver, ok = string.gsub(rpm.expand("%{flavor}"), "lua(%d)(%d)", "%1.%2"); print(ver)}
%define mod_name luasql
%define lua_archdir	%{_libdir}/lua/%{flavor_ver}
%define lua_incdir	%{_includedir}/lua%{flavor_ver}
%define lua_noarchdir	%{_datadir}/lua/%{flavor_ver}

%lua_provides
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
Version:        2.6.0
Release:        0
Summary:        Simple interface from Lua to a DBMS
License:        MIT
Group:          Development/Libraries/Other
URL:            https://github.com/lunarmodules/luasql
Source0:        https://github.com/lunarmodules/luasql/archive/refs/tags/%{version}/%{mod_name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM luasql-fix-configuration.patch gh#lunarmodules/luasql!152 mcepl@suse.com
# Clean up building and add rpm optflags.
Patch0:         luasql-fix-configuration.patch
BuildRequires:  %{flavor}-devel
BuildRequires:  libiodbc-devel
BuildRequires:  libmysqlclient-devel
BuildRequires:  pkgconf
BuildRequires:  postgresql-devel
BuildRequires:  sqlite3-devel
Requires:       %{flavor}
Requires:       libmariadb3

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
make %{?_smp_mflags} \
    DRIVER_INCS="-I%{_includedir}" DRIVER_LIBS_sqlite3="-lsqlite3" sqlite3
make %{?_smp_mflags} \
    DRIVER_INCS="-I%{_includedir}/pgsql" DRIVER_LIBS_postgres="-lpq" postgres
make %{?_smp_mflags} \
    DRIVER_INCS="-I%{_includedir}/mysql" DRIVER_LIBS_mysql="-lmysqlclient -lz" mysql
make %{?_smp_mflags} \
    DRIVER_INCS="-I%{_includedir}" DRIVER_LIBS_odbc="-liodbc" odbc

%install
%make_install LUA_LIBDIR='$(DESTDIR)%{lua_archdir}' sqlite3
%make_install LUA_LIBDIR='$(DESTDIR)%{lua_archdir}' postgres
%make_install LUA_LIBDIR='$(DESTDIR)%{lua_archdir}' mysql
%make_install LUA_LIBDIR='$(DESTDIR)%{lua_archdir}' odbc

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
