#
# spec file for package clucene-core
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           clucene-core
Version:        2.3.3.4
Release:        0
Summary:        CLucene is a C++ port of Lucene
License:        LGPL-2.1 OR Apache-2.0
Group:          Development/Libraries/C and C++
Url:            http://clucene.sourceforge.net/
#Git-Clone:	git://clucene.git.sourceforge.net/gitroot/clucene/clucene
Source0:        http://sourceforge.net/projects/clucene/files/clucene-core-unstable/2.3/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
# PATCH-FIX-UPSTREAM [rh#748196]
Patch0:         clucene-2.3.3.4-pkgconfig.patch
# PATCH-FIX-UPSTREAM [rh#794795]
Patch1:         clucene-2.3.3.4-contrib-libs.patch
Patch2:         clucene-kill-ext-includes.diff
Patch3:         clucene-new-gcc.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
CLucene is a C++ port of Lucene. It is a high-performance, full-featured text
search engine written in C++. CLucene is faster than lucene as it is written
in C++.

%package -n libclucene-core1
Summary:        C++ implementation of the Lucene text search engine
Group:          System/Libraries
Obsoletes:      libclucene2 < %{version}-%{release}
Provides:       libclucene2 = %{version}-%{release}

%description -n libclucene-core1
CLucene is a C++ port of Lucene. It is a high-performance, full-featured text
search engine written in C++. CLucene is faster than lucene as it is written
in C++.

%package -n libclucene-shared1
Summary:        CLucene cross-platform layer
Group:          System/Libraries

%description -n libclucene-shared1
This package creates a library that is used in all the CLucene
projects. It provides cross-platform macros and functions, as well as
things like cl_* string macros, file handling functions, replacement
functions, etc.

%package -n libclucene-contribs-lib1
Summary:        Language specific text analyzers for %{name}
Group:          Development/Libraries/C and C++

%description -n libclucene-contribs-lib1
CLucene is a C++ port of Lucene. It is a high-performance, full-featured text
search engine written in C++. CLucene is faster than lucene as it is written
in C++.

This package contains language specific text analyzers for clucene.

%package devel
Summary:        Development files for clucene library
Group:          Development/Libraries/C and C++
Requires:       libclucene-contribs-lib1 = %{version}
Requires:       libclucene-core1 = %{version}
Requires:       libclucene-shared1 = %{version}
Requires:       libstdc++-devel

%description devel
CLucene is a C++ port of Lucene. It is a high-performance, full-featured text
search engine written in C++. CLucene is faster than lucene as it is written
in C++.

This package holds the development files for clucene.

%prep
%setup -q
%autopatch -p1

# the tar ball is stripped like this:
rm -rf test/data/reuters* tests/data/utf* # test/data is not allowed to be distributed bnc#253602

%build
%cmake \
  -DBUILD_CONTRIBS_LIB=ON \
  -DLUCENE_SYS_INCLUDES=%{_libdir}
make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install

find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_libdir}/CLuceneConfig.cmake

# remove duplicates
%fdupes -s %{buildroot}

%post -n libclucene-core1 -p /sbin/ldconfig
%postun -n libclucene-core1 -p /sbin/ldconfig
%post -n libclucene-shared1 -p /sbin/ldconfig
%postun -n libclucene-shared1 -p /sbin/ldconfig
%post -n libclucene-contribs-lib1 -p /sbin/ldconfig
%postun -n libclucene-contribs-lib1 -p /sbin/ldconfig

%files -n libclucene-core1
%doc APACHE.license AUTHORS ChangeLog COPYING doc/ LGPL.license README README.PACKAGE REQUESTS
%{_libdir}/libclucene-core.so.1
%{_libdir}/libclucene-core.so.%{version}

%files -n libclucene-shared1
%doc APACHE.license COPYING LGPL.license
%{_libdir}/libclucene-shared.so.1
%{_libdir}/libclucene-shared.so.%{version}

%files -n libclucene-contribs-lib1
%{_libdir}/libclucene-contribs-lib.so.1*
%{_libdir}/libclucene-contribs-lib.so.%{version}

%files devel
%{_libdir}/libclucene*.so

%{_includedir}/CLucene*
%dir %{_libdir}/CLucene/
%{_libdir}/CLucene/clucene-config.h

%{_libdir}/CLucene/CLuceneConfig.cmake
%{_libdir}/pkgconfig/libclucene-core.pc

%changelog
