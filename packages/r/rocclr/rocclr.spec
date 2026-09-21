#
# spec file for package rocclr
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
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#


%global upstreamname clr

%bcond_with preview
%if %{with preview}
%global rocm_major 7
%global rocm_minor 14
%global rocm_patch 0
%global rocm_release %{rocm_major}.%{rocm_minor}
%global pkg_src therock-%{rocm_release}
%else
%global rocm_major 7
%global rocm_minor 2
%global rocm_patch 2
%global rocm_release %{rocm_major}.%{rocm_minor}
%global pkg_src rocm-%{rocm_release}.%{rocm_patch}
%endif

%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix %{rocm_release}
%global skip_install_rpath OFF
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global skip_install_rpath ON
%endif
%global pkg_name rocclr%{pkg_suffix}

# ROCclr loads comgr at run time by soversion, so this needs to be checked when
# updating this package as it's used for the comgr requires for opencl and hip:
%global comgr_maj_api_ver 3
# See the file "rocclr/device/comgrctx.cpp" for reference:
# https://github.com/ROCm-Developer-Tools/ROCclr/blob/develop/device/comgrctx.cpp#L62

%global toolchain clang

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

%if 0%{?suse_version} <= 1600
# python3-CppHeaderParser not available on 15.6
%bcond_with cppheaderparser
%else
%bcond_without cppheaderparser
%endif
%if %{with cppheaderparser}
%global build_prof_api ON
%else
%global build_prof_api OFF
%endif

%if 0%{?rhel}
%if %{rhel} < 11
# No ocl-icd-devel in cs9,cs10
%bcond_with ocl
%else
%bcond_without ocl
%endif
%endif
%if 0%{?suse_version}
%if %{suse_version} <= 1500
%bcond_with ocl
%else
%bcond_without ocl
%endif
%endif
%if 0%{?fedora}
%if %{with compat}
%bcond_with ocl
%else
%bcond_without ocl
%endif
%endif

%if %{with ocl}
%global build_ocl ON
%else
%global build_ocl OFF
%endif

%bcond_with docs

Name:           %{pkg_name}
Version:        %{rocm_version}
%if %{with preview}
Release:        1%{?dist}
%else
Release:        3%{?dist}
%endif
Summary:        ROCm Compute Language Runtime
License:        Apache-2.0 AND MIT AND MIT-Khronos-old
# The main license is MIT
# OpenCL parts are licensed with Khronos AND Apache-2.0
URL:            https://github.com/ROCm/rocm-systems
Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz
# TODO: it would be nice to separate this into its own package:
Source1:        %{url}/releases/download/%{pkg_src}/hip.tar.gz#/hip-%{version}.tar.gz

# a fix for building blender
Patch1:         0001-rocclr-long-variants-for-__ffsll.patch

#https://github.com/ROCm/clr/pull/97
Patch2:         909fa3dcb644f7ca422ed1a980a54ac426d831b1.patch

%if %{without preview}
# std::filesystem is c++17 and that is too new for suse 15
# https://github.com/ROCm/rocm-systems/issues/1947
Patch3:         0001-rocclr-replace-std-filesystem-exists-with-access.patch
%endif

# Fix for reproducible builds
Patch4:         reproducible.patch

BuildRequires:  cmake
%if %{with docs}
BuildRequires:  doxygen
%endif
%if 0%{?fedora} || 0%{?suse_version}
BuildRequires:  fdupes
%endif
%if 0%{?fedora}
BuildRequires:  perl-generators
%endif
BuildRequires:  gcc-c++
BuildRequires:  hipcc%{pkg_suffix}
BuildRequires:  libffi-devel
BuildRequires:  libzstd-devel
BuildRequires:  perl

%if 0%{?rhel}
%if %{rhel} < 10
BuildRequires:  libglvnd-devel
%else
BuildRequires:  pkgconfig(opengl)
%endif
%endif
%if 0%{?suse_version}
%if %{suse_version} <= 1500
BuildRequires:  Mesa-libEGL-devel
BuildRequires:  Mesa-libGL-devel
%else
BuildRequires:  pkgconfig(gl)
%endif
%endif
%if 0%{?fedora}
BuildRequires:  pkgconfig(opengl)
%endif

%if %{with ocl}
%if 0%{?fedora}
BuildRequires:  pkgconfig(OpenCL)
%else
BuildRequires:  pkgconfig(ocl-icd)
%endif
%endif
BuildRequires:  pkgconfig(numa)
%if %{with cppheaderparser}
%if 0%{?suse_version}
BuildRequires:  %{python_module CppHeaderParser}
%else
BuildRequires:  python3-cppheaderparser
%endif
%endif
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-runtime%{pkg_suffix}-devel >= %{rocm_release}
%if %{with preview}
BuildRequires:  simde-devel
%endif
BuildRequires:  zlib-devel

# ROCclr relies on some x86 intrinsics
# 32bit userspace is excluded as it likely doesn't work and is not very useful
# Also depends on rocm-runtime which doesn't build non x86
ExclusiveArch:  x86_64

%if %{with ocl}
# rocclr bundles OpenCL 2.2 headers
# Some work is needed to unbundle this, as it fails to compile with latest
Provides:       bundled(opencl-headers) = 2.2
%endif

%description
ROCm Compute Language Runtime

%if %{with ocl}
%package -n rocm-opencl%{pkg_suffix}
Summary:        ROCm OpenCL platform and device tool
Requires:       comgr(major) = %{comgr_maj_api_ver}
%if 0%{?fedora}
Recommends:     OpenCL-ICD-Loader
Requires:       opencl-filesystem
%endif
%if 0%{?rhel}
Recommends:     ocl-icd
Requires:       opencl-filesystem
%endif
%if 0%{?suse_version}
Recommends:     LibOpenCL1
%endif
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocm-runtime%{pkg_suffix}

%description -n rocm-opencl%{pkg_suffix}
ROCm OpenCL language runtime.
Supports offline and in-process/in-memory compilation.

%package -n rocm-opencl%{pkg_suffix}-devel
Summary:        ROCm OpenCL development package
Requires:       rocm-opencl%{pkg_suffix}%{?_isa} = %{version}-%{release}
%if 0%{?fedora}
Requires:       OpenCL-ICD-Loader-devel%{?_isa}
%else
Requires:       ocl-icd-devel%{?_isa}
%endif

%if 0%{?suse_version}
%ldconfig_scriptlets -n rocm-opencl%{pkg_suffix}
%endif

%description -n rocm-opencl%{pkg_suffix}-devel
The AMD ROCm OpenCL development package.

%package -n rocm-clinfo%{pkg_suffix}
Summary:        ROCm OpenCL platform and device tool
Requires:       rocm-filesystem%{pkg_suffix}

%description -n rocm-clinfo%{pkg_suffix}
A simple ROCm OpenCL application that enumerates all possible platform and
device information.
%endif

%package -n rocm-hip%{pkg_suffix}
Summary:        ROCm HIP platform and device tool
Requires:       hipcc%{pkg_suffix}
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocm-runtime%{pkg_suffix}
Requires:       comgr%{pkg_suffix}(major) = %{comgr_maj_api_ver}

%description -n rocm-hip%{pkg_suffix}
HIP is a C++ Runtime API and Kernel Language that allows developers to create
portable applications for AMD and NVIDIA GPUs from the same source code.

%if 0%{?suse_version}
%ldconfig_scriptlets -n rocm-hip%{pkg_suffix}
%endif

%package -n rocm-hip%{pkg_suffix}-devel
Summary:        ROCm HIP development package
Requires:       rocm-comgr%{pkg_suffix}-devel
Requires:       rocm-hip%{pkg_suffix}%{?_isa} = %{version}-%{release}
Requires:       rocm-runtime%{pkg_suffix}-devel >= %{rocm_release}
# For roc-obj-ls
Requires:       binutils
Requires:       gawk

Provides:       hip%{pkg_suffix}-devel = %{version}-%{release}

%description -n rocm-hip%{pkg_suffix}-devel
ROCm HIP development package.

%if %{with docs}
%package -n hip%{pkg_suffix}-doc
Summary:        HIP API documentation package
BuildArch:      noarch

%description -n hip%{pkg_suffix}-doc
This package contains documentation for the hip package
%endif

%prep
%autosetup -N -a 1 -n %{upstreamname}

# ROCclr patches
%autopatch -p1

# Disable RPATH
# https://github.com/ROCm-Developer-Tools/hipamd/issues/22
sed -i '/INSTALL_RPATH/d' \
    opencl/tools/clinfo/CMakeLists.txt hipamd/CMakeLists.txt

# Upstream doesn't want OpenCL sonames because they don't guarantee API/ABI.
# For Fedora, SOVERSION can be major.minor (i.e. rocm_release) as rocm patch
# releases are very unlikely to break anything:
echo "set_target_properties(amdocl PROPERTIES VERSION %{version} SOVERSION %rocm_release)" \
    >> opencl/amdocl/CMakeLists.txt
echo "libamdocl64.so.%{rocm_release}" > opencl/config/amdocl64.icd
echo "set_target_properties(cltrace PROPERTIES VERSION %{version} SOVERSION %rocm_release)" \
    >> opencl/tools/cltrace/CMakeLists.txt

# Clean up unused bundled code
# Only keep opencl2.2 headers as are they needed for now:
ls -d opencl/khronos/* | grep -v headers | xargs rm -r
ls -d opencl/khronos/headers/* | grep -v opencl2.2 | xargs rm -r
# Unused opencl 2.2 test code:
rm -r opencl/khronos/headers/opencl2.2/tests/

# Don't change default C FLAGS and CXX FLAGS:
sed -i '/CMAKE_C.*_FLAGS/d' hipamd/src/CMakeLists.txt

# Stop cmake from trying to install HIPCC again:
sed -i "/install(PROGRAMS.*{[Hh][Ii][Pp][Cc]/d" hipamd/CMakeLists.txt

%if %{with docs}
# Disable doxygen timestamps:
sed -i 's/^\(HTML_TIMESTAMP.*\)YES/\1NO/' \
    hip/docs/doxygen-input/doxy.cfg
%endif

# Use cpack is not needed when we are doing the packaging here
# Gets confused on TW
sed -i -e 's@add_subdirectory(packaging)@#add_subdirectory(packaging)@' hipamd/CMakeLists.txt
sed -i -e 's@add_subdirectory(packaging)@#add_subdirectory(packaging)@' opencl/CMakeLists.txt

# cmake version
sed -i -e 's@cmake_minimum_required(VERSION 3.3)@cmake_minimum_required(VERSION 3.5)@' hipamd/src/hiprtc/cmake/hiprtc-config.cmake.in

%build

# So we can set HIP_COMMON_DIR
p=$PWD

# Something searches for clang in its path
export PATH=%{rocmllvm_bindir}:$PATH

%cmake \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_INSTALL_RPATH=%{pkg_prefix}/%{pkg_libdir} \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_SKIP_INSTALL_RPATH=%{skip_install_rpath} \
    -DHIPCC_BIN_DIR=%{pkg_prefix}/bin \
    -DHIP_COMMON_DIR=$p/hip \
    -DHIP_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DHIP_PLATFORM=amd \
    -DROCM_PATH=%{pkg_prefix} \
    -DBUILD_ICD=OFF \
    -DCLR_BUILD_HIP=ON \
    -DCLR_BUILD_OCL=%{build_ocl} \
    -DFILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DHIP_ENABLE_ROCPROFILER_REGISTER=OFF \
    -DUSE_PROF_API=%{build_prof_api} \
    -DCMAKE_BUILD_TYPE=%{build_type}

%cmake_build

%install
%cmake_install

%if %{with ocl}
%if %{without compat}
# Install OpenCL ICD configuration:
install -D -m 644 opencl/config/amdocl64.icd \
  %{buildroot}%{_sysconfdir}/OpenCL/vendors/amdocl64.icd
%endif

# Avoid file conflicts with opencl-headers package:
mkdir -p %{buildroot}%{pkg_prefix}/include/%{name}
mv %{buildroot}%{pkg_prefix}/include/CL %{buildroot}%{pkg_prefix}/include/%{name}/CL

# Avoid file conflicts with clinfo package:
mv %{buildroot}%{pkg_prefix}/bin/clinfo %{buildroot}%{pkg_prefix}/bin/rocm-clinfo
%endif

# Clean up file dupes
%if 0%{?fedora} || 0%{?suse_version}
%fdupes %{buildroot}/
%endif

# TODO send upstream a patch, libhip should be installed with cmake's 'TARGETS'
chmod 755 %{buildroot}%{pkg_prefix}/%{pkg_libdir}/lib*.so*

# Unnecessary file and is not FHS compliant:
rm %{buildroot}%{pkg_prefix}/%{pkg_libdir}/.hipInfo

%if %{without preview}
# Windows files:
rm %{buildroot}%{pkg_prefix}/bin/*.bat
%endif

%if %{with preview}
# 7.13+ needs some help installing scripts
mkdir -p %{buildroot}%{pkg_prefix}/bin
install -m 755 hip/bin/hipcc_cmake_linker_helper %{buildroot}%{pkg_prefix}/bin/
install -m 755 hip/bin/hipdemangleatp            %{buildroot}%{pkg_prefix}/bin/
%endif

rm -f %{buildroot}%{pkg_prefix}/share/doc/packages/rocclr*/LICENSE.md
rm -f %{buildroot}%{pkg_prefix}/share/doc/opencl*/LICENSE.md
rm -f %{buildroot}%{pkg_prefix}/share/doc/hip-asan/LICENSE.md
rm -f %{buildroot}%{pkg_prefix}/share/doc/hip/LICENSE.md

%if %{with ocl}
%files -n rocm-opencl%{pkg_suffix}
%if 0%{?suse_version}
%dir %{_sysconfdir}/OpenCL/
%dir %{_sysconfdir}/OpenCL/vendors
%endif
%if %{without compat}
%license opencl/LICENSE.md
%config(noreplace) %{_sysconfdir}/OpenCL/vendors/amdocl64.icd
%endif
%if %{with preview}
%{pkg_prefix}/%{pkg_libdir}/opencl/libamdocl64.so.%{rocm_major}{,.*}
%else
%{pkg_prefix}/%{pkg_libdir}/libamdocl64.so.%{rocm_major}{,.*}
%endif
%{pkg_prefix}/%{pkg_libdir}/libcltrace.so.%{rocm_major}{,.*}

%files -n rocm-opencl%{pkg_suffix}-devel
%if %{with preview}
%{pkg_prefix}/%{pkg_libdir}/opencl/libamdocl64.so
%else
%{pkg_prefix}/%{pkg_libdir}/libamdocl64.so
%endif
%{pkg_prefix}/%{pkg_libdir}/libcltrace.so
%{pkg_prefix}/include/%{name}

%files -n rocm-clinfo%{pkg_suffix}
%license opencl/LICENSE.md
%{pkg_prefix}/bin/rocm-clinfo
%endif

%files -n rocm-hip%{pkg_suffix}
%license hipamd/LICENSE.md
%{pkg_prefix}/%{pkg_libdir}/libamdhip64.so.%{rocm_major}{,.*}
%{pkg_prefix}/%{pkg_libdir}/libhiprtc.so.%{rocm_major}{,.*}
%{pkg_prefix}/%{pkg_libdir}/libhiprtc-builtins.so.%{rocm_major}{,.*}
%{pkg_prefix}/share/hip
%if %{with preview}
%{pkg_prefix}/bin/hrr-playback
%endif

%files -n rocm-hip%{pkg_suffix}-devel
%{pkg_prefix}/%{pkg_libdir}/libamdhip64.so
%{pkg_prefix}/%{pkg_libdir}/libhiprtc.so
%{pkg_prefix}/%{pkg_libdir}/libhiprtc-builtins.so
%{pkg_prefix}/%{pkg_libdir}/cmake/hip*
%{pkg_prefix}/include/hip
%if %{with cppheaderparser}
%{pkg_prefix}/include/hip_prof_str.h
%endif
%if %{without preview}
%{pkg_prefix}/bin/roc-*
%endif
%{pkg_prefix}/bin/hipcc_cmake_linker_helper
%{pkg_prefix}/bin/hipdemangleatp

%if %{with docs}
%files -n hip%{pkg_suffix}-doc
%license hip/LICENSE.md
%{pkg_prefix}/share/doc/hip
%endif

%changelog
