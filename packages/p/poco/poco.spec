#
# spec file for package poco
#
# Copyright (c) 2022 SUSE LLC
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


%define sover  92
# disabled for now as 4 of them fail
%bcond_with tests
Name:           poco
Version:        1.12.2
Release:        0
Summary:        C++ Framework for Network-based Applications
License:        BSL-1.0
Group:          System/Libraries
URL:            https://pocoproject.org
Source:         https://github.com/pocoproject/%{name}/archive/%{name}-%{version}-release.tar.gz
BuildRequires:  cmake >= 2.8.12
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  mysql-devel
BuildRequires:  ninja
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  unixODBC-devel
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3) >= 3.7
BuildRequires:  pkgconfig(zlib)

%description
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n poco-devel
Summary:        C++ Framework for Network-based Applications
Group:          Development/Libraries/C and C++
Requires:       libPocoCppParser%{sover} = %{version}
Requires:       libPocoCrypto%{sover} = %{version}
Requires:       libPocoData%{sover} = %{version}
Requires:       libPocoDataMySQL%{sover} = %{version}
Requires:       libPocoDataODBC%{sover} = %{version}
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
Requires:       libexpat-devel
Requires:       libmysqlclient-devel
Requires:       libstdc++-devel
Requires:       openssl-devel
Requires:       pcre-devel
Requires:       poco-cpspc = %{version}
Requires:       unixODBC-devel
Provides:       libpoco-devel = %{version}

%description -n poco-devel
C++ class libraries and frameworks for building
network- and Internet-based applications.

%package -n libPocoActiveRecord%{sover}
Summary:        POCO C++ Active Record
Group:          System/Libraries

%description -n libPocoActiveRecord%{sover}
ActiveRecord is a simple and lightweight object-relational mapping (ORM)
framework based on the Active Record pattern and the Data library.

%package -n poco-cpspc
Summary:        POCO C++ Server Page Compiler
Group:          Development/Tools/Doc Generators

%description -n poco-cpspc
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
%setup -q -n "poco-poco-%{version}-release"

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
    -DENABLE_JSON=ON \
    -DENABLE_MONGODB=ON \
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
    -DPOCO_UNBUNDLED=ON
%cmake_build

%install
%cmake_install
mv %{buildroot}/%{_bindir}/arc %{buildroot}/%{_bindir}/poco-arc
rm -rf %{buildroot}%{_libdir}/cmake/Poco/V*
%fdupes -s %{buildroot}/%{_libdir}/cmake/Poco

%check
%if %{with tests}
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}:$(pwd)/build/lib:$LD_LIBRARY_PATH
%ctest
%endif

%files -n libPocoActiveRecord%{sover}
%{_libdir}/libPocoActiveRecord.so.%{sover}

%post   -n libPocoActiveRecord%{sover} -p /sbin/ldconfig
%postun -n libPocoActiveRecord%{sover} -p /sbin/ldconfig

%files -n libPocoCrypto%{sover}
%{_libdir}/libPocoCrypto.so.%{sover}

%post   -n libPocoCrypto%{sover} -p /sbin/ldconfig
%postun -n libPocoCrypto%{sover} -p /sbin/ldconfig

%files -n libPocoCppParser%{sover}
%{_libdir}/libPocoCppParser.so.%{sover}

%post   -n libPocoCppParser%{sover} -p /sbin/ldconfig
%postun -n libPocoCppParser%{sover} -p /sbin/ldconfig

%files -n libPocoData%{sover}
%{_libdir}/libPocoData.so.%{sover}

%post   -n libPocoData%{sover} -p /sbin/ldconfig
%postun -n libPocoData%{sover} -p /sbin/ldconfig

%files -n libPocoDataMySQL%{sover}
%{_libdir}/libPocoDataMySQL.so.%{sover}

%post   -n libPocoDataMySQL%{sover} -p /sbin/ldconfig
%postun -n libPocoDataMySQL%{sover} -p /sbin/ldconfig

%files -n libPocoDataODBC%{sover}
%{_libdir}/libPocoDataODBC.so.%{sover}

%post   -n libPocoDataODBC%{sover} -p /sbin/ldconfig
%postun -n libPocoDataODBC%{sover} -p /sbin/ldconfig

%files -n libPocoDataSQLite%{sover}
%{_libdir}/libPocoDataSQLite.so.%{sover}

%post   -n libPocoDataSQLite%{sover} -p /sbin/ldconfig
%postun -n libPocoDataSQLite%{sover} -p /sbin/ldconfig

%files -n libPocoEncodings%{sover}
%{_libdir}/libPocoEncodings.so.%{sover}

%post   -n libPocoEncodings%{sover} -p /sbin/ldconfig
%postun -n libPocoEncodings%{sover} -p /sbin/ldconfig

%files -n libPocoFoundation%{sover}
%{_libdir}/libPocoFoundation.so.%{sover}

%post   -n libPocoFoundation%{sover} -p /sbin/ldconfig
%postun -n libPocoFoundation%{sover} -p /sbin/ldconfig

%files -n libPocoJSON%{sover}
%{_libdir}/libPocoJSON.so.%{sover}

%post   -n libPocoJSON%{sover} -p /sbin/ldconfig
%postun -n libPocoJSON%{sover} -p /sbin/ldconfig

%files -n libPocoMongoDB%{sover}
%{_libdir}/libPocoMongoDB.so.%{sover}

%post   -n libPocoMongoDB%{sover} -p /sbin/ldconfig
%postun -n libPocoMongoDB%{sover} -p /sbin/ldconfig

%files -n libPocoNet%{sover}
%{_libdir}/libPocoNet.so.%{sover}

%post   -n libPocoNet%{sover} -p /sbin/ldconfig
%postun -n libPocoNet%{sover} -p /sbin/ldconfig

%files -n libPocoNetSSL%{sover}
%{_libdir}/libPocoNetSSL.so.%{sover}

%post   -n libPocoNetSSL%{sover} -p /sbin/ldconfig
%postun -n libPocoNetSSL%{sover} -p /sbin/ldconfig

%files -n libPocoPDF%{sover}
%{_libdir}/libPocoPDF.so.%{sover}

%post   -n libPocoPDF%{sover} -p /sbin/ldconfig
%postun -n libPocoPDF%{sover} -p /sbin/ldconfig

%files -n libPocoPrometheus%{sover}
%{_libdir}/libPocoPrometheus.so.%{sover}

%post   -n libPocoPrometheus%{sover} -p /sbin/ldconfig
%postun -n libPocoPrometheus%{sover} -p /sbin/ldconfig

%files -n libPocoRedis%{sover}
%{_libdir}/libPocoRedis.so.%{sover}

%post   -n libPocoRedis%{sover} -p /sbin/ldconfig
%postun -n libPocoRedis%{sover} -p /sbin/ldconfig

%files -n libPocoUtil%{sover}
%{_libdir}/libPocoUtil.so.%{sover}

%post   -n libPocoUtil%{sover} -p /sbin/ldconfig
%postun -n libPocoUtil%{sover} -p /sbin/ldconfig

%files -n libPocoXML%{sover}
%{_libdir}/libPocoXML.so.%{sover}

%post   -n libPocoXML%{sover} -p /sbin/ldconfig
%postun -n libPocoXML%{sover} -p /sbin/ldconfig

%files -n libPocoZip%{sover}
%{_libdir}/libPocoZip.so.%{sover}

%post   -n libPocoZip%{sover} -p /sbin/ldconfig
%postun -n libPocoZip%{sover} -p /sbin/ldconfig

%files -n libPocoJWT%{sover}
%{_libdir}/libPocoJWT.so.%{sover}

%post   -n libPocoJWT%{sover} -p /sbin/ldconfig
%postun -n libPocoJWT%{sover} -p /sbin/ldconfig

%files -n poco-devel
%license LICENSE
%doc CHANGELOG CONTRIBUTORS NEWS README
%{_includedir}/Poco
%{_bindir}/poco-arc
%{_libdir}/libPoco*.so
%dir %{_libdir}/cmake/Poco/
%{_libdir}/cmake/Poco/*.cmake

%files -n poco-cpspc
%{_bindir}/cpspc
%{_bindir}/f2cpsp

%changelog
