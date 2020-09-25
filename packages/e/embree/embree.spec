#
# spec file for package embree
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019-2020 LISA GmbH, Bingen, Germany.
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


Name:           embree
Version:        3.11.0
Release:        0
Summary:        Ray Tracing Kernels
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/embree/embree
Source:         https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 2.8.6
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  tbb-devel
BuildRequires:  pkgconfig(glfw3)
# SSE2 is required: https://github.com/embree/embree/issues/186
ExclusiveArch:  x86_64

%description
Intel Embree is a collection of ray tracing kernels originally developed
at Intel. The target users of Intel Embree are graphics application engineers
who want to improve the performance of their photo-realistic rendering
application by leveraging Embree's ray tracing kernels.

Note:
This version is specifically dedicated to Blender Cycles, as it is using the
build options that are required for it. In order to reduce the risk of
incompatibilities, it is built as static libraries, which is also enforced by
the Blender Cycles build for the time being.

%package	devel-static
Summary:        Development files for embree
Group:          Development/Libraries/C and C++
Provides:       %{name} = %{version}

%description	devel-static
This package contains the C++ header files and static libraries for %{name},
specifically compiled for Blender Cycles needs.

%prep
%setup -q

%build
# we need fat lto objects here
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CXXFLAGS="%{optflags}"
# blender insists in using static embree
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DEMBREE_STATIC_LIB=ON \
    -DEMBREE_LIB_INSTALL_DIR=%{_libdir} \
    -DEMBREE_ISPC_SUPPORT=OFF \
    -DEMBREE_TUTORIALS=OFF \
    -DEMBREE_RAY_MASK=ON \
    -DEMBREE_FILTER_FUNCTION=ON \
    -DEMBREE_BACKFACE_CULLING=OFF \
    -DEMBREE_MAX_ISA=AVX2

%make_build

%install
%cmake_install
mv %{buildroot}%{_libdir}/cmake/%{name}-%{version} %{buildroot}%{_libdir}/cmake/%{name}3
rm -r %{buildroot}%{_mandir}
rm -r %{buildroot}/usr/share/doc

%files devel-static
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{_includedir}/embree3
%{_libdir}/cmake/embree3
%{_libdir}/*.a

%changelog
