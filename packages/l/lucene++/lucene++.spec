#
# spec file for package lucene++
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


Name:           lucene++
Version:        3.0.8
Release:        0
Summary:        A high-performance, full-featured text search engine written in C++
License:        Apache-2.0 OR LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/luceneplusplus/LucenePlusPlus
Source:         https://github.com/luceneplusplus/LucenePlusPlus/archive/rel_%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM lucene++-3.0.8-fix-contrib-soname.patch -- https://github.com/luceneplusplus/LucenePlusPlus/pull/161
Patch0:         lucene++-3.0.8-fix-contrib-soname.patch
# PATCH-FIX-UPSTREAM lucene++-3.0.8-fix-pc-libdir.patch -- https://github.com/luceneplusplus/LucenePlusPlus/pull/162
Patch1:         lucene++-3.0.8-fix-pc-libdir.patch
# PATCH-FIX-UPSTREAM lucene++-3.0.8-fix-cmake-issues.patch -- https://github.com/luceneplusplus/LucenePlusPlus/pull/163
Patch2:         lucene++-3.0.8-fix-cmake-issues.patch
# PATCH-FIX-UPSTREAM lucene++-3.0.8-fix-missing-headers.patch -- hillwood@opensuse.org
# contrib headers should be installed
Patch3:         lucene++-3.0.8-fix-missing-headers.patch
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)

%description
An up to date C++ port of the popular Java Lucene library, a high-performance, full-featured text search engine.

%package -n liblucene++0
Summary:        A high-performance, full-featured text search engine written in C++
Group:          Development/Libraries/C and C++

%description -n liblucene++0
An up to date C++ port of the popular Java Lucene library, a high-performance, full-featured text search engine.

%package devel
Summary:        Development files for lucene++
Group:          Development/Libraries/C and C++
Requires:       liblucene++0 = %{version}

%description devel
Development files for lucene++, a high-performance, full-featured text search engine written in C++

%prep
%autosetup -p1 -n LucenePlusPlus-rel_%{version}

%build
%cmake -DINSTALL_GTEST=OFF
%make_build lucene++ lucene++-contrib

%install
%cmake_install

%check
# Exclude known failing test on ix86 (https://github.com/luceneplusplus/LucenePlusPlus/issues/98)
%ifarch %{ix86}
%define test_filter -Boolean2Test.testRandomQueries
%endif
# Tweak path to allow lucene++-tester to find liblucene++ and libgtest
export LD_LIBRARY_PATH="$PWD/build/src/core:$PWD/build/src/contrib:$PWD/build/lib"
build/src/test/lucene++-tester %{?test_filter:--gtest_filter=%{test_filter}}

%post -n liblucene++0 -p /sbin/ldconfig
%postun -n liblucene++0 -p /sbin/ldconfig

%files -n liblucene++0
%{_libdir}/liblucene++.so.*
%{_libdir}/liblucene++-contrib.so.*
%license COPYING APACHE.license GPL.license LGPL.license
%doc AUTHORS README* REQUESTS

%files devel
%license COPYING APACHE.license GPL.license LGPL.license
%{_includedir}/lucene++/
%{_libdir}/cmake/liblucene++/
%{_libdir}/cmake/liblucene++-contrib/
%{_libdir}/liblucene++.so
%{_libdir}/liblucene++-contrib.so
%{_libdir}/pkgconfig/liblucene++.pc
%{_libdir}/pkgconfig/liblucene++-contrib.pc

%changelog
