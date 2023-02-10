#
# spec file for package mysql-connector-cpp
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


%define libname libmysqlcppconn9
%define x_libname libmysqlcppconn8-2
Name:           mysql-connector-cpp
Version:        8.0.32
Release:        0
Summary:        MySQL Connector/C++: Standardized database driver for C++ development
License:        SUSE-GPL-2.0-with-FLOSS-exception
Group:          Development/Libraries/C and C++
URL:            http://dev.mysql.com/downloads/connector/
Source:         http://dev.mysql.com/get/Downloads/Connector-C++/mysql-connector-c++-%{version}-src.tar.gz
# PATCH-FIX-OPENSUSE fix options for mysql_config
Patch1:         mysql-connector-cpp-config.patch
# PATCH-FIX-UPSTREAM - bsc#1067883 kstreitova@suse.com -- fix build with libmariadb by fixing copypaste errors in libmysql_dynamic_proxy.cpp file
Patch3:         mysql-connector-cpp-libmysql_dynamic_proxy_typos.patch
# PATCH-FIX-OPENSUSE fix library to work with MariaDB instead of MySQL
Patch4:         mysql-connector-cpp-mariadb.patch
# PATCH-FIX-OPENSUSE use system protobuf (due to some build issues in OBS)
Patch6:         mysql-connector-cpp-use-system-protobuf.patch
# PATCH-FIX-OPENSUSE test for optional flag (not present in mariadb or older mysql)
Patch7:         mysql-connector-cpp-test-feature.patch
BuildRequires:  cmake >= 2.6.2
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libmysqlclient-devel
BuildRequires:  protobuf-devel
BuildRequires:  zlib-devel
Obsoletes:      mysql-connector-c++ < %{version}
Provides:       mysql-connector-c++ = %{version}
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel >= 1.34.0
%endif

%description
MySQL Connector/C++ is a library for applications written in C or C++ that
communicate with MySQL database servers. Version 8.0 of Connector/C++
implements three different APIs which can be used by applications:

* The new X DevAPI for applications written in C++.
* The new X DevAPI for C for applications written in plain C.
* The legacy JDBC4-based API also implemented in version 1.1 of the connector.

The Driver for C++ is designed to work best with MySQL 5.1 or later. Note - its
full functionality is not available when connecting to MySQL 5.0. You cannot
connect to MySQL 4.1 or earlier.

%package -n libmysqlcppconn-devel
Summary:        Development files for MySQL Connector/C++
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Obsoletes:      mysql-connector-c++-devel < %{version}
Provides:       mysql-connector-c++-devel = %{version}
%if 0%{?suse_version} > 1325
Requires:       libboost_headers-devel
%else
Requires:       boost-devel >= 1.34.0
%endif

%description -n libmysqlcppconn-devel
MySQL Connector/C++ API is a MySQL database connector for C++ development. The
MySQL driver for C++ can be used to connect to MySQL from C++ applications. The
driver mimics the JDBC 4.0 API. It implements a significant subset of JDBC 4.0.

The Driver for C++ is designed to work best with MySQL 5.1 or later. Note - its
full functionality is not available when connecting to MySQL 5.0. You cannot
connect to MySQL 4.1 or earlier.

%package -n %{libname}
Summary:        MySQL Connector/C++: Standardized database driver for C++ development
Group:          Development/Libraries/C and C++

%description -n %{libname}
MySQL Connector/C++ is a MySQL database connector for C++ development. The
MySQL driver for C++ can be used to connect to MySQL from C++ applications. The
driver mimics the JDBC 4.0 API. It implements a significant subset of JDBC 4.0.

The Driver for C++ is designed to work best with MySQL 5.1 or later. Note - its
full functionality is not available when connecting to MySQL 5.0. You cannot
connect to MySQL 4.1 or earlier.

%package -n libmysqlcppconn8-devel
Summary:        Development files for MySQL Connector/C++
Group:          Development/Libraries/C and C++
Requires:       %{x_libname} = %{version}
Obsoletes:      mysql-connector-c++-devel < %{version}
Provides:       mysql-connector-c++-devel = %{version}
%if 0%{?suse_version} > 1325
Requires:       libboost_headers-devel
%else
Requires:       boost-devel >= 1.34.0
%endif

%description -n libmysqlcppconn8-devel
MySQL Connector/C++ 8.0 implements the X DevAPI. The X DevAPI allows one to work
with MySQL Servers implementing a document store via the X Plugin. One can also
execute plain SQL queries using this API.

The Driver for C++ is designed to work best with MySQL 5.1 or later. Note - its
full functionality is not available when connecting to MySQL 5.0. You cannot
connect to MySQL 4.1 or earlier.

%package -n %{x_libname}
Summary:        MySQL Connector/C++: Standardized database driver for C++ development
Group:          Development/Libraries/C and C++

%description -n %{x_libname}
MySQL Connector/C++ 8.0 implements the X DevAPI. The X DevAPI allows one to work
with MySQL Servers implementing a document store via the X Plugin. One can also
execute plain SQL queries using this API.

The Driver for C++ is designed to work best with MySQL 5.1 or later. Note - its
full functionality is not available when connecting to MySQL 5.0. You cannot
connect to MySQL 4.1 or earlier.

%prep
%setup -q -n mysql-connector-c++-%{version}-src
%autopatch -p1
chmod -x jdbc/examples/*

%build
%cmake \
	-DMYSQLCPPCONN_GCOV_ENABLE=OFF \
	-DMYSQLCPPCONN_ICU_ENABLE=OFF \
	-DMYSQLCPPCONN_BUILD_EXAMPLES=OFF \
	-DMYSQLCLIENT_STATIC_LINKING=OFF \
	-DMYSQLCLIENT_STATIC_BINDING=0 \
	-DMYSQL_CXX_LINKAGE=0 \
    -DWITH_JDBC=ON \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib}
%cmake_build

%install
%cmake_install
rm -f %{buildroot}%{_libdir}/libmysqlcppconn-static.a
rm -f %{buildroot}%{_prefix}/[A-Z]*
mkdir -p %{buildroot}%{_docdir}/libmysqlcppconn-devel
install -m 0644 README.txt %{buildroot}%{_docdir}/libmysqlcppconn-devel/
mkdir -p %{buildroot}%{_docdir}/libmysqlcppconn-devel/examples
install -m 0644 jdbc/examples/* %{buildroot}%{_docdir}/libmysqlcppconn-devel/examples/
mkdir -p %{buildroot}%{_docdir}/libmysqlcppconn8-devel
install -m 0644 README.txt %{buildroot}%{_docdir}/libmysqlcppconn8-devel/

%fdupes -s %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post -n %{x_libname} -p /sbin/ldconfig

%postun -n %{x_libname} -p /sbin/ldconfig

%files -n libmysqlcppconn-devel
%license LICENSE.txt
%doc README.txt examples
%{_includedir}/jdbc
%{_includedir}/mysql/jdbc.h
%{_libdir}/libmysqlcppconn.so

%files -n %{libname}
%{_libdir}/libmysqlcppconn.so.*

%files -n libmysqlcppconn8-devel
%license LICENSE.txt
%doc README.txt
%{_includedir}/mysqlx
%{_libdir}/libmysqlcppconn8.so

%files -n %{x_libname}
%{_libdir}/libmysqlcppconn8.so.*

%changelog
