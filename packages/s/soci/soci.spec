#
# spec file for package soci
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


%define sover   4
%bcond_without tests
Name:           soci
Version:        4.1.4
Release:        0
Summary:        The C++ Database Access Library
License:        BSL-1.0
URL:            https://soci.sourceforge.io/
Source:         https://github.com/SOCI/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(odbc)
BuildRequires:  pkgconfig(sqlite3)
%if 0%{?suse_version}
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

%package -n lib%{name}_core%{sover}
Summary:        The C++ Database Access Library
Requires:       lib%{name}%{sover}-backend
Suggests:       lib%{name}_empty%{sover}

%description -n lib%{name}_core%{sover}
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

%package        devel
Summary:        Development files for soci
Requires:       lib%{name}_core%{sover} = %{version}
%if 0%{?suse_version}
Requires:       libboost_headers-devel
%else
Requires:       boost-devel
%endif

%description    devel
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

The soci development package includes the header files, libraries,
development tools necessary for compiling and linking applications
which will use soci.

%package -n lib%{name}_empty%{sover}
Summary:        Empty back-end for soci
Provides:       lib%{name}%{sover}-backend = %{version}

%description -n lib%{name}_empty%{sover}
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

This package contains an empty back-end.

%package empty-devel
Summary:        Development files for the soci empty back-end
Requires:       %{name}-devel = %{version}
Requires:       lib%{name}_empty%{sover} = %{version}

%description empty-devel
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

The soci development package includes the header files, libraries,
development tools necessary for compiling and linking applications
which will use soci with an empty back-end.

%package -n lib%{name}_sqlite3-%{sover}
Summary:        SQLite back-end for soci
Provides:       lib%{name}%{sover}-backend = %{version}

%description -n lib%{name}_sqlite3-%{sover}
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

This package contains the back-end for SQLite.

%package sqlite3-devel
Summary:        Development files for the soci SQLite back-end
Requires:       %{name}-devel = %{version}
Requires:       lib%{name}_sqlite3-%{sover} = %{version}
Requires:       pkgconfig(sqlite3)

%description sqlite3-devel
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

The soci development package includes the header files, libraries,
development tools necessary for compiling and linking applications
which will use soci with SQLite.

%package -n lib%{name}_postgresql%{sover}
Summary:        PostgreSQL back-end for soci
Provides:       lib%{name}%{sover}-backend = %{version}

%description -n lib%{name}_postgresql%{sover}
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

This package contains the back-end for PostgreSQL.

%package postgresql-devel
Summary:        Development files for the soci PostgreSQL back-end
Requires:       %{name}-devel = %{version}
Requires:       lib%{name}_postgresql%{sover} = %{version}
Requires:       pkgconfig(libpq)

%description postgresql-devel
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

The soci development package includes the header files, libraries,
development tools necessary for compiling and linking applications
which will use soci with PostgreSQL.

%package -n lib%{name}_mysql%{sover}
Summary:        MariaDB back-end for soci
Provides:       lib%{name}%{sover}-backend = %{version}

%description -n lib%{name}_mysql%{sover}
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

This package contains the back-end for MariaDB.

%package mysql-devel
Summary:        Development files for the soci MariaDB back-end
Requires:       %{name}-devel = %{version}
Requires:       lib%{name}_mysql%{sover} = %{version}
Requires:       pkgconfig(libmariadb)

%description mysql-devel
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

The soci development package includes the header files, libraries,
development tools necessary for compiling and linking applications
which will use soci with MariaDB.

%package -n lib%{name}_odbc%{sover}
Summary:        ODBC back-end for soci
Provides:       lib%{name}%{sover}-backend = %{version}

%description -n lib%{name}_odbc%{sover}
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

This package contains the back-end for unixODBC.

%package odbc-devel
Summary:        Development files for the soci ODBC back-end
Requires:       %{name}-devel = %{version}
Requires:       lib%{name}_odbc%{sover} = %{version}
Requires:       pkgconfig(odbc)

%description odbc-devel
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

The soci development package includes the header files, libraries,
development tools necessary for compiling and linking applications
which will use soci with unixODBC.

%prep
%autosetup -p1

%build
# Support for building tests.
%define soci_testflags -DSOCI_TESTS=OFF
%if %{with tests}
%define soci_testflags -DSOCI_TESTS=ON -DSOCI_EMPTY_TEST_CONNSTR="dummy" -DSOCI_SQLITE3_TEST_CONNSTR="test.db" -DSOCI_POSTGRESQL_TEST_CONNSTR:STRING="dbname=soci_test" -DSOCI_MYSQL_TEST_CONNSTR:STRING="db=soci_test user=mloskot password=pantera"
%endif

%cmake \
  -DWITH_BOOST=ON       \
  -DSOCI_EMPTY=ON       \
  -DSOCI_SQLITE3=ON     \
  -DSOCI_POSTGRESQL=ON  \
  -DSOCI_MYSQL=ON       \
  -DSOCI_ODBC=ON        \
  -DSOCI_FIREBIRD=OFF   \
  -DSOCI_DB2=OFF        \
  -DSOCI_ORACLE=OFF     \
  -DSOCI_FMT_BUILTIN=OFF \
  -DSOCI_SQLITE3_BUILTIN=OFF \
  %{soci_testflags}
%cmake_build

%install
%cmake_install

%if %{with tests}
%check
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:%{buildroot}%{_libdir}
%{ctest --exclude-regex 'soci_(odbc|mysql|postgresql)_test'}
%endif

%post -n lib%{name}_core%{sover} -p /sbin/ldconfig
%postun -n lib%{name}_core%{sover} -p /sbin/ldconfig
%post -n lib%{name}_empty%{sover} -p /sbin/ldconfig
%postun -n lib%{name}_empty%{sover} -p /sbin/ldconfig
%post -n lib%{name}_sqlite3-%{sover} -p /sbin/ldconfig
%postun -n lib%{name}_sqlite3-%{sover} -p /sbin/ldconfig
%post -n lib%{name}_postgresql%{sover} -p /sbin/ldconfig
%postun -n lib%{name}_postgresql%{sover} -p /sbin/ldconfig
%post -n lib%{name}_mysql%{sover} -p /sbin/ldconfig
%postun -n lib%{name}_mysql%{sover} -p /sbin/ldconfig
%post -n lib%{name}_odbc%{sover} -p /sbin/ldconfig
%postun -n lib%{name}_odbc%{sover} -p /sbin/ldconfig

%files -n lib%{name}_core%{sover}
%license LICENSE_1_0.txt
%doc AUTHORS CHANGES README.md
%{_libdir}/lib%{name}_core.so.*

%files devel
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/*.h
%{_libdir}/lib%{name}_core.so
%{_libdir}/cmake/soci-%{version}/

%files -n lib%{name}_empty%{sover}
%{_libdir}/lib%{name}_empty.so.*

%files empty-devel
%{_includedir}/%{name}/empty/
%{_libdir}/lib%{name}_empty.so

%files -n lib%{name}_sqlite3-%{sover}
%{_libdir}/lib%{name}_sqlite3.so.*

%files sqlite3-devel
%{_includedir}/%{name}/sqlite3/
%{_libdir}/lib%{name}_sqlite3.so

%files -n lib%{name}_postgresql%{sover}
%{_libdir}/lib%{name}_postgresql.so.*

%files postgresql-devel
%{_includedir}/%{name}/postgresql/
%{_libdir}/lib%{name}_postgresql.so

%files -n lib%{name}_mysql%{sover}
%{_libdir}/lib%{name}_mysql.so.*

%files mysql-devel
%{_includedir}/%{name}/mysql/
%{_libdir}/lib%{name}_mysql.so

%files -n lib%{name}_odbc%{sover}
%{_libdir}/lib%{name}_odbc.so.*

%files odbc-devel
%{_includedir}/%{name}/odbc/
%{_libdir}/lib%{name}_odbc.so

%changelog
