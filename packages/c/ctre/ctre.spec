#
# spec file for package ctre
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


%define __builder ninja
Name:           ctre
Version:        3.11.0
Release:        0
Summary:        Compile time regular expressions library
License:        Apache-2.0
URL:            https://compile-time.re
Source:         https://github.com/hanickadot/compile-time-regular-expressions/archive/refs/tags/v%{version}.tar.gz#/%{name}-%version.tar.gz
# PATCH-FIX-UPSTREAM ctre-cmake-4_4-compat.patch gh#hanickadot/compile-time-regular-expressions#368 badshah400@gmail.com -- Make build compatible with cmake 4.4 by adding appropriate CMAKE_EXPERIMENTAL_CXX_IMPORT_STD key from upstream cmake [https://github.com/Kitware/CMake/blob/master/Help/dev/experimental.rst]
Patch0:         ctre-cmake-4_4-compat.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig

%description
A compile-time regular expressions with support for
matching/searching/capturing during compile-time or runtime.

%package devel
Summary:        Header and cmake files for ctre, a regular expressions library

%description devel
This package provides the header files and other development files needed for
developing applications against ctre.

%prep
%autosetup -p1 -n compile-time-regular-expressions-%{version}
sed -Ei "s/VERSION 3.9.0/VERSION 3.11.0/" CMakeLists.txt

%build
%cmake \
  -DCTRE_MODULE:BOOL=OFF \
	-DCTRE_BUILD_TESTS:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%make_build

%files devel
%license LICENSE
%doc README.md
%{_includedir}/ctll/
%{_includedir}/ctre/
%{_includedir}/unicode-db/
%{_includedir}/*.hpp
%{_libdir}/cmake/ctre/
%{_libdir}/pkgconfig/*.pc

%changelog
