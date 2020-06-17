#
# spec file for package tensorflow
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


#
%define pname tensorflow
%define vers 1.15.3
%define _vers 1_15_3
%define libmaj 1
%define libmin 15
%define libref 3
%define python_ver_hack python3.[0-9]
%global flavor @BUILD_FLAVOR@%{nil}
# Build tensorflow, not Tensorflow-lite
%define is_lite 0
%if "%{flavor}" == "standard"
%bcond_with cuda
%bcond_with mpi
%bcond_with opencl
%endif
%if "%{flavor}" == "lite"
%define is_lite 1
%define package_suffix -lite
%bcond_with cuda
%bcond_with mpi
%bcond_with opencl
%endif
%if "%{flavor}" == "hpc"
%define compiler_family gnu
%bcond_with cuda
%bcond_with mpi
%bcond_with opencl
%bcond_without hpc
%endif
%if "%{flavor}" == "hpc-openmpi2"
%define mpi_flavor openmpi
%define mpi_vers 2
%define compiler_family gnu
%bcond_with cuda
%bcond_without mpi
%bcond_with opencl
%bcond_without hpc
%endif
%if "%{flavor}" == "hpc-mvapich2"
%define mpi_flavor mvapich2
%define compiler_family gnu
%bcond_with cuda
%bcond_without mpi
%bcond_with opencl
%bcond_without hpc
%endif
%if "%{flavor}" == "cuda-10-1"
%bcond_without cuda
%bcond_with mpi
%bcond_with opencl
%endif
%if "%{flavor}" == "opencl"
%bcond_without opencl
%bcond_with cuda
%bcond_with mpi
%endif
%if %{with hpc}
%{!?compiler_family:%global compiler_family gnu}
%{hpc_init -c %compiler_family %{?with_mpi:-m %mpi_flavor} %{?c_f_ver:-v %{c_f_ver}} %{?mpi_ver:-V %{mpi_ver}} %{?ext:-e %{ext}}}
%{?with_mpi:%global hpc_module_pname p%{pname}}
%define python_flavor python3
%define package_name   %{hpc_package_name %_vers}
%define package_name_provide tensorflow%{hpc_package_name_tail}
%define package_name_conflict tensorflow2%{hpc_package_name_tail}
%define libname(l:s:)   lib%{pname}%{-l*}%{hpc_package_name_tail %{?_vers}}
%define package_python_sitearch %hpc_python_sitearch
%define package_python_sitelib %{hpc_prefix}/lib/python%{python3_version}/site-packages/
%define package_prefix %hpc_prefix
%define package_bindir %hpc_bindir
%define package_libdir %hpc_libdir
%else
%define package_name   %pname%{?package_suffix}
%define package_name_conflict tensorflow2%{?package_suffix}
%define package_python_sitearch %{python3_sitearch}
%define package_python_sitelib %{python3_sitelib}
%define package_prefix %_prefix
%define package_bindir %_bindir
%define package_libdir %_libdir
%define libname(l:s:)   lib%{pname}%{!-l:%{-s:-}}%{-l*}%{-s*}%{?package_suffix}
%endif

Name:           %{package_name}
Version:        %vers
Release:        0
Summary:        A framework used for deep learning
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND FSFUL AND MIT AND MPL-2.0 AND OpenSSL AND Python-2.0
Group:          Development/Languages/Python
URL:            https://www.tensorflow.org/
Source0:        https://github.com/tensorflow/tensorflow/archive/v%{version}.tar.gz#/tensorflow-%{version}.tar.gz
Source1:        tensorflow-rpmlintrc
# IMPORTANT
# although some of the following libraries are available in factory they could
# not be used as
#   * explicit versions are needed which differ from the factory ones
#   * bazel and the obs version have different symbols due to hidden compiler flags
# License10: Apache-2.0
Source10:       https://github.com/bazelbuild/rules_closure/archive/308b05b2419edb5c8ee0471b67a40403df940149.tar.gz#/rules_closure.tar.gz
# License12:  Python-2.0
Source12:       https://pypi.python.org/packages/bc/cc/3cdb0a02e7e96f6c70bd971bc8a90b8463fda83e264fa9c5c1c98ceabd81/backports.weakref-1.0rc1.tar.gz#/backports.weakref-1.0rc1.tar.gz
# License13: BSD-3-Clause
Source14:       https://files.pythonhosted.org/packages/4e/35/11749bf99b2d4e3cceb4d55ca22590b0d7c2c62b9de38ac4a4a7f4687421/gast-0.2.2.tar.gz
# License15: MIT
Source15:       https://github.com/google/farmhash/archive/816a4ae622e964763ca0862d9dbd19324a1eaf45.tar.gz#/farmhash.tar.gz
# License17: Apache-2.0
Source17:       https://github.com/google/gemmlowp/archive/12fed0cd7cfcd9e169bf1925bc3a7a58725fdcc3.zip#/gemmlowp.zip
# License18: BSD-3-Clause
Source18:       https://github.com/hfp/libxsmm/archive/1.9.tar.gz#/libxsmm_1.9.tar.gz
# License19: Apache-2.0
Source19:       https://github.com/abseil/abseil-cpp/archive/43ef2148c0936ebf7cb4be6b19927a9d9d145b8f.tar.gz#/abseil-cpp.tar.gz
# License21: Apache-2.0
Source21:       https://github.com/googleapis/googleapis/archive/f81082ea1e2f85c43649bee26e0d9871d4b41cdb.zip#/googleapis.zip
# License23: BSD-3-Clause
Source23:       https://github.com/NVlabs/cub/archive/1.8.0.zip#/cub_1.8.0.zip
# License24: Apache-2.0
Source24:       https://github.com/google/highwayhash/archive/fd3d9af80465e4383162e4a7c5e2f406e82dd968.tar.gz#/highwayhash.tar.gz
# License26: MPL-2.0
# NOTE: tensorflow only uses MPL-2.0 part of eigen
Source26:       https://bitbucket.org/eigen/eigen/get/49177915a14a.tar.gz#/eigen.tar.gz
# License27: BSD-2-Clause
Source27:       https://github.com/intel/ARM_NEON_2_x86_SSE/archive/1200fe90bb174a6224a525ee60148671a786a71f.tar.gz#/arm_neon_2_x86_sse.tar.gz
# the command 'osc service localrun download_files' does not work on following URL
# https://docs.python.org/2.7/_sources/license.rst.txt
Source28:       license.rst.txt
# License30: FSFUL
Source30:       http://www.kurims.kyoto-u.ac.jp/~ooura/fft.tgz#/fft.tar.gz
# License34: BSD-3-Clause and Intel
Source34:       https://github.com/edenhill/librdkafka/archive/v0.11.5.tar.gz#/kafka-v0.11.5.tar.gz
# License35: Apache-2.0
Source35:       https://github.com/GoogleCloudPlatform/google-cloud-cpp/archive/v0.10.0.tar.gz#/google-cloud-cpp.tar.gz
# License36: Apache-2.0
Source36:       https://github.com/nlopezgi/bazel-toolchains/archive/92dd8a7a518a2fb7ba992d47c8b38299fe0be825.tar.gz#/bazel-toolchains.tar.gz
# License37: Apache-2.0
Source37:       https://github.com/bazelbuild/rules_docker/archive/a9bb1dab84cdf46e34d1b34b53a17bda129b5eba.tar.gz#/rules_docker.tar.gz
# License43: BSD and ICU License
Source44:       https://github.com/nanopb/nanopb/archive/f8ac463766281625ad710900479130c7fcb4d63b.tar.gz#/nanopb.tar.gz
# Deps sources for Tensorflow-Lite (use same eigen, gemmlowp and abseil_cpp packages as non lite version)
Source46:       https://pypi.python.org/packages/c5/60/6ac26ad05857c601308d8fb9e87fa36d0ebf889423f47c3502ef034365db/functools32-3.2.3-2.tar.gz
Source47:       https://github.com/pybind/pybind11/archive/v2.3.0.tar.gz#/pybind11-v2.3.0.tar.gz
Source48:       https://github.com/llvm-mirror/llvm/archive/7a7e03f906aada0cf4b749b51213fe5784eeff84.tar.gz#/llvm.tar.gz
Source49:       https://github.com/mborgerding/kissfft/archive/36dbc057604f00aacfc0288ddad57e3b21cfc1b8.tar.gz#/kissfft.tar.gz
Source50:       https://github.com/intel/mkl-dnn/archive/v0.20.6.tar.gz#/mkl-dnn.tar.gz
Source53:       https://storage.googleapis.com/mirror.tensorflow.org/www.kurims.kyoto-u.ac.jp/~ooura/fft2d.tgz
Source100:      https://github.com/google/googletest/archive/release-1.8.0.tar.gz
Source101:      https://github.com/intel/ARM_NEON_2_x86_SSE/archive/master.zip#/ARM_NEON_2_x86_SSE-master.zip

Patch0:         removed-docker-tools.patch
Patch1:         right-json-location.patch
Patch2:         fix-lite.patch
Patch3:         Fix-build-failures-for-python-3.8.patch
Patch4:         Fix-TensorFlow-on-Python-3.8-logger-issue.patch
Patch5:         fix-mpi-build.patch
Patch6:         fix-google-absl-memory.patch
# only for TW right now
Patch10:        json-feature-name.patch

BuildRequires:  bazel = 0.24.1
BuildRequires:  boringssl-devel
BuildRequires:  curl
BuildRequires:  curl-devel
BuildRequires:  double-conversion-devel >= 3.1.5
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  giflib-devel
BuildRequires:  git
BuildRequires:  grpc-devel
BuildRequires:  hwloc-devel
BuildRequires:  jemalloc-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libjpeg-turbo
BuildRequires:  libjpeg62-devel
BuildRequires:  libnsync-devel
BuildRequires:  libpng16-compat-devel
BuildRequires:  libpng16-devel
BuildRequires:  lmdb-devel
BuildRequires:  memory-constraints
BuildRequires:  nasm
BuildRequires:  pcre-devel
BuildRequires:  protobuf-devel
BuildRequires:  protobuf-java
BuildRequires:  python3
BuildRequires:  python3-Cython
BuildRequires:  python3-Keras-Applications
BuildRequires:  python3-Keras-Preprocessing
BuildRequires:  python3-abseil
BuildRequires:  python3-astor
BuildRequires:  python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-opt-einsum
BuildRequires:  python3-pip
BuildRequires:  python3-protobuf
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-termcolor
BuildRequires:  python3-wheel
BuildRequires:  python3-wrapt
BuildRequires:  re2-devel
BuildRequires:  snappy-devel
BuildRequires:  sqlite3-devel
BuildRequires:  swig
BuildRequires:  unzip
BuildRequires:  zlib-devel
Requires:       python3
Requires:       python3-Keras-Applications
Requires:       python3-Keras-Preprocessing
Requires:       python3-abseil
Requires:       python3-astor
Requires:       python3-gast
Requires:       python3-pip
Requires:       python3-protobuf
Requires:       python3-termcolor
Requires:       python3-wrapt
Conflicts:      %{package_name_conflict}
%if %{with hpc}
Provides:       %{package_name_provide}
%endif
%if %{with hpc}
Requires:       python3-numpy-%{compiler_family}%{?c_f_ver}-hpc
%else
Requires:       python3-numpy
%endif
%if %{with hpc}
Provides:       python3-tensorflow-%{compiler_family}%{?c_f_ver}-hpc
%else
Provides:       python3-tensorflow
%endif
%if %{with cuda}
BuildRequires:  cuda-compiler-10-1
BuildRequires:  cuda-cufft-dev-10-1
BuildRequires:  cuda-cupti-10-1
BuildRequires:  cuda-curand-dev-10-1
BuildRequires:  cuda-cusolver-dev-10-1
BuildRequires:  cuda-cusparse-dev-10-1
BuildRequires:  cuda-libraries-10-1
BuildRequires:  libcublas-devel
BuildRequires:  libcudnn7-devel
BuildRequires:  libnccl2-devel
%endif
%if %{with opencl}
BuildRequires:  opencl-cpp-headers
BuildRequires:  opencl-headers
Requires:       Mesa-libOpenCL
%endif
BuildRequires:  flatbuffers-devel
%if 0%{?suse_version} < 1550
BuildRequires:  libjpeg62-turbo
%endif
%if %{with hpc}
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  lua-lmod
BuildRequires:  suse-hpc
%hpc_requires
%if %{with mpi}
BuildRequires:  %{mpi_flavor}%{?mpi_vers}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
%endif
%endif
# just use rpmlint
# there are some serious compiler warnings, regarding no-return-in-nonvoid-function
#!BuildRequires:  -post-build-checks
%if "%flavor" == ""
ExclusiveArch:  do_not_build
%endif
%if %{is_lite}
ExcludeArch:    %ix86
%else
ExcludeArch:    %ix86 %arm
%endif

%description
This open source software library for numerical computation is used for data
flow graphs. The graph nodes represent mathematical operations, while the graph
edges represent the multidimensional data arrays (tensors) that flow between
them. This flexible architecture enables you to deploy computation to one or
more CPUs in a desktop, server, or mobile device without rewriting code.

%{?with_hpc:%{hpc_master_package -a -L}}

%package -n %{package_name}-devel
Summary:        Header files of tensorflow
Group:          Development/Languages/Python
Requires:       %{package_name} = %{version}
Conflicts:      %{package_name_conflict}-devel
%if %{with hpc}
Provides:       %{package_name_provide}-devel
%endif

%description  -n %{package_name}-devel
This open source software library for numerical computation is used for data
flow graphs. The graph nodes represent mathematical operations, while the graph
edges represent the multidimensional data arrays (tensors) that flow between
them. This flexible architecture enables you to deploy computation to one or
more CPUs in a desktop, server, or mobile device without rewriting code.

This package provides necessary headers for the C/C++ Api

%package -n %{package_name}-doc
Summary:        Examples from the tensorflow website
Group:          Documentation/Other
Requires:       %{package_name} = %{version}

%description  -n %{package_name}-doc
This open source software library for numerical computation is used for data
flow graphs. The graph nodes represent mathematical operations, while the graph
edges represent the multidimensional data arrays (tensors) that flow between
them. This flexible architecture enables you to deploy computation to one or
more CPUs in a desktop, server, or mobile device without rewriting code.

This package provides examples from the website.

%package -n libtensorflow%{libmaj}%{?hpc_package_name_tail}
Summary:        Shared library for tensorflow
Group:          Libraries

%description  -n  libtensorflow%{libmaj}%{?hpc_package_name_tail}
This open source software library for numerical computation is used for data
flow graphs. The graph nodes represent mathematical operations, while the graph
edges represent the multidimensional data arrays (tensors) that flow between
them. This flexible architecture enables you to deploy computation to one or
more CPUs in a desktop, server, or mobile device without rewriting code.

%package -n libtensorflow_cc%{libmaj}%{?hpc_package_name_tail}
Summary:        Shared library for tensorflow
Group:          Libraries

%description  -n  libtensorflow_cc%{libmaj}%{?hpc_package_name_tail}
This open source software library for numerical computation is used for data
flow graphs. The graph nodes represent mathematical operations, while the graph
edges represent the multidimensional data arrays (tensors) that flow between
them. This flexible architecture enables you to deploy computation to one or
more CPUs in a desktop, server, or mobile device without rewriting code.

%package -n libtensorflow_framework%{libmaj}%{?hpc_package_name_tail}
Summary:        Shared library for tensorflow
Group:          Libraries

%description  -n  libtensorflow_framework%{libmaj}%{?hpc_package_name_tail}
This open source software library for numerical computation is used for data
flow graphs. The graph nodes represent mathematical operations, while the graph
edges represent the multidimensional data arrays (tensors) that flow between
them. This flexible architecture enables you to deploy computation to one or
more CPUs in a desktop, server, or mobile device without rewriting code.


%prep
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# fighting bazel
%define bazeldir %{_sourcedir}/BAZEL
%define bz_cachdir %{_sourcedir}/BAZEL_CACHE
# macro for removing nested directories
%define sanitize_dir() _uglydir=$(ls -d *); shopt -s dotglob;mv $_uglydir/* .; rmdir $_uglydir
# macro for copying the files to the bazel cache dir
%define makebazelcache() mkdir -p %{bz_cachdir}/content_addressable/sha256/%{?2:%2}%{?!2:$(sha256sum %1 | cut -f 1 -d ' ')}/; cp %1 %{bz_cachdir}/content_addressable/sha256/%{?2:%2}%{?!2:$(sha256sum %1 | cut -f 1 -d ' ')}/file ;

# make clean for rebuild
mkdir -p %{bazeldir}

#create right direcory for bazel cache which depends on the actual source file
%makebazelcache %{SOURCE10}
%makebazelcache %{SOURCE12}
%makebazelcache %{SOURCE14}
%makebazelcache %{SOURCE15}
%makebazelcache %{SOURCE17}
%makebazelcache %{SOURCE18}
%makebazelcache %{SOURCE19}
%makebazelcache %{SOURCE21}
%makebazelcache %{SOURCE23}
%makebazelcache %{SOURCE24}
%makebazelcache %{SOURCE26}
%makebazelcache %{SOURCE27}
%makebazelcache %{SOURCE28}
%makebazelcache %{SOURCE30}
%makebazelcache %{SOURCE34}
%makebazelcache %{SOURCE35}
%makebazelcache %{SOURCE36}
%makebazelcache %{SOURCE37}
%makebazelcache %{SOURCE44}
%makebazelcache %{SOURCE46}
%makebazelcache %{SOURCE47}
%makebazelcache %{SOURCE48}
%makebazelcache %{SOURCE49}
%makebazelcache %{SOURCE50}
%makebazelcache %{SOURCE53}

# unpack tensorflow

%setup -q -c -n %{pname}-%{version}
%sanitize_dir
pwd
%patch0 -p 1
%patch1 -p 1
%patch2 -p 1
%patch3 -p 1
%patch4 -p 1
%if %{with mpi}
%patch5 -p 1
%endif
%patch6 -p 1
%if 0%{?suse_version} > 1500 
%patch10 -p 1
%endif

%if %{is_lite}
mkdir tensorflow/lite/tools/make/downloads/
pushd tensorflow/lite/tools/make/downloads/
#  eigen, gemmlowp and abseil_cpp
cp %{SOURCE26} %{SOURCE17} %{SOURCE19} .
mkdir tmp
tar xzf eigen.tar.gz -C tmp && mv tmp/* eigen
unzip gemmlowp.zip -d tmp && mv tmp/* gemmlowp
tar xzf %{SOURCE100} -C tmp && mv tmp/* fgoogletest
tar xzf abseil-cpp.tar.gz -C tmp && mv tmp/* absl
tar xzf %{SOURCE27} 
mv ARM_NEON_2_x86_SSE* neon_2_sse
tar xzf %{SOURCE15} -C tmp && mv tmp/* farmhash
# We use installed flatbuffers
tar xzf %{SOURCE30} -C tmp && mv tmp/* fft2d
# sed fixes from tensorflow/lite/tools/make/download_dependencies.sh
sed -i -e 's#static uint32x4_t p4ui_CONJ_XOR = vld1q_u32( conj_XOR_DATA );#static uint32x4_t p4ui_CONJ_XOR; // = vld1q_u32( conj_XOR_DATA ); - Removed by script#' \
  "./eigen/Eigen/src/Core/arch/NEON/Complex.h"
sed -i -e 's#static uint32x2_t p2ui_CONJ_XOR = vld1_u32( conj_XOR_DATA );#static uint32x2_t p2ui_CONJ_XOR;// = vld1_u32( conj_XOR_DATA ); - Removed by scripts#' \
  "./eigen/Eigen/src/Core/arch/NEON/Complex.h"
sed -i -e 's#static uint64x2_t p2ul_CONJ_XOR = vld1q_u64( p2ul_conj_XOR_DATA );#static uint64x2_t p2ul_CONJ_XOR;// = vld1q_u64( p2ul_conj_XOR_DATA ); - Removed by script#' \
  "./eigen/Eigen/src/Core/arch/NEON/Complex.h"
find -name fixedpoint.h
popd
%endif

%build
export CC_OPT_FLAGS=$CXXFLAGS
%if !%{is_lite}
%limit_build -m 6200
%endif

%if %{is_lite}
make %{?_smp_mflags} -f tensorflow/lite/tools/make/Makefile \
    $(pwd)/tensorflow/lite/tools/make/gen/linux_$(uname -m)/lib/libtensorflow-lite.a \
    $(pwd)/tensorflow/lite/tools/make/gen/linux_$(uname -m)/bin/minimal
# Build of benchmark-lib.a is broken
%else

%if %{with hpc}
%hpc_setup
module load gnu
%if %{with mpi}
module load %mpi_flavor
export MPI_HOME=${MPI_HOME:-$MPI_DIR}
%endif #mpi
%endif #hpc

export TEST_TMPDIR=%{bazeldir}
export PYTHON_LIB_PATH=%{python3_sitearch}
export PYTHON_BIN_PATH=%{_bindir}/python3
export CC_OPT_FLAGS=-O2
export TF_NEED_JEMALLOC=0
export TF_NEED_GCP=0
export TF_NEED_HDFS=1
export TF_NEED_S3=1
export TF_ENABLE_XLA=0
export TF_NEED_VERBS=0
export TF_NEED_OPENCL=0
export TF_NEED_ROCM=0
export TF_SYSTEM_LIBS="\
  absl_py,\
  astor_archive,\
  boringssl,\
  com_google_protobuf,\
  com_googlesource_code_re2,\
  curl,\
  cython,\
  double_conversion,\
  enum34_archive,\
  flatbuffers,\
  gif_archive,\
  grpc,\
  hwloc,\
  icu,\
  jsoncpp_git,\
  jpeg,\
  keras_applications_archive,\
  lmdb,\
  nasm,\
  nsync,\
  opt_einsum_archive,\
  org_sqlite,\
  pasta,\
  pcre,\
  png_archive,\
  snappy,\
  swig,\
  six_archive,\
  termcolor_archive,\
  wrapt,\
  zlib_archive"
%if %{with cuda}
export TF_NEED_CUDA=1
%else
export TF_NEED_CUDA=0
%endif
%if %{with mpi}
export TF_NEED_MPI=1
%else
export TF_NEED_MPI=0
%endif
export TF_NEED_AWS=1
export TF_NEED_KAFKA=1
export TF_NEED_GDR=0
%if %{with opencl}
export TF_NEED_OPENCL_SYCL=1
%else
export TF_NEED_OPENCL_SYCL=0
%endif
export TF_DOWNLOAD_CLANG=0
export ANDROID_NDK_HOME=0
# force the use python3
mkdir %{_topdir}/bin
cd %{_topdir}/bin
ln -s $(which python3) python
export PATH=%{_topdir}/bin/:${PATH}
cd -
%ifarch x86_64
%define copt -c opt --config=avx_linux 
%else
%define copt -c opt
%endif

./configure
bazel build \
  --repository_cache=%{bz_cachdir} \
  --ignore_unsupported_sandboxing \
	--verbose_failures \
  --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=1" \
  --config=noaws \
	%{?copts} --jobs %{?jobs} \
	//tensorflow/tools/pip_package:build_pip_package
bazel-bin/tensorflow/tools/pip_package/build_pip_package %{_topdir}/%{name}-%{version}
bazel build \
  --repository_cache=%{bz_cachdir} \
  --ignore_unsupported_sandboxing \
	--verbose_failures \
  --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=1" \
  --config=noaws \
	%{?copts} --jobs %{?jobs} \
  //tensorflow:libtensorflow.so
bazel build \
  --repository_cache=%{bz_cachdir} \
  --ignore_unsupported_sandboxing \
	--verbose_failures \
  --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=1" \
  --config=noaws \
	%{?copts} --jobs %{?jobs} \
  //tensorflow:libtensorflow_cc.so
bazel build \
  --repository_cache=%{bz_cachdir} \
  --ignore_unsupported_sandboxing \
	--verbose_failures \
  --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=1" \
  --config=noaws \
	%{?copts} --jobs %{?jobs} \
  //tensorflow:libtensorflow_framework.so

# Generate protobuf (for armNN) - https://github.com/ARM-software/armnn/blob/branches/armnn_19_08/scripts/generate_tensorflow_protobuf.sh
export OUTPUT_DIR=./pb/
mkdir -p $OUTPUT_DIR
for i in `find -name *.proto`; do
    protoc $i \
      --proto_path=. \
      --proto_path=%{_includedir} \
      --cpp_out=$OUTPUT_DIR
done
%endif

%install

%if %{is_lite}
pushd tensorflow/lite/tools/make/gen/linux_*/
install -D bin/minimal %{buildroot}%{_bindir}/tflite_minimal
install -D lib/libtensorflow-lite.a %{buildroot}%{_libdir}/libtensorflow-lite.a
popd
install -D tensorflow/lite/schema/schema_generated.h %{buildroot}%{_includedir}/tensorflow/lite/schema/schema_generated.h
install -D tensorflow/lite/schema/schema.fbs %{buildroot}%{_includedir}/tensorflow/lite/schema/schema.fbs
%else

pip install %{_topdir}/%{name}-%{version}/*whl --root=%{buildroot}%{?hpc_prefix} \
	--no-warn-script-location --no-index --no-deps --no-compile
# remove spurious executeable bits
# for hpc build remove usr prefix dir
%if %{with hpc}
cd %{buildroot}%{?hpc_prefix}
mv usr/* .
cd -
%endif
%fdupes -s %{buildroot}%{?hpc_prefix}  
# install after fdupes
cp -vd  \
  bazel-bin/tensorflow/libtensorflow.so \
  bazel-bin/tensorflow/libtensorflow.so.%{libmaj} \
  bazel-bin/tensorflow/libtensorflow.so.%{libmaj}.%{libmin}.%{libref} \
  bazel-bin/tensorflow/libtensorflow_cc.so \
  bazel-bin/tensorflow/libtensorflow_cc.so.%{libmaj} \
  bazel-bin/tensorflow/libtensorflow_cc.so.%{libmaj}.%{libmin}.%{libref} \
  bazel-bin/tensorflow/libtensorflow_framework.so \
  bazel-bin/tensorflow/libtensorflow_framework.so.%{libmaj} \
  bazel-bin/tensorflow/libtensorflow_framework.so.%{libmaj}.%{libmin}.%{libref} \
 %{buildroot}%{package_libdir}/

find %{buildroot} -name \*.h -type f -exec chmod 644 {} +
find %{buildroot} -name LICENSE\* -type f -exec chmod 644 {} +

%if %{with hpc}
sitesearch_path=`python3 -c "import sysconfig as s; print(s.get_paths(vars={'platbase':'%{hpc_prefix}','base':'%{hpc_prefix}'}).get('platlib'))"`
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{pname} built with the %{compiler_family} toolchain."
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} toolchain"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{SUMMARY:0}"
module-whatis "URL: %{url}"

set     version                     %{version}

prepend-path    PATH                %{hpc_prefix}/bin
prepend-path    LD_LIBRARY_PATH     %{hpc_prefix}/%_lib
prepend-path    TENSORFLOWDIR       %{hpc_prefix}
prepend-path    PYTHONPATH          ${sitesearch_path}

if [ expr [ module-info mode load ] || [module-info mode display ] ] {
  if { ![is-loaded python3-numpy] } {
      module load python3-numpy
    }
}
%if %{with mpi}
if [ expr [ module-info mode load ] || [module-info mode display ] ] {
  if { ![is-loaded %mpi_flavor] } {
      module load %mpi_flavor
    }
}

%endif

%{hpc_modulefile_add_pkgconfig_path}

EOF
%endif

# Install generated protobuf
export OUTPUT_DIR=./pb/
find -name *.pb.*
%if %{with hpc}
mkdir -p %{buildroot}/%{package_python_sitelib}/tensorflow_core/include/tensorflow/
%endif
cp -r $OUTPUT_DIR/tensorflow/* %{buildroot}/%{package_python_sitelib}/tensorflow_core/include/tensorflow/

# %%{is_lite}
%endif

%post -n libtensorflow%{libmaj}%{?hpc_package_name_tail} -p /sbin/ldconfig
%postun -n libtensorflow%{libmaj}%{?hpc_package_name_tail} -p /sbin/ldconfig
%post -n libtensorflow_cc%{libmaj}%{?hpc_package_name_tail} -p /sbin/ldconfig
%postun -n libtensorflow_cc%{libmaj}%{?hpc_package_name_tail} -p /sbin/ldconfig
%post -n libtensorflow_framework%{libmaj}%{?hpc_package_name_tail} -p /sbin/ldconfig
%postun -n libtensorflow_framework%{libmaj}%{?hpc_package_name_tail} -p /sbin/ldconfig

# Lite version is very different so package it separetly
%if %{is_lite}
%files
%{package_bindir}/*
%files -n %{package_name}-devel
%{package_libdir}/libtensorflow-lite.a
%dir %{_includedir}/tensorflow/lite/schema/
%{_includedir}/tensorflow/lite/schema/*
%else # not lite build
%files
%defattr(-,root,root,-)
%{package_bindir}/estimator_ckpt_converter
%{package_bindir}/saved_model_cli
%{package_bindir}/tensorboard
%{package_bindir}/tf_upgrade_v2
%{package_bindir}/tflite_convert
%{package_bindir}/freeze_graph
%{package_bindir}/toco*
%{package_python_sitearch}/tensorflow_core/*
%{package_python_sitearch}/tensorflow-%{version}*
%{package_python_sitearch}/tensorflow
%exclude %{package_python_sitearch}/tensorflow_core/include
%if %{with hpc}
%hpc_modules_files
%{package_python_sitelib}/tensorflow_core/*
%exclude %{package_python_sitelib}/tensorflow_core/include
%{package_libdir}/libtensorflow_framework.so.%{libmaj}*
%{package_libdir}/libtensorflow_cc.so.%{libmaj}*
%{package_libdir}/libtensorflow.so.%{libmaj}*
%else
%files -n libtensorflow_framework%{libmaj}%{?hpc_package_name_tail}
%{package_libdir}/libtensorflow_framework.so.%{libmaj}*
%files -n libtensorflow_cc%{libmaj}%{?hpc_package_name_tail}
%{package_libdir}/libtensorflow_cc.so.%{libmaj}*
%files -n libtensorflow%{libmaj}%{?hpc_package_name_tail}
%{package_libdir}/libtensorflow.so.%{libmaj}*
%files -n %{package_name}-doc
%doc README.md RELEASE.md ACKNOWLEDGMENTS AUTHORS
%license LICENSE
%endif
%files -n %{package_name}-devel
%{package_python_sitelib}/tensorflow_core/include
%{package_python_sitearch}/tensorflow_core/include
%{package_libdir}/libtensorflow.so
%{package_libdir}/libtensorflow_cc.so
%{package_libdir}/libtensorflow_framework.so
%endif

%changelog
