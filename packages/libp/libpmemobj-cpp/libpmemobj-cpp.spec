#
# spec file for package libpmemobj-cpp
#
# Copyright (c) 2020 SUSE LLC
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


Name:           libpmemobj-cpp
%define lname   libpmemobj-cpp0
Version:        1.11
Release:        0
Summary:        C++ bindings for libpmemobj
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://pmem.io/pmdk/
Source:         https://github.com/pmem/libpmemobj-cpp/archive/%version.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libpmemobj) >= 1.8
ExclusiveArch:  x86_64 ppc64le

%description
There are three main features of the C++ bindings to libpmemobj:

  * the `persistent_ptr<>` smart pointer,
  * the `transaction`, which comes in two flavours - scoped and closure,
  * the `p<>` property.

The main issue with the C API is a large set of macros and difficulty
in manual usage of `setjmp`.

%package devel
Summary:        C++ bindings for libpmemobj
Group:          Development/Libraries/C and C++
Obsoletes:      libpmemobj++-devel < %version
Provides:       libpmemobj++-devel = %version

%description devel
This package contains the header files for pmemobj's C++ interface.

%package devel-doc
Summary:        Example C++ programs for libpmemobj++
Group:          Documentation/Other

%description devel-doc
Example C++ programs (with source) on how to use libpmemobj++.

%prep
%autosetup -p1

%build
%cmake \
%if 0%{?suse_version} < 1500
	-DTEST_ARRAY=OFF -DTEST_VECTOR=OFF -DTEST_STRING=OFF \
	-DTEST_CONCURRENT_HASHMAP=OFF -DTEST_SEGMENT_VECTOR_ARRAY_EXPSIZE=OFF \
	-DTEST_SEGMENT_VECTOR_VECTOR_EXPSIZE=OFF \
	-DTEST_SEGMENT_VECTOR_VECTOR_FIXEDSIZE=OFF \
	-DTEST_ENUMERABLE_THREAD_SPECIFIC=OFF \
%endif
	-DCMAKE_INSTALL_DOCDIR="%_docdir/%name"
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc ChangeLog
%_includedir/libpmemobj++/
%_libdir/libpmemobj++/
%_libdir/pkgconfig/*.pc

%files devel-doc
%_docdir/%name/

%changelog
