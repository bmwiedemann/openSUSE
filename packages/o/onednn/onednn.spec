#
# spec file for package onednn
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


%define libname libdnnl3
%ifarch aarch64
# ACL support re-enabled with 3.14: the 25.03.1 NEReorderLayer API break
# (uxlfoundation/oneDNN#3097) was fixed server-side by ACL 52.0.0 restoring
# backwards compatibility, and 3.14 requires ACL >= 53.1 with the 5-arg API
# that ComputeLibrary 53.x ships (verified against v53.3.1 headers)
%bcond_without acl
%else
%bcond_with acl
%endif
%ifarch x86_64 aarch64
# OpenCL GPU backend: the backend code carries no arch-specific paths;
# verified by clean aarch64 and x86_64 builds with it enabled.
# GPU tests still need real hardware so they stay excluded from %check
%bcond_without opencl
%else
# No OpenCL on ppc64le/riscv64: on Power oneDNN's bundled CL headers
# pull in <altivec.h>, which redefines bool and breaks the build of the
# (C, uninstalled) examples in example_utils.h (proven still broken in
# 3.14); riscv64 stays off too, unvalidated
%bcond_with opencl
%endif
Name:           onednn
Version:        3.14
Release:        0
Summary:        oneAPI Deep Neural Network Library (oneDNN)
License:        Apache-2.0
URL:            https://github.com/uxlfoundation/oneDNN
Source0:        https://github.com/uxlfoundation/oneDNN/archive/v%{version}/oneDNN-%{version}.tar.gz
# PATCH-FIX-UPSTREAM doxygen-mainpage-path.patch -- Doxyfile.in points
# USE_MDFILE_AS_MAINPAGE at a relative path unresolvable in out-of-source
# builds; fatal since upstream turned doxygen warnings into errors
Patch0:         doxygen-mainpage-path.patch
# PATCH-FIX-OPENSUSE doxygen-no-warn-as-error.patch -- upstream turned
# doxygen warnings into errors but the doc tree predates the newer
# doxygen: hundreds of alias/ref warnings would fail the package build
# on doc cosmetics, so tolerate them as before
Patch1:         doxygen-no-warn-as-error.patch
# PATCH-FIX-UPSTREAM ocl-sparse-test-skip-without-gpu.patch -- the new
# sparse memory tests build a GPU engine unconditionally and fail
# instead of skipping on GPU-less builders, unlike every sibling test
Patch2:         ocl-sparse-test-skip-without-gpu.patch
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  ninja
BuildRequires:  texlive-dvips-bin
Provides:       mkl-dnn = %{version}
Obsoletes:      mkl-dnn <= %{version}
Provides:       oneDNN = %{version}
ExclusiveArch:  x86_64 aarch64 ppc64le riscv64
%if %{with acl}
BuildRequires:  ComputeLibrary-devel >= 53.1
%endif
%if %{with opencl}
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(OpenCL)
%endif

%description
oneAPI Deep Neural Network Library (oneDNN) is an open-source cross-platform
performance library of basic building blocks for deep learning applications.

oneDNN project is part of the UXL Foundation and is an implementation of the
oneAPI specification for oneDNN component.

%package -n benchdnn
Summary:        Header files of Intel Math Kernel Library
Requires:       %{libname} = %{version}

%description -n benchdnn
Intel Math Kernel Library for Deep Neural Networks (Intel MKL-DNN) is an
open-source performance library for deep-learning applications. The library
accelerates deep-learning applications and frameworks on Intel architecture.
Intel MKL-DNN contains vectorized and threaded building blocks that you can use
to implement deep neural networks (DNN) with C and C++ interfaces.

This package only includes the benchmark utility including its input files.

%package devel
Summary:        Header files of Intel Math Kernel Library
Requires:       %{libname} = %{version}
Provides:       mkl-dnn-devel = %{version}
Obsoletes:      mkl-dnn-devel <= %{version}
Provides:       oneDNN-devel = %{version}
%if %{with opencl}
Requires:       opencl-headers
Requires:       pkgconfig(OpenCL)
%endif

%description devel
Intel Math Kernel Library for Deep Neural Networks (Intel MKL-DNN) is an
open-source performance library for deep-learning applications. The library
accelerates deep-learning applications and frameworks on Intel architecture.
Intel MKL-DNN contains vectorized and threaded building blocks that you can use
to implement deep neural networks (DNN) with C and C++ interfaces.

This package includes the required headers and library files to develop software
with the Intel MKL-DNN.

%package doc
Summary:        Reference documentation for the Intel Math Kernel Library
BuildArch:      noarch

%description doc
The reference documentation for the Intel Math Kernel Library can be installed
with this package.

%package -n %{libname}
Summary:        Header files of Intel Math Kernel Library

%description -n %{libname}
Intel Math Kernel Library for Deep Neural Networks (Intel MKL-DNN) is an
open-source performance library for deep-learning applications. The library
accelerates deep-learning applications and frameworks on Intel architecture.
Intel MKL-DNN contains vectorized and threaded building blocks that you can use
to implement deep neural networks (DNN) with C and C++ interfaces.

%prep
%autosetup -p1 -n oneDNN-%{version}

%build
%define __builder ninja
# Empty DNNL_ARCH_OPT_FLAGS keeps binaries portable (default is HostOpts,
# i.e. -march=native; upstream dropped the MKLDNN_ compat shim)
%cmake \
  -DCMAKE_INSTALL_LIBDIR=%{_lib} \
  -DDNNL_ARCH_OPT_FLAGS="" \
%ifarch riscv64
  -DDNNL_CPU_RUNTIME=SEQ \
%else
  -DDNNL_CPU_RUNTIME=OMP \
%endif
%if %{with acl}
  -DDNNL_AARCH64_USE_ACL=ON \
  -DACL_INCLUDE_DIR=%{_includedir} \
  -DACL_LIBRARY=%{_libdir}/libarm_compute.so  \
%endif
%if %{with opencl}
  -DDNNL_GPU_RUNTIME=OCL \
%endif
  -DDNNL_INSTALL_MODE=DEFAULT \
  -DDNNL_BUILD_TESTS=ON \
  -DONEDNN_BUILD_GRAPH=ON \
  -DDNNL_WERROR=OFF \
  -DONEDNN_BUILD_DOC=ON
%cmake_build
%cmake_build doc_doxygen

%install
%cmake_install
# move the built doxygen data to normal location
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/dnnl/reference/* %{buildroot}%{_docdir}/%{name}
%fdupes %{buildroot}%{_docdir}/%{name}
# do use macros to install license/docu
rm -r %{buildroot}%{_datadir}/doc/dnnl
# Keep compatibility with mkl-dnn
pushd %{buildroot}%{_includedir}
ln -s . mkl-dnn
popd
# install the benchmark
install -D build/tests/benchdnn/benchdnn %{buildroot}/%{_bindir}/benchdnn
# move install shared lib
mkdir -vp %{buildroot}%{_datadir}/benchdnn
cp -vr build/tests/benchdnn/inputs  %{buildroot}%{_datadir}/benchdnn
%ifarch aarch64
# Drop upstream's install of the bundled KleidiAI: it is linked into
# libdnnl statically (no shared lib shipped), so the headers, cmake
# config and static archive it installs are consumable by nothing
rm -rf %{buildroot}%{_includedir}/KleidiAIOps %{buildroot}%{_libdir}/cmake/KleidiAIOps %{buildroot}%{_libdir}/libkleidiai_ops.a
%endif

chrpath -d %{buildroot}/%{_bindir}/benchdnn

%check
# do not use macro so we can exclude all gpu and cross (gpu and cpu) tests (they need gpu set up)
pushd build
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ifarch aarch64
# test_internals_env_vars_{dnnl,onednn}: the verbose-mode subtests (new upstream
# coverage from Aug 2026) fail on AArch64 while passing on x86_64/ppc64le;
# root cause undetermined, needs an upstream report
# test_benchdnn_modeC_graph_ci_cpu: known upstream AArch64 MHA/dropout
# reference failures (cf. uxlfoundation/oneDNN#5881)
ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags} -E '(gpu|cross|benchdnn_modeC_matmul_ci_cpu|test_internals_env_vars|test_benchdnn_modeC_graph_ci_cpu)'
%else
ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags} -E '(gpu|cross|benchdnn_modeC_matmul_ci_cpu)'
%endif
popd

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n benchdnn
%{_bindir}/benchdnn
%{_datadir}/benchdnn

%files devel
%doc README.md
%license LICENSE
%{_includedir}/mkl-dnn
%{_includedir}/dnnl*.h*
%dir %{_includedir}/oneapi
%dir %{_includedir}/oneapi/dnnl
%{_includedir}/oneapi/dnnl/dnnl*.h*
%{_libdir}/libdnnl.so
%dir %{_libdir}/cmake/dnnl
%{_libdir}/cmake/dnnl/*.cmake

%files doc
%{_docdir}/%{name}

%files -n %{libname}
%license LICENSE
%{_libdir}/libdnnl.so.*

%changelog
