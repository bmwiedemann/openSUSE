#
# spec file for package embree
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019-2022 LISA GmbH, Bingen, Germany.
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


%define libname libembree3

Name:           embree
Version:        3.13.5
Release:        0
Summary:        Ray Tracing Kernels
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/embree/embree
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.1.0
BuildRequires:  gcc-c++
BuildRequires:  ispc
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  tbb-devel
BuildRequires:  pkgconfig(glfw3)
# SSE2 resp. NEON is required: https://github.com/embree/embree#supported-platforms
ExclusiveArch:  x86_64 aarch64

%description
Intel Embree is a collection of ray tracing kernels originally developed
at Intel. The target users of Intel Embree are graphics application engineers
who want to improve the performance of their photo-realistic rendering
application by leveraging Embree's ray tracing kernels.

%package devel
Summary:        Development files for embree
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Obsoletes:      %{name}-devel-static <= %{version}

%description devel
This package contains the C++ header and CMake config files.

%package -n %{libname}
Summary:        Shared library providing Embree raytracing kernels
Group:          System/Libraries

%description -n %{libname}
Embree is a collection of ray tracing kernels.

This package contains the shared library.

%prep
%autosetup -p1

%build
%limit_build -m 1700
%ifarch aarch64
# https://github.com/embree/embree/issues/410
%global optflags %{optflags} -flax-vector-conversions
%endif
%cmake \
    -DEMBREE_IGNORE_CMAKE_CXX_FLAGS=OFF \
    -DEMBREE_STATIC_LIB=OFF \
    -DEMBREE_LIB_INSTALL_DIR=%{_libdir} \
    -DEMBREE_ISPC_SUPPORT=ON \
    -DEMBREE_TASKING_SYSTEM=INTERNAL \
    -DEMBREE_RAY_MASK=ON \
    -DEMBREE_FILTER_FUNCTION=ON \
    -DEMBREE_BACKFACE_CULLING=OFF \
%ifarch x86_64
    -DEMBREE_MAX_ISA=AVX2 \
%endif
%ifarch aarch64
    -DEMBREE_ARM=ON \
%endif
    -DEMBREE_TUTORIALS=OFF

%cmake_build

%install
%cmake_install
rm -r %{buildroot}%{_mandir}
rm -r %{buildroot}/usr/share/doc

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/*.so.*

%files devel
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{_includedir}/embree3
%{_libdir}/cmake/%{name}-%{version}
%{_libdir}/*.so

%changelog
