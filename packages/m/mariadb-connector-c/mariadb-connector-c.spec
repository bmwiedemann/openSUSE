#
# spec file for package mariadb-connector-c
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


%define sover 3
%define libname libmariadb
# equivalent mariadb version
%define mariadb_version 10.3.21
%if ! %{defined _rundir}
%define _rundir %{_localstatedir}/run
%endif
%bcond_with sqlite3
Name:           mariadb-connector-c
Version:        3.3.10
Release:        0
Summary:        MariaDB connector in C
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/MariaDB/mariadb-connector-c
Source:         https://downloads.mariadb.com/Connectors/c/connector-c-%{version}/%{name}-%{version}-src.tar.gz
Source1:        https://downloads.mariadb.com/Connectors/c/connector-c-%{version}/%{name}-%{version}-src.tar.gz.asc
# Imported from keyserver based on keyid @ https://mariadb.com/kb/en/mariadb-enterprise/mariadb-enterprise-installation-guide/
Source2:        mariadb.keyring
Source3:        baselibs.conf
Patch1:         mariadb-connector-c-2.3.1_unresolved_symbols.patch
Patch4:         private_library.patch
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
%if %{with sqlite3}
BuildRequires:  pkgconfig(sqlite3)
%endif

%description
MariaDB Connector is used to connect applications developed in
C or C++ to MariaDB and MySQL databases. This is a different
implementation from the traditional libmariadbclient/libmysqlclient
that is shipped with mariadb-server/mysql-server, but the API is the same.

%package -n %{libname}%{sover}
Summary:        MariaDB connector in C
Group:          System/Libraries

%description -n %{libname}%{sover}
MariaDB Connector is used to connect applications developed in
C or C++ to MariaDB and MySQL databases. This is a different
implementation from the traditional libmariadbclient/libmysqlclient
that is shipped with mariadb-server/mysql-server, but the API is the same.

This package holds the runtime components.

%package -n %{libname}_plugins
Summary:        Plugins for the MariaDB C Connector
# We need "Conflicts" because we moved some plugins here:
# dialog.so was in mariadb-client package
# mysql_clear_password.so was in mariadb package
Group:          System/Libraries
Conflicts:      mariadb <= 10.1.25
Conflicts:      mariadb-client <= 10.1.25

%description -n %{libname}_plugins
MariaDB Connector is used to connect applications developed in
C or C++ to MariaDB and MySQL databases.

This package holds MariaDB library plugins.

%package -n %{libname}private
Summary:        Additional internal libraries for the MariaDB C Connector
Group:          System/Libraries

%description -n %{libname}private
MariaDB Connector is used to connect applications developed in
C or C++ to MariaDB and MySQL databases.

This package holds the runtime components with private API.

%package -n %{libname}-devel
Summary:        Development files for the MariaDB Connector C API
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{sover} = %{version}
Requires:       pkgconfig(openssl)
Requires:       pkgconfig(zlib)
# mysql-devel needs to be provided as some pkgs still depend on it
Provides:       mysql-devel = %{mariadb_version}
Obsoletes:      mysql-devel < %{mariadb_version}
Provides:       libmysqlclient-devel = %{mariadb_version}
Obsoletes:      libmysqlclient-devel < %{mariadb_version}

%description -n %{libname}-devel
MariaDB Connector is used to connect applications developed in
C or C++ to MariaDB and MySQL databases.

This package holds the development files.

%prep
%autosetup -p1 -n %{name}-%{version}-src

%build
# plugin types seems to require no aliasing assumptions
%define _lto_cflags %{nil}
export CFLAGS="%{optflags} -fno-strict-aliasing"

%cmake \
  %if %{with sqlite3}
  -DWITH_SQLITE:BOOL=ON \
  %endif
  -DWITH_EXTERNAL_ZLIB:BOOL=ON \
  -DMARIADB_UNIX_ADDR:STRING=%{_rundir}/mysql/mysql.sock \
  -DINSTALL_LAYOUT=RPM \
  -DINSTALL_LIBDIR:STRING=%{_lib} \
  -DINSTALL_INCLUDEDIR:STRING=include/mysql \
  -DINSTALL_PLUGINDIR:STRING=%{_lib}/mysql/plugin/ \
  -DWITH_MYSQLCOMPAT=ON \
  -DWITH_SSL=OPENSSL \
  -DINSTALL_PCDIR="%{_lib}/pkgconfig"
%make_jobs

%install
%cmake_install

# remove static linked libraries
rm %{buildroot}%{_libdir}/libmariadbclient.a
rm %{buildroot}%{_libdir}/libmysqlclient.a
rm %{buildroot}%{_libdir}/libmysqlclient_r.a
rm %{buildroot}%{_libdir}/libmariadb.a

# add a compatibility symlinks
ln -s mariadb_config %{buildroot}%{_bindir}/mysql_config
ln -s mariadb_version.h %{buildroot}%{_includedir}/mysql/mysql_version.h
ln -s libmariadb.pc %{buildroot}%{_libdir}/pkgconfig/mysqlclient.pc

ln -s %{_includedir}/mysql %{buildroot}%{_includedir}/mariadb

# install some extra required header file
install -Dpm 0644 build/include/ma_config.h \
  %{buildroot}%{_includedir}/mysql/my_config.h

%post   -n %{libname}%{sover} -p /sbin/ldconfig
%post   -n %{libname}private -p /sbin/ldconfig
%postun -n %{libname}%{sover} -p /sbin/ldconfig
%postun -n %{libname}private -p /sbin/ldconfig

%files -n %{libname}%{sover}
%license COPYING.LIB
%doc README
%{_libdir}/libmariadb.so.%{sover}

%files -n %{libname}_plugins
%dir %{_libdir}/mysql/
%dir %{_libdir}/mysql/plugin/
%{_libdir}/mysql/plugin/dialog.so
%{_libdir}/mysql/plugin/mysql_clear_password.so
%{_libdir}/mysql/plugin/auth_gssapi_client.so
%{_libdir}/mysql/plugin/remote_io.so
%{_libdir}/mysql/plugin/sha256_password.so
%{_libdir}/mysql/plugin/caching_sha2_password.so
%{_libdir}/mysql/plugin/client_ed25519.so

%files -n %{libname}private
%{_libdir}/libmariadbprivate.so

%files -n %{libname}-devel
%{_bindir}/mariadb_config
%{_bindir}/mysql_config
%dir %{_includedir}/mysql
%{_includedir}/mysql/*
%{_includedir}/mariadb
%{_libdir}/pkgconfig/libmariadb.pc
%{_libdir}/pkgconfig/mysqlclient.pc
%{_libdir}/libmariadb.so
%{_libdir}/libmysqlclient.so
%{_libdir}/libmysqlclient_r.so
%{_mandir}/man3/*

%changelog
