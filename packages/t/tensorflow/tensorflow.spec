#
# spec file for package tensorflow
#
# Copyright (c) 2019 SUSE LLC
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
%define vers 1.13.2
%define _vers 1_13_2
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
%bcond_with cuda
%bcond_with mpi
%bcond_with opencl
%define package_suffix -lite
%endif

%if "%{flavor}" == "hpc"
%bcond_with cuda
%bcond_with mpi
%bcond_with opencl
%bcond_with avx2
%bcond_without hpc
%define compiler_family gnu
%endif

%if "%{flavor}" == "avx2"
%bcond_with cuda
%bcond_with mpi
%bcond_with opencl
%bcond_without avx2
%define package_suffix -avx2
%endif

%if "%{flavor}" == "hpc-avx2"
%bcond_with cuda
%bcond_with mpi
%bcond_with opencl
%bcond_without hpc
%bcond_without avx2
%define compiler_family gnu
%define ext avx2
%endif

%if "%{flavor}" == "hpc-avx2-openmpi3"
%define mpi_flavor openmpi
%define mpi_vers 3
%bcond_with cuda
%bcond_without mpi
%bcond_with opencl
%bcond_without hpc
%bcond_without avx2
%define compiler_family gnu
%define ext avx2
%endif

%if "%{flavor}" == "hpc-avx2-openmpi2"
%define mpi_flavor openmpi
%define mpi_vers 2
%bcond_with cuda
%bcond_without mpi
%bcond_with opencl
%bcond_without hpc
%bcond_without avx2
%define compiler_family gnu
%define ext avx2
%endif

%if "%{flavor}" == "hpc-avx2-mvapich2"
%define mpi_flavor mvapich2
%bcond_with cuda
%bcond_without mpi
%bcond_with opencl
%bcond_without hpc
%bcond_without avx2
%define compiler_family gnu
%define ext avx2
%endif

%if "%{flavor}" == "hpc-openmpi2"
%define mpi_flavor openmpi
%define mpi_vers 2
%bcond_with cuda
%bcond_without mpi
%bcond_with opencl
%bcond_without hpc
%bcond_with avx2
%define compiler_family gnu
%endif

%if "%{flavor}" == "hpc-mvapich2"
%define mpi_flavor mvapich2
%bcond_with cuda
%bcond_without mpi
%bcond_with opencl
%bcond_without hpc
%bcond_with avx2
%define compiler_family gnu
%endif

%if "%{flavor}" == "cuda-9.0"
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
%define libname(l:s:)   lib%{pname}%{-l*}%{hpc_package_name_tail %{?_vers}}
%define package_python_sitearch %hpc_python_sitearch
%define package_python_sitelib %{hpc_prefix}/lib64/%{python_ver_hack}/site-packages/
%define package_prefix %hpc_prefix
%define package_bindir %hpc_bindir
%define package_libdir %hpc_libdir
%else
%define package_name   %pname%{?package_suffix}
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
Source10:       https://github.com/bazelbuild/rules_closure/archive/dbb96841cc0a5fb2664c37822803b06dab20c7d1.tar.gz#/rules_closure.tar.gz
# License12:  Python-2.0
Source12:       https://pypi.python.org/packages/bc/cc/3cdb0a02e7e96f6c70bd971bc8a90b8463fda83e264fa9c5c1c98ceabd81/backports.weakref-1.0rc1.tar.gz#/backports.weakref-1.0rc1.tar.gz
# License13: BSD-3-Clause
Source13:       https://github.com/google/double-conversion/archive/3992066a95b823efc8ccc1baf82a1cfc73f6e9b8.zip#/double_conversion.zip
# License14: BSD-3-Clause
Source14:       https://pypi.python.org/packages/5c/78/ff794fcae2ce8aa6323e789d1f8b3b7765f601e7702726f430e814822b96/gast-0.2.0.tar.gz#/gast-0.2.0.tar.gz
# License15: MIT
Source15:       https://github.com/google/farmhash/archive/816a4ae622e964763ca0862d9dbd19324a1eaf45.tar.gz#/farmhash.tar.gz
# License16: Apache-2.0
Source16:       https://github.com/google/nsync/archive/1.20.0.tar.gz#/nsync_1.20.0.tar.gz
# License17: Apache-2.0
Source17:       https://github.com/google/gemmlowp/archive/38ebac7b059e84692f53e5938f97a9943c120d98.zip#/gemmlowp.zip
# License18: BSD-3-Clause
Source18:       https://github.com/hfp/libxsmm/archive/1.9.tar.gz#/libxsmm_1.9.tar.gz
# License19: Apache-2.0
Source19:       https://github.com/abseil/abseil-cpp/archive/389ec3f906f018661a5308458d623d01f96d7b23.tar.gz#/abseil-cpp.tar.gz
# License20: OpenSSL and ISC and Intel
Source20:       https://github.com/google/boringssl/archive/7f634429a04abc48e2eb041c81c5235816c96514.tar.gz#/boring_ssl.tar.gz
# License21: Apache-2.0
Source21:       https://github.com/googleapis/googleapis/archive/f81082ea1e2f85c43649bee26e0d9871d4b41cdb.zip#/googleapis.zip
# License23: Apache-2.0
Source22:       https://github.com/google/flatbuffers/archive/v1.9.0.tar.gz#/flatbuffers_v1.9.0.tar.gz
# License23: BSD-3-Clause
Source23:       https://github.com/NVlabs/cub/archive/1.8.0.zip#/cub_1.8.0.zip
# License24: Apache-2.0
Source24:       https://github.com/google/highwayhash/archive/fd3d9af80465e4383162e4a7c5e2f406e82dd968.tar.gz#/highwayhash.tar.gz
# License25: Apache-2.0
Source25:       https://github.com/abseil/abseil-py/archive/pypi-v0.2.2.tar.gz#/abseil-pypi-v0.2.2.tar.gz
# License26: MPL-2.0
# NOTE: tensorflow only uses MPL-2.0 part of eigen
Source26:       https://bitbucket.org/eigen/eigen/get/9f48e814419e.tar.gz#/eigen.tar.gz
# License27: BSD-2-Clause
Source27:       https://github.com/intel/ARM_NEON_2_x86_SSE/archive/1200fe90bb174a6224a525ee60148671a786a71f.tar.gz#/arm_neon_2_x86_sse.tar.gz
Source28:       https://mirror.bazel.build/docs.python.org/2.7/_sources/license.txt#/python-license.txt
# License29: MIT
Source29:       https://github.com/open-source-parsers/jsoncpp/archive/1.8.4.tar.gz#/json-cpp-1.8.4.tar.gz
# License30: FSFUL
Source30:       http://www.kurims.kyoto-u.ac.jp/~ooura/fft.tgz#/fft.tar.gz
# License33: Apache-2.0
Source33:       https://github.com/aws/aws-sdk-cpp/archive/1.3.15.tar.gz#/aws-sdk-cpp-1.3.15.tar.gz
# License34: BSD-3-Clause and Intel
Source34:       https://github.com/edenhill/librdkafka/archive/v0.11.5.tar.gz#/kafka-v0.11.5.tar.gz
# License35: Apache-2.0
Source35:       https://github.com/GoogleCloudPlatform/google-cloud-cpp/archive/v0.4.0.tar.gz#/google-cloud-cpp.tar.gz
# License36: Apache-2.0
Source36:       https://github.com/nlopezgi/bazel-toolchains/archive/3f8c58fe530fedc446de04673bc1e32985887dea.tar.gz#/bazel-toolchains.tar.gz
# License37: Apache-2.0
Source37:       https://github.com/bazelbuild/rules_docker/archive/a9bb1dab84cdf46e34d1b34b53a17bda129b5eba.tar.gz#/rules_docker.tar.gz
# License40: MIT
Source40:       https://github.com/google/nsync/archive/1.20.1.tar.gz#/google-nsync-1.20.1.tar.gz
# License42: Apache-2.0
Source42:       https://github.com/google/flatbuffers/archive/1f5eae5d6a135ff6811724f6c57f911d1f46bb15.tar.gz#/google-flatbuffers-1.10.0~pre.tar.gz
# License43: BSD and ICU License
Source43:       https://github.com/unicode-org/icu/archive/release-62-1.tar.gz#/unicode-org-icu.tar.gz
# License44: BSD like
Source44:       https://github.com/nanopb/nanopb/archive/f8ac463766281625ad710900479130c7fcb4d63b.tar.gz#/nanopb.tar.gz
# License45: Python license itself, do need as sha256b have to match so could not use system one
Source45:       https://mirror.bazel.build/docs.python.org/2.7/_sources/license.rst.txt
# Deps sources for Tensorflow-Lite (use same eigen, gemmlowp and abseil_cpp packages as non lite version)
Source100:      https://github.com/google/googletest/archive/release-1.8.0.tar.gz
Source101:      https://github.com/intel/ARM_NEON_2_x86_SSE/archive/master.zip
Source102:      http://github.com/google/farmhash/archive/816a4ae622e964763ca0862d9dbd19324a1eaf45.tar.gz
# Source103:      http://mirror.tensorflow.org/github.com/google/flatbuffers/archive/v1.11.0.tar.gz
Source104:      http://www.kurims.kyoto-u.ac.jp/~ooura/fft.tgz
Patch1:         support-new-bazel.patch
Patch2:         fix_mvapich_mpi_bzl.patch
# PATCH-FIX-UPSTREAM https://github.com/tensorflow/tensorflow/pull/22856
Patch3:         tensorflow-make_aws_sdk_work_on_aarch64.patch
# PATCH-FIX-OPENSUSE - Use installed flatbuffers lib for Tensorflow-Lite
Patch4:         tensorflow-fix_lite.patch
Patch5:         remove-keras.patch
Patch6:         grpc-namespace-corrections.patch

Requires:       python3
Requires:       python3-Keras-Applications
Requires:       python3-Keras-Preprocessing
Requires:       python3-abseil
Requires:       python3-astor
Requires:       python3-gast
Requires:       python3-protobuf
Requires:       python3-termcolor
%if %{with hpc}
Requires:       python3-numpy-%{compiler_family}%{?c_f_ver}-hpc
%else
Requires:       python3-numpy
%endif
Requires:       python3-pip
%if %{with hpc}
Provides:       python3-tensorflow-%{compiler_family}%{?c_f_ver}-hpc
%else
Provides:       python3-tensorflow
%endif
BuildRequires:  bazel == 0.19.2
BuildRequires:  curl
%if %{with cuda}
Requires:       cuda-9.0
BuildRequires:  cuda-9.0
%endif
%if %{with opencl}
Requires:       Mesa-libOpenCL
BuildRequires:  opencl-cpp-headers
BuildRequires:  opencl-headers
%endif
BuildRequires:  curl-devel
BuildRequires:  fdupes
%if %{is_lite}
BuildRequires:  flatbuffers-devel
%endif
BuildRequires:  fftw3-devel
BuildRequires:  giflib-devel
BuildRequires:  grpc-devel
BuildRequires:  jemalloc-devel
BuildRequires:  libjpeg-turbo
%if 0%{?suse_version} < 1550
BuildRequires:  libjpeg62-turbo
%endif
BuildRequires:  libjpeg-devel
BuildRequires:  libjpeg62-devel
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
BuildRequires:  python3-astor
BuildRequires:  python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-pip
BuildRequires:  python3-protobuf
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-termcolor
BuildRequires:  python3-wheel
BuildRequires:  re2-devel
BuildRequires:  snappy-devel
BuildRequires:  sqlite3-devel
BuildRequires:  swig
BuildRequires:  unzip
BuildRequires:  zlib-devel
%if %{with hpc}
%hpc_requires
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  lua-lmod
BuildRequires:  suse-hpc
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
%if %{with avx2}
ExclusiveArch:  x86_64
%define copts --copt=-mavx --copt=-mavx2 --copt=-mfma --copt=-mfpmath=both --copt=-msse4.2
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
%makebazelcache %{SOURCE13}
%makebazelcache %{SOURCE14}
%makebazelcache %{SOURCE15}
%makebazelcache %{SOURCE16}
%makebazelcache %{SOURCE17}
%makebazelcache %{SOURCE18}
%makebazelcache %{SOURCE19}
%makebazelcache %{SOURCE20}
%makebazelcache %{SOURCE21}
%makebazelcache %{SOURCE22}
%makebazelcache %{SOURCE23}
%makebazelcache %{SOURCE24}
%makebazelcache %{SOURCE25}
%makebazelcache %{SOURCE26}
%makebazelcache %{SOURCE27}
%makebazelcache %{SOURCE28}
%makebazelcache %{SOURCE29}
%makebazelcache %{SOURCE30}
%makebazelcache %{SOURCE33}
%makebazelcache %{SOURCE34}
%makebazelcache %{SOURCE35}
%makebazelcache %{SOURCE36}
%makebazelcache %{SOURCE37}
%makebazelcache %{SOURCE40}
%makebazelcache %{SOURCE42}
%makebazelcache %{SOURCE43}
%makebazelcache %{SOURCE44}
%makebazelcache %{SOURCE45}

# unpack tensorflow

%setup -q -c -n %{pname}-%{version}
%sanitize_dir
pwd
%patch1 -p 1
%patch2 -p 1
%patch3 -p 1
%patch4 -p 1
%patch5 -p 1
# grpc patches only needed for TW atm
%if 0%{?suse_version} > 1500
%patch6 -p 1
%endif

echo $MPI_DIR

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
unzip %{SOURCE101} -d neon_2_sse
tar xzf %{SOURCE102} -C tmp && mv tmp/* farmhash
# We use installed flatbuffers
tar xzf %{SOURCE104} -C tmp && mv tmp/* fft2d
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
%if !%{is_lite}
%limit_build -m 6000
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
export PYTHON_BIN_PATH=/usr/bin/python3
export CC_OPT_FLAGS=-O2
export TF_NEED_JEMALLOC=0 
export TF_NEED_GCP=0 
export TF_NEED_HDFS=1
export TF_NEED_S3=1
export TF_ENABLE_XLA=0 
export TF_NEED_VERBS=0 
export TF_NEED_OPENCL=0 
export TF_NEED_ROCM=0
export TF_SYSTEM_LIBS="com_google_protobuf,com_google_protobuf_cc,protobuf_archive,nasm,com_googlesource_code_re2,nasm,jpeg,png_archive,org_sqlite,gif_archive,six_archive,astor_archive,termcolor_archive,pcre,swig,curl,lmdb,zlib_archive,snappy,cython,grpc"
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
./configure
bazel build --repository_cache=%{bz_cachdir} --ignore_unsupported_sandboxing \
	--verbose_failures --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=1" \
	%{?copts} --jobs %{?jobs} \
	//tensorflow/tools/pip_package:build_pip_package
bazel-bin/tensorflow/tools/pip_package/build_pip_package %{_topdir}/%{name}-%{version}
bazel build -c opt //tensorflow:libtensorflow.so
bazel build -c opt //tensorflow:libtensorflow_cc.so

# Generate protobuf (for armNN) - https://github.com/ARM-software/armnn/blob/branches/armnn_19_08/scripts/generate_tensorflow_protobuf.sh
export TF_PROTO_FILES=tensorflow/contrib/makefile/tf_proto_files.txt
export OUTPUT_DIR=./pb/
mkdir -p $OUTPUT_DIR
for i in `cat $TF_PROTO_FILES`; do
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
	--no-warn-script-location --no-index --no-deps 
# remove spurious executeable bits
# for hpc build remove usr prefix dir
%if %{with hpc} 
cd %{buildroot}%{?hpc_prefix}
mv usr/* .
rmdir usr
mv lib/%{python_ver_hack}/site-packages/* lib64/%{python_ver_hack}/site-packages/
rm -r lib
cd -
%endif
# install libtensorflow*.so
install -D bazel-bin/tensorflow/libtensorflow.so %{buildroot}%{package_libdir}/libtensorflow.so
install -D bazel-bin/tensorflow/libtensorflow_cc.so %{buildroot}%{package_libdir}/libtensorflow_cc.so
install -D bazel-bin/tensorflow/libtensorflow_framework.so %{buildroot}%{package_libdir}/libtensorflow_framework.so
# remove external libs
%fdupes -s %{buildroot}%{?hpc_prefix}  
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
cp -r $OUTPUT_DIR/tensorflow/* %{buildroot}/%{package_python_sitelib}/tensorflow/include/tensorflow/

# %%{is_lite}
%endif

%post -n %{package_name}-devel -p /sbin/ldconfig
%postun -n %{package_name}-devel -p /sbin/ldconfig

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
%{package_python_sitearch}/*
%{package_bindir}/*
%{package_python_sitelib}/tensorflow/
%exclude %{package_python_sitelib}/tensorflow/include
%exclude %{package_python_sitelib}/tensorflow/examples
%if %{with hpc}
%hpc_modules_files
%endif
%files -n %{package_name}-devel
%{package_python_sitelib}/tensorflow/include
%{package_libdir}/libtensorflow*.so
%files -n %{package_name}-doc
%{package_python_sitelib}/tensorflow/examples

%endif

%changelog
