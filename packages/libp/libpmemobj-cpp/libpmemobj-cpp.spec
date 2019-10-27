#
# spec file for package libpmemobj-cpp
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


Name:           libpmemobj-cpp
%define lname   libpmemobj-cpp0
Summary:        C++ bindings for libpmemobj
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Version:        1.8
Release:        0
URL:            http://pmem.io/pmdk/
Source:         https://github.com/pmem/libpmemobj-cpp/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libpmemobj) >= 1.7
ExclusiveArch:  x86_64

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
Obsoletes:      libpmemobj++-devel < %{version}
Provides:       libpmemobj++-devel = %{version}

%description devel
This package contains the header files for pmemobj's C++ interface.

%package devel-doc
Summary:        Example C++ programs for libpmemobj++
Group:          Documentation/Other

%description devel-doc
Example C++ programs (with source) on how to use libpmemobj++.

%prep
%setup -q

%build
%cmake \
%if %{suse_version} < 1500
	-DENABLE_ARRAY=OFF -DENABLE_VECTOR=OFF -DENABLE_STRING=OFF	\
%endif
	-DCMAKE_INSTALL_DOCDIR="%_docdir/%name"
make %{?_smp_mflags}

%install
%cmake_install

%files devel
%license LICENSE
%doc ChangeLog
%_includedir/libpmemobj++/
%_libdir/libpmemobj++/
%{_libdir}/pkgconfig/*.pc

%files devel-doc
%_docdir/%name/

%changelog
