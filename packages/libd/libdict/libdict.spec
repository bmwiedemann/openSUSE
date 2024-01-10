#
# spec file for package libdict
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2022, Martin Hauke <mardnh@gmx.de>
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


%define sover 1_0
Name:           libdict
Version:        1.0.3
Release:        0
Summary:        C library of key-value data structures with an object-oriented interface
License:        BSD-2-Clause
Group:          Development/Languages/C and C++
URL:            https://github.com/rtbrick/libdict
Source:         https://github.com/rtbrick/libdict/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         libsuffix.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cunit)

%description
libdict is a C library that provides the following data structures with
efficient insert, lookup, and delete routines:

* height-balanced (AVL) tree
* red-black tree
* splay tree
* weight-balanced tree
* path-reduction tree
* treap
* hashtable, using separate chaining
* hashtable, using open addressing with linear probing

%package -n libdict%{sover}
Summary:        C library of key-value data structures with an object-oriented interface
Group:          System/Libraries

%description -n libdict%{sover}
libdict is a C library that provides the following data structures with
efficient insert, lookup, and delete routines.

%package devel
Summary:        Header files for libdict
Group:          Development/Libraries/C and C++
Requires:       libdict%{sover} = %{version}

%description devel
Development and header files for libdict.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%post   -n libdict%{sover} -p /sbin/ldconfig
%postun -n libdict%{sover} -p /sbin/ldconfig

%files -n libdict%{sover}
%license LICENSE
%doc README.md REFERENCES
%{_libdir}/libdict.so.1.*

%files devel
%{_bindir}/libdict-anagram
%{_bindir}/libdict-benchmark
%{_bindir}/libdict-demo
%{_includedir}/libdict
%{_libdir}/libdict.so

%changelog
