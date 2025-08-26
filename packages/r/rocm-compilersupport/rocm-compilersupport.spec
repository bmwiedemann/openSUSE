#
# spec file for package rocm-compilersupport
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


%global comgr_maj_api_ver 3
# local, fedora
%global _comgr_full_api_ver %{comgr_maj_api_ver}.0
# mock, suse
%global comgr_full_api_ver %{comgr_maj_api_ver}.0.0
# Upstream tags are based on rocm releases:
%global rocm_release 6.4
%global rocm_patch 2
%global rocm_version %{rocm_release}.%{rocm_patch}
# What LLVM is upstream using (use LLVM_VERSION_MAJOR from llvm/CMakeLists.txt):
%global llvm_maj_ver 19
%global upstreamname llvm-project

%global toolchain clang

%global _smp_mflags %{nil}
%global _lto_cflags %{nil}
%global bundle_prefix %{_libdir}/rocm/llvm
%global llvm_triple %{_target_platform}
%global amd_device_libs_prefix lib64/rocm/llvm/lib/clang/%{llvm_maj_ver}

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# Older hipcc was perl, it has been deprecated
%bcond_with perl
# Enable ppc and aarch64 builds
%bcond_with alt_arch

Name:           rocm-compilersupport
Version:        %{llvm_maj_ver}
Release:        15.rocm%{rocm_version}%{?dist}
Summary:        Various AMD ROCm LLVM related services
%if 0%{?suse_version}
Group:          Development/Languages/Other
%endif

URL:            https://github.com/ROCm/llvm-project
# hipcc is MIT, comgr and device-libs are NCSA:
License:        MIT AND NCSA
Source0:        https://github.com/ROCm/%{upstreamname}/archive/refs/tags/rocm-%{rocm_version}.tar.gz#/%{name}-%{rocm_version}.tar.gz
Source1:        rocm-compilersupport.prep.in

Patch3:         0001-Remove-err_drv_duplicate_config-check.patch
Patch4:         0001-Replace-use-of-mktemp-with-mkstemp.patch
# Subject: [PATCH] [gold] Fix compilation (#130334)
Patch5:         %{url}/commit/b0baa1d8bd68a2ce2f7c5f2b62333e410e9122a1.patch
# Link comgr with static versions of llvm's libraries
Patch6:         0001-comgr-link-with-static-llvm.patch

Patch8:         0001-rocm-llvm-work-around-new-assert-in-array.patch

BuildRequires:  cmake
BuildRequires:  perl
%if 0%{?fedora} || 0%{?suse_version}
BuildRequires:  fdupes
%endif
BuildRequires:  binutils-devel
BuildRequires:  gcc-c++
BuildRequires:  libffi-devel
BuildRequires:  libzstd-devel
BuildRequires:  rocm-cmake
BuildRequires:  zlib-devel
Provides:       bundled(llvm-project) = %{llvm_maj_ver}

%if 0%{?rhel} || 0%{?suse_version}
ExclusiveArch:  x86_64
%global targets_to_build "X86;AMDGPU"
%else
%if %{with alt_arch}
ExclusiveArch:  x86_64 aarch64 ppc64le
%else
ExclusiveArch:  x86_64
%endif

%ifarch x86_64
%global targets_to_build "X86;AMDGPU"
%endif
%ifarch aarch64
%global targets_to_build "AArch64;AMDGPU"
%endif
%ifarch ppc64le
%global targets_to_build "PowerPC;AMDGPU"
%endif
%endif

%description
%{summary}

%package macros
Summary:        ROCm Compiler RPM macros
BuildArch:      noarch

%description macros
This package contains ROCm compiler related RPM macros.

%package -n rocm-device-libs
Summary:        AMD ROCm LLVM bit code libraries
Requires:       rocm-clang-devel
Requires:       rocm-lld
Requires:       rocm-llvm-static

%description -n rocm-device-libs
This package contains a set of AMD specific device-side language runtime
libraries in the form of bit code. Specifically:
 - Open Compute library controls
 - Open Compute Math library
 - Open Compute Kernel library
 - OpenCL built-in library
 - HIP built-in library
 - Heterogeneous Compute built-in library


%if 0%{?suse_version}
# 15.6
# rocm-comgr.x86_64: E: shlib-policy-name-error (Badness: 10000) libamd_comgr2
# Your package contains a single shared library but is not named after its SONAME.
%global comgr_name libamd_comgr3
%else
%global comgr_name rocm-comgr
%endif

%package -n %{comgr_name}
Summary:        AMD ROCm LLVM Code Object Manager
Provides:       rocm-comgr = %{comgr_full_api_ver}-%{release}
Provides:       comgr(major) = %{comgr_maj_api_ver}

%description -n %{comgr_name}
The AMD Code Object Manager (Comgr) is a shared library which provides
operations for creating and inspecting code objects.

%post -n %{comgr_name}  -p /sbin/ldconfig
%postun -n %{comgr_name} -p /sbin/ldconfig

%package -n %{comgr_name}-devel
Summary:        AMD ROCm LLVM Code Object Manager
Requires:       %{comgr_name}%{?_isa} = %{version}-%{release}
Requires:       rocm-device-libs
%if 0%{?suse_version}
Provides:       rocm-comgr-devel = %{version}-%{release}
%endif

%description -n %{comgr_name}-devel
The AMD Code Object Manager (Comgr) development package.

%package -n hipcc
Summary:        HIP compiler driver
Requires:       perl-base
Requires:       rocm-device-libs = %{version}-%{release}
Suggests:       rocminfo
%if 0%{?suse_version}
Provides:       hip = %{version}-%{release}
Obsoletes:      hip <= %{version}-%{release}
%endif

%description -n hipcc
hipcc is a compiler driver utility that will call clang or nvcc, depending on
target, and pass the appropriate include and library options for the target
compiler and HIP infrastructure.

hipcc will pass-through options to the target compiler. The tools calling hipcc
must ensure the compiler options are appropriate for the target compiler.

%package -n hipcc-libomp-devel
Summary:        OpenMP header files for hipcc
Requires:       hipcc = %{version}-%{release}
Requires:       libomp-devel

%description -n hipcc-libomp-devel
OpenMP header files compatible with HIPCC.

# ROCM LLVM

%package -n rocm-llvm-filesystem
Summary:        Filesystem package that owns the rocm llvm directory

%description -n rocm-llvm-filesystem
This package owns the rocm llvm directory : %{bundle_prefix}

%package -n rocm-llvm-libs
Summary:        The ROCm LLVM lib
Requires:       rocm-libc++%{?_isa} = %{version}-%{release}
Requires:       rocm-llvm-filesystem%{?_isa} = %{version}-%{release}

%description -n rocm-llvm-libs
%{summary}

%package -n rocm-llvm
Summary:        The ROCm LLVM
Requires:       rocm-llvm-libs%{?_isa} = %{version}-%{release}
# https://bugzilla.redhat.com/show_bug.cgi?id=2362780
#  /usr/lib64/rocm/llvm/bin/amdgpu-arch
#  Failed to 'dlopen' libhsa-runtime64.so
Recommends:     rocm-runtime-devel

%description -n rocm-llvm
%{summary}

%package -n rocm-llvm-devel
Summary:        Libraries and header files for ROCm LLVM
Requires:       rocm-llvm%{?_isa} = %{version}-%{release}
Requires:       zlib-devel

%description -n rocm-llvm-devel
%{summary}

%post -n rocm-llvm-devel -p /sbin/ldconfig
%postun -n rocm-llvm-devel -p /sbin/ldconfig

%package -n rocm-llvm-static
Summary:        Static libraries for ROCm LLVM
Requires:       rocm-llvm-devel%{?_isa} = %{version}-%{release}

%description -n rocm-llvm-static
%{summary}

# ROCM CLANG
%package -n rocm-clang-libs
Summary:        The ROCm compiler libs
Requires:       rocm-llvm-libs%{?_isa} = %{version}-%{release}

%description -n rocm-clang-libs
%{summary}

%post -n rocm-clang-libs -p /sbin/ldconfig
%postun -n rocm-clang-libs -p /sbin/ldconfig

%package -n rocm-clang-runtime-devel
Summary:        The ROCm compiler runtime

%description -n rocm-clang-runtime-devel
%{summary}

%package -n rocm-clang
Summary:        The ROCm compiler
Requires:       git
Requires:       python3
Requires:       rocm-clang-libs%{?_isa} = %{version}-%{release}
Requires:       rocm-clang-runtime-devel%{?_isa} = %{version}-%{release}
Requires:       rocm-libc++-devel%{?_isa} = %{version}-%{release}

%description -n rocm-clang
%{summary}

%package -n rocm-clang-devel
Summary:        Libraries and header files for ROCm CLANG
Requires:       rocm-clang%{?_isa} = %{version}-%{release}

%description -n rocm-clang-devel
%{summary}

# CLANG TOOLS EXTRA
%package -n rocm-clang-tools-extra
Summary:        Extra tools for clang
Requires:       rocm-clang-libs%{?_isa} = %{version}-%{release}

%description -n rocm-clang-tools-extra
A set of extra tools built using Clang's tooling API.

%package -n rocm-clang-tools-extra-devel
Summary:        Development header files for clang tools
Requires:       rocm-clang-tools-extra = %{version}-%{release}

%description -n rocm-clang-tools-extra-devel
Development header files for clang tools.

# ROCM LLD

%package -n rocm-lld
Summary:        The ROCm Linker
Requires:       rocm-llvm-libs%{?_isa} = %{version}-%{release}

%description -n rocm-lld
%{summary}

# ROCM LIBC++
%package -n rocm-libc++
Summary:        The ROCm libc++
Requires:       rocm-llvm-filesystem%{?_isa} = %{version}-%{release}

%description -n rocm-libc++
%{summary}

%package -n rocm-libc++-devel
Summary:        The ROCm libc++ libraries and headers
Requires:       rocm-libc++%{?_isa} = %{version}-%{release}

%description -n rocm-libc++-devel
%{summary}

%package -n rocm-libc++-static
Summary:        The ROCm libc++ static libraries
Requires:       rocm-libc++-devel%{?_isa} = %{version}-%{release}

%description -n rocm-libc++-static
%{summary}

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{rocm_version}

# rm llvm-project bits we do not need
rm -rf {bolt,flang,libc,libclc,lldb,llvm-libgcc,mlir,polly}

#Force static linking of libclang in comgr
sed -i "s/TARGET clangFrontendTool/true/" amd/comgr/CMakeLists.txt

install -pm 755 %{SOURCE1} prep.sh
sed -i -e 's@%%{_prefix}@%{_prefix}@' prep.sh
sed -i -e 's@%%{_lib}@%{_lib}@' prep.sh
sed -i -e 's@%%{amd_device_libs_prefix}@%{amd_device_libs_prefix}@' prep.sh
sed -i -e 's@%%{bundle_prefix}@%{bundle_prefix}@' prep.sh
grep -v '%%{' prep.sh

. ./prep.sh

%build
CLANG_VERSION=%llvm_maj_ver
LLVM_BINDIR=%{bundle_prefix}/bin
LLVM_LIBDIR=%{bundle_prefix}/lib
LLVM_CMAKEDIR=%{bundle_prefix}/lib/cmake/llvm

echo "%%rocmllvm_version $CLANG_VERSION"   > macros.rocmcompiler
echo "%%rocmllvm_bindir $LLVM_BINDIR"     >> macros.rocmcompiler
echo "%%rocmllvm_libdir $LLVM_LIBDIR"     >> macros.rocmcompiler
echo "%%rocmllvm_cmakedir $LLVM_CMAKEDIR" >> macros.rocmcompiler

# Real cores, No hyperthreading
COMPILE_JOBS=`cat /proc/cpuinfo | grep -m 1 'cpu cores' | awk '{ print $4 }'`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
# Take into account memmory usage per core, do not thrash real memory
LINK_MEM=4
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
LINK_JOBS=`eval "expr 1 + ${MEM_GB} / ${LINK_MEM}"`
JOBS=${COMPILE_JOBS}
if [ "$LINK_JOBS" -lt "$JOBS" ]; then
    JOBS=$LINK_JOBS
fi

%global llvm_projects "clang;clang-tools-extra;lld"
%global llvm_runtimes "compiler-rt;libcxx;libcxxabi"

p=$PWD

#
# BASE LLVM
#
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
 -DCOMPILER_RT_BUILD_CTX_PROFILE=OFF \\\
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
 -DLLVM_TOOL_GOLD_BUILD=ON \\\
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

pushd .
%if 0%{?suse_version}
%define __sourcedir llvm
%define __builddir build-llvm
%else
%define _vpath_srcdir llvm
%define _vpath_builddir build-llvm
%endif

# Mixing use of gcc and clang in the build conflicts with rpm's setting of flags.
# Set them manually as CMAKE_<LANG>_FLAGS
export CFLAGS=""
export CXXFLAGS=""
export LDFLAGS=""

# So just built tools can find their *.so's
export LD_LIBRARY_PATH=$PWD/build-llvm/lib
export CC=/usr/bin/gcc
export CXX=/usr/bin/g++

%if 0%{?suse_version}
%cmake \
%else
%__cmake -S llvm -B build-llvm \
%endif
       %{llvmrocm_cmake_config} \
       -DCMAKE_CXX_COMPILER=/usr/bin/g++ \
       -DCMAKE_C_COMPILER=/usr/bin/gcc \
       -DCMAKE_INSTALL_PREFIX=%{bundle_prefix} \
       -DCMAKE_INSTALL_LIBDIR=lib \
       -DLLVM_ENABLE_PROJECTS=%{llvm_projects}

%if 0%{?suse_version}
%cmake_build -j ${JOBS}
%else
%make_build -C build-llvm -j ${JOBS}
%endif

popd

build_stage1=$p/build-llvm

%global llvmrocm_stage1_config \\\
    -DCMAKE_AR=$build_stage1/bin/llvm-ar \\\
    -DCMAKE_C_COMPILER=$build_stage1/bin/clang \\\
    -DCMAKE_CXX_COMPILER=$build_stage1/bin/clang++ \\\
    -DCMAKE_LINKER=$build_stage1/bin/ld.lld \\\
    -DCMAKE_RANLIB=$build_stage1/bin/llvm-ranlib \\\
    -DLLVM_DIR=$build_stage1/lib/cmake/llvm \\\
    -DClang_DIR=$build_stage1/lib/cmake/clang \\\
    -DLLD_DIR=$build_stage1/lib/cmake/lld

#
# Rebuild and add libc++
#
pushd .
%if 0%{?suse_version}
%define __sourcedir llvm
%define __builddir build-llvm-2
%else
%define _vpath_srcdir llvm
%define _vpath_builddir build-llvm-2
%endif

export LD_LIBRARY_PATH=$PWD/build-llvm-2/lib

%cmake \
       %{llvmrocm_cmake_config} \
       %{llvmrocm_stage1_config} \
       -DCMAKE_INSTALL_PREFIX=%{bundle_prefix} \
       -DCMAKE_INSTALL_RPATH=%{bundle_prefix}/lib \
       -DCMAKE_INSTALL_LIBDIR=lib \
       -DCMAKE_SKIP_INSTALL_RPATH=OFF \
       -DCLANG_DEFAULT_LINKER=lld \
       -DLLVM_ENABLE_LLD=ON \
       -DLLVM_TOOL_COMPILER_RT_BUILD=ON \
       -DLLVM_TOOL_LIBCXXABI_BUILD=ON \
       -DLLVM_TOOL_LIBCXX_BUILD=ON \
       -DLLVM_ENABLE_PROJECTS=%{llvm_projects} \
       -DLLVM_ENABLE_RUNTIMES=%{llvm_runtimes}

%cmake_build -j ${JOBS}
popd

build_stage2=$p/build-llvm-2

%global llvmrocm_tools_config \\\
       -DLLVM_DIR=$build_stage2/lib/cmake/llvm \\\
       -DClang_DIR=$build_stage2/lib/cmake/clang \\\
       -DLLD_DIR=$build_stage2/lib/cmake/lld

export CC=$build_stage2/bin/clang
export CXX=$build_stage2/bin/clang++
export LD=$build_stage2/bin/ld.lld

#
# DEVICE LIBS
#
pushd .
%if 0%{?suse_version}
%define __sourcedir amd/device-libs
%define __builddir build-devicelibs
%else
%define _vpath_srcdir amd/device-libs
%define _vpath_builddir build-devicelibs
%endif

%cmake \
       %{llvmrocm_cmake_config} \
       %{llvmrocm_tools_config} \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC_NEW="%{amd_device_libs_prefix}/amdgcn" \
       -DROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC_OLD=""

%cmake_build -j ${JOBS}
popd

build_devicelibs=$p/build-devicelibs
%global llvmrocm_devicelibs_config \\\
	-DAMDDeviceLibs_DIR=$build_devicelibs/%{_lib}/cmake/AMDDeviceLibs

#
# HIPCC
#
pushd .
%if 0%{?suse_version}
%define __sourcedir amd/hipcc
%define __builddir build-hipcc
%else
%define _vpath_srcdir amd/hipcc
%define _vpath_builddir build-hipcc
%endif

%cmake \
       %{llvmrocm_cmake_config} \
       %{llvmrocm_tools_config} \
       %{llvmrocm_devicelibs_config} \
       -DCMAKE_INSTALL_RPATH=%{bundle_prefix}/lib \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DCMAKE_SKIP_INSTALL_RPATH=OFF

%cmake_build -j ${JOBS}
popd

#
# COMGR
#
pushd .
%if 0%{?suse_version}
%define __sourcedir amd/comgr
%define __builddir build-comgr
%else
%define _vpath_srcdir amd/comgr
%define _vpath_builddir build-comgr
%endif

%cmake -G "Unix Makefiles" \
       %{llvmrocm_cmake_config} \
       %{llvmrocm_tools_config} \
       %{llvmrocm_devicelibs_config} \
       -DBUILD_SHARED_LIBS=ON \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_INSTALL_LIBDIR=%{_lib}

# cmake produces a link.txt that includes libLLVM*.so, hack it out
%if 0%{?suse_version}
sed -i -e 's@libLLVM.so.19.0git@libLLVMCore.a@' CMakeFiles/amd_comgr.dir/link.txt
# Order of link is wrong include some missing libs
sed -i -e 's@-lrt -lm@-lLLVMCoverage -lLLVMFrontendDriver -lLLVMFrontendHLSL -lLLVMLTO -lLLVMOption -lLLVMSymbolize -lLLVMWindowsDriver -lrt -lm@' CMakeFiles/amd_comgr.dir/link.txt
%else
sed -i -e 's@libLLVM.so.19.0git@libLLVMCore.a@' build-comgr/CMakeFiles/amd_comgr.dir/link.txt
# Order of link is wrong include some missing libs
sed -i -e 's@-lrt -lm@-lLLVMCoverage -lLLVMFrontendDriver -lLLVMFrontendHLSL -lLLVMLTO -lLLVMOption -lLLVMSymbolize -lLLVMWindowsDriver -lrt -lm@' build-comgr/CMakeFiles/amd_comgr.dir/link.txt
%endif

%cmake_build -j ${JOBS}

# Check that static linking happened
# ldd build-comgr/libamd_comgr.so

popd

%check
%if 0%{?suse_version}
%define __sourcedir amd/device-libs
%define __builddir build-devicelibs
%else
%define _vpath_srcdir amd/device-libs
%define _vpath_builddir build-devicelibs
%endif
pushd .
# Workaround for bug in cmake tests not finding amdgcn:
ln -s %{amd_device_libs_prefix}/amdgcn build-devicelibs/amdgcn
%ctest
popd

%install
install -Dpm 644 macros.rocmcompiler \
    %{buildroot}%{_rpmmacrodir}/macros.rocmcompiler

#
# BASE LLVM
#
pushd .
%if 0%{?suse_version}
%define __builddir build-llvm-2
%else
%define _vpath_builddir build-llvm-2
%endif

%cmake_install

popd

#
# DEVICE LIBS
#
pushd .
%if 0%{?suse_version}
%define __builddir build-devicelibs
%else
%define _vpath_builddir build-devicelibs
%endif

%cmake_install
popd

#
# COMGR
#
pushd .
%if 0%{?suse_version}
%define __builddir build-comgr
%else
%define _vpath_builddir build-comgr
%endif

%cmake_install
popd

#
# HIPCC
#
pushd .
%if 0%{?suse_version}
%define __builddir build-hipcc
%else
%define _vpath_builddir build-hipcc
%endif

%cmake_install
popd

# Make directories users of rocm-rpm-modules will install to
%global modules_gpu_list gfx8 gfx9 gfx10 gfx11 gfx12 gfx906 gfx908 gfx90a gfx942 gfx950 gfx1031 gfx1036 gfx1100 gfx1101 gfx1102 gfx1103 gfx1150 gfx1151 gfx1152 gfx1153 gfx1200 gfx1201
for gpu in %{modules_gpu_list}
do
    mkdir -p %{buildroot}%{_libdir}/rocm/$gpu/lib/cmake
    mkdir -p %{buildroot}%{_libdir}/rocm/$gpu/bin
    mkdir -p %{buildroot}%{_libdir}/rocm/$gpu/include
done
mkdir -p %{buildroot}%{_libdir}/rocm/lib/cmake
mkdir -p %{buildroot}%{_libdir}/rocm/bin
mkdir -p %{buildroot}%{_libdir}/rocm/include

rm -rf %{buildroot}%{_prefix}/hip
if [ -f %{buildroot}%{_prefix}/share/doc/packages/rocm-compilersupport/LICENSE.TXT ]; then
    rm %{buildroot}%{_prefix}/share/doc/packages/rocm-compilersupport/LICENSE.*
fi
if [ -f %{buildroot}%{_prefix}/share/doc/packages/rocm-compilersupport/NOTICES.txt ]; then
    rm %{buildroot}%{_prefix}/share/doc/packages/rocm-compilersupport/NOTICES.txt
fi
if [ -f %{buildroot}%{_prefix}/share/doc/packages/rocm-compilersupport/README.md ]; then
    rm %{buildroot}%{_prefix}/share/doc/packages/rocm-compilersupport/README.md
fi

%if 0%{?suse_version}
find %{buildroot}%{bundle_prefix}/bin -type f -executable -exec strip {} \;
find %{buildroot}%{_bindir}           -type f -executable -exec strip {} \;
find %{buildroot}%{bundle_prefix}/lib -type f -name '*.so*' -exec strip {} \;
find %{buildroot}%{_libdir}           -type f -name '*.so*' -exec strip {} \;
%endif

# Remove lld's libs
rm -rf %{buildroot}%{bundle_prefix}/include/lld
rm -rf %{buildroot}%{bundle_prefix}/lib/cmake/lld
rm -rf %{buildroot}%{bundle_prefix}/lib/liblld*

# Remove exec perm
chmod a-x %{buildroot}%{bundle_prefix}/share/opt-viewer/optpmap.py
chmod a-x %{buildroot}%{bundle_prefix}/share/opt-viewer/style.css

%if %{with perl}
# Fix perl module files installation:
# Eventually upstream plans to deprecate Perl usage, see README.md
mkdir -p %{buildroot}%{perl_vendorlib}
mv %{buildroot}%{_bindir}/hip*.pm %{buildroot}%{perl_vendorlib}
%else
rm %{buildroot}%{_bindir}/hip*.pm
rm %{buildroot}%{_bindir}/hip*.pl
%endif

#Clean up dupes:
%if 0%{?fedora} || 0%{?suse_version}
%fdupes %{buildroot}%{_prefix}
%endif

%files macros
%{_rpmmacrodir}/macros.rocmcompiler

%files -n rocm-device-libs
%dir %{_libdir}/cmake/AMDDeviceLibs
%license amd/device-libs/LICENSE.TXT
%doc amd/device-libs/README.md amd/device-libs/doc/*.md
%{_libdir}/cmake/AMDDeviceLibs/*.cmake
%{_prefix}/%{amd_device_libs_prefix}/amdgcn
%if 0%{?rhel} || 0%{?fedora}
%exclude %{_docdir}/ROCm-Device-Libs
%endif

%files -n %{comgr_name}
%license amd/comgr/LICENSE.txt
%license amd/comgr/NOTICES.txt
%doc amd/comgr/README.md
%{_libdir}/libamd_comgr.so.*
%if 0%{?rhel} || 0%{?fedora}
%exclude %{_docdir}/amd_comgr
%endif

%files -n %{comgr_name}-devel
%dir %{_includedir}/amd_comgr
%dir %{_libdir}/cmake/amd_comgr
%{_includedir}/amd_comgr/amd_comgr.h
%{_libdir}/libamd_comgr.so
%{_libdir}/cmake/amd_comgr/*.cmake

%files -n hipcc
%license amd/hipcc/LICENSE.txt
%doc amd/hipcc/README.md
%{_bindir}/hipcc
%{_bindir}/hipconfig

%if %{with perl}
%{_bindir}/hipcc.pl
%{_bindir}/hipconfig.pl
%{perl_vendorlib}/hip*.pm
%endif

%if 0%{?rhel} || 0%{?fedora}
%exclude %{_docdir}/hipcc
%endif

%files -n hipcc-libomp-devel

# ROCM LLVM
%files -n rocm-llvm-filesystem
%dir %{_libdir}/rocm
# For rocm-rpm-modules
%dir %{_libdir}/rocm/bin
%dir %{_libdir}/rocm/include
%dir %{_libdir}/rocm/lib
%dir %{_libdir}/rocm/gfx8
%dir %{_libdir}/rocm/gfx8/bin
%dir %{_libdir}/rocm/gfx8/include
%dir %{_libdir}/rocm/gfx8/lib
%dir %{_libdir}/rocm/gfx8/lib/cmake
%dir %{_libdir}/rocm/gfx9
%dir %{_libdir}/rocm/gfx9/bin
%dir %{_libdir}/rocm/gfx9/include
%dir %{_libdir}/rocm/gfx9/lib
%dir %{_libdir}/rocm/gfx9/lib/cmake
%dir %{_libdir}/rocm/gfx10
%dir %{_libdir}/rocm/gfx10/bin
%dir %{_libdir}/rocm/gfx10/include
%dir %{_libdir}/rocm/gfx10/lib
%dir %{_libdir}/rocm/gfx10/lib/cmake
%dir %{_libdir}/rocm/gfx11
%dir %{_libdir}/rocm/gfx11/bin
%dir %{_libdir}/rocm/gfx11/include
%dir %{_libdir}/rocm/gfx11/lib
%dir %{_libdir}/rocm/gfx11/lib/cmake
%dir %{_libdir}/rocm/gfx12
%dir %{_libdir}/rocm/gfx12/bin
%dir %{_libdir}/rocm/gfx12/include
%dir %{_libdir}/rocm/gfx12/lib
%dir %{_libdir}/rocm/gfx12/lib/cmake
%dir %{_libdir}/rocm/gfx906
%dir %{_libdir}/rocm/gfx906/bin
%dir %{_libdir}/rocm/gfx906/include
%dir %{_libdir}/rocm/gfx906/lib
%dir %{_libdir}/rocm/gfx906/lib/cmake
%dir %{_libdir}/rocm/gfx908
%dir %{_libdir}/rocm/gfx908/bin
%dir %{_libdir}/rocm/gfx908/include
%dir %{_libdir}/rocm/gfx908/lib
%dir %{_libdir}/rocm/gfx908/lib/cmake
%dir %{_libdir}/rocm/gfx90a
%dir %{_libdir}/rocm/gfx90a/bin
%dir %{_libdir}/rocm/gfx90a/include
%dir %{_libdir}/rocm/gfx90a/lib
%dir %{_libdir}/rocm/gfx90a/lib/cmake
%dir %{_libdir}/rocm/gfx942
%dir %{_libdir}/rocm/gfx942/bin
%dir %{_libdir}/rocm/gfx942/include
%dir %{_libdir}/rocm/gfx942/lib
%dir %{_libdir}/rocm/gfx942/lib/cmake
%dir %{_libdir}/rocm/gfx950
%dir %{_libdir}/rocm/gfx950/bin
%dir %{_libdir}/rocm/gfx950/include
%dir %{_libdir}/rocm/gfx950/lib
%dir %{_libdir}/rocm/gfx950/lib/cmake
%dir %{_libdir}/rocm/gfx1031
%dir %{_libdir}/rocm/gfx1031/bin
%dir %{_libdir}/rocm/gfx1031/include
%dir %{_libdir}/rocm/gfx1031/lib
%dir %{_libdir}/rocm/gfx1031/lib/cmake
%dir %{_libdir}/rocm/gfx1036
%dir %{_libdir}/rocm/gfx1036/bin
%dir %{_libdir}/rocm/gfx1036/include
%dir %{_libdir}/rocm/gfx1036/lib
%dir %{_libdir}/rocm/gfx1036/lib/cmake
%dir %{_libdir}/rocm/gfx1100
%dir %{_libdir}/rocm/gfx1100/bin
%dir %{_libdir}/rocm/gfx1100/include
%dir %{_libdir}/rocm/gfx1100/lib
%dir %{_libdir}/rocm/gfx1100/lib/cmake
%dir %{_libdir}/rocm/gfx1101
%dir %{_libdir}/rocm/gfx1101/bin
%dir %{_libdir}/rocm/gfx1101/include
%dir %{_libdir}/rocm/gfx1101/lib
%dir %{_libdir}/rocm/gfx1101/lib/cmake
%dir %{_libdir}/rocm/gfx1102
%dir %{_libdir}/rocm/gfx1102/bin
%dir %{_libdir}/rocm/gfx1102/include
%dir %{_libdir}/rocm/gfx1102/lib
%dir %{_libdir}/rocm/gfx1102/lib/cmake
%dir %{_libdir}/rocm/gfx1103
%dir %{_libdir}/rocm/gfx1103/bin
%dir %{_libdir}/rocm/gfx1103/include
%dir %{_libdir}/rocm/gfx1103/lib
%dir %{_libdir}/rocm/gfx1103/lib/cmake
%dir %{_libdir}/rocm/gfx1150
%dir %{_libdir}/rocm/gfx1150/bin
%dir %{_libdir}/rocm/gfx1150/include
%dir %{_libdir}/rocm/gfx1150/lib
%dir %{_libdir}/rocm/gfx1150/lib/cmake
%dir %{_libdir}/rocm/gfx1151
%dir %{_libdir}/rocm/gfx1151/bin
%dir %{_libdir}/rocm/gfx1151/include
%dir %{_libdir}/rocm/gfx1151/lib
%dir %{_libdir}/rocm/gfx1151/lib/cmake
%dir %{_libdir}/rocm/gfx1152
%dir %{_libdir}/rocm/gfx1152/bin
%dir %{_libdir}/rocm/gfx1152/include
%dir %{_libdir}/rocm/gfx1152/lib
%dir %{_libdir}/rocm/gfx1152/lib/cmake
%dir %{_libdir}/rocm/gfx1153
%dir %{_libdir}/rocm/gfx1153/bin
%dir %{_libdir}/rocm/gfx1153/include
%dir %{_libdir}/rocm/gfx1153/lib
%dir %{_libdir}/rocm/gfx1153/lib/cmake
%dir %{_libdir}/rocm/gfx1200
%dir %{_libdir}/rocm/gfx1200/bin
%dir %{_libdir}/rocm/gfx1200/include
%dir %{_libdir}/rocm/gfx1200/lib
%dir %{_libdir}/rocm/gfx1200/lib/cmake
%dir %{_libdir}/rocm/gfx1201
%dir %{_libdir}/rocm/gfx1201/bin
%dir %{_libdir}/rocm/gfx1201/include
%dir %{_libdir}/rocm/gfx1201/lib
%dir %{_libdir}/rocm/gfx1201/lib/cmake
# For llvm
%dir %{bundle_prefix}
%dir %{bundle_prefix}/bin
%dir %{bundle_prefix}/include
%dir %{bundle_prefix}/include/clang
%dir %{bundle_prefix}/include/clang-c
%dir %{bundle_prefix}/include/llvm
%dir %{bundle_prefix}/include/llvm-c
%dir %{bundle_prefix}/lib
%dir %{bundle_prefix}/lib/clang
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/cuda_wrappers
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/llvm_libc_wrappers
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/openmp_wrappers
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/ppc_wrappers
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/lib
%dir %{bundle_prefix}/lib/clang/%{llvm_maj_ver}/lib/linux
%dir %{bundle_prefix}/lib/cmake
%dir %{bundle_prefix}/lib/cmake/clang
%dir %{bundle_prefix}/lib/cmake/llvm
%dir %{bundle_prefix}/share
%dir %{bundle_prefix}/share/clang
%dir %{bundle_prefix}/share/opt-viewer

%files -n rocm-llvm-libs
%{bundle_prefix}/lib/libLLVM-*.so
%{bundle_prefix}/lib/libLLVM.so.*
%{bundle_prefix}/lib/libLTO.so.*
%{bundle_prefix}/lib/libRemarks.so.*

%post -n rocm-llvm-libs -p /sbin/ldconfig
%postun -n rocm-llvm-libs -p /sbin/ldconfig

%files -n rocm-llvm
%license llvm/LICENSE.TXT
%{bundle_prefix}/bin/bugpoint
%{bundle_prefix}/bin/llc
%{bundle_prefix}/bin/lli
%{bundle_prefix}/bin/amdgpu-arch
%{bundle_prefix}/bin/dsymutil
%{bundle_prefix}/bin/llvm*
%{bundle_prefix}/bin/opt
%{bundle_prefix}/bin/reduce-chunk-list
%{bundle_prefix}/bin/sancov
%{bundle_prefix}/bin/sanstats
%{bundle_prefix}/bin/verify-uselistorder
%{bundle_prefix}/share/opt-viewer/*

%files -n rocm-llvm-devel
%license llvm/LICENSE.TXT
%{bundle_prefix}/include/llvm/*
%{bundle_prefix}/include/llvm-c/*
%{bundle_prefix}/lib/cmake/llvm/*
%{bundle_prefix}/lib/libLLVM.so
%{bundle_prefix}/lib/libLTO.so
%{bundle_prefix}/lib/libRemarks.so
%{bundle_prefix}/lib/LLVMgold.so

%files -n rocm-llvm-static
%license llvm/LICENSE.TXT
%{bundle_prefix}/lib/libLLVM*.a

# ROCM CLANG
%files -n rocm-clang-libs
%{bundle_prefix}/lib/libclang*.so.*

%files -n rocm-clang-runtime-devel
%{bundle_prefix}/lib/clang/%{llvm_maj_ver}/include/*
%{bundle_prefix}/lib/clang/%{llvm_maj_ver}/lib/linux/clang_rt.*
%{bundle_prefix}/lib/clang/%{llvm_maj_ver}/lib/linux/libclang_rt.*

%files -n rocm-clang
%license clang/LICENSE.TXT
%{bundle_prefix}/bin/c-index-test
%{bundle_prefix}/bin/clang*
%{bundle_prefix}/bin/diagtool
%{bundle_prefix}/bin/find-all-symbols
%{bundle_prefix}/bin/flang
%{bundle_prefix}/bin/git-clang-format
%{bundle_prefix}/bin/hmaptool
%{bundle_prefix}/bin/modularize
%{bundle_prefix}/bin/nvptx-arch
%{bundle_prefix}/bin/pp-trace
%{bundle_prefix}/share/clang/*
%{bundle_prefix}/share/clang-doc

%files -n rocm-clang-devel
%license clang/LICENSE.TXT
%{bundle_prefix}/include/clang/*
%{bundle_prefix}/include/clang-c/*
%{bundle_prefix}/lib/cmake/clang/*
%{bundle_prefix}/lib/libclang*.so

# ROCM CLANG TOOLS EXTRA
%files -n rocm-clang-tools-extra
%license clang-tools-extra/LICENSE.TXT
%{bundle_prefix}/bin/run-clang-tidy

%files -n rocm-clang-tools-extra-devel
%dir %{bundle_prefix}/include/clang-tidy
%license clang-tools-extra/LICENSE.TXT
%{bundle_prefix}/include/clang-tidy/*

# ROCM LLD
%files -n rocm-lld
%license lld/LICENSE.TXT
%{bundle_prefix}/bin/ld.lld
%{bundle_prefix}/bin/ld64.lld
%{bundle_prefix}/bin/lld
%{bundle_prefix}/bin/lld-link
%{bundle_prefix}/bin/wasm-ld

# ROCM LIBC++
%files -n rocm-libc++
%license libcxx/LICENSE.TXT
%{bundle_prefix}/lib/libc++.so.*
%{bundle_prefix}/lib/libc++abi.so.*
%{bundle_prefix}/lib/libc++.modules.json

%post -n rocm-libc++ -p /sbin/ldconfig
%postun -n rocm-libc++ -p /sbin/ldconfig

%files -n rocm-libc++-devel
%dir %{bundle_prefix}/share/libc++
%{bundle_prefix}/include/c++/
%{bundle_prefix}/share/libc++/
%{bundle_prefix}/lib/libc++.so
%{bundle_prefix}/lib/libc++abi.so

%files -n rocm-libc++-static
%{bundle_prefix}/lib/libc++.a
%{bundle_prefix}/lib/libc++abi.a
%{bundle_prefix}/lib/libc++experimental.a

%changelog
