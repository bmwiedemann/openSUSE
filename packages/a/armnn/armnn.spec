#
# spec file for package armnn
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


# Disable LTO until UnitTests passes with LTO enabled - https://github.com/ARM-software/armnn/issues/341
%define _lto_cflags %{nil}
%define target @BUILD_FLAVOR@%{nil}
%if "%{target}" != ""
%define package_suffix -%{target}
%endif
# Use Tensorflow version 2
%define tf_version_2 1
# Compute library has neon enabled for aarch64 only
%ifarch aarch64
%bcond_without compute_neon
%else
%bcond_with compute_neon
%endif
%if "%{target}" == "opencl"
%bcond_without compute_cl
%else
%bcond_with compute_cl
%endif
# stb-devel is available on Leap 15.1+
%if 0%{?suse_version} > 1500 || ( 0%{?sle_version} > 150000 && 0%{?is_opensuse} )
%bcond_without armnn_tests
%else
%bcond_with armnn_tests
%endif
# Extra tests require opencv(3)-devel, but it is broken for Leap 15.x - boo#1154091
%if 0%{?suse_version} > 1500
%bcond_without armnn_extra_tests
%else
%bcond_with armnn_extra_tests
%endif
# flatbuffers-devel is available on Leap 15.2+
%if 0%{?suse_version} > 1500 || ( 0%{?sle_version} >= 150200 && 0%{?is_opensuse} )
%bcond_without armnn_flatbuffers
%else
%bcond_with armnn_flatbuffers
%endif
# Enable TensorFlow on TW and Leap 15.2/SLE15SP2 for aarch64 and x86_64 (TF fails to build on armv7)
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
%ifarch aarch64 x86_64
%bcond_without armnn_tf
%else
%bcond_with armnn_tf
%endif # ifarch
%else  # suse_version
%bcond_with armnn_tf
%endif # suse_version
# ONNX is available on Leap 15.2+
%if 0%{?suse_version} > 1500 || ( 0%{?sle_version} >= 150200 && 0%{?is_opensuse} )
%bcond_without armnn_onnx
%else
%bcond_with armnn_onnx
%endif
%define version_major 20
%define version_minor 02
# Do not package ArmnnConverter and ArmnnQuantizer, by default
%bcond_with armnn_tools
# Enable CAFFE
%bcond_without armnn_caffe
Name:           armnn%{?package_suffix}
Version:        %{version_major}.%{version_minor}
Release:        0
Summary:        Arm NN SDK enables machine learning workloads on power-efficient devices
License:        MIT
Group:          Development/Libraries/Other
URL:            https://developer.arm.com/products/processors/machine-learning/arm-nn
Source0:        https://github.com/ARM-software/armnn/archive/v%{version}.tar.gz#/armnn-%{version}.tar.gz
Source1:        armnn-rpmlintrc
# PATCH-FIX-UPSTREAM - https://github.com/ARM-software/armnn/commit/6445cfff7519effd1df04eac88ae17d6e4e6693b
Patch1:         armnn-enable-use-of-arm-compute-shared-library.patch
# PATCHES to add downstream ArmnnExamples binary - https://layers.openembedded.org/layerindex/recipe/87610/
Patch200:       0003-add-more-test-command-line-arguments.patch
Patch201:       0005-add-armnn-mobilenet-test-example.patch
Patch202:       0006-armnn-mobilenet-test-example.patch
Patch203:       0009-command-line-options-for-video-port-selection.patch
Patch204:       0010-armnnexamples-update-for-19.08-modifications.patch
Patch205:       armnn-fix_find_opencv.patch
BuildRequires:  ComputeLibrary-devel >= %{version_major}.%{version_minor}
BuildRequires:  cmake >= 3.0.2
BuildRequires:  gcc-c++
BuildRequires:  protobuf-devel
BuildRequires:  python-rpm-macros
BuildRequires:  valgrind-devel
BuildRequires:  vim
# Make armnn-opencl pulls lib*-opencl, and armnn pulls non opencl libs
Requires:       libarmnn%{version_major}%{?package_suffix} = %{version}
ExcludeArch:    %ix86
%if 0%{?suse_version} < 1330
BuildRequires:  boost-devel >= 1.59
%else
BuildRequires:  libboost_filesystem-devel >= 1.59
BuildRequires:  libboost_log-devel >= 1.59
BuildRequires:  libboost_program_options-devel >= 1.59
BuildRequires:  libboost_system-devel >= 1.59
BuildRequires:  libboost_test-devel >= 1.59
BuildRequires:  libboost_thread-devel >= 1.59
%endif
%if %{with armnn_caffe}
BuildRequires:  caffe-devel
%endif
%if %{with armnn_flatbuffers}
BuildRequires:  flatbuffers-devel
%if %{tf_version_2}
BuildRequires:  tensorflow2-lite-devel
%else
BuildRequires:  tensorflow-lite-devel
%endif
%endif
%if %{with compute_cl}
# Mesa-libOpenCl is required for tests
BuildRequires:  Mesa-libOpenCL
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-cpp-headers
%endif
%if %{with armnn_extra_tests}
%if 0%{?suse_version} > 1500
BuildRequires:  opencv3-devel
%else
BuildRequires:  opencv-devel
%endif
%endif
%if %{with armnn_onnx}
BuildRequires:  python3-onnx-devel
%endif
%if %{with armnn_tests}
BuildRequires:  stb-devel
%endif
%if %{with armnn_tf}
%if %{tf_version_2}
BuildRequires:  tensorflow2-devel
%else
BuildRequires:  tensorflow-devel
%endif
%endif
%if %{with compute_cl}
Recommends:     Mesa-libOpenCL
%endif
%if %{with armnn_flatbuffers}
Requires:       libarmnnSerializer%{version_major}%{?package_suffix} = %{version}
Requires:       libarmnnTfLiteParser%{version_major}%{?package_suffix} = %{version}
%endif
%if %{with armnn_caffe}
Requires:       libarmnnCaffeParser%{version_major}%{?package_suffix} = %{version}
%endif
%if %{with armnn_onnx}
Requires:       libarmnnOnnxParser%{version_major}%{?package_suffix} = %{version}
%endif
%if %{with armnn_tf}
Requires:       libarmnnTfParser%{version_major}%{?package_suffix} = %{version}
%endif
# Make sure we do not install both openCL and non-openCL (CPU only) versions.
%if "%{target}" == "opencl"
Conflicts:      armnn
%else
Conflicts:      armnn-opencl
%endif

%description
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow and Caffe, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

%package devel
Summary:        Development headers and libraries for armnn
# Make sure we do not install both openCL and non-openCL (CPU only) versions.
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libarmnn%{version_major}%{?package_suffix} = %{version}
# Make sure we do not install both openCL and non-openCL (CPU only) versions.
%if "%{target}" == "opencl"
Conflicts:      armnn-devel
%else
Conflicts:      armnn-opencl-devel
%endif
%if %{with armnn_flatbuffers}
Requires:       libarmnnSerializer%{version_major}%{?package_suffix} = %{version}
Requires:       libarmnnTfLiteParser%{version_major}%{?package_suffix} = %{version}
%endif
%if %{with armnn_caffe}
Requires:       libarmnnCaffeParser%{version_major}%{?package_suffix} = %{version}
%endif
%if %{with armnn_onnx}
Requires:       libarmnnOnnxParser%{version_major}%{?package_suffix} = %{version}
%endif
%if %{with armnn_tf}
Requires:       libarmnnTfParser%{version_major}%{?package_suffix} = %{version}
%endif

%description devel
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow and Caffe, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains the development libraries and headers for armnn.

%if %{with armnn_extra_tests}
%package -n %{name}-extratests
Summary:        Additionnal downstream tests for Arm NN
# Make sure we do not install both openCL and non-openCL (CPU only) versions.
Group:          Development/Libraries/C and C++
Requires:       %{name}
# Make sure we do not install both openCL and non-openCL (CPU only) versions.
%if "%{target}" == "opencl"
Conflicts:      armnn-extratests
%else
Conflicts:      armnn-opencl-extratests
%endif

%description -n %{name}-extratests
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow and Caffe, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains additionnal downstream tests for armnn.
%endif

%package -n libarmnn%{version_major}%{?package_suffix}
Summary:        libarmnn from armnn
Group:          Development/Libraries/C and C++
%if "%{target}" == "opencl"
Conflicts:      libarmnn%{version_major}
%else
Conflicts:      libarmnn%{version_major}-opencl
%endif

%description -n libarmnn%{version_major}%{?package_suffix}
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow and Caffe, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains the libarmnn library from armnn.

%if %{with armnn_flatbuffers}
%package -n libarmnnSerializer%{version_major}%{?package_suffix}
Summary:        libarmnnSerializer from armnn
Group:          Development/Libraries/C and C++
%if "%{target}" == "opencl"
Conflicts:      libarmnnSerializer%{version_major}
%else
Conflicts:      libarmnnSerializer%{version_major}-opencl
%endif

%description -n libarmnnSerializer%{version_major}%{?package_suffix}
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow and Caffe, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains the libarmnnSerializer library from armnn.

%package -n libarmnnTfLiteParser%{version_major}%{?package_suffix}
Summary:        libarmnnTfLiteParser from armnn
Group:          Development/Libraries/C and C++
%if "%{target}" == "opencl"
Conflicts:      libarmnnTfLiteParser%{version_major}
%else
Conflicts:      libarmnnTfLiteParser%{version_major}-opencl
%endif

%description -n libarmnnTfLiteParser%{version_major}%{?package_suffix}
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow and Caffe, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains the libarmnnTfLiteParser library from armnn.
%endif

%if %{with armnn_tf}
%package -n libarmnnTfParser%{version_major}%{?package_suffix}
Summary:        libarmnnTfParser from armnn
Group:          Development/Libraries/C and C++
%if "%{target}" == "opencl"
Conflicts:      libarmnnTfParser%{version_major}
%else
Conflicts:      libarmnnTfParser%{version_major}-opencl
%endif

%description -n libarmnnTfParser%{version_major}%{?package_suffix}
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow and Caffe, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains the libarmnnTfParser library from armnn.
%endif

%if %{with armnn_caffe}
%package -n libarmnnCaffeParser%{version_major}%{?package_suffix}
Summary:        libarmnnCaffeParser from armnn
Group:          Development/Libraries/C and C++
%if "%{target}" == "opencl"
Conflicts:      libarmnnCaffeParser%{version_major}
%else
Conflicts:      libarmnnCaffeParser%{version_major}-opencl
%endif

%description -n libarmnnCaffeParser%{version_major}%{?package_suffix}
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow and Caffe, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains the libarmnnCaffeParser library from armnn.
%endif

%if %{with armnn_onnx}
%package -n libarmnnOnnxParser%{version_major}%{?package_suffix}
Summary:        libarmnnOnnxParser from armnn
Group:          Development/Libraries/C and C++
%if "%{target}" == "opencl"
Conflicts:      libarmnnOnnxParser%{version_major}
%else
Conflicts:      libarmnnOnnxParser%{version_major}-opencl
%endif

%description -n libarmnnOnnxParser%{version_major}%{?package_suffix}
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow and Caffe, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains the libarmnnOnnxParser library from armnn.
%endif

%prep
%setup -q -n armnn-%{version}
%patch1 -p1
%patch200 -p1
%patch201 -p1
%patch202 -p1
%patch203 -p1
%patch204 -p1
%patch205 -p1
# Boost fixes for dynamic linking
sed -i 's/find_package(Boost 1.59 REQUIRED COMPONENTS unit_test_framework system filesystem program_options)/find_package(Boost 1.59 REQUIRED COMPONENTS unit_test_framework system filesystem log thread program_options)/' ./cmake/GlobalConfig.cmake


%build
%if %{with armnn_onnx}
mkdir onnx_deps
PROTO=$(find %{_libdir} -name onnx.proto)
protoc $PROTO --proto_path=. --proto_path=%{_includedir} --proto_path=$(dirname $(find %{_libdir} -name onnx)) --cpp_out=./onnx_deps
%endif
%if 0%{?suse_version} > 1500
export CXX_ADDITIONAL_FLAGS="$CXX_ADDITIONAL_FLAGS -Wno-error=deprecated-copy"
%endif
%if 0%{?sle_version} == 150200
%if %{with armnn_tf}
%if %{tf_version_2}
# TensorFlow2 in Leap 15.2 shows erros on major/minor due to '-Werror' option:
#   /usr/lib/python3.6/site-packages/tensorflow_core/include/tensorflow/core/protobuf/autotuning.pb.cc:930:13: error: In the GNU C Library, "major" is defined by <sys/sysmacros.h>.
#   For historical compatibility, it is currently defined by <sys/types.h> as well, but we plan to remove this soon. To use "major", include <sys/sysmacros.h> directly.
sed -i 's/-Werror//' ./cmake/GlobalConfig.cmake
%endif
%endif
%endif
%cmake \
  -DSHARED_BOOST=1 \
  -DCMAKE_CXX_FLAGS:STRING="%{optflags} -pthread $CXX_ADDITIONAL_FLAGS -Wno-error=implicit-fallthrough -Wno-error=unused-parameter" \
  -DBOOST_LIBRARYDIR=%{_libdir} \
%if %{with armnn_caffe}
  -DBUILD_CAFFE_PARSER=ON \
%else
  -DBUILD_CAFFE_PARSER=OFF \
%endif
  -DCAFFE_GENERATED_SOURCES=%{_includedir}/ \
%if %{with armnn_onnx}
  -DBUILD_ONNX_PARSER=ON \
  -DONNX_GENERATED_SOURCES=../onnx_deps/ \
%else
  -DBUILD_ONNX_PARSER=OFF \
%endif
%if %{with armnn_flatbuffers}
  -DBUILD_ARMNN_SERIALIZER=ON \
  -DFLATC_DIR=%{_bindir} \
  -DFLATBUFFERS_INCLUDE_PATH=%{_includedir} \
  -DBUILD_ARMNN_QUANTIZER=ON \
  -DBUILD_TF_LITE_PARSER=ON \
  -DTF_LITE_SCHEMA_INCLUDE_PATH=%{_includedir}/tensorflow/lite/schema/ \
%else
  -DBUILD_ARMNN_SERIALIZER=OFF \
  -DBUILD_ARMNN_QUANTIZER=OFF \
  -DBUILD_TF_LITE_PARSER=OFF \
%endif
%if %{with armnn_tf}
  -DBUILD_TF_PARSER=ON \
%if %{tf_version_2}
  -DTF_GENERATED_SOURCES=%{python3_sitelib}/tensorflow_core/include/ \
%else
  -DTF_GENERATED_SOURCES=%{python3_sitelib}/tensorflow/include/ \
%endif
%else
  -DBUILD_TF_PARSER=OFF \
%endif
%if %{with compute_neon} || %{with compute_cl}
  -DARMCOMPUTE_INCLUDE=%{_includedir} \
  -DHALF_INCLUDE=%{_includedir}/half \
  -DARMCOMPUTE_BUILD_DIR=%{_libdir} \
  -DARMCOMPUTE_ROOT=%{_prefix} \
%endif
%if %{with compute_neon}
  -DARMCOMPUTENEON=ON \
%else
  -DARMCOMPUTENEON=OFF \
%endif
%if %{with compute_cl}
  -DARMCOMPUTECL=ON \
  -DOPENCL_INCLUDE=%{_includedir} \
%else
  -DARMCOMPUTECL=OFF \
%endif
  -DTHIRD_PARTY_INCLUDE_DIRS=%{_includedir} \
%if %{with armnn_flatbuffers}
  -DBUILD_SAMPLE_APP=ON \
%else
  -DBUILD_SAMPLE_APP=OFF \
%endif
%if %{with armnn_tests}
  -DBUILD_UNIT_TESTS=ON \
  -DBUILD_TESTS=ON \
%else
  -DBUILD_UNIT_TESTS=OFF \
  -DBUILD_TESTS=OFF \
%endif
%if %{with armnn_extra_tests}
  -DBUILD_ARMNN_EXAMPLES=ON
%else
  -DBUILD_ARMNN_EXAMPLES=OFF
%endif

%if 0%{?suse_version} > 1500
%cmake_build
%else
%make_jobs
%endif
%if %{with armnn_tests}
pushd tests/
%if 0%{?suse_version} > 1500
%cmake_build
%else
%make_jobs
%endif
popd
%endif

%install
%cmake_install
%if %{with armnn_tests}
# Install tests manually
install -d %{buildroot}%{_bindir}
CP_ARGS="-Prf --preserve=mode,timestamps --no-preserve=ownership" \
find ./build/tests -maxdepth 1 -type f -executable -exec cp $CP_ARGS {} %{buildroot}%{_bindir} \;
%endif
%if %{with armnn_flatbuffers}
# Install Sample app
cp $CP_ARGS ./build/samples/SimpleSample %{buildroot}%{_bindir}
%if %{with armnn_tools}
# Install ArmNNConverter
cp $CP_ARGS ./build/ArmnnConverter %{buildroot}%{_bindir}
# Install ArmNNQuantizer
cp $CP_ARGS ./build/ArmnnQuantizer %{buildroot}%{_bindir}
%endif
%endif

# openCL UnitTests are failing in OBS due to the lack of openCL device
%if %{without compute_cl} && %{with armnn_tests}
%check
# Run tests
%if !%{tf_version_2}
# Skip some TF Lite tests because TensorFlow < 1.14 is used and make some tests failing
export UnitTestFlags="-t !TensorflowLiteParser/SliceSingleDim -t !TensorflowLiteParser/SliceD123 -t !TensorflowLiteParser/SliceD213 -t !TensorflowLiteParser/TransposeWithPermuteData -t !TensorflowLiteParser/TransposeWithoutPermuteDims"
%endif
LD_LIBRARY_PATH="$(pwd)/build/" \
./build/UnitTests $UnitTestFlags
%endif

%post -n libarmnn%{version_major}%{?package_suffix} -p /sbin/ldconfig
%postun -n libarmnn%{version_major}%{?package_suffix} -p /sbin/ldconfig

%if %{with armnn_flatbuffers}
%post -n libarmnnSerializer%{version_major}%{?package_suffix} -p /sbin/ldconfig
%postun -n libarmnnSerializer%{version_major}%{?package_suffix} -p /sbin/ldconfig

%post -n libarmnnTfLiteParser%{version_major}%{?package_suffix} -p /sbin/ldconfig
%postun -n libarmnnTfLiteParser%{version_major}%{?package_suffix} -p /sbin/ldconfig
%endif

%if %{with armnn_tf}
%post -n libarmnnTfParser%{version_major}%{?package_suffix} -p /sbin/ldconfig
%postun -n libarmnnTfParser%{version_major}%{?package_suffix} -p /sbin/ldconfig
%endif

%if %{with armnn_caffe}
%post -n libarmnnCaffeParser%{version_major}%{?package_suffix} -p /sbin/ldconfig
%postun -n libarmnnCaffeParser%{version_major}%{?package_suffix} -p /sbin/ldconfig
%endif

%if %{with armnn_onnx}
%post -n libarmnnOnnxParser%{version_major}%{?package_suffix} -p /sbin/ldconfig
%postun -n libarmnnOnnxParser%{version_major}%{?package_suffix} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%if %{with armnn_tests}
%{_bindir}/ExecuteNetwork
%if %{with armnn_caffe}
%{_bindir}/Caffe*-Armnn
%{_bindir}/MultipleNetworksCifar10
%endif
%if %{with armnn_flatbuffers}
%if %{with armnn_tools}
%{_bindir}/ArmnnConverter
%{_bindir}/ArmnnQuantizer
%endif
%{_bindir}/TfLite*-Armnn
%{_bindir}/Image*Generator
%endif
%if %{with armnn_onnx}
%{_bindir}/Onnx*-Armnn
%endif
%if %{with armnn_tf}
%{_bindir}/Tf*-Armnn
%endif
%if %{with armnn_flatbuffers}
%{_bindir}/SimpleSample
%endif
%endif

%if %{with armnn_extra_tests}
%files -n %{name}-extratests
%{_bindir}/ArmnnExamples
%endif

%files -n libarmnn%{version_major}%{?package_suffix}
%{_libdir}/libarmnn.so.*

%if %{with armnn_flatbuffers}
%files -n libarmnnSerializer%{version_major}%{?package_suffix}
%{_libdir}/libarmnnSerializer.so.*

%files -n libarmnnTfLiteParser%{version_major}%{?package_suffix}
%{_libdir}/libarmnnTfLiteParser.so.*
%endif

%if %{with armnn_tf}
%files -n libarmnnTfParser%{version_major}%{?package_suffix}
%{_libdir}/libarmnnTfParser.so.*
%endif

%if %{with armnn_caffe}
%files -n libarmnnCaffeParser%{version_major}%{?package_suffix}
%{_libdir}/libarmnnCaffeParser.so.*
%endif

%if %{with armnn_onnx}
%files -n libarmnnOnnxParser%{version_major}%{?package_suffix}
%{_libdir}/libarmnnOnnxParser.so.*
%endif

%files devel
%defattr(-,root,root)
%dir %{_includedir}/armnn/
%{_includedir}/armnn/*.hpp
%dir %{_includedir}/armnn/backends
%{_includedir}/armnn/backends/CMakeLists.txt
%{_includedir}/armnn/backends/*.hpp
%dir %{_includedir}/armnn/backends/profiling
%{_includedir}/armnn/backends/profiling/*.hpp
%dir %{_includedir}/armnn/profiling
%{_includedir}/armnn/profiling/*.hpp
%dir %{_includedir}/armnnUtils
%{_includedir}/armnnUtils/*.hpp
%dir %{_includedir}/armnnCaffeParser/
%{_includedir}/armnnCaffeParser/ICaffeParser.hpp
%dir %{_includedir}/armnnOnnxParser/
%{_includedir}/armnnOnnxParser/IOnnxParser.hpp
%dir %{_includedir}/armnnTfLiteParser/
%{_includedir}/armnnTfLiteParser/ITfLiteParser.hpp
%dir %{_includedir}/armnnTfParser/
%{_includedir}/armnnTfParser/ITfParser.hpp
%dir %{_includedir}/armnnDeserializer/
%{_includedir}/armnnDeserializer/IDeserializer.hpp
%dir %{_includedir}/armnnQuantizer
%{_includedir}/armnnQuantizer/INetworkQuantizer.hpp
%dir %{_includedir}/armnnSerializer/
%{_includedir}/armnnSerializer/ISerializer.hpp
%{_libdir}/libarmnn.so
%if %{with armnn_flatbuffers}
%{_libdir}/libarmnnSerializer.so
%{_libdir}/libarmnnTfLiteParser.so
%endif
%if %{with armnn_tf}
%{_libdir}/libarmnnTfParser.so
%endif
%if %{with armnn_caffe}
%{_libdir}/libarmnnCaffeParser.so
%endif
%if %{with armnn_onnx}
%{_libdir}/libarmnnOnnxParser.so
%endif

%changelog
