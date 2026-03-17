#
# spec file for package psqlODBC
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if %suse_version < 1600
%define force_gcc_version 14
%endif

Name:           psqlODBC
Version:        17.00.0008
%define tarv    17_00_0008
Release:        0
Summary:        ODBC Driver for PostgreSQL
License:        LGPL-2.1-or-later
Group:          Productivity/Databases/Clients
URL:            https://odbc.postgresql.org/
Source0:        https://github.com/postgresql-interfaces/psqlodbc/archive/refs/tags/REL-%{tarv}.tar.gz#/psqlodbc-REL-%{tarv}.tar.gz
Patch0:         psqlODBC-internal.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc%{?force_gcc_version} >= 8
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  postgresql-devel
BuildRequires:  unixODBC-devel
PreReq:         %{_bindir}/odbcinst
Obsoletes:      pg_odbc < %{version}-%{release}
Obsoletes:      postgresql-odbc < %{version}-%{release}
Provides:       pg_iface:%{_prefix}/lib/pgsql/odbcinst.ini
Provides:       pg_odbc = %{version}-%{release}
Provides:       postgresql-odbc = %{version}-%{release}

%description
This package contains the ODBC (Open DataBase Connectivity) driver and
sample configuration files needed for applications to access a
PostgreSQL database using ODBC.

%prep
%autosetup -p1 -n psqlodbc-REL-%{tarv}

%build
./bootstrap
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
%endif
export CPPFLAGS="-I/usr/include/pgsql"
%configure --with-unixodbc
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post
/sbin/ldconfig
# odbcinst uses reference counting, so we don't
# need to take care for the update case here.
odbcinst -i -l -d %{_libdir}/psqlodbcw.so -r <<EOF
[PSQL]
Description = PostgreSQL
%ifarch x86_64 ppc64 ia64 s390x
Driver64 = %{_libdir}/psqlodbcw.so
%else
Driver = %{_libdir}/psqlodbcw.so
%endif
EOF

%postun
/sbin/ldconfig
# odbcinst uses reference counting, so we don't
# need to take care for the update case here.
odbcinst -u -l -d %{_libdir}/psqlodbcw.so -n PSQL

%files
%doc *.txt docs/*
%{_libdir}/psql*

%changelog
