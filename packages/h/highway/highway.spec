#
# spec file for package highway
#
# Copyright (c) 2025 SUSE LLC
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


%define lname libhwy1

Name:           highway
Version:        1.2.0
Release:        0
Summary:        C++ library providing SIMD/vector intrinsics
License:        Apache-2.0 OR BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/google/highway
Source:         https://github.com/google/highway/archive/refs/tags/%version.tar.gz
Source1:        baselibs.conf
Patch1:         no-forced-inline.diff
# https://github.com/google/highway/issues/776
%if 0%{?suse_version} > 1550
BuildRequires:  c++_compiler
%else
BuildRequires:  gcc10-c++
%endif
BuildRequires:  cmake
BuildRequires:  memory-constraints
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(gtest)

%description
Highway is a C++ library that provides portable SIMD/vector intrinsics.

%package -n %lname
Summary:        Efficient and performance-portable SIMD
Group:          Development/Libraries/C and C++

%description -n %lname
Highway is a C++ library that provides portable SIMD/vector intrinsics.

%package devel
Summary:        Development files for Highway
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Highway is a C++ library that provides portable SIMD/vector intrinsics.

Development files for Highway.

%package devel-doc
Summary:        Documentation for Highway
Group:          Documentation/Other
BuildArch:      noarch

%description devel-doc
Highway is a C++ library that provides portable SIMD/vector intrinsics.

Documentation for Highway development.

%prep
%autosetup -p1

%ifarch riscv64
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=110812
%global _lto_cflags %{nil}
%endif

%build
export CFLAGS="%optflags -DHWY_COMPILE_ALL_ATTAINABLE"
%ifarch ppc64 ppc64le
CFLAGS="$CFLAGS -maltivec"
%endif
export CXXFLAGS="$CFLAGS"
%if 0%{?suse_version} < 1550
export CXX=g++-10
%endif
%limit_build -m 1400

%cmake \
%ifarch %arm
	-DHWY_CMAKE_ARM7:BOOL=OFF \
%endif
	-DCMAKE_SKIP_RPATH:BOOL=OFF \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
	-DHWY_SYSTEM_GTEST:BOOL=ON
%cmake_build

%install
%cmake_install

%check
export CTEST_PARALLEL_LEVEL=2
%ctest --parallel 2 --verbose || :

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libhwy*.so.*
%license LICENSE

%files devel
%_includedir/hwy/
%_libdir/libhwy*.so
%_libdir/pkgconfig/*.pc
%_libdir/cmake/

%files devel-doc
%doc README.md g3doc/* hwy/examples/

%changelog
