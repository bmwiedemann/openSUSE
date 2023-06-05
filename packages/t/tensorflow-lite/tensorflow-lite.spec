#
# spec file for package tensorflow-lite
#
# Copyright (c) 2022 SUSE LLC
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


# https://en.opensuse.org/openSUSE:LTO#Static_libraries
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
%define pythons python3

Name:           tensorflow-lite
Version:        2.10.0
Release:        0
Summary:        A framework used for deep learning for mobile and embedded devices
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT AND MPL-2.0
Group:          Development/Languages/Python
URL:            https://www.tensorflow.org/
Source0:        https://github.com/tensorflow/tensorflow/archive/v%{version}.tar.gz#/tensorflow-%{version}.tar.gz
# IMPORTANT
# Although some of the following libraries are available in Factory, they can
# not be used as explicit versions are needed which differ from the Factory ones.
# License10: MIT
Source10:       https://github.com/google/farmhash/archive/0d859a811870d10f53a594927d0d0b97573ad06d.tar.gz#/farmhash.tar.gz
# License11: Apache-2.0
Source11:       https://github.com/google/gemmlowp/archive/fda83bdc38b118cc6b56753bd540caa49e570745.zip#/gemmlowp.zip
# License12: Apache-2.0
Source12:       https://github.com/abseil/abseil-cpp/archive/997aaf3a28308eba1b9156aa35ab7bca9688e9f6.tar.gz#/abseil-cpp.tar.gz
# License13: MPL-2.0
# NOTE: tensorflow only uses MPL-2.0 part of eigen
Source13:       https://gitlab.com/libeigen/eigen/-/archive/7792b1e909a98703181aecb8810b4b654004c25d/eigen-7792b1e909a98703181aecb8810b4b654004c25d.tar.gz#/eigen.tar.gz
# License14: BSD-2-Clause
Source14:       https://github.com/intel/ARM_NEON_2_x86_SSE/archive/1200fe90bb174a6224a525ee60148671a786a71f.tar.gz#/arm_neon_2_x86_sse.tar.gz
# Deps sources for Tensorflow-Lite (use same eigen, gemmlowp and abseil_cpp packages as non lite version)
# License15: Apache-2.0
Source15:       https://github.com/google/flatbuffers/archive/v2.0.6.tar.gz#/flatbuffers.tar.gz
# License16: BSD like
Source16:       https://storage.googleapis.com/mirror.tensorflow.org/github.com/petewarden/OouraFFT/archive/v1.0.tar.gz#/fft2d.tgz
# Source17: Apache-2.0
Source17:       https://github.com/google/ruy/archive/841ea4172ba904fe3536789497f9565f2ef64129.zip#/ruy.zip
# License18: BSD-3-Clause
Source18:       https://github.com/google/XNNPACK/archive/6b409ac0a3090ebe74d0cdfb494c4cd91485ad39.zip#/xnnpack.zip
# transitive tensorflow-lite dependencies for xnnpack
# License21: BSD 2-Clause
Source21:       https://github.com/pytorch/cpuinfo/archive/5e63739504f0f8e18e941bd63b2d6d42536c7d90.tar.gz#/cpuinfo.tar.gz
# NOTE: the github url is non-deterministic for the following zipfile archives (!?) Content is the same, but the hashes of the zipfiles differ.
# License30: MIT
# Source30:       https://github.com/Maratyszcza/FP16/archive/4dfe081cf6bcd15db339cf2680b9281b8451eeb3.zip #/FP16.zip
Source30:       FP16.zip
# License31: MIT
# Source31:      https://github.com/Maratyszcza/FXdiv/archive/b408327ac2a15ec3e43352421954f5b1967701d1.zip #/FXdiv.zip
Source31:       FXdiv.zip
# License32: BSD-2-Clause
# Source32:      https://github.com/Maratyszcza/pthreadpool/archive/545ebe9f225aec6dca49109516fac02e973a3de2.zip #/pthreadpool.zip
Source32:       pthreadpool.zip
# License83: MIT
# Source83:       https://github.com/Maratyszcza/psimd/archive/072586a71b55b7f8c584153d223e95687148a900.zip #/psimd.zip
Source33:       psimd.zip
# PATCH-FIX-OPENSUSE tensorflow-lite-cmake-find-python.patch -- Let CMake find the includedirs and linker flags, code@bnavigator.de
Patch0:         tensorflow-lite-cmake-find-python.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
BuildRequires:  gcc12-fortran
BuildRequires:  git
# We use some macros here but not singlespec
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel >= 3.7
BuildRequires:  python3-numpy-devel >= 1.19.2
BuildRequires:  python3-pybind11-devel
BuildRequires:  python3-setuptools
BuildRequires:  unzip
Provides:       python3-tflite-runtime = %{version}-%{release}
Provides:       python3-tflite_runtime = %{version}-%{release}
Provides:       tensorflow2-lite = %{version}-%{release}
Obsoletes:      tensorflow2-lite < %{version}-%{release}
Requires:       python3-numpy >= 1.19.2

# just use rpmlint
# there are some serious compiler warnings, regarding no-return-in-nonvoid-function
#!BuildRequires:  -post-build-checks
ExcludeArch:    %ix86

%description
TensorFlow is an end-to-end open source platform for machine learning.
The Tensorflow Lite package is a fraction the size of the full tensorflow package
and includes the bare minimum code required to run inferences with TensorFlow Lite
 — primarily the Interpreter Python class. This small package is for when all you
want to do is execute .tflite models and avoid wasting disk space with the large
TensorFlow library.

%package devel
Summary:        Header files of tensorflow
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Provides:       tensorflow2-lite-devel = %{version}-%{release}
Obsoletes:      tensorflow2-lite-devel < %{version}-%{release}

%description devel
TensorFlow is an end-to-end open source platform for machine learning.
The Tensorflow Lite package is a fraction the size of the full tensorflow package
and includes the bare minimum code required to run inferences with TensorFlow Lite
 — primarily the Interpreter Python class. This small package is for when all you
want to do is execute .tflite models and avoid wasting disk space with the large
TensorFlow library.

This package provides necessary headers for the C/C++ Api using TensorFlow Lite.
As well as the static libtensorflow-lite.a for use in your own projects without the
Python interpreter.

%prep
# unpack tensorflow
%autosetup -p1 -n tensorflow-%{version}

# remove shebang
sed -i '1{/env python/d}' tensorflow/lite/tools/visualize.py

# prepare third-party sources, transitive dependencies of FP16
unzip %{SOURCE30} -d third_party/FP16
unzip %{SOURCE31} -d third_party/FP16
unzip %{SOURCE32} -d third_party/FP16
unzip %{SOURCE33} -d third_party/FP16

mkdir tflite-build
pushd tflite-build
# Build a python package source tree. Adapted from tensorflow/lite/tools/pip_package/build_pip_package_with_cmake.sh
TENSORFLOW_LITE_DIR=%{_builddir}/tensorflow-%{version}/tensorflow/lite
cp -r "${TENSORFLOW_LITE_DIR}/tools/pip_package/MANIFEST.in" \
      "${TENSORFLOW_LITE_DIR}/python/interpreter_wrapper" \
      ./
cp "${TENSORFLOW_LITE_DIR}/tools/pip_package/setup_with_binary.py" setup.py
mkdir tflite_runtime
cp "${TENSORFLOW_LITE_DIR}/python/interpreter.py" \
   "${TENSORFLOW_LITE_DIR}/python/metrics/metrics_interface.py" \
   "${TENSORFLOW_LITE_DIR}/python/metrics/metrics_portable.py" \
   tflite_runtime
echo "__version__ = '%{version}'" >> "tflite_runtime/__init__.py"
echo "__git_version__ = '%{version}-susebuild'" >> "tflite_runtime/__init__.py"
popd

%build
# --- Build tensorflow-lite as part of the minimal executable ---
# -Werror=return-type fails in xnnpack
%global optflags %(echo %{optflags} | sed s/-Werror=return-type//)

pushd tflite-build
%cmake ../../tensorflow/lite/examples/minimal \
  -DBUILD_STATIC_LIBS:BOOL=ON \
  -DBUILD_SHARED_LIBS:BOOL=OFF \
  -DOVERRIDABLE_FETCH_CONTENT_farmhash_URL=%{SOURCE10} \
  -DOVERRIDABLE_FETCH_CONTENT_gemmlowp_URL=%{SOURCE11} \
  -DOVERRIDABLE_FETCH_CONTENT_abseil-cpp_URL=%{SOURCE12} \
  -DOVERRIDABLE_FETCH_CONTENT_eigen_URL=%{SOURCE13} \
  -DINCLUDE_INSTALL_DIR:PATH=include/eigen3 \
  -DOVERRIDABLE_FETCH_CONTENT_neon2sse_URL=%{SOURCE14} \
  -DOVERRIDABLE_FETCH_CONTENT_flatbuffers_URL=%{SOURCE15} \
  -DOVERRIDABLE_FETCH_CONTENT_fft2d_URL=%{SOURCE16} \
  -DOVERRIDABLE_FETCH_CONTENT_ruy_URL=%{SOURCE17} \
  -DOVERRIDABLE_FETCH_CONTENT_xnnpack_URL=%{SOURCE18} \
  -DOVERRIDABLE_FETCH_CONTENT_clog_URL=%{SOURCE21} \
  -DOVERRIDABLE_FETCH_CONTENT_cpuinfo_URL=%{SOURCE21} \
  -DFP16_SOURCE_DIR:PATH=$(realpath ../../third_party/FP16/FP16-*) \
  -DFXDIV_SOURCE_DIR:PATH=$(realpath ../../third_party/FP16/FXdiv-*) \
  -DPTHREADPOOL_SOURCE_DIR:PATH=$(realpath ../../third_party/FP16/pthreadpool-*) \
  -DPSIMD_SOURCE_DIR:PATH=$(realpath ../../third_party/FP16/psimd-*) \
%ifarch %arm aarch64
  -DTFLITE_ENABLE_XNNPACK:BOOL=OFF \
%endif
  -DCMAKE_C_COMPILER=gcc-12 \
  -DCMAKE_CXX_COMPILER=g++-12 \
%{nil}
%cmake_build all _pywrap_tensorflow_interpreter_wrapper

# get the wrapper compiled above
cd ..
cp build/tensorflow-lite/_pywrap_tensorflow_interpreter_wrapper.so tflite_runtime/
export PROJECT_NAME=tflite_runtime
export PACKAGE_VERSION=%{version}
# avoid python builddir-shuffle
echo "python3" > _current_flavor
%python3_build
popd

%install
pushd tflite-build/build
install -D minimal %{buildroot}%{_bindir}/tflite_minimal
install -D tensorflow-lite/libtensorflow-lite.a %{buildroot}%{_libdir}/libtensorflow-lite.a
# Disable spurious-executable-perm
chmod -x %{buildroot}%{_libdir}/libtensorflow-lite.a
popd
for file in `find tensorflow/lite -name \*.h`; do
  # Package header files - boo#1175099
  install -D $file %{buildroot}%{_includedir}/$file
  # Disable spurious-executable-perm
  chmod -x %{buildroot}%{_includedir}/$file
done
install -D tensorflow/lite/schema/schema.fbs %{buildroot}%{_includedir}/tensorflow/lite/schema/schema.fbs
chmod -x %{buildroot}%{_includedir}/tensorflow/lite/schema/schema.fbs
install -D tensorflow/core/public/version.h %{buildroot}%{_includedir}/tensorflow/core/public/version.h
chmod -x %{buildroot}%{_includedir}/tensorflow/core/public/version.h
# Install tensorflow-lite.pc
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat <<EOF > %{buildroot}%{_libdir}/pkgconfig/tensorflow-lite.pc
Name:           tensorflow lite
Description: tensorflow lite static library
Version:        %{version}
Libs: -L%{_libdir} -ltensorflow-lite -lflatbuffers
Cflags: -I%{_includedir}
EOF
# Some tools expect tensorflow2-lite.pc
pushd %{buildroot}%{_libdir}/pkgconfig
ln -s tensorflow-lite.pc tensorflow2-lite.pc
popd
pushd tflite-build
# avoid auto-discovered python packaging of abseil files
rm build/lib/pkgconfig/absl_absl_*
rmdir build/lib/pkgconfig
export PROJECT_NAME=tflite_runtime
export PACKAGE_VERSION=%{version}
%python3_install --install-lib=%{python3_sitearch}
%fdupes %{buildroot}%{python3_sitearch}
popd

%check
PYTHONPATH=%{buildroot}%{python_sitearch} python3 -c "import tflite_runtime.interpreter as tflite"

%files
%{_bindir}/tflite_minimal
%{python3_sitearch}/tflite_runtime
%{python3_sitearch}/tflite_runtime-%{version}*-info

%files devel
%{_libdir}/libtensorflow-lite.a
%dir %{_includedir}/tensorflow/lite/
%{_includedir}/tensorflow/lite/*
%dir %{_includedir}/tensorflow/core/public/
%{_includedir}/tensorflow/core/public/version.h
%{_libdir}/pkgconfig/*.pc

%changelog
