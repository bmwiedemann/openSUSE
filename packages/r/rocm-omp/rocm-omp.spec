#
# spec file for package rocm-omp
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


%global upstreamname llvm-project

%bcond_with preview
%if %{with preview}
%global rocm_release 7.12
%global rocm_patch 0
%global pkg_src therock-%{rocm_release}
%else
%global rocm_release 7.2
%global rocm_patch 0
%global pkg_src rocm-%{rocm_release}.%{rocm_patch}
%endif

%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
%global bundle_prefix %{_libdir}/rocm/rocm-%{rocm_release}/llvm
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix %{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global bundle_prefix %{_libdir}/rocm/llvm
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif

# What LLVM is upstream using (use LLVM_VERSION_MAJOR from llvm/CMakeLists.txt):
%global llvm_maj_ver 22

%global toolchain clang

%global llvm_triple %{_target_platform}

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

Name:           rocm-omp%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        1%{?dist}
%else
Release:        4%{?dist}
%endif
Summary:        ROCm OpenMP

URL:            https://github.com/ROCm/%{upstreamname}
License:        Apache-2.0 AND (Apache-2.0 WITH LLVM-exception OR NCSA) AND BSD-3-Clause
# llvm is Apache-2.0 WITH LLVM-exception OR NCSA
# openmp/runtime is Apache-2.0
# openmp/runtime/src/thirdparty/ittnotify is BSD-3-Clause
Source0:        %{url}/archive/refs/tags/%{pkg_src}.tar.gz#/rocm-omp-%{rocm_version}.tar.gz

BuildRequires:  binutils-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
%if 0%{?fedora} || 0%{?suse_version}
BuildRequires:  fdupes
%endif
BuildRequires:  libffi-devel
BuildRequires:  libzstd-devel
BuildRequires:  perl
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-device-libs%{pkg_suffix}
BuildRequires:  rocm-filesystem%{pkg_suffix}
BuildRequires:  rocm-llvm%{pkg_suffix}-filesystem
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  zlib-devel

Provides:       bundled(ittapi) = 3.0.0
Requires:       rocm-llvm%{pkg_suffix}-filesystem

ExclusiveArch:  x86_64
%global targets_to_build "X86;AMDGPU"

%description
%{summary}

%package devel
Summary:        Libraries and headers for %{name}
# main package is empty, do not require it
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocm-llvm%{pkg_suffix}-filesystem

%description devel
%{summary}

%prep
%autosetup -p1 -n %{upstreamname}-%{pkg_src}

# rm llvm-project bits we do not need
rm -rf {bolt,clang,compiler-rt,flang,libc,libclc,libcxx,libcxxabi,libunwind,lld,lldb,llvm-libgcc,mlir,polly,pst,runtimes,utils}

# Other licenses
cp -p openmp/runtime/src/thirdparty/ittnotify/LICENSE.txt LICENSE.ittnotify.txt
cp -p openmp/LICENSE.TXT LICENSE.openmp.txt

%build

%global llvmrocm_cmake_config \\\
 -DBUILD_SHARED_LIBS=OFF \\\
 -DBUILD_TESTING=OFF \\\
 -DCLANG_ENABLE_STATIC_ANALYZER=OFF \\\
 -DCLANG_ENABLE_ARCMT=OFF \\\
 -DCLANG_TOOL_CLANG_FUZZER_BUILD=OFF \\\
 -DCMAKE_BUILD_TYPE=%{build_type} \\\
 -DCMAKE_INSTALL_DO_STRIP=ON \\\
 -DCMAKE_INSTALL_PREFIX=%{bundle_prefix} \\\
 -DCOMPILER_RT_BUILD_BUILTINS=ON \\\
 -DCOMPILER_RT_BUILD_GWP_ASAN=OFF \\\
 -DCOMPILER_RT_BUILD_LIBFUZZER=OFF \\\
 -DCOMPILER_RT_BUILD_MEMPROF=OFF \\\
 -DCOMPILER_RT_BUILD_ORC=OFF \\\
 -DCOMPILER_RT_BUILD_PROFILE=OFF \\\
 -DCOMPILER_RT_BUILD_SANITIZERS=OFF \\\
 -DCOMPILER_RT_BUILD_XRAY=OFF \\\
 -DENABLE_LINKER_BUILD_ID=ON \\\
 -DLIBCXX_INCLUDE_BENCHMARKS=OFF \\\
 -DLIBCXXABI_USE_LLVM_UNWINDER=OFF \\\
 -DLLVM_BINUTILS_INCDIR=%{_includedir} \\\
 -DLLVM_BUILD_RUNTIME=ON \\\
 -DLLVM_DEFAULT_TARGET_TRIPLE=%{llvm_triple} \\\
 -DLLVM_ENABLE_EH=ON \\\
 -DLLVM_ENABLE_FFI=ON \\\
 -DLLVM_ENABLE_LIBCXX=ON \\\
 -DLLVM_ENABLE_OCAMLDOC=OFF \\\
 -DLLVM_ENABLE_RTTI=ON \\\
 -DLLVM_ENABLE_ZLIB=ON \\\
 -DLLVM_ENABLE_ZSTD=ON \\\
 -DLLVM_INCLUDE_BENCHMARKS=OFF \\\
 -DLLVM_INCLUDE_EXAMPLES=OFF \\\
 -DLLVM_INCLUDE_TESTS=OFF \\\
 -DLLVM_TARGETS_TO_BUILD=%{targets_to_build} \\\
 -DLLVM_TOOL_LLVM_AS_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_DIS_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_DLANG_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_ISEL_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_ITANIUM_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_MC_ASSEMBLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_MC_DISASSEMBLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_MICROSOFT_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_OPT_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_RUST_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_SPECIAL_CASE_LIST_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_YAML_NUMERIC_PARSER_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_LLVM_YAML_PARSER_FUZZER_BUILD=OFF \\\
 -DLLVM_TOOL_VFABI_DEMANGLE_FUZZER_BUILD=OFF \\\
 -DMLIR_INSTALL_AGGREGATE_OBJECTS=OFF \\\
 -DLLVM_BUILD_LLVM_DYLIB=ON \\\
 -DLLVM_LINK_LLVM_DYLIB=ON \\\
 -DLLVM_BUILD_TOOLS=ON \\\
 -DLLVM_BUILD_UTILS=ON \\\
 -DMLIR_BUILD_MLIR_C_DYLIB=ON

cd openmp
%cmake %{llvmrocm_cmake_config} \
       -DBUILD_SHARED=ON \
       -DClang_DIR=%{rocmllvm_cmakedir}/../clang \
       -DCMAKE_AR=%{rocmllvm_bindir}/llvm-ar \
       -DCMAKE_BUILD_RPATH=%{rocmllvm_libdir} \
       -DCMAKE_INSTALL_RPATH=%{rocmllvm_libdir} \
       -DCMAKE_LINKER=%{rocmllvm_bindir}/ld.lld \
       -DCMAKE_RANLIB=%{rocmllvm_bindir}/llvm-ranlib \
       -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/clang++ \
       -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/clang \
       -DCMAKE_C_COMPILER_AR=%{rocmllvm_bindir}/llvm-ar \
       -DCMAKE_C_COMPILER_RANLIB=%{rocmllvm_bindir}/llvm-ranlib \
       -DLIBOMPTARGET_AMDGPU_ARCH=%{rocmllvm_bindir}/amdgpu-arch \
       -DCMAKE_INSTALL_PREFIX=%{bundle_prefix} \
       -DCMAKE_INSTALL_LIBDIR=lib \
       -DLLD_DIR=%{rocmllvm_cmakedir}/../lld \
       -DLLVM_DIR=%{rocmllvm_cmakedir} \
       -DLLVM_ENABLE_PROJECTS="openmp" \
       -DLLVM_ENABLE_RUNTIMES="" \
       -DLIBOMPTARGET_NVPTX_ENABLE_BCLIB=OFF \
       -DLIBOMPTARGET_NVPTX_CUDA_COMPILER="" \
       -DLIBOMPTARGET_NVPTX_BC_LINKER="" \
       -DLIBOMP_OMPD_GDB_SUPPORT=OFF \
       -DLIBOMPTARGET_BUILD_AMDGPU_PLUGIN=ON \
       -DLIBOMPTARGET_BUILD_CUDA_PLUGIN=OFF \
       -DLIBOMPTARGET_BUILD_DEVICERTL_BCLIB=ON \
       -DLIBOMPTARGET_NVPTX_ENABLE_BCLIB=OFF \
       -DLIBOMP_INSTALL_ALIASES=OFF \
       -DLIBOMP_ARCHER_SUPPORT=OFF \
       -DOPENMP_STANDALONE_BUILD=ON \
       -DOPENMP_LLVM_TOOLS_DIR=%{rocmllvm_bindir}

%cmake_build

%install

cd openmp
%cmake_install

#Clean up dupes:
%if 0%{?fedora} || 0%{?suse_version}
%fdupes %{buildroot}%{pkg_prefix}
%endif

rm -rf %{buildroot}%{bundle_prefix}/lib/omptest
rm -rf %{buildroot}%{bundle_prefix}/lib/cmake/omptest

%files devel
%license LICENSE.TXT LICENSE.ittnotify.txt LICENSE.openmp.txt
%{bundle_prefix}/include/omp*.h
%{bundle_prefix}/lib/cmake/openmp/
%{bundle_prefix}/lib/libomp*.so

%changelog
