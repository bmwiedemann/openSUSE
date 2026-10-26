#
# spec file for package tvm
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


%define libbacktrace_version 08f7c7e
%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
# regular cmake builddir conflicts with the python singlespec
%global __builddir build_cmake
# TVM's DNNL integration targets the oneDNN 2.x API and fails against
# Factory's oneDNN 3.x (upstream untouched since 2022, no v3 port)
%bcond_with onednn
# Disable pytest until python3-xgboost is available
%bcond_with pytest
%bcond_without cpptest
Name:           tvm
Version:        0.27.0
Release:        0
Summary:        An end-to-end Deep Learning Compiler Stack
License:        Apache-2.0
URL:            https://tvm.apache.org/
Source:         https://github.com/apache/tvm/archive/refs/tags/v%{version}.tar.gz#/tvm-%{version}.tar.gz
Source1:        https://github.com/apache/tvm-ffi/archive/refs/tags/v0.1.14-post1.tar.gz#/tvm-ffi.tar.gz
# License2: BSD-3-Clause
Source2:        https://github.com/tlc-pack/libbacktrace/archive/%{libbacktrace_version}.tar.gz#/libbacktrace.tar.gz
# PATCH-FIX-OPENSUSE tvm-llvm-isystem-usr-include.patch -- Factory LLVM ships headers directly in /usr/include; as -isystem it breaks GCC #include_next
Patch0:         tvm-llvm-isystem-usr-include.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module cloudpickle}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scikit-build-core}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module synr}
BuildRequires:  %{python_module tornado}
BuildRequires:  cmake
BuildRequires:  dlpack-devel >= 1.1
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  llvm-devel >= 15
BuildRequires:  memory-constraints
BuildRequires:  openblas-devel
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig
BuildRequires:  spirv-headers
BuildRequires:  spirv-tools
BuildRequires:  spirv-tools-devel
BuildRequires:  vulkan-devel
BuildRequires:  pkgconfig(OpenCL)
Requires:       python-apache-tvm-ffi >= 0.1.14.post0
Requires:       python-attrs
Requires:       python-cloudpickle
Requires:       python-decorator
Requires:       python-numpy
Requires:       python-psutil
Requires:       python-synr
# Tests are failing on 32-bit
ExcludeArch:    %{arm} %{ix86}
%if %{with pytest}
BuildRequires:  %{python_module typing_extensions}
%endif
%if %{with cpptest}
BuildRequires:  gmock
BuildRequires:  gtest
%endif
%if %{with onednn}
BuildRequires:  onednn-devel
%endif
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
tar xf %{SOURCE1} && rmdir tvm-ffi && mv tvm-ffi-* tvm-ffi
pushd tvm-ffi
rm -rf 3rdparty && ln -s ../../3rdparty
popd
tar xf %{SOURCE2} && mv libbacktrace-* libbacktrace
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
  -DUSE_LLVM=ON \
  -DUSE_BLAS="openblas" \
%if %{with onednn}
  -DUSE_DNNL=ON \
%else
  -DUSE_DNNL=OFF \
%endif
  -DUSE_OPENCL=ON \
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
# version comes from the git tag via setuptools_scm; the tarball has no .git
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
# Fix rpm runtime dependency rpmlint error replace the shebang in all the scripts with %%{_bindir}/python3
find . -name "*.py" -exec sed -i 's|#!%{_bindir}/env python|#!%{_bindir}/python3|' {} ";"
%pyproject_wheel

%install
%cmake_install
# remove endian hack
rm -f %{buildroot}%{_includedir}/endian.h
export TVM_LIBRARY_PATH="$(pwd)/%{__builddir}"
%pyproject_install
# Package libtvm_ffi.so
cp build_cmake/lib/libtvm_ffi.so %{buildroot}%{_libdir}
# Remove src,include,3rdparty dirs
%python_expand rm -rf %{buildroot}/%{$python_sitearch}/tvm/{src,include,3rdparty}/
# Regenerate tvmc which is not provided anymore
# https://tvm.apache.org/docs/v0.8.0/tutorial/tvmc_command_line_driver.html#using-tvmc
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/tvmc <<-EOF
#!/usr/bin/sh
python3 -m tvm.driver.tvmc $@
EOF
chmod +x %{buildroot}%{_bindir}/tvmc
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
%{python_sitearch}/apache_tvm-*.dist-info/

%changelog
