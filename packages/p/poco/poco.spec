#
# spec file for package poco
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover  112
# disabled for now as 4 of them fail
%bcond_with tests
Name:           poco
Version:        1.14.2
Release:        0
Summary:        C++ Framework for Network-based Applications
License:        BSL-1.0
Group:          Development/Libraries/C and C++
URL:            https://pocoproject.org
Source:         https://github.com/pocoproject/%{name}/archive/%{name}-%{version}-release.tar.gz
BuildRequires:  apache2-devel
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.15
BuildRequires:  fdupes
BuildRequires:  mysql-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(apr-1)
BuildRequires:  pkgconfig(apr-util-1)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(odbc)
BuildRequires:  pkgconfig(sqlite3) >= 3.7
BuildRequires:  pkgconfig(zlib)

%description
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package devel
Summary:        C++ Framework for Network-based Applications
Group:          Development/Libraries/C and C++
Requires:       libPocoCppParser%{sover} = %{version}
Requires:       libPocoCrypto%{sover} = %{version}
Requires:       libPocoData%{sover} = %{version}
Requires:       libPocoDataMySQL%{sover} = %{version}
Requires:       libPocoDataODBC%{sover} = %{version}
Requires:       libPocoDataPostgreSQL%{sover} = %{version}
Requires:       libPocoDataSQLite%{sover} = %{version}
Requires:       libPocoEncodings%{sover} = %{version}
Requires:       libPocoFoundation%{sover} = %{version}
Requires:       libPocoJSON%{sover} = %{version}
Requires:       libPocoJWT%{sover} = %{version}
Requires:       libPocoMongoDB%{sover} = %{version}
Requires:       libPocoNet%{sover} = %{version}
Requires:       libPocoNetSSL%{sover} = %{version}
Requires:       libPocoPDF%{sover} = %{version}
Requires:       libPocoPrometheus%{sover} = %{version}
Requires:       libPocoRedis%{sover} = %{version}
Requires:       libPocoUtil%{sover} = %{version}
Requires:       libPocoXML%{sover} = %{version}
Requires:       libPocoZip%{sover} = %{version}
Requires:       poco-cpspc = %{version}
Provides:       libpoco-devel = %{version}

%description devel
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoActiveRecord%{sover}
Summary:        POCO C++ Active Record
Group:          System/Libraries

%description -n libPocoActiveRecord%{sover}
ActiveRecord is a simple and lightweight object-relational mapping (ORM)
framework based on the Active Record pattern and the Data library.

%package cpspc
Summary:        POCO C++ Server Page Compiler
Group:          Development/Tools/Doc Generators

%description cpspc
This program compiles web pages containing embedded C++ code into a C++ class
that can be used with the HTTP server from the POCO Net library.

%package -n libPocoCrypto%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-crypto = %{version}

%description -n libPocoCrypto%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoCppParser%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-cppparser = %{version}

%description -n libPocoCppParser%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoData%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-data = %{version}

%description -n libPocoData%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoDataMySQL%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-datamysql = %{version}

%description -n libPocoDataMySQL%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoDataODBC%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-dataodbc = %{version}

%description -n libPocoDataODBC%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoDataPostgreSQL%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-datapostgresql = %{version}

%description -n libPocoDataPostgreSQL%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoDataSQLite%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-datasqlite = %{version}

%description -n libPocoDataSQLite%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoEncodings%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-encodings = %{version}

%description -n libPocoEncodings%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoFoundation%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-foundation = %{version}

%description -n libPocoFoundation%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoJSON%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-json = %{version}

%description -n libPocoJSON%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoMongoDB%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-mongodb = %{version}

%description -n libPocoMongoDB%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoRedis%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-redis = %{version}

%description -n libPocoRedis%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoNet%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-net = %{version}

%description -n libPocoNet%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoNetSSL%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-netssl = %{version}

%description -n libPocoNetSSL%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoPDF%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-pdf = %{version}

%description -n libPocoPDF%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoPrometheus%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-prometheus = %{version}

%description -n libPocoPrometheus%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoUtil%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-util = %{version}

%description -n libPocoUtil%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoXML%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-xml = %{version}

%description -n libPocoXML%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoZip%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-zip = %{version}

%description -n libPocoZip%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoJWT%{sover}
Summary:        C++ Framework for Network-based Applications
Group:          System/Libraries
Provides:       poco-jwt = %{version}

%description -n libPocoJWT%{sover}
C++ class libraries and frameworks for building
network- and Internet-based applications.

%prep
%autosetup -p1 -n poco-poco-%{version}-release

%build
# ENABLE_APPACHECONNECTOR
# ENABLE_SEVENZIP
# ENABLE_PODOC
%define __builder ninja
%cmake \
    -DCMAKE_SHARED_LINKER_FLAGS="" \
    -DENABLE_CPPPARSER=ON \
    -DENABLE_CRYPTO=ON \
    -DENABLE_DATA=ON \
    -DENABLE_DATA_MYSQL=ON \
    -DENABLE_DATA_ODBC=ON \
    -DENABLE_DATA_SQLITE=ON \
    -DENABLE_DATA_POSTGRESQL=ON \
    -DENABLE_JSON=ON \
    -DENABLE_MONGODB=ON \
    -DENABLE_APACHECONNECTOR=ON \
    -DENABLE_NET=ON \
    -DENABLE_NETSSL=ON \
    -DENABLE_NETSSL_WIN=OFF \
    -DENABLE_PAGECOMPILER=ON \
    -DENABLE_PAGECOMPILER_FILE2PAGE=ON \
    -DENABLE_PDF=ON \
    -DENABLE_UTIL=ON \
    -DENABLE_XML=ON \
    -DENABLE_ZIP=ON \
%if %{with tests}
    -DENABLE_TESTS=ON \
%endif
    -DFORCE_OPENSSL=ON \
    -DPOCO_UNBUNDLED=ON \
    %{nil}
%cmake_build

%install
%cmake_install

%fdupes %{buildroot}/%{_libdir}/cmake/Poco

%check
%if %{with tests}
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}:$(pwd)/build/lib:$LD_LIBRARY_PATH
%ctest
%endif

%ldconfig_scriptlets -n libPocoActiveRecord%{sover}
%ldconfig_scriptlets -n libPocoCrypto%{sover}
%ldconfig_scriptlets -n libPocoCppParser%{sover}
%ldconfig_scriptlets -n libPocoData%{sover}
%ldconfig_scriptlets -n libPocoDataMySQL%{sover}
%ldconfig_scriptlets -n libPocoDataODBC%{sover}
%ldconfig_scriptlets -n libPocoDataPostgreSQL%{sover}
%ldconfig_scriptlets -n libPocoDataSQLite%{sover}
%ldconfig_scriptlets -n libPocoEncodings%{sover}
%ldconfig_scriptlets -n libPocoFoundation%{sover}
%ldconfig_scriptlets -n libPocoJSON%{sover}
%ldconfig_scriptlets -n libPocoMongoDB%{sover}
%ldconfig_scriptlets -n libPocoNet%{sover}
%ldconfig_scriptlets -n libPocoNetSSL%{sover}
%ldconfig_scriptlets -n libPocoPDF%{sover}
%ldconfig_scriptlets -n libPocoPrometheus%{sover}
%ldconfig_scriptlets -n libPocoRedis%{sover}
%ldconfig_scriptlets -n libPocoUtil%{sover}
%ldconfig_scriptlets -n libPocoXML%{sover}
%ldconfig_scriptlets -n libPocoZip%{sover}
%ldconfig_scriptlets -n libPocoJWT%{sover}

%files -n libPocoActiveRecord%{sover}
%license LICENSE
%{_libdir}/libPocoActiveRecord.so.%{sover}

%files -n libPocoCrypto%{sover}
%license LICENSE
%{_libdir}/libPocoCrypto.so.%{sover}

%files -n libPocoCppParser%{sover}
%license LICENSE
%{_libdir}/libPocoCppParser.so.%{sover}

%files -n libPocoData%{sover}
%license LICENSE
%{_libdir}/libPocoData.so.%{sover}

%files -n libPocoDataMySQL%{sover}
%license LICENSE
%{_libdir}/libPocoDataMySQL.so.%{sover}

%files -n libPocoDataODBC%{sover}
%license LICENSE
%{_libdir}/libPocoDataODBC.so.%{sover}

%files -n libPocoDataPostgreSQL%{sover}
%license LICENSE
%{_libdir}/libPocoDataPostgreSQL.so.%{sover}

%files -n libPocoDataSQLite%{sover}
%license LICENSE
%{_libdir}/libPocoDataSQLite.so.%{sover}

%files -n libPocoEncodings%{sover}
%license LICENSE
%{_libdir}/libPocoEncodings.so.%{sover}

%files -n libPocoFoundation%{sover}
%license LICENSE
%{_libdir}/libPocoFoundation.so.%{sover}

%files -n libPocoJSON%{sover}
%license LICENSE
%{_libdir}/libPocoJSON.so.%{sover}

%files -n libPocoMongoDB%{sover}
%license LICENSE
%{_libdir}/libPocoMongoDB.so.%{sover}

%files -n libPocoNet%{sover}
%license LICENSE
%{_libdir}/libPocoNet.so.%{sover}

%files -n libPocoNetSSL%{sover}
%license LICENSE
%{_libdir}/libPocoNetSSL.so.%{sover}

%files -n libPocoPDF%{sover}
%license LICENSE
%{_libdir}/libPocoPDF.so.%{sover}

%files -n libPocoPrometheus%{sover}
%license LICENSE
%{_libdir}/libPocoPrometheus.so.%{sover}

%files -n libPocoRedis%{sover}
%license LICENSE
%{_libdir}/libPocoRedis.so.%{sover}

%files -n libPocoUtil%{sover}
%license LICENSE
%{_libdir}/libPocoUtil.so.%{sover}

%files -n libPocoXML%{sover}
%license LICENSE
%{_libdir}/libPocoXML.so.%{sover}

%files -n libPocoZip%{sover}
%license LICENSE
%{_libdir}/libPocoZip.so.%{sover}

%files -n libPocoJWT%{sover}
%license LICENSE
%{_libdir}/libPocoJWT.so.%{sover}

%files devel
%license LICENSE
%doc CHANGELOG CONTRIBUTORS README
%{_includedir}/Poco
%{_bindir}/poco-arc
%{_libdir}/libPoco*.so
%dir %{_libdir}/cmake/Poco/
%{_libdir}/cmake/Poco/*.cmake

%files cpspc
%license LICENSE
%{_bindir}/cpspc
%{_bindir}/f2cpsp

%changelog
