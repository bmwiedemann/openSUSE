#
# spec file for package pocl
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2014 Guillaume GARDET <guillaume@opensuse.org>
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


%global sover  2

%if 0%{?suse_version} >= 1600
  %bcond_without  spirv
%else
  %bcond_with     spirv
%endif

%if 0%{?suse_version} >= 1600
  %bcond_without  ttb
%else
  %bcond_with     ttb
%endif
%if 0%{?suse_version} >= 1600
  %bcond_without  levelzero
%else
  %bcond_with     levelzero
%endif

%bcond_with vulkan

Name:           pocl
Version:        7.0
Release:        0
Summary:        Portable Computing Language - an OpenCL implementation
# The whole code is under MIT
# except include/utlist.h which is under BSD (and unbundled)
License:        MIT
Group:          Development/Tools/Other
URL:            https://portablecl.org/
Source0:        https://github.com/pocl/pocl/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source98:       maint.README
Source99:       pocl-rpmlintrc
# Version 7.0: Supports LLVM versions 19 and 20
BuildRequires:  ((clang-devel >= 19 with clang-devel < 21) or clang20-devel)
BuildRequires:  cmake >= 3.15
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(hwloc)
BuildRequires:  pkgconfig(ocl-icd)
# PPC has limited support/testing from upstream
# s390(x) is also not supported, so use ExclusiveArch
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 riscv64
%if %{with ttb}
BuildRequires:  pkgconfig(tbb)
%endif
%if %{with spirv}
BuildRequires:  libLLVMSPIRVLib-devel
BuildRequires:  spirv-tools
%endif
%if %{with levelzero}
BuildRequires:  pkgconfig(level-zero)
%endif
%if %{with vulkan}
BuildRequires:  pkgconfig(vulkan)
%endif

%description
Portable Computing Language (pocl) is an implementation of the OpenCL standard
which can be adapted for new targets and devices, both for homogeneous CPU and
heterogenous GPUs/accelerators.

pocl uses Clang as an OpenCL C frontend and LLVM for the kernel compiler
implementation, and as a portability layer. If your desired target has an LLVM
backend, it should be possible to get OpenCL support by using pocl.

pocl yields improved performance portability by using a kernel compiler that
can generate multi-work-item work-group functions that exploit various types of
parallel hardware resources, such as VLIW, superscalar, SIMD, SIMT, multicore
and multithread.

%package -n libpocl%{sover}
Summary:        Shared Library part of pocl
Group:          System/Libraries
Recommends:     libpocl-devices-tbb = %{version}

%description -n libpocl%{sover}
Portable Computing Language (pocl) is an implementation of the OpenCL standard
which can be adapted for new targets and devices, both for homogeneous CPU and
heterogenous GPUs/accelerators.

This subpackage contains the shared library part of pocl.

%package -n libpocl-devices-tbb
Summary:        TBB device for pocl

%description -n libpocl-devices-tbb
Portable Computing Language (pocl) is an implementation of the OpenCL standard
which can be adapted for new targets and devices, both for homogeneous CPU and
heterogenous GPUs/accelerators.

This subpackage contains the Thread Building Blocks (TBB) device for pocl.

%package -n libpocl-devices-levelzero
Summary:        Level Zero device for pocl

%description -n libpocl-devices-levelzero
Portable Computing Language (pocl) is an implementation of the OpenCL standard
which can be adapted for new targets and devices, both for homogeneous CPU and
heterogenous GPUs/accelerators.

This subpackage contains the Level Zero device for pocl.

%package devel
Summary:        Development files for the Portable Computing Language
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       libpocl%{sover} = %{version}
Requires:       opencl-headers >= 2.2

%description devel
Portable Computing Language (pocl) is an implementation of the OpenCL standard
which can be adapted for new targets and devices, both for homogeneous CPU and
heterogenous GPUs/accelerators.

This subpackage provides the development files needed for pocl.

%prep
%autosetup -p1

%build
%global __builder ninja
%cmake \
  -DPOCL_INSTALL_ICD_VENDORDIR=%{_datadir}/OpenCL/vendors \
  -DENABLE_LLVM=ON \
  -DWITH_LLVM_CONFIG=%{_bindir}/llvm-config \
  -DENABLE_ICD=ON \
  -DSTATIC_LLVM=OFF \
  -DENABLE_REMOTE_DISCOVERY_AVAHI=ON \
  -DENABLE_REMOTE_ADVERTISEMENT_AVAHI=ON \
  -DENABLE_REMOTE_DISCOVERY_DHT=ON \
  -DENABLE_REMOTE_ADVERTISEMENT_DHT=ON \
  -DENABLE_CUDA=OFF \
  -DINSTALL_OPENCL_HEADERS=OFF \
%if %{with spirv}
  -DENABLE_SPIRV=ON \
%endif
%if %{with ttb}
  -DENABLE_TBB_DEVICE=ON \
%endif
%if %{with levelzero}
  -DENABLE_LEVEL0=ON \
%endif
%if %{with vulkan}
  -DENABLE_VULKAN=ON \
%endif
%ifarch %{ix86} x86_64
  -DKERNELLIB_HOST_CPU_VARIANTS=distro \
%endif
%ifarch %{arm}
  -DLLC_HOST_CPU=cortex-a9 \
%endif
%ifarch aarch64
  -DLLC_HOST_CPU=cortex-a53 \
%endif
%ifarch riscv64
  -DLLC_HOST_CPU=generic-rv64 \
%endif
%if 0%{?suse_version} <= 1500 && 0%{?sle_version} <= 150300
  -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
%endif
  %{nil}

%cmake_build

%install
%cmake_install

%post -n libpocl%{sover} -p /sbin/ldconfig
%postun -n libpocl%{sover} -p /sbin/ldconfig

%files
%doc CHANGES README.* doc/sphinx/source/*.rst
%license LICENSE
%dir %{_datadir}/OpenCL/
%dir %{_datadir}/OpenCL/vendors
%{_datadir}/OpenCL/vendors/pocl.icd
%{_bindir}/poclcc
%dir %{_libdir}/pocl/
%{_libdir}/pocl/libpocl-devices-basic.so
%{_libdir}/pocl/libpocl-devices-pthread.so
%{_datadir}/pocl/

%files -n libpocl%{sover}
%{_libdir}/libpocl.so.%{sover}*

%files devel
%{_libdir}/libpocl.so
%{_libdir}/pkgconfig/pocl.pc

%if %{with ttb}
%files -n libpocl-devices-tbb
%{_libdir}/pocl/libpocl-devices-tbb.so
%endif

%if %{with levelzero}
%files -n libpocl-devices-levelzero
%{_libdir}/pocl/libpocl-devices-level0.so
%endif

%changelog
