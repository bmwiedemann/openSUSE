#
# spec file for package xrt
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


%define soversion 2.23.244
%define sosuffix 2
# XRT version string as used by the upstream build system (branch.release)
%define xrt_branch 202610
Name:           xrt
Version:        202610.2.21.21
Release:        0
Summary:        Xilinx Runtime (XRT)
License:        Apache-2.0 AND MIT AND BSD-3-Clause AND GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/Xilinx/XRT
#!RemoteAsset: git+https://github.com/Xilinx/XRT#%version
#!CreateArchive
Source:         XRT-%{version}.tar.gz
Patch:          fix.patch
Patch1:         hip-build-compat.patch
BuildRequires:  cmake >= 3.19.0
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  glibc-devel-static
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ninja
BuildRequires:  patchelf
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-pybind11-devel
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libudev)
ExclusiveArch:  x86_64
%ifarch x86_64
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-opencl-devel
%endif
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
%if 0%{suse_version} < 1699
BuildRequires:  libboost_system-devel
%endif
BuildRequires:  ncurses-devel
BuildRequires:  opencl-headers
BuildRequires:  openssl-devel
BuildRequires:  protobuf-devel
BuildRequires:  rapidjson-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemtap-headers
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(uuid)
# Kernel driver sources are shipped for DKMS based packaging
BuildRequires:  kernel-macros
BuildRequires:  gmock
BuildRequires:  gtest

%description
Xilinx Runtime (XRT) is the runtime infrastructure for Xilinx accelerators
built on the AMD Data Center GPU Max / Alveo platforms and Versal ACAP
based designs.  XRT provides the userspace libraries, the OpenCL ICD
runtime, the emulation flow and the tools (xclbinutil, xbutil, xbmgmt,
...) needed to program and manage those devices.

%package -n libxrt_core%{sosuffix}
Summary:        Xilinx Runtime core library
Group:          System/Libraries

%description -n libxrt_core%{sosuffix}
Xilinx Runtime (XRT) is the runtime infrastructure for Xilinx accelerators.
This package provides the XCL and XRT core runtime libraries.

%package -n libxrt_hip%{sosuffix}
Summary:        Xilinx Runtime library HIP ROCm support
Group:          System/Libraries

%description -n libxrt_hip%{sosuffix}
Xilinx Runtime (XRT) is the runtime infrastructure for Xilinx accelerators.
This package provides the HIP AMD ROCm library.

%package devel
Summary:        Development files for Xilinx Runtime (XRT)
Group:          Development/Libraries/C and C++
Requires:       libxrt_core%{sosuffix} = %{version}

%description devel
Xilinx Runtime (XRT) is the runtime infrastructure for Xilinx accelerators.
This package contains the headers and CMake configuration files required to
build applications against XRT.

%package opencl-icd
Summary:        Xilinx OpenCL ICD (installable client driver)
Group:          Development/Libraries/C and C++
Requires:       libxrt_core%{sosuffix} = %{version}
Provides:       opencl-icd

%description opencl-icd
This package provides the Xilinx installable client driver (ICD) for
OpenCL, allowing the Khronos OpenCL ICD loader to dispatch to the Xilinx
runtime.

%package tools
Summary:        Command line tools for Xilinx Runtime (XRT)
Group:          Development/Tools/Building
Requires:       libxrt_core%{sosuffix} = %{version}

%description tools
This package contains the command line utilities shipped with Xilinx
Runtime such as xclbinutil, xbutil, xbmgmt, xclcheck, demo, reset and the
software emulation helpers.

%package kmod
Summary:        Kernel driver sources for Xilinx Runtime (XRT)
Group:          System/Kernel
Requires:       dkms >= 2.3
Requires(post): dkms >= 2.3
Requires(preun): dkms >= 2.3

%description kmod
This package contains the sources of the Xilinx kernel drivers (xclmgmt,
xocl, and zynqmp) for DKMS based building and installation.

%package -n python3-xrt
Summary:        Python bindings for Xilinx Runtime (XRT)
Group:          Development/Languages/Python
Requires:       libxrt_core%{sosuffix} = %{version}

%description -n python3-xrt
This package contains the Python module and the pybind11 based bindings
that allow Python applications to program Xilinx accelerators.

%prep
%autosetup -n XRT-%{version} -p1

# Fix missing <cstdint> include in utils.h (newer libstdc++ requires it explicitly)
if [ -f src/runtime_src/core/common/utils.h ] &&
   ! grep -Eq '^[[:space:]]*#[[:space:]]*include[[:space:]]*<cstdint>' src/runtime_src/core/common/utils.h; then
  sed -i '0,/^[[:space:]]*#[[:space:]]*include[[:space:]]*<iostream>/s/^[[:space:]]*#[[:space:]]*include[[:space:]]*<iostream>/&\n#include <cstdint>/' src/runtime_src/core/common/utils.h
fi

%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DXRT_NPU=1 \
  -DCMAKE_BUILD_RPATH_USE_ORIGIN=ON \
%ifarch x86_64
  -DXRT_ENABLE_HIP=ON \
%else
  -DXRT_ENABLE_HIP=OFF \
%endif
  -DXRT_ENABLE_TRACER=OFF \
  -DXRT_ENABLE_DKMS=OFF \
  -DXRT_INSTALL_STATIC_LIBRARY=OFF \
  -DXRT_ENABLE_EMULATION=OFF

%cmake_build

%install
%cmake_install

# The upstream cpack logic installs the documentation/licenses relative to the
# sources; keep only what cmake installed into the buildroot.
rm -f %{buildroot}%{_prefix}/xrt.ini
rm -rf %{buildroot}%{_prefix}/linux
rm -rf %{buildroot}/usr/license
rm -rf %{buildroot}/usr/share/doc
rm -rf %{buildroot}/usr/version.json
rm -rf %{buildroot}%_libdir/lib*.a
# pkgconfig files and cmake config files are picked up by the devel package

%find_lang %{name} || true

%post -n libxrt_core%{sosuffix} -p /sbin/ldconfig
%postun -n libxrt_core%{sosuffix} -p /sbin/ldconfig
%post -n libxrt_hip%{sosuffix} -p /sbin/ldconfig
%postun -n libxrt_hip%{sosuffix} -p /sbin/ldconfig

%files -n libxrt_core%{sosuffix}
%license LICENSE
%{_libdir}/libxrt_core.so.*
%{_libdir}/libxrt_coreutil.so.*
%_libdir/libxdp_core.so.*
%_libdir/libxilinxopencl.so.*
%_libdir/libxrt++.so.*
%_libdir/libxrt_trace.so.*
%_libdir/xrt

%files -n libxrt_hip%{sosuffix}
%{_libdir}/libxrt_hip.so.*

%files opencl-icd
%dir %{_sysconfdir}/OpenCL
%dir %{_sysconfdir}/OpenCL/vendors
%{_libdir}/libxilinxopencl.so
%{_sysconfdir}/OpenCL/vendors/xilinx.icd

%files tools
%doc CHANGELOG.rst NOTICE
%{_bindir}/*
/usr/share/completions

%files devel
%{_includedir}/hip/
%{_includedir}/xrt/
%{_includedir}/CL/
%{_libdir}/libxrt_core.so
%{_libdir}/libxrt_coreutil.so
%{_libdir}/libxrt_hip.so
%{_libdir}/pkgconfig/xrt.pc
%_libdir/libxrt++.so
#_libdir/libaiebu.a
#_libdir/libxilinxopencl.a
#_libdir/libxrt++.a
#_libdir/libxrt_core.a
#_libdir/libxrt_coreutil.a
/usr/share/cmake/AIEBU
/usr/share/cmake/XRT

%files -n python3-xrt
%_libdir/python*/site-packages/pyxrt.cpython-*-linux-gnu.so

%changelog
