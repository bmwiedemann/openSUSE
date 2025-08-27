#
# spec file for package tvm
#
# Copyright (c) 2025 SUSE LLC and contributors
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

# System dmlc is too old - https://github.com/apache/tvm/issues/17459#issuecomment-2429144716
%bcond_with system_dmlc
%define dmlc_version 3031e4a

%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%ifarch aarch64 x86_64 ppc64le
%bcond_without onednn
%else
%bcond_with onednn
%endif
# Disable pytest until python3-xgboost is available
%bcond_with pytest
%ifarch aarch64
%bcond_without arm_compute_lib
%else
%bcond_with arm_compute_lib
%endif
%bcond_without cpptest
# regular cmake builddir conflicts with the python singlespec
%global __builddir build_cmake
Name:           tvm
Version:        0.19.0
Release:        0
Summary:        An end-to-end Deep Learning Compiler Stack
License:        Apache-2.0
URL:            https://tvm.apache.org/
Source:         https://github.com/apache/tvm/archive/refs/tags/v%{version}.tar.gz#/tvm-%{version}.tar.gz
# License2: MIT
Source2:        https://github.com/dmlc/dmlc-core/archive/%{dmlc_version}.tar.gz#/dmlc-core.tar.gz
# PATCH-FIX-OPENSUSE lib-finder-python-cmake.patch -- custom cmake path
Patch1:         lib-finder-python-cmake.patch
# PATCH-FIX-OPENSUSE tvm-fix-openblas.patch -- We use openblas headers instead of netlib cblas
Patch2:         tvm-fix-openblas.patch
# PATCH-FIX-OPENSUSE tvm-disable-vulkan-test-check.patch -- Cannot test in OBS despite enabled in library
Patch3:         tvm-disable-vulkan-test-check.patch
# PATCH-FIX-UPSTREAM 18202.patch -- https://github.com/apache/tvm/pull/18202
Patch4:         18202.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module cloudpickle}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module synr}
BuildRequires:  %{python_module tornado}
%if %{with pytest}
BuildRequires:  %{python_module typing_extensions}
%endif
%if %{with arm_compute_lib}
BuildRequires:  ComputeLibrary-devel
%endif
BuildRequires:  antlr4-java
BuildRequires:  cmake
BuildRequires:  dlpack-devel >= 0.7
%if %{with system_dmlc}
BuildRequires:  dmlc-core-devel
%endif
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git
%if %{with cpptest}
BuildRequires:  gmock
BuildRequires:  gtest
%endif
BuildRequires:  llvm-devel
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
Requires:       python-cloudpickle
Requires:       python-decorator
Requires:       python-numpy
Requires:       python-psutil
Requires:       python-synr
%if %{with onednn}
BuildRequires:  onednn-devel
%endif
# Tests are failing on 32-bit
ExcludeArch:    %{arm} %{ix86}
%python_subpackages

%description
TVM is a deep learning compiler stack for CPUs, GPUs, and specialized accelerators.

%package -n tvmc
Summary:        TVM command line driver
Requires:       libtvm = %{version}
Requires:       python3-scipy
Requires:       python3-setuptools
Requires:       python3-tvm = %{version}
Recommends:     python3-Pillow
Recommends:     python3-onnx

%description -n tvmc
TVMC is a tool that exposes TVM features such as auto-tuning, compiling,
profiling and execution of models, via a command line interface.

%package -n %{name}-devel
Summary:        Headers for the TVM Deep Learning Compiler Stack
Requires:       libtvm = %{version}

%description -n %{name}-devel
TVM is a deep learning compiler stack for CPUs, GPUs, and specialized accelerators.

This package contains the headers.

%package -n libtvm
Summary:        Libraries generated for TVM
# renamed up to libtvm here
Provides:       tvm = %{version}-%{release}
Obsoletes:      tvm < %{version}-%{release}

%description -n libtvm
Libraries generated for TVM without any provided soname.

%prep
%setup -q
%autopatch -p1
pushd 3rdparty
%if %{without system_dmlc}
tar xf %{SOURCE2} && rmdir dmlc-core && mv dmlc-core-* dmlc-core
%endif
popd

# Workaround - https://discuss.tvm.ai/t/build-fails-on-tvm-0-6-0-0-6-1-with-gcc10-and-gcc7/7462/5?u=ggardet
ln -s %{_includedir}/endian.h include/endian.h
# Workaround for tests/cpp/relay/ir/indexed_graph_test.cc:20:10: fatal error: ../../../src/relay/ir/indexed_graph.h: No such file or directory
pushd tests/
ln -s ../src
popd
#  Workaround for tests/cpp/target_test.cc:29:10: fatal error: ../../../src/target/llvm/llvm_instance.h: No such file or directory
pushd ../
ln -s tvm-%{version}/src
popd

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
%if %{with system_dmlc}
  -DDMLC_PATH="%{_includedir}/dmlc" \
%else
  -DDMLC_PATH="$(pwd)/../3rdparty/dmlc-core/include" \
%endif
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
  -DUSE_LIBBACKTRACE=OFF \
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
%python_expand chmod 0755 %{buildroot}%{$python_sitearch}/tvm/driver/tvmc/main.py %{buildroot}%{$python_sitearch}/tvm/contrib/torch/pytorch_tvm.py
popd
# Remove /usr/tvm/*.so
rm -rf %{buildroot}%{_prefix}/tvm
# Remove src,include,3rdparty dirs
%python_expand rm -rf %{buildroot}/%{$python_sitearch}/tvm/{src,include,3rdparty}/
%if %{without system_dmlc}
rm -rf %{buildroot}%{_includedir}/dmlc
%endif
# Remove .cpp file
%python_expand rm %{buildroot}/%{$python_sitearch}/tvm/_ffi/_cython/core.cpp
# tvmc shebang should be default python, not highest available version
sed -i -r 's|#!/usr/bin/python3(.*)|#!/usr/bin/python3|' %{buildroot}%{_bindir}/tvmc
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%if %{with cpptest}
pushd %{__builddir}
%cmake_build cpptest
popd
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$(pwd)
# to avoid CI thread throttling.
export TVM_BIND_THREADS=0
export OMP_NUM_THREADS=1
%{python_expand #
export PYTHONPATH=%{buildroot}%{$python_sitearch}
export PYTHONDONTWRITEBYTECODE=1
# TextureCopy: no openCL in environment
# aarch64 OBS workers do not support SVE or FP16 yet
ctestflags="-E (TextureCopy|TvmVMMemoryManagerTest|AProfileParser.DefaultSVESupportSVESupport|AProfileParser.DefaultFP16Support)"
%ctest $ctestflags
}
%endif

%if %{with pytest}
mkdir python_gen
cp python/gen_requirements.py python_gen/
export PYTHONPATH=$(pwd)/python_gen
export TVM_INCLUDE_PATH=%{buildroot}%{_prefix}
export TVM_TEST_TARGETS="llvm"
export TVM_FFI="cython"
# No python module for XGBoost
donttest="test_xgb_model"
donttest="$donttest or test_sketch_search_policy_xgbmodel"
donttest="$donttest or test_sketch_search_policy_custom_sketch"
donttest="$donttest or test_task_tuner_without_measurement"
donttest="$donttest or test_autotvm_xgboost_mode"
donttest="$donttest or test_meta_schedule_xgb_model"
donttest="$donttest or test_meta_schedule_xgb_model_reload"
donttest="$donttest or test_meta_schedule_xgb_model_reupdate"
donttest="$donttest or test_tune_matmul"
# No OpenCL device
donttest="$donttest or test_simplex_data_transferring"
donttest="$donttest or test_duplex_data_transferring"
# no minrpc in installed path (test looks in src)
donttest="$donttest or test_rpc_echo"
donttest="$donttest or test_rpc_remote_module"
%ifnarch x86_64
# test_fp16_to_fp32 fails on non-x86 as it uses skylake as llvm target
donttest="$donttest or test_fp16_to_fp32"
%endif
%ifarch ppc64le
donttest="$donttest or test_popcount or test_vmlal_s16 or test_llvm_add_pipeline"
%endif
%ifarch ppc64
donttest="$donttest or test_check_correctness or test_graph_simple or test_llvm_add_pipeline or test_popcount or test_rpc_array or test_rpc_file_exchange or test_rpc_remote_module or test_rpc_return_func or test_rpc_return_ndarray or test_rpc_simple or test_rpc_tracker_register or test_rpc_tracker_request or test_vmlal_s16"
%endif
# probes vulkan on test collection
ignorefiles="--ignore tests/python/unittest/test_target_codegen_vulkan.py"
ignorefiles="$ignorefiles --ignore tests/python/unittest/test_tir_intrin.py"
ignorefiles="$ignorefiles --ignore tests/python/unittest/test_tvm_testing_features.py"
# No python module for XGBoost
ignorefiles="$ignorefiles --ignore tests/python/unittest/test_meta_schedule_cost_model.py"
%if 0%{?suse_version} <= 1500
# Skip some tests on Leap/SLE (some tests would need python 3.7+)
donttest="$donttest or test_meta_schedule_local_runner_time_out or test_meta_schedule_local_runner_exception"
%endif
%pytest_arch -v tests/python/unittest -m "not gpu" -k "not ($donttest)" $ignorefiles
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
%{_includedir}/tvm
%dir %{_libdir}/cmake/tvm/
%{_libdir}/cmake/tvm/*.cmake

%files %{python_files}
%{python_sitearch}/tvm
%dir %{python_sitearch}/tvm*.egg-info/
%{python_sitearch}/tvm*.egg-info/*

%changelog
