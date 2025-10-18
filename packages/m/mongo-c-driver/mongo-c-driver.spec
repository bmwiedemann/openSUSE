#
# spec file for package mongo-c-driver
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


Name:           mongo-c-driver
Version:        1.30.2
Release:        0
Summary:        Client library written in C for MongoDB
# See THIRD_PARTY_NOTICES
License:        Apache-2.0 AND ISC AND MIT AND Zlib
Group:          Development/Libraries/C and C++
URL:            https://github.com/mongodb/mongo-c-driver
Source:         https://github.com/mongodb/mongo-c-driver/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(snappy)
BuildRequires:  pkgconfig(zlib)
Provides:       bundled(jsonsl)
Provides:       bundled(libutf8proc) = 2.8.0
Provides:       bundled(uthash) = 2.3.0

%description
mongo-c-driver is a library for building high-performance
applications that communicate with the MongoDB NoSQL
database in the C language. It can also be used to write
fast client implementations in languages such as Python,
Ruby, or Perl.

%package -n libmongoc-1_0-0
Summary:        A client library written in C for MongoDB
Group:          System/Libraries

%description -n libmongoc-1_0-0
mongo-c-driver is a library for building high-performance
applications that communicate with the MongoDB NoSQL
database in the C language.

%package devel
Summary:        Development files for mongo-c-driver
Group:          Development/Libraries/C and C++
Requires:       libmongoc-1_0-0 = %{version}

%description devel
The mongo-c-driver-devel package contains libraries and header files for
developing applications that use mongo-c-driver.

%package -n libbson-1_0-0
Summary:        A library for parsing and generating BSON documents
Group:          System/Libraries

%description -n libbson-1_0-0
Libbson is a library providing useful routines related to
building, parsing, and iterating BSON documents. It is a
useful base for those wanting to write high-performance
C extensions to higher level languages such as Python,
Ruby, or Perl.

%package -n bson-devel
Summary:        Development files for libbson
Group:          Development/Libraries/C and C++
Requires:       libbson-1_0-0 = %{version}

%description -n bson-devel
The bson-devel package contains libraries and header files for
developing applications that use libbson.

%prep
%autosetup -p1

%build
%cmake \
  -DBUILD_VERSION=%{version} \
  -DENABLE_MONGOC=ON \
  -DENABLE_BSON=ON \
  -DENABLE_STATIC=OFF \
  -DENABLE_TESTS=OFF \
  -DENABLE_ZLIB=SYSTEM
%make_jobs

%install
%cmake_install
rm %{buildroot}/%{_datadir}/mongo-c-driver/{uninstall.sh,COPYING,NEWS,README.rst,THIRD_PARTY_NOTICES}
%fdupes %{buildroot}/%{_libdir}/cmake

%ldconfig_scriptlets -n libmongoc-1_0-0
%ldconfig_scriptlets -n libbson-1_0-0

%files -n libmongoc-1_0-0
%license COPYING
%license THIRD_PARTY_NOTICES
%{_libdir}/libmongoc-1.0.so.*

%files -n libbson-1_0-0
%{_libdir}/libbson-1.0.so.*

%files devel
%doc NEWS README.rst
%{_bindir}/mongoc-stat
%{_includedir}/libmongoc-1.0
%{_libdir}/libmongoc-1.0.so
%{_libdir}/pkgconfig/libmongoc-1.0.pc
%{_libdir}/pkgconfig/libmongoc-ssl-1.0.pc
%{_libdir}/cmake/libmongoc-1.0
%{_libdir}/cmake/mongoc-1.0

%files -n bson-devel
%{_includedir}/libbson-1.0
%{_libdir}/libbson-1.0.so
%{_libdir}/pkgconfig/libbson-1.0.pc
%{_libdir}/cmake/libbson-1.0
%{_libdir}/cmake/bson-1.0

%changelog
