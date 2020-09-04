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
# Build python binding
%bcond_without python


%ifarch x86_64
%bcond_without mkldnn
%else
%bcond_with mkldnn
%endif

# Build fails on TW with LLVM
%if 0%{?suse_version} > 1500
%bcond_with llvm
%else
%bcond_without llvm
%endif

Name:           tvm
Version:        0.6.1
Release:        0
Summary:        An End to End Deep Learning Compiler Stack
License:        Apache-2.0
URL:            https://tvm.apache.org/
Source:         https://github.com/apache/incubator-tvm/archive/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  dlpack-devel
BuildRequires:  dmlc-core-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gtest
%if %{with llvm}
BuildRequires:  llvm-devel
%endif
%if %{with mkldnn}
BuildRequires:  mkl-dnn-devel
%endif
#BuildRequires:  openblas-devel
BuildRequires:  pkgconfig
BuildRequires:  spirv-headers
BuildRequires:  spirv-tools
BuildRequires:  spirv-tools-devel
BuildRequires:  vulkan-devel
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  rang-devel
%if %{with python}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module setuptools}
%if 0%{?suse_version} > 1500
BuildRequires:  xgboost
%endif
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module tornado}
%endif
%if %{with python}
%python_subpackages
%endif

%description
TVM is an open deep learning compiler stack for CPUs, GPUs, and specialized accelerators. 
It aims to close the gap between the productivity-focused deep learning frameworks, and the performance- or efficiency-oriented hardware backends.

%package -n %{name}-devel
Summary:        An End to End Deep Learning Compiler Stack
Requires:       %{name} = %{version}

%description -n %{name}-devel
TVM is an open deep learning compiler stack for CPUs, GPUs, and specialized accelerators. 
It aims to close the gap between the productivity-focused deep learning frameworks, and the performance- or efficiency-oriented hardware backends.

%prep
%setup -q -n incubator-%{name}-%{version}
# Workaround - https://discuss.tvm.ai/t/build-fails-on-tvm-0-6-0-0-6-1-with-gcc10-and-gcc7/7462/5?u=ggardet
ln -s /usr/include/endian.h include/endian.h

%build
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
%if %{with llvm}
  -DUSE_LLVM=ON \
%else
  -DUSE_LLVM=OFF \
%endif
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
  -DUSE_VULKAN=ON
%cmake_build
%if %{with python}
pushd ../python
%python_build
popd
%endif

%install
%cmake_install
%if %{with python}
pushd python 
%python_install
popd
# Remove /usr/tvm/*.so
rm -rf %{buildroot}/usr/tvm
# Remove .cpp file
rm %{buildroot}/%{python_sitearch}/tvm/_ffi/_cython/core.cpp
%fdupes %{buildroot}%{python_sitearch}
%endif

%if %{with llvm}
# UnitTests requires LLVM support
%check
LD_LIBRARY_PATH="$(pwd)/build/" \
  ./tests/scripts/task_cpp_unittest.sh
%if %{with python}
# Drop test which needs an openCL device
rm tests/python/unittest/test_runtime_ndarray.py
# Disable python tests for now as a number of them requires hardware for Vulkan
# ./tests/scripts/task_python_unittest.sh
%endif
%endif

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_libdir}/libtvm.so
%{_libdir}/libnnvm_compiler.so
%{_libdir}/libtvm_topi.so
%{_libdir}/libtvm_runtime.so

%files -n %{name}-devel
%dir %{_includedir}/tvm
%{_includedir}/tvm/*

%if %{with python}
%files %{python_files}
%dir %{python_sitearch}/tvm
%{python_sitearch}/tvm/*
%dir %{python_sitearch}/tvm*egg-info/
%{python_sitearch}/tvm*egg-info/*
%endif

%changelog
