#
# spec file for package tensorflow2
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


#
%define pname tensorflow2
%define vers 2.4.1
#%%define cand -rc4
%define _vers 2_4_1
%define libmaj 2
%define libmin 4
%define libref 1
%define python_ver_hack python3.[0-9]
%ifarch aarch64
%define mklconfig mkl_aarch64
%else
%define mklconfig mkl
%endif

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
%bcond_without hpc
%define compiler_family gnu
%endif

%if "%{flavor}" == "hpc-openmpi2"
%define mpi_flavor openmpi
%define mpi_vers 2
%bcond_with cuda
%bcond_without mpi
%bcond_with opencl
%bcond_without hpc
%define compiler_family gnu
%endif

%if "%{flavor}" == "hpc-mvapich2"
%define mpi_flavor mvapich2
%bcond_with cuda
%bcond_without mpi
%bcond_with opencl
%bcond_without hpc
%define compiler_family gnu
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
# hpc macros expect this, but we do not use python-rpm-macros
%define python_flavor python3
%define package_name   %{hpc_package_name %_vers}
%define package_name_provide tensorflow2%{hpc_package_name_tail}
%define package_name_conflict tensorflow%{hpc_package_name_tail}
%define libname(l:s:)   lib%{pname}%{-l*}%{hpc_package_name_tail %{?_vers}}
%define package_python_sitearch %hpc_python_sitearch
%define package_python_sitelib %{hpc_prefix}/lib64/%{python_ver_hack}/site-packages/
%define package_prefix %hpc_prefix
%define package_bindir %hpc_bindir
%define package_libdir %hpc_libdir
%define package_includedir %hpc_includedir
%else
%define package_name   %pname%{?package_suffix}
%define package_name_conflict tensorflow%{?package_suffix}
%define package_python_sitearch %{python3_sitearch}
%define package_python_sitelib %{python3_sitelib}
%define package_prefix %_prefix
%define package_bindir %_bindir
%define package_libdir %_libdir
%define package_includedir %_includedir
%define libname(l:s:)   lib%{pname}%{!-l:%{-s:-}}%{-l*}%{-s*}%{?package_suffix}
%endif
Name:           %{package_name}
Version:        %vers
Release:        0
Summary:        A framework used for deep learning
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND FSFUL AND MIT AND MPL-2.0 AND OpenSSL AND Python-2.0
Group:          Development/Languages/Python
URL:            https://www.tensorflow.org/
Source0:        https://github.com/tensorflow/tensorflow/archive/v%{version}%{?cand}.tar.gz#/tensorflow-%{version}.tar.gz
Source1:        tensorflow2-rpmlintrc
# IMPORTANT
# although some of the following libraries are available in factory they could
# not be used as
#   * explicit versions are needed which differ from the factory ones
#   * bazel and the obs version have different symbols due to hidden compiler flags
# License10: Apache-2.0
Source10:       https://github.com/bazelbuild/rules_closure/archive/308b05b2419edb5c8ee0471b67a40403df940149.tar.gz#/rules_closure.tar.gz
# License15: MIT
Source15:       https://github.com/google/farmhash/archive/816a4ae622e964763ca0862d9dbd19324a1eaf45.tar.gz#/farmhash.tar.gz
# License17: Apache-2.0
Source17:       https://github.com/google/gemmlowp/archive/fda83bdc38b118cc6b56753bd540caa49e570745.zip#/gemmlowp.zip
# License18: BSD-3-Clause
Source18:       https://github.com/hfp/libxsmm/archive/1.9.tar.gz#/libxsmm_1.9.tar.gz
# License19: Apache-2.0
Source19:       https://github.com/abseil/abseil-cpp/archive/df3ea785d8c30a9503321a3d35ee7d35808f190d.tar.gz#/abseil-cpp.tar.gz
# License21: Apache-2.0
Source21:       https://github.com/googleapis/googleapis/archive/541b1ded4abadcc38e8178680b0677f65594ea6f.zip#/googleapis.zip
# License24: Apache-2.0
Source24:       https://github.com/google/highwayhash/archive/fd3d9af80465e4383162e4a7c5e2f406e82dd968.tar.gz#/highwayhash.tar.gz
# License26: MPL-2.0
# NOTE: tensorflow only uses MPL-2.0 part of eigen
Source26:       https://gitlab.com/libeigen/eigen/-/archive/011e0db31d1bed8b7f73662be6d57d9f30fa457a/eigen-011e0db31d1bed8b7f73662be6d57d9f30fa457a.tar.gz#/eigen.tar.gz
# License27: BSD-2-Clause
Source27:       https://github.com/intel/ARM_NEON_2_x86_SSE/archive/1200fe90bb174a6224a525ee60148671a786a71f.tar.gz#/arm_neon_2_x86_sse.tar.gz
Source28:       https://docs.python.org/2.7/_sources/license.rst.txt#/license.rst.txt
# License34: BSD-3-Clause and Intel
Source34:       https://github.com/edenhill/librdkafka/archive/v0.11.5.tar.gz#/kafka-v0.11.5.tar.gz
# License35: Apache-2.0
Source35:       https://github.com/GoogleCloudPlatform/google-cloud-cpp/archive/v0.4.0.tar.gz#/google-cloud-cpp.tar.gz
# License37: Apache-2.0
Source37:       https://github.com/bazelbuild/rules_docker/archive/v0.15.0.tar.gz#/rules_docker-0.15.0.tar.gz
# License44: BSD like
Source44:       https://github.com/nanopb/nanopb/archive/f8ac463766281625ad710900479130c7fcb4d63b.tar.gz#/nanopb.tar.gz
# License45: Python license itself, do need as sha256b have to match so could not use system one
Source45:       https://storage.googleapis.com/mirror.tensorflow.org/docs.python.org/2.7/_sources/license.rst.txt#/python-license.txt
# License46: Another python2 license:
Source46:       https://raw.githubusercontent.com/simonpercivall/astunparse/v1.6.2/LICENSE#/python-license-astunparse
# Deps sources for Tensorflow-Lite (use same eigen, gemmlowp and abseil_cpp packages as non lite version)
# License53: BSD like
Source53:       https://storage.googleapis.com/mirror.tensorflow.org/www.kurims.kyoto-u.ac.jp/~ooura/fft2d.tgz
# License54: Apache-2.0 WITH LLVM-exception OR NCSA
Source54:       https://github.com/llvm/llvm-project/archive/f402e682d0ef5598eeffc9a21a691b03e602ff58.tar.gz#/llvm.tar.gz
# License56:  BSD-3-Clause
Source56:       https://github.com/mborgerding/kissfft/archive/36dbc057604f00aacfc0288ddad57e3b21cfc1b8.tar.gz#/kissfft.tar.gz
# Wrong rules package in Factory
# License58:  Apache-2.0
Source58:       https://github.com/bazelbuild/rules_cc/archive/01d4a48911d5e7591ecb1c06d3b8af47fe872371.zip#/rules_cc.tar.gz
# Source59: Apache-2.0
Source59:       https://github.com/bazelbuild/rules_android/archive/v0.1.1.zip#/rules_android.zip
# License60: BSD 2-Clause
Source60:       https://github.com/pytorch/cpuinfo/archive/6cecd15784fcb6c5c0aa7311c6248879ce2cb8b2.zip#/cpuinfo.zip
# License23: BSD-3-Clause
Source62:       https://github.com/joe-kuo/sobol_data/archive/835a7d7b1ee3bc83e575e302a985c66ec4b65249.tar.gz#/sobol_data.tar.gz
# Source63: Apache-2.0
Source63:       https://github.com/google/ruy/archive/5bb02fbf90824c2eb6cd7418f766c593106a332b.zip#/ruy.zip
# License64: Apache-2.0
Source64:       https://github.com/dmlc/dlpack/archive/3efc489b55385936531a06ff83425b719387ec63.tar.gz#/dlpack.tar.gz
# License65: BSD like
Source65:       https://github.com/petewarden/OouraFFT/archive/v1.0.tar.gz#/DouraFFT.tar.gz
# License66: BSD-3-Clause
# Factory version does not work
Source66:       https://github.com/google/re2/archive/506cfa4bffd060c06ec338ce50ea3468daa6c814.tar.gz#/re2.tar.gz
# License67: Apache-2.0 WITH LLVM-exception OR NCSA
Source67:       https://github.com/llvm/llvm-project/releases/download/llvmorg-10.0.1/openmp-10.0.1.src.tar.xz
# License68: Apache License 2.0
Source68:       https://github.com/oneapi-src/oneDNN/archive/v1.6.4.tar.gz#/oneDNN.tar.gz
# License69: BSD-2-Clause
Source69:       https://files.pythonhosted.org/packages/ec/c4/8c651f3240a73c28a218194f3d527eb2be5a173d08501060cdee84ade33f/tblib-1.3.2.tar.gz
# License70: BSD-3-Clause
Source70:       https://files.pythonhosted.org/packages/c7/11/345f3173809cea7f1a193bfbf02403fff250a3360e0e118a1630985e547d/dill-0.3.1.1.tar.gz
# License71: PSF
Source71:       https://files.pythonhosted.org/packages/6a/28/d32852f2af6b5ead85d396249d5bdf450833f3a69896d76eb480d9c5e406/typing_extensions-3.7.4.2.tar.gz
Source100:      https://github.com/google/googletest/archive/release-1.8.0.tar.gz

Patch10:        removed-external-toolchains.patch
# see https://github.com/tensorflow/tensorflow/pull/35943
Patch13:        remove-weakref.patch
Patch14:        fix-lite.patch
# Fix from upstream for gcc10.1
Patch20:        removed-clog-build-as-included-in-cpuinfo.patch
# Fix for numpy 1.20 -- https://stackoverflow.com/questions/66373169 , https://github.com/tensorflow/tensorflow/issues/47691
Patch21:        numpy-tensor-small.patch
# Fix for hdf5 3.0 -- https://github.com/tensorflow/tensorflow/issues/44467
Patch22:        tf-keras-hdf5-3.patch

Requires:       python3
Requires:       python3-Keras-Preprocessing
Requires:       python3-abseil
Requires:       python3-astor
Requires:       python3-astunparse
Requires:       python3-flatbuffers
Requires:       python3-gast
Requires:       python3-opt-einsum
Requires:       python3-protobuf
Requires:       python3-termcolor
Requires:       python3-wrapt
%if %{with hpc}
Requires:       python3-numpy-%{compiler_family}%{?c_f_ver}-hpc
%else
Requires:       python3-numpy
%endif
Requires:       python3-pip
%if !%{is_lite}
%if %{with hpc}
Provides:       python3-tensorflow-%{compiler_family}%{?c_f_ver}-hpc
%else
Provides:       python3-tensorflow
%endif
Provides:       tensorflow
%endif
%if !%{is_lite}
BuildRequires:  bazel == 3.4.1
#BuildRequires:  bazel-rules-cc-source
#BuildRequires:  bazel-apple-support-source
#BuildRequires:  bazel-rules-apple-source
BuildRequires:  bazel-rules-java-source
BuildRequires:  bazel-rules-proto-source
BuildRequires:  bazel-rules-python-source
BuildRequires:  bazel-rules-swift-source
BuildRequires:  bazel-skylib-source
BuildRequires:  bazel-toolchains-source
BuildRequires:  bazel-workspaces
#BuildRequires:  bazel-rules-foreign-cc-source
%endif
BuildRequires:  curl
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
BuildRequires:  libnccl-devel
%endif
%if %{with opencl}
Requires:       Mesa-libOpenCL
BuildRequires:  opencl-cpp-headers
BuildRequires:  opencl-headers
%endif
BuildRequires:  boringssl-devel
BuildRequires:  curl-devel
BuildRequires:  double-conversion-devel >= 3.1.5
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  flatbuffers-devel
BuildRequires:  giflib-devel
BuildRequires:  git
%if 0%{?suse_version} > 1500
%if %{with cuda}
# use gcc-7 for build with cuda, as nvcc can not handle
# gcc9
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%endif
%endif
BuildRequires:  grpc-devel
BuildRequires:  jemalloc-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-turbo
BuildRequires:  libnsync-devel
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
# Requiring 3.9.1 which is the actual one in Leap 15.2
BuildRequires:  protobuf-devel >= 3.9.1
BuildRequires:  protobuf-java
BuildRequires:  python-pybind11-common-devel
BuildRequires:  python3
BuildRequires:  python3-Cython
BuildRequires:  python3-Keras-Preprocessing
BuildRequires:  python3-abseil
BuildRequires:  python3-astor
BuildRequires:  python3-astunparse
BuildRequires:  python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-flatbuffers
BuildRequires:  python3-gast
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
BuildRequires:  snappy-devel
BuildRequires:  sqlite3-devel
BuildRequires:  swig
BuildRequires:  unzip
BuildRequires:  upb-devel
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
%if %{with hpc}
Provides:       %{package_name_provide}
%endif
Conflicts:      %{package_name_conflict}

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
%if %{with hpc}
Provides:       %{package_name_provide}-devel
%endif
Conflicts:      %{package_name_conflict}-devel
%if !%{is_lite}
Requires:       libtensorflow%{libmaj}%{?hpc_package_name_tail} = %{version}
Requires:       libtensorflow_cc%{libmaj}%{?hpc_package_name_tail} = %{version}
Requires:       libtensorflow_framework%{libmaj}%{?hpc_package_name_tail} = %{version}
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

%ifarch x86_64
%package -n libiomp5%{?hpc_package_name_tail}
Summary:        Shared library for tensorflow
Group:          Libraries

%description  -n   libiomp5%{?hpc_package_name_tail}
This open source software library for numerical computation is used for data
flow graphs. The graph nodes represent mathematical operations, while the graph
edges represent the multidimensional data arrays (tensors) that flow between
them. This flexible architecture enables you to deploy computation to one or
more CPUs in a desktop, server, or mobile device without rewriting code.
%endif

%prep
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
%makebazelcache %{SOURCE15}
%makebazelcache %{SOURCE17}
%makebazelcache %{SOURCE18}
%makebazelcache %{SOURCE19}
%makebazelcache %{SOURCE21}
%makebazelcache %{SOURCE24}
%makebazelcache %{SOURCE26}
%makebazelcache %{SOURCE27}
%makebazelcache %{SOURCE28}
%makebazelcache %{SOURCE34}
%makebazelcache %{SOURCE35}
%makebazelcache %{SOURCE44}
%makebazelcache %{SOURCE45}
%makebazelcache %{SOURCE46}
%makebazelcache %{SOURCE53}
%makebazelcache %{SOURCE54}
%makebazelcache %{SOURCE56}
%makebazelcache %{SOURCE58}
%makebazelcache %{SOURCE59}
%makebazelcache %{SOURCE60}
%makebazelcache %{SOURCE62}
%makebazelcache %{SOURCE63}
%makebazelcache %{SOURCE64}
%makebazelcache %{SOURCE65}
%makebazelcache %{SOURCE66}
%makebazelcache %{SOURCE67}
%makebazelcache %{SOURCE68}
%makebazelcache %{SOURCE69}
%makebazelcache %{SOURCE70}
%makebazelcache %{SOURCE71}

# unpack tensorflow
%setup -q -c -n %{pname}-%{version}
%sanitize_dir
%patch10 -p 1
%patch13 -p 1
%patch14 -p 1
%patch20 -p 1
%patch21 -p 1
%patch22 -p 1

%define make_depend_src() test -e $(basename %{1}| sed 's/-.*//') && rmdir %{?2}%{!?2:$(basename %{1}| sed 's/-.*//')}; test -e %{2} && rmdir %{2}; tar xzf %{1}; mv $(basename %{1} | sed 's/\.tar\.gz//' ) %{?2}%{!?2:$(basename %{1}| sed 's/-.*//')}
# extract bazel rules
cd %{bazeldir}
%make_depend_src %{S:37}
cd -

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
unzip %{SOURCE63} -d tmp && mv tmp/* ruy
unzip %{SOURCE60} -d tmp && mv tmp/* cpuinfo
tar xzf %{SOURCE27}
mv ARM_NEON_2_x86_SSE* neon_2_sse
tar xzf %{SOURCE15} -C tmp && mv tmp/* farmhash
# We use installed flatbuffers
tar xzf %{SOURCE53} -C tmp && mv tmp/* fft2d
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
%endif
%endif
# remove external repos
#rm /home/abuild/rpmbuild/SOURCES/BAZEL/_bazel_abuild/48d1e3f2f1a94ce79e8483f24416e037/external/bazel_toolchains/repositories/repositories.bzl
cp  -r /usr/src/bazel-toolchains /home/abuild/rpmbuild/SOURCES/bazel-toolchains
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
export TF_SYSTEM_LIBS="\
    absl_py,\
    astor_archive,\
    astunparse_archive,\
    boringssl,\
    com_github_googleapis_googleapis,\
    com_github_googlecloudplatform_google_cloud_cpp,\
    com_github_grpc_grpc,\
    com_google_protobuf,\
    curl,\
    cython,\
    double_conversion,\
    enum34_archive,\
    flatbuffers,\
    functools32_archive,\
    gast_archive,\
    gif,\
    hwloc,\
    icu,\
    libjpeg_turbo,\
    jsoncpp_git,\
    lmdb,\
		nasm,\
    nsync,\
    opt_einsum_archive,\
    org_sqlite,\
    pasta,\
    pcre,\
    png,\
    pybind11,\
    six_archive,\
    snappy,\
    termcolor_archive,\
    wrapt,\
    zlib"
    #com_googlesource_code_re2,\
%if %{with cuda}
export PATH=PATH="/usr/local/cuda-10.1/bin/:${PATH}"
export CUDA_HOME="/usr/local/cuda-10.1,/usr"
export CUDA_TOOLKIT_PATH=/"usr/local/cuda-10.1,/usr"
export TF_CUDA_PATHS="/usr/local/cuda-10.1,/usr"
export TF_NEED_CUDA=1
export TF_NCCL_VERSION=2.7.3
%else
export TF_NEED_CUDA=0
%endif
%if %{with mpi}
export TF_NEED_MPI=1
%else
export TF_NEED_MPI=0
%endif
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
%if 0%{?suse_version} > 1500
%if %{with cuda}
ln -s $(which gcc-7) gcc
ln -s $(which g++-7) g++
%endif
%endif
export PATH=%{_topdir}/bin/:${PATH}
cd -
./configure

%define bazelopts \\\
  -s -c opt \\\
  --repository_cache=%{bz_cachdir} \\\
  --ignore_unsupported_sandboxing \\\
  --verbose_failures \\\
  --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=1" \\\
  --config=%{mklconfig} \\\
  --config=v2 \\\
  --config=noaws \\\
  --incompatible_no_support_tools_in_action_inputs=false \\\
  --override_repository="upb=/usr/share/bazel-workspaces/upb" \\\
  --override_repository="bazel_skylib=/usr/src/bazel-skylib"\\\
  --override_repository="bazel_toolchains=/home/abuild/rpmbuild/SOURCES/bazel-toolchains" \\\
  --override_repository="rules_java=/usr/src/bazel-rules-java" \\\
  --override_repository="build_bazel_rules_swift=/usr/src/bazel-rules-swift" \\\
  --override_repository="rules_python=/usr/src/bazel-rules-python" \\\
  --override_repository="io_bazel_rules_docker=%{bazeldir}/rules_docker" \\\
  --jobs %{?jobs} \\\
%{nil}
#  --override_repository="build_bazel_rules_apple=/usr/src/bazel-rules-apple" \\\
#  --override_repository="build_bazel_apple_support=/usr/src/bazel-apple-support" \\\
#  --override_repository="rules_cc=/usr/src/bazel-rules-cc" \\\

bazel build %{bazelopts} tensorflow/tools/pip_package:build_pip_package

bazel-bin/tensorflow/tools/pip_package/build_pip_package %{_topdir}/%{name}-%{version}

# Generate protobuf (for armNN) - https://github.com/ARM-software/armnn/blob/branches/armnn_19_08/scripts/generate_tensorflow_protobuf.sh
export OUTPUT_DIR=./pb/
mkdir -p $OUTPUT_DIR
for i in `find -name *.proto`; do
    protoc $i \
      --proto_path=. \
      --proto_path=%{_includedir} \
      --cpp_out=$OUTPUT_DIR
done

bazel build \
  %bazelopts \
  //tensorflow:libtensorflow.so

bazel build \
  %bazelopts \
  //tensorflow:libtensorflow_cc.so

bazel build \
 %bazelopts \
 //tensorflow:libtensorflow_framework.so

bazel build \
 %bazelopts \
 --config opt //tensorflow/tools/lib_package:libtensorflow
%endif # is_lite

%install

%if %{is_lite}
pushd tensorflow/lite/tools/make/gen/linux_*/
install -D bin/minimal %{buildroot}%{_bindir}/tflite_minimal
install -D lib/libtensorflow-lite.a %{buildroot}%{_libdir}/libtensorflow-lite.a
# Disable spurious-executable-perm
chmod -x %{buildroot}%{_libdir}/libtensorflow-lite.a
popd
install -D tensorflow/lite/schema/schema_generated.h %{buildroot}%{_includedir}/tensorflow/lite/schema/schema_generated.h
install -D tensorflow/lite/schema/schema.fbs %{buildroot}%{_includedir}/tensorflow/lite/schema/schema.fbs
for file in `find tensorflow/lite -name \*.h`; do
  # Package header files - boo#1175099
  install -D $file %{buildroot}%{_includedir}/$file
  # Disable spurious-executable-perm
  chmod -x %{buildroot}%{_includedir}/$file
done
# Install tensorflow-lite.pc
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat <<EOF > %{buildroot}%{_libdir}/pkgconfig/tensorflow-lite.pc
Name:           tensorflow lite
Description: tensorflow lite static library
Version:        %{vers}
Requires:       
Libs: -L%{_libdir} -ltensorflow-lite -lflatbuffers
Cflags: -I%{_includedir}
EOF
# Some tools expect tensorflow2-lite.pc
pushd %{buildroot}%{_libdir}/pkgconfig
ln -s tensorflow-lite.pc tensorflow2-lite.pc
popd
%else

pip install %{_topdir}/%{name}-%{version}/*whl --root=%{buildroot}%{?hpc_prefix} \
	--no-warn-script-location --no-index --no-deps --no-compile

# install C-headers
pushd .
cd  %{buildroot}%{?hpc_prefix}/usr/
tar -xzf  %{_topdir}/BUILD/%{pname}-%{version}/bazel-bin/tensorflow/tools/lib_package/libtensorflow.tar.gz
mv lib/lib*.so* lib64/
mv LICENSE THIRD_PARTY_TF_C_LICENSES %{_topdir}/BUILD/%{pname}-%{version}/
popd
# remove spurious executeable bits
# for hpc build remove usr prefix dir
%if %{with hpc}
cd %{buildroot}%{?hpc_prefix}
mv usr/* .
rmdir usr
#mv lib/%{python_ver_hack}/site-packages/tensorflow_core/include/* lib64/%{python_ver_hack}/site-packages/tensorflow_core/include/
rm -r lib
cd -
%else
# Generate and install pkgconfig files for non-hpc - tensorflow.pc and tensorflow_cc.pc
sh tensorflow/c/generate-pc.sh --prefix=/usr --libdir %{_lib} --version %{vers}
mkdir -p %{buildroot}%{package_libdir}/pkgconfig
cp *.pc %{buildroot}%{package_libdir}/pkgconfig
%endif
# install libtensorflow*.so
#install -D bazel-bin/tensorflow/libtensorflow.so %{buildroot}%{package_libdir}/libtensorflow.so

%fdupes -s %{buildroot}%{?hpc_prefix}

# install after fdupes
cp -vd  \
  bazel-bin/tensorflow/libtensorflow_cc.so \
  bazel-bin/tensorflow/libtensorflow_cc.so.%{libmaj} \
  bazel-bin/tensorflow/libtensorflow_cc.so.%{libmaj}.%{libmin}.%{libref} \
 %{buildroot}%{package_libdir}/

%ifarch x86_64
mv %{buildroot}/%{package_python_sitearch}/_solib_k8/_U_S_Sthird_Uparty_Smkl_Cmkl_Ulibs_Ulinux___Uexternal_Sllvm_Uopenmp/libiomp5.so %{buildroot}/%{package_libdir}/
# Fix symlink
pushd %{buildroot}%{package_python_sitearch}/tensorflow/include/external/llvm_openmp/
rm libiomp5.so
ln -s %{package_libdir}/libiomp5.so
popd
%endif

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
mkdir -p  %{buildroot}/%{package_python_sitelib}/tensorflow_core/include/tensorflow/
export OUTPUT_DIR=./pb/
#find -name *.pb.*
cp -r $OUTPUT_DIR/tensorflow/* %{buildroot}/%{package_python_sitelib}/tensorflow_core/include/tensorflow/

# %%{is_lite}
%endif

%post -n libtensorflow%{libmaj}%{?hpc_package_name_tail} -p /sbin/ldconfig
%postun -n libtensorflow%{libmaj}%{?hpc_package_name_tail} -p /sbin/ldconfig
%post -n libtensorflow_cc%{libmaj}%{?hpc_package_name_tail} -p /sbin/ldconfig
%postun -n libtensorflow_cc%{libmaj}%{?hpc_package_name_tail} -p /sbin/ldconfig
%post -n libtensorflow_framework%{libmaj}%{?hpc_package_name_tail} -p /sbin/ldconfig
%postun -n libtensorflow_framework%{libmaj}%{?hpc_package_name_tail} -p /sbin/ldconfig

%if %{is_lite}
%files
# Lite version is very different so package it separetly
%{package_bindir}/*

%files -n %{package_name}-devel
%{package_libdir}/libtensorflow-lite.a
%dir %{_includedir}/tensorflow/lite/
%{_includedir}/tensorflow/lite/*
%{package_libdir}/pkgconfig/*.pc

%else

%files
# not lite build
%defattr(-,root,root,-)
%{package_bindir}/estimator_ckpt_converter
%{package_bindir}/saved_model_cli
%{package_bindir}/tensorboard
%{package_bindir}/tf_upgrade_v2
%{package_bindir}/tflite_convert
%{package_bindir}/toco*
%{package_bindir}/import_pb_to_tensorboard
#%%{package_python_sitearch}/tensorflow_core/*
%{package_python_sitearch}/tensorflow-%{version}*
%{package_python_sitearch}/tensorflow
#%%{package_python_sitelib}/tensorflow/
%exclude %{package_python_sitelib}/tensorflow_core/include
%exclude %{package_python_sitelib}/tensorflow/include
%exclude %{package_python_sitearch}/tensorflow/include
%if %{with hpc}
%hpc_modules_files
%endif

%files -n %{package_name}-devel
%{package_python_sitelib}/tensorflow_core/include
#%%{package_python_sitearch}/tensorflow_core/include
%{package_includedir}/tensorflow/
%{package_libdir}/libtensorflow.so
%{package_libdir}/libtensorflow_cc.so
%{package_libdir}/libtensorflow_framework.so
%if %{without hpc}
%{package_libdir}/pkgconfig/*.pc
%endif

%files -n libtensorflow_framework%{libmaj}%{?hpc_package_name_tail}
%{package_libdir}/libtensorflow_framework.so.%{libmaj}*

%files -n libtensorflow_cc%{libmaj}%{?hpc_package_name_tail}
%{package_libdir}/libtensorflow_cc.so.%{libmaj}*

%files -n libtensorflow%{libmaj}%{?hpc_package_name_tail}
%{package_libdir}/libtensorflow.so.%{libmaj}*

%ifarch x86_64
%files -n libiomp5%{?hpc_package_name_tail}
%{package_libdir}/libiomp5.so
%endif

%files -n %{package_name}-doc
#%%{package_python_sitelib}/tensorflow/examples
%license THIRD_PARTY_TF_C_LICENSES LICENSE

%endif

%changelog
