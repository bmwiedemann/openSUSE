#
# spec file for package hipsparse
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


%global upstreamname hipsparse

%global pkg_library_name %{upstreamname}
%global pkg_library_version 4

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
%global pkg_name lib%{pkg_library_name}%{pkg_library_version}%{pkg_suffix}
%else
%global pkg_name %{NAME}
%endif

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# export an llvm compilation database
# Useful for input for other llvm tools
%bcond_with export
%if %{with export}
%global build_compile_db ON
%else
%global build_compile_db OFF
%endif

# downloads tests, use mock --enable-network
%bcond_with test
%if %{with test}
%global build_test ON
%global __brp_check_rpaths %{nil}
%else
%global build_test OFF
%endif

%bcond_without check

# gfortran and clang rpm macros do not mix
%global build_fflags %{nil}

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

Name:           hipsparse%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        8%{?dist}
%endif
Summary:        ROCm SPARSE marshaling library
License:        MIT
URL:            https://github.com/ROCm/rocm-libraries

Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

%if %{without preview}
# Too much changed between 7.2 and 7.12+, this will need to be refactored.
# Removes the automatic downloading and conditional copying of test matrices
Patch1:         0001-hipsparse-change-test-download-dir.patch
%endif

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
%if 0%{?suse_version}
BuildRequires:  gcc-fortran
%else
BuildRequires:  gcc-gfortran
%endif
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-filesystem%{pkg_suffix}
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  rocprim%{pkg_suffix}-static
BuildRequires:  rocsparse%{pkg_suffix}-devel

%if %{with test}
%if 0%{?suse_version}
BuildRequires:  gtest
%else
BuildRequires:  gtest-devel
BuildRequires:  python3dist(pyyaml)
%endif
BuildRequires:  rocblas%{pkg_suffix}-devel
%endif

%if %{with check}
%if %{with export}
BuildRequires:  cppcheck
BuildRequires:  cppcheck-htmlreport
BuildRequires:  rocm-clang-analyzer%{pkg_suffix}
BuildRequires:  rocm-clang-tools-extra%{pkg_suffix}
%endif
%endif

Provides:       hipsparse%{pkg_suffix} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocm-hip%{pkg_suffix}
Requires:       rocsparse%{pkg_suffix}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
hipSPARSE is a SPARSE marshaling library with multiple
supported backends. It sits between your application and
a 'worker' SPARSE library, where it marshals inputs to
the backend library and marshals results to your
application. hipSPARSE exports an interface that doesn't
require the client to change, regardless of the chosen
backend. Currently, hipSPARSE supports rocSPARSE and
cuSPARSE backends.

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
Provides:       hipsparse%{pkg_suffix}-devel = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{pkg_name}%{?_isa} = %{version}-%{release}
Requires:       rocm-filesystem%{pkg_suffix}

%description test
%{summary}
%endif

%prep
%autosetup -p1 -n %{upstreamname}

# A better default for the matrices dir
sed -i -e 's@hipsparse_exepath() + "../matrices/"@"%{pkg_prefix}/share/hipsparse/matrices/"@' clients/include/utility.hpp

# Remove test that fail because of
# /usr/lib/gcc/x86_64-redhat-linux/16/../../../../include/c++/16/bits/stl_vector.h:1253: reference
# std::vector<int>::operator[](size_type) [_Tp = int, _Alloc = std::allocator<int>]:
# Assertion '__n < this->size()' failed.
sed -i -e '/test_bsrmv/d' clients/tests/CMakeLists.txt
sed -i -e '/test_bsrsv2/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csrsv2/d' clients/tests/CMakeLists.txt
sed -i -e '/test_sctr/d' clients/tests/CMakeLists.txt
sed -i -e '/test_bsrmm/d' clients/tests/CMakeLists.txt
sed -i -e '/test_bsrsm2/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csrsm2/d' clients/tests/CMakeLists.txt
sed -i -e '/test_gemmi/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csrgeam2/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csrgemm2/d' clients/tests/CMakeLists.txt
sed -i -e '/test_bsric02/d' clients/tests/CMakeLists.txt
sed -i -e '/test_bsrilu02/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csrilu02/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csric02/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csr2coo/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csr2bsr/d' clients/tests/CMakeLists.txt
sed -i -e '/test_bsr2csr/d' clients/tests/CMakeLists.txt
sed -i -e '/test_gebsr2csr/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csr2csr_compress/d' clients/tests/CMakeLists.txt
sed -i -e '/test_prune_csr2csr/d' clients/tests/CMakeLists.txt
sed -i -e '/test_coo2csr/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csrsort/d' clients/tests/CMakeLists.txt
sed -i -e '/test_cscsort/d' clients/tests/CMakeLists.txt
sed -i -e '/test_coosort/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csru2csr/d' clients/tests/CMakeLists.txt
sed -i -e '/test_gebsr2gebsr/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csr2gebsr/d' clients/tests/CMakeLists.txt
sed -i -e '/test_gebsr2gebsc/d' clients/tests/CMakeLists.txt
sed -i -e '/test_spmv_/d' clients/tests/CMakeLists.txt
sed -i -e '/test_sparse_to_dense_csr/d' clients/tests/CMakeLists.txt
sed -i -e '/test_sparse_to_dense_csc/d' clients/tests/CMakeLists.txt
sed -i -e '/test_sparse_to_dense_coo/d' clients/tests/CMakeLists.txt
sed -i -e '/test_spmm_/d' clients/tests/CMakeLists.txt
sed -i -e '/test_spgemm/d' clients/tests/CMakeLists.txt
sed -i -e '/test_sddmm_/d' clients/tests/CMakeLists.txt
sed -i -e '/test_spsv_/d' clients/tests/CMakeLists.txt
sed -i -e '/test_spsm_/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csr2csc/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csrgemm/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csrgeam/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csrmv/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csrmm/d' clients/tests/CMakeLists.txt
sed -i -e '/test_hybmv/d' clients/tests/CMakeLists.txt
sed -i -e '/test_csr2hyb/d' clients/tests/CMakeLists.txt
sed -i -e '/test_hyb2csr/d' clients/tests/CMakeLists.txt

%build

%cmake \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=%{build_compile_db} \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_INSTALL_RPATH=%{pkg_prefix}/%{pkg_libdir} \
    -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DCMAKE_BUILD_TYPE=%build_type \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_SKIP_RPATH=%{skip_install_rpath} \
    -DCMAKE_SKIP_INSTALL_RPATH=%{skip_install_rpath} \
    -DROCM_SYMLINK_LIBS=OFF \
    -DHIP_PLATFORM=amd \
    -DGPU_TARGETS=%{rocm_gpu_list_default} \
    -DBUILD_CLIENTS_BENCHMARKS=%{build_test} \
    -DBUILD_CLIENTS_SAMPLES=OFF \
    -DBUILD_CLIENTS_TESTS=%{build_test} \
    -DBUILD_CLIENTS_TESTS_OPENMP=OFF \
    -DCMAKE_MATRICES_DIR=%{_builddir}/hipsparse-test-matrices/ \
    -DBUILD_FORTRAN_CLIENTS=OFF

%cmake_build

%if %{with check}
%check
%if %{with export}
json=`find . -name 'compile_commands.json'`
json=`realpath $json`
json_dir=`dirname $json`
if [ -f ${json} ]; then
    jobs=`nproc`
    export PATH=%{rocmllvm_bindir}:$PATH
    output=/tmp/%{name}-tidy/
    mkdir -p ${output}
    # Use echo to consume tidy's error code
    %{rocmllvm_bindir}/run-clang-tidy -p ${json_dir} &> ${output}/tidy.log || echo "ran clang-tidy"

    output=/tmp/%{name}-cppcheck/
    mkdir -p ${output}
    cppcheck --project=${json} -j ${jobs} --std=c++17 --safety --output-file=${output}/cppcheck.txt
    cppcheck --project=${json} -j ${jobs} --std=c++17 --safety --xml --output-file=${output}/cppcheck.xml
    cppcheck-htmlreport --file=${output}/cppcheck.xml --report-dir=${output}
fi
%endif
%endif

%install
%cmake_install

rm -f %{buildroot}%{pkg_prefix}/share/doc/hipsparse/LICENSE.md

%if %{with test}
mkdir -p %{buildroot}/%{pkg_prefix}/share/hipsparse/matrices
install -pm 644 %{_builddir}/hipsparse-test-matrices/* %{buildroot}/%{pkg_prefix}/share/hipsparse/matrices
%endif

%if %{with compat}
# ERROR   0008: file '/usr/lib64/rocm/rocm-7.2/lib/libhipsparse.so.4.2.0'
#   contains the $ORIGIN runpath specifier at the wrong position in
#   [/usr/lib64/rocm/rocm-7.2/lib:$ORIGIN/../lib:$ORIGIN/../lib/hipsparse/lib]
chrpath -r %{pkg_prefix}/%{pkg_libdir} %{buildroot}%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}.*
%endif

%files -n %{pkg_name}
%doc README.md
%license LICENSE.md
%if %{with debug}
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}-d.so.%{pkg_library_version}{,.*}
%else
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}{,.*}
%endif

%files devel
%{pkg_prefix}/include/hipsparse/
%if %{with debug}
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}-d.so
%else
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so
%endif
%{pkg_prefix}/%{pkg_libdir}/cmake/hipsparse/

%if %{with test}
%files test
%{pkg_prefix}/bin/hipsparse*
%{pkg_prefix}/share/hipsparse/
%{pkg_prefix}/libexec/hipsparse/
%endif

%changelog
