#
# spec file for package rocblas
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


%global upstreamname rocblas

%global pkg_library_name %{upstreamname}
%global pkg_library_version 5

%bcond_with preview
%if %{with preview}
%global rocm_release 7.14
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
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix %{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%global skip_install_rpath OFF
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%global skip_install_rpath ON
%endif

%if 0%{?suse_version}
%global pkg_name lib%{pkg_library_name}%{pkg_library_version}%{pkg_suffix}
%else
%global pkg_name %{NAME}
%endif

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%if 0%{?suse_version}
# %%toolchain and %%build_cxxflags are Fedora rpm machinery; openSUSE implements
# neither, and its %%cmake injects %%optflags verbatim. Without this the host
# hardening flags reach the amdgcn device passes, where clang rejects them with
# "option 'cf-protection=return' cannot be specified on this target".
%global optflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%endif

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

%bcond_without compress
%if %{with compress}
%global build_compress ON
%else
%global build_compress OFF
%endif

# Some parts of install are not legal, make test optional
# Ex
# rocblas-test.x86_64: E: script-without-shebang /usr/bin/rocblas_clients_readme.txt
# rocblas-test.x86_64: E: script-without-shebang /usr/bin/rocblas_common.yaml
# rocblas-test.x86_64: E: script-without-shebang /usr/bin/rocblas_extras.yaml
%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif

# Option to test suite for testing on real HW:
# May have to set gpu under test with
# export HIP_VISIBLE_DEVICES=<num> - 0, 1 etc.
%bcond_with check

%bcond_without tensile
%if %{with tensile}
%global build_tensile ON
%else
%global build_tensile OFF
%endif

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

# SUSE/OSB times out because -O is added to the make args
# This accumulates all the output from the long running tensile
# jobs.
%global _make_output_sync %{nil}

# OracleLinux 9 has a problem with it's strip not recognizing *.co's
%global __strip %rocmllvm_bindir/llvm-strip

# Use ninja if it is available
# Ninja is available on suse but obs times out with ninja build, make doesn't
%if 0%{?fedora}
%bcond_without ninja
%else
%bcond_with ninja
%endif

%if %{with ninja}
%global cmake_generator -G Ninja
%else
%global cmake_generator %{nil}
%endif

%global cmake_config \\\
  -DBLAS_INCLUDE_DIR=%{_includedir}/%{blaslib} \\\
  -DBLAS_LIBRARY=%{blaslib} \\\
  -DBUILD_CLIENTS_BENCHMARKS=%{build_test} \\\
  -DBUILD_CLIENTS_TESTS=%{build_test} \\\
  -DBUILD_CLIENTS_TESTS_OPENMP=OFF \\\
  -DBUILD_FORTRAN_CLIENTS=OFF \\\
  -DBUILD_OFFLOAD_COMPRESS=%{build_compress} \\\
  -DBUILD_WITH_PIP=OFF \\\
  -DBUILD_WITH_TENSILE=%{build_tensile} \\\
  -DBUILD_WITH_HIPBLASLT=OFF \\\
  -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \\\
  -DCMAKE_BUILD_TYPE=%{build_type} \\\
  -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \\\
  -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \\\
  -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \\\
  -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \\\
  -DCMAKE_INSTALL_RPATH=%{pkg_prefix}/%{pkg_libdir} \\\
  -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \\\
  -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \\\
  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \\\
  -DCMAKE_SKIP_RPATH=%{skip_install_rpath} \\\
  -DCMAKE_SKIP_INSTALL_RPATH=%{skip_install_rpath} \\\
  -DCMAKE_VERBOSE_MAKEFILE=ON \\\
  -DGPU_TARGETS=%{gpu_list} \\\
  -DROCM_SYMLINK_LIBS=OFF \\\
  -DHIP_PLATFORM=amd \\\
  -DTensile_CPU_THREADS=${CORES} \\\
  -DTensile_DIR=${TP}/cmake \\\
  -DTensile_LIBRARY_FORMAT=%{tensile_library_format} \\\
  -DTensile_ROOT=${TP} \\\
  -DTensile_VERBOSE=%{tensile_verbose}

%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100

%bcond_without bundled_tensile

Name:           rocblas%{pkg_suffix}
Summary:        BLAS implementation for ROCm
License:        BSD-3-Clause AND MIT
# Most of the files are MIT
# Some files are MIT and BSD-3-Clause
#  library/src/blas2/gemv_device.hpp
#  library/src/blas2/rocblas_hemv_symv_kernels.cpp
#  library/src/blas2/rocblas_trsv_kernels.cpp
#  library/src/blas3/rocblas_trmm_kernels.cpp
URL:            https://github.com/ROCm/rocm-libraries
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        9%{?dist}
%endif

Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{pkg_src}/tensile.tar.gz#/tensile-%{version}.tar.gz

%if %{with preview}
Patch1:         0001-improve-the-warning-for-asm-caps-mismatches.patch
Patch2:         0002-add-generic-gpu-targets.patch
Patch3:         0003-improve-fallback-name-to-handle-generics.patch
Patch4:         0004-generic-arches-need-a-solution-index.patch
Patch5:         0005-rocblas-add-rocblas_internal_get_generic_arch_name.patch
Patch6:         0006-rocblas-generalize-finding-tensile-for-generics.patch
%else
# Fix tensile output install path to use CMAKE_INSTALL_LIBDIR
Patch1:         0001-fixup-install-of-tensile-output.patch
# Add support for Fedora-specific GPU architectures (gfx1035, gfx1150-1152)
Patch101:       0001-tensile-fedora-gpus.patch
# Add support for gfx1153 GPU architecture in Tensile
Patch102:       0001-tensile-gfx1153.patch
# Update default ROCm and LLVM binary paths to /usr and /usr/lib64/rocm/llvm
Patch103:       0001-tensile-set-default-paths.patch
# Force Tensile to ignore assembly capability cache checks
Patch104:       0001-tensile-ignore-cache-check.patch
# Add gfx1152 and gfx1153 to Tensile's supported CMake architectures
Patch105:       0001-tensile-add-cmake-arches.patch
# Add support for gfx1036 GPU architecture in Tensile
Patch106:       0001-tensile-gfx1036.patch
%endif

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-filesystem%{pkg_suffix}
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  rocminfo%{pkg_suffix}

%if %{with tensile}
%if 0%{?suse_version}
%if 0%{?suse_version} <= 1600
%global tensile_library_format yaml
%else
%global tensile_library_format msgpack
%endif
# OBS vm times out without console output
%global tensile_verbose 2
%else
%global tensile_verbose 1
%global tensile_library_format msgpack
# suse_version
%endif
%else
%global tensile_verbose %{nil}
%global tensile_library_format %{nil}
# tensile
%endif

%if %{with tensile}
%if %{with bundled_tensile}
%if 0%{?suse_version}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module joblib}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} <= 1600
%else
BuildRequires:  msgpack-cxx-devel
# suse version <= 1600
%endif
%else
BuildRequires:  msgpack-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
%if 0%{?fedora} || 0%{?rhel} > 9
BuildRequires:  python3dist(joblib)
%endif
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(pyyaml)
# suse version
%endif
%else
%if 0%{?suse_version}
%if 0%{?suse_version} <= 1600
%else
BuildRequires:  msgpack-cxx-devel
# suse version <= 1600
%endif
BuildRequires:  %{python_module joblib}
BuildRequires:  %{python_module tensile-devel}
%else
BuildRequires:  msgpack-devel
BuildRequires:  python3dist(tensile)
# suse_version
%endif
# bundled_tensile
%endif
# tensile
%endif

%if %{with compress}
BuildRequires:  pkgconfig(libzstd)
%endif

%if %{with test}
%if %{with preview}
BuildRequires:  amdsmi%{pkg_suffix}-devel
%endif
BuildRequires:  libomp-devel
BuildRequires:  rocm-smi%{pkg_suffix}-devel
BuildRequires:  rocminfo%{pkg_suffix}

%if 0%{?suse_version}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  gcc-fortran
BuildRequires:  gtest
BuildRequires:  openblas-devel
%global blaslib openblas
%else
BuildRequires:  gcc-gfortran
BuildRequires:  gtest-devel
BuildRequires:  python3dist(pyyaml)
%if 0%{?rhel}
BuildRequires:  flexiblas-devel
%global blaslib flexiblas
%else
BuildRequires:  blas-devel
%global blaslib cblas
%endif
%endif
%endif

%if %{with ninja}
%if 0%{?fedora} || 0%{?rhel}
BuildRequires:  ninja-build
%endif
%if 0%{?suse_version}
BuildRequires:  ninja
%define __builder ninja
%endif
%endif

Provides:       rocblas%{pkg_suffix} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocm-hip%{pkg_suffix}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
rocBLAS is the AMD library for Basic Linear Algebra Subprograms
(BLAS) on the ROCm platform. It is implemented in the HIP
programming language and optimized for AMD GPUs.

%if 0%{?suse_version}
%package -n %{pkg_name}
Summary:        Shared libraries for %{name}

%description -n %{pkg_name}
%{summary}

%ldconfig_scriptlets -n %{pkg_name}
%endif

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{pkg_name}%{?_isa} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}
%if %{without compat}
Requires:       cmake(hip)
%endif

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{pkg_name}%{?_isa} = %{version}-%{release}
Requires:       diffutils

%description test
%{summary}
%endif

%prep
%setup -q -n %{upstreamname}
%if %{with preview}
%patch -P5 -p3
%patch -P6 -p3
%else
%patch -P1 -p1
%endif

tar xf %{SOURCE1}
cd tensile
%if %{with preview}
%patch -P1 -p3
%patch -P2 -p3
%patch -P3 -p3
%patch -P4 -p3
%else
%patch -P101 -p1
%patch -P102 -p1
%patch -P103 -p1
%patch -P104 -p1
%patch -P105 -p1
%patch -P106 -p1
%endif

#Fix a few things:
chmod 755 Tensile/Configs/miopen/convert_cfg.py
sed -i -e 's@bin/python@bin/python3@' Tensile/Configs/miopen/convert_cfg.py
sed -i -e 's@bin/python@bin/python3@' Tensile/Tests/create_tests.py
sed -i -e 's@bin/env python3@bin/python3@' Tensile/bin/Tensile
sed -i -e 's@bin/env python3@bin/python3@' Tensile/bin/TensileCreateLibrary

# I'm assuming we don't need these:
rm -r Tensile/Configs/miopen/archives

# hack where TensileGetPath is located
sed -i -e 's@${Tensile_PREFIX}/bin/TensileGetPath@TensileGetPath@g' Tensile/cmake/TensileConfig.cmake

# Use /usr instead of /opt/rocm for prefix
# Is this needed with bundled?
sed -i -e 's@/opt/rocm@%{pkg_prefix}@g' Tensile/Common.py
sed -i -e 's@/opt/rocm@%{pkg_prefix}@g' Tensile/Tests/yaml_only/test_config.py

# Ignora asm cap
sed -i -e 's@globalParameters["IgnoreAsmCapCache"] = False@globalParameters["IgnoreAsmCapCache"] = True@' Tensile/Common.py
sed -i -e 's@arguments["IgnoreAsmCapCache"] = args.IgnoreAsmCapCache@arguments["IgnoreAsmCapCache"] = True@' Tensile/TensileCreateLibrary.py
sed -i -e 's@if not ignoreCacheCheck and derivedAsmCaps@if False and derivedAsmCaps@' Tensile/Common.py

# Reduce requirements
sed -i -e '/joblib/d' requirements.*
sed -i -e '/rich/d' requirements.*
sed -i -e '/msgpack/d' requirements.*
sed -i -e '/pyyaml/d' requirements.*

# Generalize prefix
%if %{with preview}
sed -i -e 's@DEFAULT_ROCM_BIN_PATH_POSIX = Path("/opt/rocm/bin")@DEFAULT_ROCM_BIN_PATH_POSIX = Path("%{pkg_prefix}/bin")@' Tensile/Utilities/Toolchain.py
sed -i -e 's@DEFAULT_ROCM_LLVM_BIN_PATH_POSIX = Path("/opt/rocm/lib/llvm/bin")@DEFAULT_ROCM_LLVM_BIN_PATH_POSIX = Path("%{rocmllvm_bindir}")@' Tensile/Utilities/Toolchain.py
%else
sed -i -e 's@/usr/bin@%{pkg_prefix}/bin@' Tensile/Utilities/Toolchain.py
sed -i -e 's@/usr/lib64/rocm/llvm/bin@%{rocmllvm_bindir}@' Tensile/Utilities/Toolchain.py
%endif

# Make sure hip/hip_runtime.h is found
sed -i -e 's@"-D__HIP_HCC_COMPAT_MODE__=1"@"-D__HIP_HCC_COMPAT_MODE__=1","-I%{pkg_prefix}/include"@' Tensile/BuildCommands/SourceCommands.py

cd ..

sed -i -e 's@pkg_search_module(PKGBLAS cblas)@pkg_search_module(PKGBLAS %blaslib)@' clients/CMakeLists.txt
sed -i -e 's@target_link_libraries( rocblas-test PRIVATE ${BLAS_LIBRARY} ${GTEST_BOTH_LIBRARIES} roc::rocblas )@target_link_libraries( rocblas-test PRIVATE %blaslib ${GTEST_BOTH_LIBRARIES} roc::rocblas )@' clients/gtest/CMakeLists.txt

# no git in this build
sed -i -e 's@find_package(Git REQUIRED)@find_package(Git)@' library/CMakeLists.txt

# On Tumbleweed Q2,2025
# /usr/include/gtest/internal/gtest-port.h:279:2: error: C++ versions less than C++14 are not supported.
#   279 | #error C++ versions less than C++14 are not supported.
# Convert the c++11's to c++14
sed -i -e 's@CXX_STANDARD 11@CXX_STANDARD 14@' clients/samples/CMakeLists.txt

%if 0%{?suse_version}
# Suse's libgfortran.so for gcc 14 is here
# /usr/lib64/gcc/x86_64-suse-linux/14/libgfortran.so
# Without adding this path with -L, it isn't found, but thankfully it isn't really needed
sed -i -e 's@list( APPEND COMMON_LINK_LIBS "-lgfortran")@#list( APPEND COMMON_LINK_LIBS "-lgfortran")@' clients/{benchmarks,gtest}/CMakeLists.txt
%endif

%build

%if %{with tensile}
%if %{with bundled_tensile}
cd tensile

%if 0%{?suse_version}
TL=$PWD
python3 setup.py install --root $TL
TP=${TL}/usr/lib/python%{python3_version}/site-packages/Tensile/
%else
TL=$PWD/install
# pip install --no-index --find-links /usr/lib/python%{python3_version}/site-packages --target $TL .
/usr/bin/python3 -m pip install -vvv --no-build-isolation --no-index --find-links /usr/lib/python%{python3_version}/site-packages --find-links /usr/lib64/python%{python3_version}/site-packages --target $TL .
TP=${TL}/Tensile/
%endif
cd ..
%else
TP=`/usr/bin/TensileGetPath`
%endif
%endif

CORES=`lscpu | grep 'Core(s)' | awk '{ print $4 }'`
if [ ${CORES}x = x ]; then
    CORES=1
fi
# Try again..
if [ ${CORES} = 1 ]; then
    CORES=`lscpu | grep '^CPU(s)' | awk '{ print $2 }'`
    if [ ${CORES}x = x ]; then
        CORES=4
    fi
fi

export CLANG_PATH=%{rocmllvm_bindir}
export TENSILE_ROCM_ASSEMBLER_PATH=${CLANG_PATH}/clang++
export TENSILE_ROCM_OFFLOAD_BUNDLER_PATH=${CLANG_PATH}/clang-offload-bundler
# Work around problem with koji's ld
export HIPCC_LINK_FLAGS_APPEND=-fuse-ld=lld

%cmake %{cmake_generator} %{cmake_config}

%cmake_build

%install
%cmake_install

# Extra license
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocblas/LICENSE.md

# rocblas.x86_64: W: unstripped-binary-or-object /usr/lib64/rocblas/library/Kernels.so-000-gfx1010.hsaco
# The below stripping silience rpmlint but is reported to cause runtime problems
# So do not strip
# %{rocmllvm_bindir}/llvm-strip %{buildroot}%{pkg_prefix}/%{pkg_libdir}/rocblas/library/*.hsaco

%if %{with compat}
# ERROR   0008: file '/usr/lib64/rocm/rocm-7.2/lib/librocblas.so.5.2'
#   contains the $ORIGIN runpath specifier at the wrong position in
#   [/usr/lib64/rocm/rocm-7.2/lib:$ORIGIN/../lib:$ORIGIN/../lib/rocblas/lib]
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}.*
%if %{with test}
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/bin/rocblas-test
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/bin/rocblas-bench
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/bin/rocblas-gemm-tune
%endif
%endif

%check
%if %{with test}
%if %{with check}
%if 0%{?suse_version}
export LD_LIBRARY_PATH=%{__builddir}/library/src:$LD_LIBRARY_PATH
%{__builddir}/clients/staging/rocblas-test --gtest_brief=1
%else
export LD_LIBRARY_PATH=%{_vpath_builddir}/library/src:$LD_LIBRARY_PATH
%{_vpath_builddir}/clients/staging/rocblas-test --gtest_brief=1
%endif
%endif
%endif

%files -n %{pkg_name}
%license LICENSE.md
%doc README.md
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}{,.*}
%if %{with tensile}
%{pkg_prefix}/%{pkg_libdir}/rocblas/
%endif

%files devel
%{pkg_prefix}/include/rocblas/
%{pkg_prefix}/%{pkg_libdir}/cmake/rocblas/
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so

%if %{with test}
%files test
%{pkg_prefix}/bin/rocblas*
%endif

%changelog
