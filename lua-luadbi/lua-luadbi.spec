#
# spec file for package lua-luadbi
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define mod_name luadbi
Version:        0.5
Release:        0
Summary:        A database interface library for Lua
License:        MIT
Group:          Productivity/Databases/Tools
URL:            https://code.google.com/p/luadbi
# Formely found on code.google.com
Source:         luadbi.%{version}.tar.gz
# PATCH-FIX-UPSTREAM marguerite@opensuse.org - fix postgresql headers' path
Patch0:         luadbi-postgresql-headers.patch
BuildRequires:  %{flavor}-devel
BuildRequires:  libmysqld-devel
BuildRequires:  postgresql-devel
BuildRequires:  postgresql-server-devel
BuildRequires:  sqlite3-devel
Requires:       %{flavor}
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
LuaDBI is a database interface library for Lua. It is designed to provide a
RDBMS agnostic API for handling database operations. LuaDBI also provides
support for prepared statement handles, placeholders and bind parameters for
all database operations.

Currently LuaDBI supports DB2, Oracle, MySQL, PostgreSQL and SQLite databases
with native database drivers. But openSUSE version doesn't build with DB2 and
Oracle.

%prep
%setup -q -n luadbi-%{version}
%patch0 -p1

sed -i \
    -e 's:-g -pedantic -Wall -O2:%{optflags} -fPIC -I%{lua_incdir}:g' \
    Makefile

%build
make %{?_smp_mflags} LIBDIR=%{_libdir}

%install
install -d %{buildroot}%{lua_archdir}
install -d %{buildroot}%{lua_noarchdir}

cp -r *.so %{buildroot}%{lua_archdir}
cp -r *.lua %{buildroot}%{lua_noarchdir}

%files
%license COPYING
%doc README
%{lua_archdir}/*.so
%{lua_noarchdir}/*.lua

%changelog
