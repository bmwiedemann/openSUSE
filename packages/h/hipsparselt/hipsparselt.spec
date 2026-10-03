#
# spec file for package hipsparselt
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


%global upstreamname hipsparselt

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
%global skip_install_rpath OFF
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global skip_install_rpath ON
%endif
%if 0%{?suse_version}
%global hipsparselt_name libhipsparselt0
%else
%global hipsparselt_name hipsparselt
%endif

# The tensilelite that hipSPARELt use comes from hipBLASLt
# But not the matching release tag, a custom commit that is
# stored in the toplevel tensilelite_tag.txt file
#
# https://github.com/ROCm/hipSPARSELt/issues/248
#
# When keeping sync the hipblaslt project patch is difficult,
# use the hipblaslt repo tag, not the tensilelit_tag file

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

# On CS10
# Depends on finding the build dir
# $ hipsparselt-test
# hipSPARSELt version: 203
# ...
# [ FATAL ] /builddir/build/BUILD/googletest-1.14.0/googletest/src/gtest-internal-inl.h:685:: Condition !original_working_dir_.IsEmpty() failed. Failed to get the current working directory.
#
# So need to build with rpmbuild, not mock and run test on same machine with a newer gtest
%bcond_with test
%if %{with test}
%global __brp_check_rpaths %{nil}
%global build_test ON
%else
%global build_test OFF
%endif
# Fortran is only used in testing
%global build_fflags %{nil}

%global tensile_version 4.33.0
%global tensile_verbose 1

# match hipblaslt
%global gpu_list "gfx942;gfx950"

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

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

# Request for python-nanobind on EPEL
# https://bugzilla.redhat.com/show_bug.cgi?id=2402409
%if 0%{?fedora}
%bcond_without nanobind
%else
%bcond_with nanobind
%endif

%if 0%{?suse_version}
%{?sle15_python_module_pythons}
%{?!python_module:%define python_module() python3-%{**}}
%else
%define python_exec python3
%define python_expand python3
%endif

Name:           hipsparselt%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        6%{?dist}
%endif
Summary:        A SPARSE marshaling library
License:        MIT
URL:            https://github.com/ROCm/rocm-libraries

Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

# Force sync to same version of hipblaslt
Source1:        %{url}/releases/download/rocm-%{version}/hipblaslt.tar.gz#/hipblaslt-%{version}.tar.gz

%global nanobind_version 2.9.2
%global nanobind_giturl https://github.com/wjakob/nanobind
Source10:       %{nanobind_giturl}/archive/v%{nanobind_version}/nanobind-%{nanobind_version}.tar.gz
%global robinmap_version 1.3.0
%global robinmap_giturl https://github.com/Tessil/robin-map
Source11:       %{robinmap_giturl}/archive/v%{robinmap_version}/robin-map-%{robinmap_version}.tar.gz

%if %{with preview}
#Source3:        %{url}/releases/download/%{pkg_src}/stinkytofu.tar.gz#/stinkytofu-%{version}.tar.gz
#Source4:        %{url}/releases/download/%{pkg_src}/origami.tar.gz#/origami-%{version}.tar.gz
%endif

%if %{with preview}
Patch1:         0001-hipblaslt-preview-tensilelit-remove-yappi-dependency.patch
Patch4:         0001-hipblaslt-preview-tensilelit-use-nanobind-tarball.patch
%else
# This are patches from the hiblaslt package for patching tensile
Patch1:         0001-hipblaslt-tensilelite-remove-yappi-dependency.patch
Patch2:         0001-hipblaslt-tensilelite-use-fedora-paths.patch
Patch4:         0001-hipblaslt-find-origami-package.patch
# do not try to fetch, point to the nanobind tarball
Patch5:         0001-hipblaslt-tensilelite-use-nanobind-tarball.patch
%endif

%if %{with ninja}
BuildRequires:  ninja-build
%endif

BuildRequires:  amdsmi%{pkg_suffix}-devel
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hipcc%{pkg_suffix}
BuildRequires:  hipsparse%{pkg_suffix}-devel
BuildRequires:  libzstd-devel
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-filesystem%{pkg_suffix}
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-llvm%{pkg_suffix}-devel
BuildRequires:  rocm-omp-devel
BuildRequires:  rocm-origami%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  rocm-smi%{pkg_suffix}-devel
BuildRequires:  rocminfo%{pkg_suffix}
BuildRequires:  rocsparse%{pkg_suffix}-devel
BuildRequires:  roctracer%{pkg_suffix}-devel
BuildRequires:  zlib-devel

# For tensilelite
%if 0%{?suse_version}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module joblib}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module setuptools}
BuildRequires:  msgpack-cxx-devel
BuildRequires:  python-rpm-macros
%global tensile_library_format yaml
%global tensile_verbose 2
%else
BuildRequires:  python3-devel
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)
%if %{with nanobind}
BuildRequires:  python3dist(nanobind)
%endif
BuildRequires:  msgpack-devel
%global tensile_library_format msgpack
%global tensile_verbose 1
%endif

%if %{with test}
BuildRequires:  chrpath
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-gfortran
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
%endif

Provides:       hipsparselt%{pkg_suffix} = %{version}-%{release}
Provides:       bundled(python-tensile) = %{tensile_version}
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocm-hip%{pkg_suffix}
Requires:       rocm-origami%{pkg_suffix}
Requires:       roctracer%{pkg_suffix}

%if %{without nanobind}
# BSD-3-Clause
Provides:       bundled(nanobind) = %{nanobind_version}
Provides:       bundled(robin-map) = %{robinmap_version}
%endif

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
hipSPARSELt is a SPARSE marshaling library, with multiple
supported backends. It sits between the application and a
'worker' SPARSE library, marshaling inputs into the backend
library and marshaling results back to the application.
hipSPARSELt exports an interface that does not require the
client to change, regardless of the chosen backend. Currently,
hipSPARSELt supports the rocSPARSELt backend.

%if 0%{?suse_version}
%package -n %{hipsparselt_name}
Summary:        Runtime for %{name}

%description -n %{hipsparselt_name}
%summary

%ldconfig_scriptlets -n %{hipsparselt_name}
%endif

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{hipsparselt_name}%{?_isa} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}
Provides:       hipsparselt%{pkg_suffix}-devel = %{version}-%{release}

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}

%description test
%{summary}
%endif

%prep
%if %{with preview}
# Make a sparse rocm-libraries
mkdir shared projects
cd shared
# stinkytofu
tar xf %{SOURCE3}
cd stinkytofu
# src/serialization/asm/PatternParser.cpp:794:13: error: unknown type name 'uint32_t'
sed -i -e '/#include <sstream>.*/a#include <stdint.h>' src/serialization/asm/PatternParser.cpp
sed -i -e '/#include <vector>.*/a#include <stdint.h>' include/stinkytofu/serialization/logical/IRSerializer.hpp
# src/transforms/asm/dag/ReadyQueue.hpp:49:31: error: use of undeclared identifier 'UINT_MAX'
sed -i -e '/#include <queue>.*/a#include <limits.h>' src/transforms/asm/dag/ReadyQueue.hpp
sed -i -e '/#include <string_view>.*/a#include <limits.h>' src/serialization/asm/IRParser.cpp
sed -i -e '/#include <utility>.*/a#include <limits.h>' src/transforms/asm/StinkyWmmaVgprReorderPass.cpp
# No clang-tidy
sed -i -e 's@include(ClangTidy)@@' CMakeLists.txt
sed -i -e 's@add_clang_tidy_custom_target()@@' CMakeLists.txt
# No ../../cmake/modues/default_amdclang.cmake
sed -i -e '/default_amdclang/d' CMakeLists.txt
cd ..
tar xf %{SOURCE4}
cd ../projects
# hipsparselt
tar xf %{SOURCE0}
# hipblaslt
tar xf %{SOURCE1}
cd hipblaslt
# tensile path to tools need to change
sed -i -e 's@globalParameters["ROCmPath"] = "/opt/rocm"@globalParameters["ROCmPath"] = "%{pkg_prefix}"@' tensilelite/Tensile/Common/GlobalParameters.py
sed -i -e 's@DEFAULT_ROCM_BIN_PATH_POSIX = Path("/opt/rocm/bin")@DEFAULT_ROCM_BIN_PATH_POSIX = Path("%{pkg_prefix}/bin")@' tensilelite/Tensile/Toolchain/Validators.py
sed -i -e 's@DEFAULT_ROCM_LLVM_BIN_PATH_POSIX = Path("/opt/rocm/lib/llvm/bin")@DEFAULT_ROCM_LLVM_BIN_PATH_POSIX = Path("%{rocmllvm_bindir}")@' tensilelite/Tensile/Toolchain/Validators.py

# nanobind bundle
tar xf %{SOURCE10}
mv nanobind-* nanobind
cd nanobind
tar xf %{SOURCE11}
cp -r robin-map-*/* ext/robin_map/
cd ..
tar czf nanobind.tar.gz nanobind
cd ../..
%patch 1 -p1
%patch 4 -p1
%else

%setup -q -n %{upstreamname}

tar xf %{SOURCE1}
cd hipblaslt
%autopatch -p3

# Use PATH to find where TensileGetPath and other tensile bins are
sed -i -e 's@${Tensile_PREFIX}/bin/TensileGetPath@TensileGetPath@g'            tensilelite/Tensile/cmake/TensileConfig.cmake

# Make sure hip/hip_runtime.h is found
sed -i -e 's@-x hip @-I%{pkg_prefix}/include -x hip @' device-library/matrix-transform/CMakeLists.txt
sed -i -e 's@"-D__HIP_HCC_COMPAT_MODE__=1"@"-D__HIP_HCC_COMPAT_MODE__=1","-I%{pkg_prefix}/include"@' tensilelite/Tensile/Toolchain/Component.py

%if %{with nanobind}
# Disable download of nanobind
sed -i -e 's@FetchContent_MakeAvailable(nanobind)@find_package(nanobind)@' tensilelite/rocisa/CMakeLists.txt
%else
# Use bundled nanobind
tar xf %{SOURCE10}
mv nanobind-* nanobind
cd nanobind
tar xf %{SOURCE11}
cp -r robin-map-*/* ext/robin_map/
cd ..
tar czf nanobind.tar.gz nanobind
%endif

cd ..

# Prevent the virtualenv install from cmake
sed -i -e 's@virtualenv_install@#virtualenv_install@' CMakeLists.txt

# Unforce the setting of libdir
# https://github.com/ROCm/hipSPARSELt/issues/256
sed -i -e 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' CMakeLists.txt

# change looking for cblas to flexiblas
sed -i -e 's@find_package( cblas REQUIRED CONFIG )@#find_package( cblas REQUIRED CONFIG )@' clients/CMakeLists.txt
sed -i -e 's@set( BLAS_LIBRARY "blas" )@set( BLAS_LIBRARY "flexiblas" )@' clients/CMakeLists.txt

%if %{without preview}
# We are building from a tarball, not a git repo
sed -i -e 's@find_package(Git REQUIRED)@#find_package(Git REQUIRED)@' hipblaslt/cmake/dependencies.cmake
%endif
%endif

%build
%if %{with preview}
cd projects/hipsparselt
HIPBLASLT_PATH=${PWD}/../hipblaslt
%else

HIPBLASLT_PATH=$PWD/hipblaslt
cd hipblaslt
# disable openmp
sed -i -e 's@option(HIPBLASLT_ENABLE_OPENMP "Use OpenMP to improve performance." ON)@option(HIPBLASLT_ENABLE_OPENMP "Use OpenMP to improve performance." OFF)@' CMakeLists.txt

# Do a manual install instead of cmake's virtualenv
cd tensilelite
TL=$PWD

python3 setup.py install --root $TL
cd ../..

# Should not have to do this
export PATH=%{pkg_prefix}/bin:%{rocmllvm_bindir}:$PATH
CLANG_PATH=`hipconfig --hipclangpath`
ROCM_CLANG=${CLANG_PATH}/clang
RESOURCE_DIR=`${ROCM_CLANG} -print-resource-dir`
export DEVICE_LIB_PATH=${RESOURCE_DIR}/amdgcn/bitcode
export TENSILE_ROCM_ASSEMBLER_PATH=${CLANG_PATH}/clang++
export TENSILE_ROCM_OFFLOAD_BUNDLER_PATH=${CLANG_PATH}/clang-offload-bundler

# Look for the just built tensilelite
export PATH=${TL}/%{_bindir}:$PATH
export PYTHONPATH=${TL}%{python3_sitelib}:$PYTHONPATH
export Tensile_DIR=${TL}%{python3_sitelib}/Tensile
# Uncomment and see if the path is sane
# TensileGetPath
%endif

%cmake %{cmake_generator} \
       -DGPU_TARGETS=%{gpu_list} \
       -DBLAS_INCLUDE_DIR=%{_includedir}/flexiblas \
       -DBUILD_CLIENTS_TESTS=%{build_test} \
       -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
       -DBUILD_VERBOSE=ON \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/amdclang \
       -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/amdclang++ \
       -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
       -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
       -DCMAKE_INSTALL_RPATH=%{pkg_prefix}/%{pkg_libdir} \
       -DCMAKE_PREFIX_PATH=%{python3_sitelib}/nanobind \
       -DCMAKE_SKIP_RPATH=%{skip_install_rpath} \
       -DCMAKE_SKIP_INSTALL_RPATH=%{skip_install_rpath} \
       -DCMAKE_Fortran_COMPILER=gfortran \
       -DCMAKE_VERBOSE_MAKEFILE=ON \
       -DHIP_PLATFORM=amd \
       -DHIPSPARSELT_HIPBLASLT_PATH=${HIPBLASLT_PATH} \
       -DHIPSPARSELT_ENABLE_CLIENT=OFF \
       -DHIPSPARSELT_ENABLE_OPENMP=OFF \
       -DROCM_SYMLINK_LIBS=OFF \
       -DTensile_LIBRARY_FORMAT=%{tensile_library_format} \
       -DTensile_TEST_LOCAL_PATH=${TL} \
       -DTensile_VERBOSE=%{tensile_verbose} \
       -DVIRTUALENV_BIN_DIR=%{_bindir} \
       -DVIRTUALENV_SITE_PATH=${TL}%{python3_sitelib} \
       %{nil}

%if %{with preview}
# To find the just built stinkytofu
export LD_LIBRARY_PATH=${PWD}/%{_vpath_builddir}/hipblaslt/tensilelite/rocisa/stinkytofu:$LD_LIBRARY_PATH
%endif

%cmake_build

%install
%if %{with preview}
cd projects/hipsparselt
%endif

%cmake_install

# Extra license
rm -f %{buildroot}%{pkg_prefix}/share/doc/hipsparselt/LICENSE.md

# hipsparselt.x86_64: W: unstripped-binary-or-object /usr/lib64/hipsparselt/library/Kernels.so-000-gfx1100.hsaco
find %{buildroot}%{pkg_prefix}/%{pkg_libdir}/hipsparselt/library/ \
     -name 'Kernels*.hsaco' -exec %{rocmllvm_bindir}/llvm-strip {} +
# hipsparselt.x86_64: W: unstripped-binary-or-object /usr/lib64/hipsparselt/library/extop_gfx942.co
find %{buildroot}%{pkg_prefix}/%{pkg_libdir}/hipsparselt/library/ \
     -name 'extop_*.co' -exec %{rocmllvm_bindir}/llvm-strip {} +

# hipsparselt.x86_64: E: ldd-failed /usr/lib64/hipsparselt/library/Kernels.so-000-gfx1100.hsaco /usr/bin/bash: warning: setlocale: LC_ALL: cannot change locale (en_US.UTF-8): No such file or directory
# ldd: warning: you do not have execution permission for `/usr/lib64/hipsparselt/library/Kernels.so-000-gfx1100.hsaco'
# not a dynamic executable
# Do something about the prems
find %{buildroot}%{pkg_prefix}/%{pkg_libdir}/hipsparselt/library/ \
     -name 'Kernels*.hsaco' -exec chmod a+x {} +

%if %{without compat}
# hipsparselt.x86_64: E: binary-or-shlib-defines-rpath /usr/lib64/libhipsparselt.so.0.2 (RUNPATH: $ORIGIN/../lib:$ORIGIN/../llvm/lib:$ORIGIN/../lib:$ORIGIN/../lib/hipsparselt/lib)
chrpath -d %{buildroot}%{pkg_prefix}/%{pkg_libdir}/libhipsparselt.so.*
%else
# ERROR   0008: file '/usr/lib64/rocm/rocm-7.2/lib/libhipsparselt.so.0.2' contains the $ORIGIN runpath specifier at the wrong position in [/usr/lib64/rocm/rocm-7.2/lib:$ORIGIN/../lib:$ORIGIN/../lib/hipsparselt/lib]
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/%{pkg_libdir}/libhipsparselt.so.*
%endif

%if %{with test}
%if %{without preview}
# hipsparselt-test's rpath is pretty messed up
# chrpath -l /usr/bin/hipsparselt-test
# /usr/bin/hipsparselt-test: RUNPATH=$ORIGIN/../lib:$ORIGIN/../lib/hipsparselt-clients/lib:/usr/llvm/lib
# So adjust it here
chrpath -r %{rocmllvm_libdir} %{buildroot}%{pkg_prefix}/bin/hipsparselt-test
%endif
%endif

%files -n %{hipsparselt_name}
%if %{with preview}
%doc projects/hipsparselt/README.md
%license projects/hipsparselt/LICENSE.md
%else
%doc README.md
%license LICENSE.md
%endif
%{pkg_prefix}/%{pkg_libdir}/libhipsparselt.so.0{,.*}
%{pkg_prefix}/%{pkg_libdir}/hipsparselt/

%files devel
%{pkg_prefix}/include/hipsparselt/
%{pkg_prefix}/%{pkg_libdir}/cmake/hipsparselt/
%{pkg_prefix}/%{pkg_libdir}/libhipsparselt.so

%if %{with test}
%files test
%if %{without preview}
# TODO: no tests for preview ?
%{pkg_prefix}/bin/hipsparselt*
%endif
%endif

%changelog
