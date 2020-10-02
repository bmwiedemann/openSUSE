#
# spec file for package tvm
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%ifarch x86_64
%bcond_without mkldnn
%else
%bcond_with mkldnn
%endif
# regular cmake builddir conflicts with the python singlespec
%global __builddir build_cmake
Name:           tvm
Version:        0.6.1
Release:        0
Summary:        An End to End Deep Learning Compiler Stack
License:        Apache-2.0
URL:            https://tvm.apache.org/
Source:         https://github.com/apache/incubator-tvm/archive/v%{version}.tar.gz
Patch0:         lib-finder-python-cmake.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado}
BuildRequires:  cmake
BuildRequires:  dlpack-devel
BuildRequires:  dmlc-core-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gtest
#BuildRequires:  openblas-devel
BuildRequires:  memory-constraints
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
# Tests are failing on 32-bit
ExcludeArch:    %{arm} %{ix86}
%if 0%{?suse_version} > 1500
BuildRequires:  xgboost
%endif
%if 0%{?suse_version} > 1500
Requires:       xgboost
%endif
# Build fails on TW with LLVM10 - boo#1176220
%if 0%{?suse_version} > 1500
BuildRequires:  llvm9-devel
%else
BuildRequires:  llvm-devel
%endif
%if %{with mkldnn}
BuildRequires:  mkl-dnn-devel
%endif
%python_subpackages

%package nnvm
Summary:        NNVM Compiler: Open Compiler for AI Frameworks
Requires:       python-numpy
BuildArch:      noarch

%description nnvm
The NNVM compiler can directly take models from deep learning frameworks such as Apache MXNet.
It also support model exchange formats such as ONNX and CoreML.
ONNX support enables NNVM to compile deep learning models from PyTorch, Caffe2 and CNTK.

%package topi
Summary:        TVM Operator Inventory (TOPI)
Requires:       python-decorator
Requires:       python-numpy
BuildArch:      noarch

%description topi
TOPI provides numpy-style generic operations and schedules with higher abstractions than TVM.

%description
TVM is an open deep learning compiler stack for CPUs, GPUs, and specialized accelerators.
It aims to close the gap between the productivity-focused deep learning frameworks, and the performance- or efficiency-oriented hardware backends.

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
%setup -q -n incubator-%{name}-%{version}
%autopatch -p1

# Workaround - https://discuss.tvm.ai/t/build-fails-on-tvm-0-6-0-0-6-1-with-gcc10-and-gcc7/7462/5?u=ggardet
ln -s %{_includedir}/endian.h include/endian.h

%build
%limit_build -m 800
# USE_ANTLR - fails to find the antlr4 we provide
# USE_CUDA - we would need cuda
# USE_METAL
# USE_MICRO USE_MICRO_STANDALONE_RUNTIME
# USE_GRAPH_RUNTIME
# USE_NNPACK
# USE_ROCBLAS USE_ROCM
%cmake \
  -DDMLC_PATH="%{_includedir}/dmlc" \
  -DDLPACK_PATH="%{_includedir}/dlpack" \
  -DRANG_PATH="%{_includedir}/rang" \
  -DUSE_LLVM=ON \
  -DUSE_BLAS="none" \
%if %{with mkldnn}
  -DUSE_MKLDNN=ON \
%else
  -DUSE_MKLDNN=OFF \
%endif
%if 0%{?suse_version} > 1500
  -DUSE_OPENCL=ON \
%else
  -DUSE_OPENCL=OFF \
%endif
  -DUSE_OPENGL=ON \
  -DUSE_OPENMP=ON \
  -DUSE_RANDOM=ON \
  -DUSE_RPC=ON \
  -DUSE_RTTI=ON \
  -DUSE_SORT=ON \
  -DUSE_THREADS=ON \
  -DUSE_VULKAN=ON \
  -DINSTALL_DEV=ON
%cmake_build
cd ..
export TVM_LIBRARY_PATH="$(pwd)/%{__builddir}"
for folder in '' nnvm topi; do
  pushd ./$folder/python
  %python_build
  popd
done

%install
%cmake_install
# remove endian hack
rm -f %{buildroot}%{_includedir}/endian.h
export TVM_LIBRARY_PATH="$(pwd)/%{__builddir}"
for folder in '' nnvm topi; do
  pushd ./$folder/python
  %python_install
  popd
done
# Remove /usr/{tvm,nnvm,topi}/*.so
rm -rf %{buildroot}%{_prefix}/{tvm,nnvm,topi}
# Remove .cpp file
%python_expand rm %{buildroot}/%{$python_sitearch}/tvm/_ffi/_cython/core.cpp
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd %{__builddir}
%make_build cpptest
export LD_LIBRARY_PATH=$(pwd)
for test in *_test; do
    ./$test
done
popd
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

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig

%files -n libtvm
%license LICENSE
%doc README.md
%{_libdir}/libtvm.so
%{_libdir}/libnnvm_compiler.so
%{_libdir}/libtvm_topi.so
%{_libdir}/libtvm_runtime.so

%files -n %{name}-devel
%dir %{_includedir}/nnvm
%dir %{_includedir}/topi
%dir %{_includedir}/tvm
%{_includedir}/nnvm/*
%{_includedir}/topi/*
%{_includedir}/tvm/*

%files %{python_files}
%dir %{python_sitearch}/tvm
%{python_sitearch}/tvm/*
%dir %{python_sitearch}/tvm*egg-info/
%{python_sitearch}/tvm*egg-info/*

%files %{python_files nnvm}
%dir %{python_sitelib}/nnvm
%{python_sitelib}/nnvm/*
%dir %{python_sitelib}/nnvm*egg-info/
%{python_sitelib}/nnvm*egg-info/*

%files %{python_files topi}
%dir %{python_sitelib}/topi
%{python_sitelib}/topi/*
%dir %{python_sitelib}/topi*egg-info/
%{python_sitelib}/topi*egg-info/*

%changelog
