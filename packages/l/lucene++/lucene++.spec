#
# spec file for package lucene++
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        3.0.9
Release:        0
Summary:        A high-performance, full-featured text search engine written in C++
License:        Apache-2.0 OR LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/luceneplusplus/LucenePlusPlus
Source:         https://github.com/luceneplusplus/LucenePlusPlus/archive/rel_%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM lucene++-3.0.9-fix-cmake-issues.patch -- https://github.com/luceneplusplus/LucenePlusPlus/pull/203
Patch4:         lucene++-3.0.9-fix-boost1.85.patch
# PATCH-FIX-UPSTREAM lucene++-3.0.9-migrate-to-boost-asio-io_context.patch -- https://github.com/luceneplusplus/LucenePlusPlus/pull/210
Patch5:         lucene++-3.0.9-migrate-to-boost-asio-io_context.patch
# PATCH-FIX-UPSTREAM https://github.com/luceneplusplus/LucenePlusPlus/pull/200
Patch6:         lucene++-3.0.9-fix-linking-DefaultSimilarity.patch
# PATCH-FIX-UPSTREAM https://github.com/luceneplusplus/LucenePlusPlus/pull/218
Patch7:         lucene++-3.0.9-fix-cmake.patch
# PATCH-FIX-UPSTREAM https://github.com/luceneplusplus/LucenePlusPlus/pull/219
Patch8:         lucene++-3.0.9-fix-boost1.89.patch
# PATCH-FIX-UPSTREAM -- Fix build against Boost 1.90
Patch9:         https://patch-diff.githubusercontent.com/raw/luceneplusplus/LucenePlusPlus/pull/222.patch
BuildRequires:  cmake >= 3.10
BuildRequires:  gcc-c++
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_regex-devel
%if 0%{?suse_version} < 1600
BuildRequires:  libboost_system-devel
%endif
BuildRequires:  libboost_thread-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gtest)
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
%autosetup -N -n LucenePlusPlus-rel_%{version}
%patch -p1 -P 4
%patch -p1 -P 5
%patch -p1 -P 6
%patch -p1 -P 7
%if 0%{?suse_version} >= 1600
%patch -p1 -P 8
%patch -p1 -P 9
%endif

%build
# Remove cmake4 error due to not setting
# min cmake version - sflees.de
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DINSTALL_GTEST=OFF
%make_build lucene++ lucene++-contrib

%install
%cmake_install

%check
# Disable test failing with "config out of range"
export skip_tests_filter=-$(echo \
    SortTest.testEmptyFieldSort \
    SortTest.testParallelMultiSort \
    ParallelMultiSearcherTest.testEmptyIndex \
    ParallelMultiSearcherTest.testFieldSelector \
    ParallelMultiSearcherTest.testNormalization \
    ParallelMultiSearcherTest.testCustomSimilarity \
    ParallelMultiSearcherTest.testDocFreq \
%ifarch %{ix86} # Exclude known failing test on ix86 (https://github.com/luceneplusplus/LucenePlusPlus/issues/98)
    Boolean2Test.testRandomQueries \
%endif
    %{nil} | tr ' ' ':')
# Tweak path to allow lucene++-tester to find liblucene++ and libgtest
export LD_LIBRARY_PATH="$PWD/build/src/core:$PWD/build/src/contrib:$PWD/build/lib"
build/src/test/lucene++-tester --gtest_filter="${skip_tests_filter}"

%ldconfig_scriptlets -n liblucene++0

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
