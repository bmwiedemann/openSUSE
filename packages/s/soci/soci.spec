#
# spec file for package soci
#
# Copyright (c) 2021 SUSE LLC
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


%define sover   4_0
%bcond_without tests
Name:           soci
Version:        4.0.2
Release:        0
Summary:        The C++ Database Access Library
License:        BSL-1.0
Group:          Productivity/Databases/Tools
URL:            https://soci.sourceforge.io/
Source:         https://github.com/SOCI/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE fix-build-when-SIGSTKSZ-is-no-longer-a-constant.patch -- upstream commit
Patch0:         fix-build-when-SIGSTKSZ-is-no-longer-a-constant.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
%if 0%{?suse_version}
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(odbc)
BuildRequires:  pkgconfig(sqlite3)

%description
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

%package -n lib%{name}_core%{sover}
Summary:        The C++ Database Access Library
Group:          Productivity/Databases/Tools
Requires:       lib%{name}%{sover}-backend
Suggests:       lib%{name}_empty%{sover}

%description -n lib%{name}_core%{sover}
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

%package        devel
Summary:        Development files for soci
Group:          Development/Tools/Other
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
Group:          Productivity/Databases/Tools
Provides:       lib%{name}%{sover}-backend = %{version}

%description -n lib%{name}_empty%{sover}
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

This package contains an empty back-end.

%package empty-devel
Summary:        Development files for the soci empty back-end
Group:          Development/Tools/Other
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
Group:          Productivity/Databases/Tools
Provides:       lib%{name}%{sover}-backend = %{version}

%description -n lib%{name}_sqlite3-%{sover}
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

This package contains the back-end for SQLite.

%package sqlite3-devel
Summary:        Development files for the soci SQLite back-end
Group:          Development/Tools/Other
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
Group:          Productivity/Databases/Tools
Provides:       lib%{name}%{sover}-backend = %{version}

%description -n lib%{name}_postgresql%{sover}
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

This package contains the back-end for PostgreSQL.

%package postgresql-devel
Summary:        Development files for the soci PostgreSQL back-end
Group:          Development/Tools/Other
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
Group:          Productivity/Databases/Tools
Provides:       lib%{name}%{sover}-backend = %{version}

%description -n lib%{name}_mysql%{sover}
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

This package contains the back-end for MariaDB.

%package mysql-devel
Summary:        Development files for the soci MariaDB back-end
Group:          Development/Tools/Other
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
Group:          Productivity/Databases/Tools
Provides:       lib%{name}%{sover}-backend = %{version}

%description -n lib%{name}_odbc%{sover}
soci is a C++ database access library that provides the illusion of
embedding SQL in regular C++ code, staying entirely within the C++
standard.

This package contains the back-end for unixODBC.

%package odbc-devel
Summary:        Development files for the soci ODBC back-end
Group:          Development/Tools/Other
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
%setup -q
%patch0 -p1

sed -i 's/-Werror //' cmake/SociConfig.cmake

%build
# Support for building tests.
%define soci_testflags -DBUILD_TESTS="NONE"
%if %{with tests}
%define soci_testflags -DSOCI_TEST=ON -DSOCI_TEST_EMPTY_CONNSTR="dummy" -DSOCI_TEST_SQLITE3_CONNSTR="test.db" -DSOCI_TEST_POSTGRESQL_CONNSTR:STRING="dbname=soci_test" -DSOCI_TEST_MYSQL_CONNSTR:STRING="db=soci_test user=mloskot password=pantera"
%endif

%cmake \
  -DWITH_BOOST=ON      \
  -DWITH_EMPTY=ON      \
  -DWITH_SQLITE3=ON    \
  -DWITH_POSTGRESQL=ON \
  -DWITH_MYSQL=ON      \
  -DWITH_ODBC=ON       \
  -DWITH_FIREBIRD=OFF  \
  -DWITH_DB2=OFF       \
  -DWITH_ORACLE=OFF    \
  %{soci_testflags}    \
  -DSOCI_CXX11=ON      \
  -DSOCI_STATIC=OFF
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
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/SOCI
%{_libdir}/cmake/SOCI/*.cmake

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
