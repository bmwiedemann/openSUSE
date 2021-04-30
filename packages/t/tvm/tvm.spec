#
# spec file for package tvm
#
# Copyright (c) 2021 SUSE LLC
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


%define _lto_cflags %{nil}

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
# https://numpy.org/neps/nep-0029-deprecation_policy.html
%define skip_python36 1
%ifarch aarch64 x86_64 ppc64le
%bcond_without onednn
%else
%bcond_with onednn
%endif
%ifarch aarch64
%bcond_without arm_compute_lib
%else
%bcond_with arm_compute_lib
%endif
# regular cmake builddir conflicts with the python singlespec
%global __builddir build_cmake
Name:           tvm
Version:        0.7.0
Release:        0
Summary:        An End to End Deep Learning Compiler Stack
License:        Apache-2.0
URL:            https://tvm.apache.org/
Source:         https://github.com/apache/tvm/archive/v%{version}.tar.gz
Patch0:         lib-finder-python-cmake.patch
# Fix cblas.h path
Patch1:         tvm-fix-openblas.patch
# PATCH-FIX-UPSTREAM - https://github.com/apache/tvm/issues/7319
Patch2:         tvm-fix-catch.patch
# PATCH-FIX-UPSTREAM - https://github.com/apache/tvm/pull/6717 https://github.com/apache/tvm/pull/6738
Patch3:         tvm-fix-llvm12.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado}
%if %{with arm_compute_lib}
BuildRequires:  ComputeLibrary-devel
%endif
BuildRequires:  antlr4-java
BuildRequires:  cmake
BuildRequires:  dlpack-devel
BuildRequires:  dmlc-core-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gtest
BuildRequires:  memory-constraints
BuildRequires:  openblas-devel
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig
BuildRequires:  rang-devel
BuildRequires:  spirv-headers
BuildRequires:  spirv-tools
BuildRequires:  spirv-tools-devel
BuildRequires:  vulkan-devel
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glfw3)
Requires:       python-attrs
Requires:       python-decorator
Requires:       python-numpy
Requires:       python-psutil
BuildRequires:  llvm-devel
%if %{with onednn}
BuildRequires:  onednn-devel
%endif
# Tests are failing on 32-bit
ExcludeArch:    %{arm} %{ix86}
%python_subpackages

%description
TVM is an open deep learning compiler stack for CPUs, GPUs, and specialized accelerators.
It aims to close the gap between the productivity-focused deep learning frameworks, and the performance- or efficiency-oriented hardware backends.

%package -n tvmc
Summary:        TVM command line driver
Requires:       libtvm = %{version}
Requires:       python3-scipy
Requires:       python3-typed-ast
Recommends:     python3-Pillow
Recommends:     python3-onnx

%description -n tvmc
TVMC is a tool that exposes TVM features such as auto-tuning, compiling,
profiling and execution of models, via a command line interface.

%package -n %{name}-devel
Summary:        An End to End Deep Learning Compiler Stack
Requires:       libtvm = %{version}

%description -n %{name}-devel
TVM is an open deep learning compiler stack for CPUs, GPUs, and specialized accelerators.
It aims to close the gap between the productivity-focused deep learning frameworks, and the performance- or efficiency-oriented hardware backends.

%package -n libtvm
Summary:        Libraries generated for TVM
# renamed up to libtvm here
Provides:       tvm
Obsoletes:      tvm

%description -n libtvm
Libraries generated for TVM without any provided soname.

%prep
%setup -q
%autopatch -p1

# Workaround - https://discuss.tvm.ai/t/build-fails-on-tvm-0-6-0-0-6-1-with-gcc10-and-gcc7/7462/5?u=ggardet
ln -s %{_includedir}/endian.h include/endian.h

%build
%limit_build -m 800
# USE_CUDA - we would need cuda
# USE_METAL
# USE_MICRO USE_MICRO_STANDALONE_RUNTIME
# USE_NNPACK
# USE_ROCBLAS USE_ROCM
%cmake \
%if %{with arm_compute_lib}
  -DUSE_ARM_COMPUTE_LIB_GRAPH_RUNTIME=ON \
  -DUSE_ARM_COMPUTE_LIB=ON \
%endif
  -DDMLC_PATH="%{_includedir}/dmlc" \
  -DDLPACK_PATH="%{_includedir}/dlpack" \
  -DRANG_PATH="%{_includedir}/rang" \
  -DUSE_GRAPH_RUNTIME=ON \
  -DUSE_LLVM=ON \
  -DUSE_BLAS="openblas" \
%if %{with onednn}
  -DUSE_MKLDNN=ON \
%else
  -DUSE_MKLDNN=OFF \
%endif
  -DUSE_OPENCL=ON \
  -DUSE_OPENGL=ON \
  -DUSE_OPENMP=ON \
  -DUSE_RANDOM=ON \
  -DUSE_RPC=ON \
  -DUSE_RTTI=ON \
  -DUSE_SORT=ON \
  -DUSE_THREADS=ON \
  -DUSE_VULKAN=ON \
  -DUSE_ANTLR="/usr/share/java/antlr4/antlr4-runtime.jar" \
  -DINSTALL_DEV=ON
%cmake_build
cd ..
export TVM_LIBRARY_PATH="$(pwd)/%{__builddir}"
pushd python
# Fix rpm runtime dependency rpmlint error replace the shebang in all the scripts with %%{_bindir}/python3
find . -name "*.py" -exec sed -i 's|#!%{_bindir}/env python|#!%{_bindir}/python3|' {} ";"
%python_build
popd

%install
%cmake_install
# remove endian hack
rm -f %{buildroot}%{_includedir}/endian.h
export TVM_LIBRARY_PATH="$(pwd)/%{__builddir}"
pushd python
%python_install
%python_expand chmod 0755 %{buildroot}%{$python_sitearch}/tvm/driver/tvmc/main.py
popd
# Remove /usr/tvm/*.so
rm -rf %{buildroot}%{_prefix}/tvm
# Remove .cpp file
%python_expand rm %{buildroot}/%{$python_sitearch}/tvm/_ffi/_cython/core.cpp
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd %{__builddir}
%make_build cpptest
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$(pwd)
for test in *_test; do
    ./$test
done
popd
# Tests requires pytest with ExitCode defined, only available on Tumbleweed so far
# Tests fail on TW as it tries to run Vulkan
%if 0
export TVM_INCLUDE_PATH=%{buildroot}%{_prefix}
# this test needs working vulkan
rm tests/python/unittest/test_runtime_ndarray.py
# test_device_module_dump or test_conv2d_scalar_bop or test_broadcast_bop or test_tensor_scalar_bop or test_vulkan or test_add_pipeline or test_cmp_load_store - also need vulkan
# test_task_tuner_without_measurement or test_fit or test_tuner or test_opencl_ternary_expression or test_opencl_inf_nan or test_gpu or test_simplex_data_transferring or test_duplex_data_transferring - Needs openCL
# test_fp16_to_fp32 fails on non-x86 as it uses skylake as llvm target
more_not_test=''
%ifarch ppc64le
more_not_test="or test_popcount or test_vmlal_s16 or test_llvm_add_pipeline"
%endif
%ifarch ppc64
more_not_test="or test_check_correctness or test_graph_simple or test_llvm_add_pipeline or test_popcount or test_rpc_array or test_rpc_file_exchange or test_rpc_remote_module or test_rpc_return_func or test_rpc_return_ndarray or test_rpc_simple or test_rpc_tracker_register or test_rpc_tracker_request or test_vmlal_s16"
%endif
%{python_expand # test with both $python sitearch and sitelib
export PYTHONPATH="%{buildroot}%{$python_sitearch}:%{buildroot}%{$python_sitelib}"
$python -m pytest -v tests/python/unittest -k "not (test_device_module_dump or test_conv2d_scalar_bop or test_broadcast_bop or test_tensor_scalar_bop or test_vulkan or test_add_pipeline or test_cmp_load_store or test_task_tuner_without_measurement or test_fit or test_tuner or test_opencl_ternary_expression or test_opencl_inf_nan or test_gpu or test_simplex_data_transferring or test_duplex_data_transferring or test_fp16_to_fp32 $more_not_test)"}
%endif

%post -n libtvm -p /sbin/ldconfig
%postun -n libtvm -p /sbin/ldconfig

%files -n tvmc
%{_bindir}/tvmc

%files -n libtvm
%license LICENSE
%doc README.md
%{_libdir}/libtvm*.so

%files -n %{name}-devel
%dir %{_includedir}/tvm
%{_includedir}/tvm/*

%files %{python_files}
%dir %{python_sitearch}/tvm
%{python_sitearch}/tvm/*
%dir %{python_sitearch}/tvm*egg-info/
%{python_sitearch}/tvm*egg-info/*

%changelog
