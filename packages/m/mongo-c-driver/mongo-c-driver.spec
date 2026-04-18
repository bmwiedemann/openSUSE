#
# spec file for package mongo-c-driver
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


%define soname 2
Name:           mongo-c-driver
Version:        2.3.0
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

%package -n libmongoc%{soname}
Summary:        A client library written in C for MongoDB
Group:          System/Libraries

%description -n libmongoc%{soname}
mongo-c-driver is a library for building high-performance
applications that communicate with the MongoDB NoSQL
database in the C language.

%package devel
Summary:        Development files for mongo-c-driver
Group:          Development/Libraries/C and C++
Requires:       libmongoc%{soname} = %{version}

%description devel
The mongo-c-driver-devel package contains libraries and header files for
developing applications that use mongo-c-driver.

%package -n libbson%{soname}
Summary:        A library for parsing and generating BSON documents
Group:          System/Libraries
Requires:       pkgconfig(libsasl2)

%description -n libbson%{soname}
Libbson is a library providing useful routines related to
building, parsing, and iterating BSON documents. It is a
useful base for those wanting to write high-performance
C extensions to higher level languages such as Python,
Ruby, or Perl.

%package -n bson-devel
Summary:        Development files for libbson
Group:          Development/Libraries/C and C++
Requires:       libbson%{soname} = %{version}

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
rm %{buildroot}/%{_datadir}/mongo-c-driver/%{version}/{uninstall.sh,COPYING,NEWS,README.rst,THIRD_PARTY_NOTICES}
%fdupes %{buildroot}/%{_libdir}/cmake

%ldconfig_scriptlets -n libmongoc%{soname}
%ldconfig_scriptlets -n libbson%{soname}

%check

%files -n libmongoc%{soname}
%license COPYING
%license THIRD_PARTY_NOTICES
%{_libdir}/libmongoc%{soname}.so.*

%files -n libbson%{soname}
%{_libdir}/libbson%{soname}.so.*

%files devel
%doc NEWS README.rst
%{_bindir}/mongoc%{soname}-stat
%{_includedir}/mongoc-%{version}
%{_libdir}/libmongoc%{soname}.so
%{_libdir}/pkgconfig/mongoc%{soname}.pc
%{_libdir}/cmake/mongoc-%{version}

%files -n bson-devel
%{_includedir}/bson-%{version}
%{_libdir}/libbson%{soname}.so
%{_libdir}/pkgconfig/bson%{soname}.pc
%{_libdir}/cmake/bson-%{version}

%changelog
