#
# spec file for package armnn
#
# Copyright (c) 2024 SUSE LLC
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


# Disable LTO until UnitTests passes with LTO enabled - https://github.com/ARM-software/armnn/issues/623
%define _lto_cflags %{nil}

# Disable Python binding for now
%bcond_with PyArmnn

%define target @BUILD_FLAVOR@%{nil}
%if "%{target}" != ""
%define package_suffix -%{target}
%endif
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
# Extra tests require opencv(3)-devel, but it is broken for Leap 15.1 - boo#1154091
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
# FIXME: disabled for now, as it fails since version 21.05
%bcond_with armnn_extra_tests
%else
%bcond_with armnn_extra_tests
%endif
# flatbuffers-devel is available on Leap 15.2+/SLE15SP2+
# But tensorflow-lite >= 2.10 is only avaialble on Tumbleweed
%if 0%{?suse_version} > 1500
%bcond_without armnn_flatbuffers
%else
%bcond_with armnn_flatbuffers
%endif
# ONNX is available on Leap 15.2+/SLE15SP2+, but there is a compatibility issue
# with ONNX 1.7.0 in Tumbleweed - https://github.com/ARM-software/armnn/issues/419
%if 0%{?sle_version} >= 150200
%bcond_without armnn_onnx
%else
%bcond_with armnn_onnx
%endif
%define version_major 24
%define version_minor 05
%define version_lib 33
%define version_lib_testutils 3
%define version_lib_tfliteparser 24
%define version_lib_onnxparser 24
Name:           armnn%{?package_suffix}
Version:        %{version_major}.%{version_minor}
Release:        0
Summary:        Arm NN SDK enables machine learning workloads on power-efficient devices
License:        MIT
Group:          Development/Libraries/Other
URL:            https://developer.arm.com/products/processors/machine-learning/arm-nn
Source0:        https://github.com/ARM-software/armnn/archive/v%{version}.tar.gz#/armnn-%{version}.tar.gz
Source1:        armnn-rpmlintrc
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
Requires:       libarmnn%{version_lib}%{?package_suffix} = %{version}
ExcludeArch:    %ix86
%if 0%{?suse_version} < 1330
BuildRequires:  boost-devel >= 1.59
%else
BuildRequires:  libboost_filesystem-devel >= 1.59
BuildRequires:  libboost_program_options-devel >= 1.59
BuildRequires:  libboost_system-devel >= 1.59
BuildRequires:  libboost_test-devel >= 1.59
%if %{with armnn_extra_tests}
BuildRequires:  libboost_log-devel >= 1.59
BuildRequires:  libboost_thread-devel >= 1.59
%endif
%endif
%if %{with armnn_flatbuffers}
BuildRequires:  flatbuffers-devel
%if 0%{?suse_version} > 1550
BuildRequires:  tensorflow-lite-devel >= 2.10
%else
BuildRequires:  tensorflow2-lite-devel >= 2.10
%endif
%endif
%if %{with compute_cl}
# Mesa-libOpenCl is required for tests
BuildRequires:  Mesa-libOpenCL
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-cpp-headers
BuildRequires:  opencl-headers
%endif
%if %{with armnn_extra_tests}
%if 0%{?suse_version} > 1500
BuildRequires:  opencv3-devel
%else
BuildRequires:  opencv-devel
%endif
%endif
%if %{with armnn_onnx}
BuildRequires:  python3-onnx
%endif
%if %{with armnn_tests}
BuildRequires:  stb-devel
%endif
%if %{with PyArmnn}
BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  swig >= 4
%endif
%if %{with compute_cl}
Recommends:     Mesa-libOpenCL
%endif
%if %{with armnn_flatbuffers}
Requires:       libarmnnSerializer%{version_lib}%{?package_suffix} = %{version}
Requires:       libarmnnTfLiteParser%{version_lib_tfliteparser}%{?package_suffix} = %{version}
%endif
%if %{with armnn_onnx}
Requires:       libarmnnOnnxParser%{version_lib_onnxparser}%{?package_suffix} = %{version}
%endif
# Make sure we do not install both openCL and non-openCL (CPU only) versions.
%if "%{target}" == "opencl"
Conflicts:      armnn
%else
Conflicts:      armnn-opencl
%endif
ExclusiveArch:  aarch64 armv7l armv7hl x86_64

%description
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow Lite, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

%package devel
Summary:        Development headers and libraries for armnn
# Make sure we do not install both openCL and non-openCL (CPU only) versions.
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libarmnn%{version_lib}%{?package_suffix} = %{version}
Requires:       libarmnnBasePipeServer%{version_lib}%{?package_suffix} = %{version}
Requires:       libarmnnTestUtils%{version_lib_testutils}%{?package_suffix}
Requires:       libtimelineDecoder%{version_lib}%{?package_suffix} = %{version}
Requires:       libtimelineDecoderJson%{version_lib}%{?package_suffix} = %{version}
# Make sure we do not install both openCL and non-openCL (CPU only) versions.
%if "%{target}" == "opencl"
Conflicts:      armnn-devel
%else
Conflicts:      armnn-opencl-devel
%endif
%if %{with armnn_flatbuffers}
Requires:       libarmnnSerializer%{version_lib}%{?package_suffix} = %{version}
Requires:       libarmnnTfLiteParser%{version_lib_tfliteparser}%{?package_suffix} = %{version}
%endif
%if %{with armnn_onnx}
Requires:       libarmnnOnnxParser%{version_lib_onnxparser}%{?package_suffix} = %{version}
%endif

%description devel
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow Lite, allowing them to run efficiently – without
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
such as TensorFlow Lite, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains additionnal downstream tests for armnn.
%endif

%package -n libarmnn%{version_lib}%{?package_suffix}
Summary:        libarmnn from armnn
Group:          Development/Libraries/C and C++
%if "%{target}" == "opencl"
Conflicts:      libarmnn%{version_lib}
%else
Conflicts:      libarmnn%{version_lib}-opencl
%endif

%description -n libarmnn%{version_lib}%{?package_suffix}
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow Lite, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains the libarmnn library from armnn.

%package -n libarmnnBasePipeServer%{version_lib}%{?package_suffix}
Summary:        libarmnnBasePipeServer from armnn
Group:          Development/Libraries/C and C++
%if "%{target}" == "opencl"
Conflicts:      libarmnnBasePipeServer%{version_lib}
%else
Conflicts:      libarmnnBasePipeServer%{version_lib}-opencl
%endif

%description -n libarmnnBasePipeServer%{version_lib}%{?package_suffix}
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow Lite, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains the libarmnnBasePipeServer library from armnn.

%package -n libarmnnTestUtils%{version_lib_testutils}%{?package_suffix}
Summary:        libarmnnTestUtils from armnn
Group:          Development/Libraries/C and C++
%if "%{target}" == "opencl"
Conflicts:      libarmnnTestUtils%{version_lib_testutils}
%else
Conflicts:      libarmnnTestUtils%{version_lib_testutils}-opencl
%endif

%description -n libarmnnTestUtils%{version_lib_testutils}%{?package_suffix}
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow Lite, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains the libarmnnTestUtils library from armnn.

%package -n libtimelineDecoder%{version_lib}%{?package_suffix}
Summary:        libtimelineDecoder from armnn
Group:          Development/Libraries/C and C++
%if "%{target}" == "opencl"
Conflicts:      libtimelineDecoder%{version_lib}
%else
Conflicts:      libtimelineDecoder%{version_lib}-opencl
%endif

%description -n libtimelineDecoder%{version_lib}%{?package_suffix}
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow Lite, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains the libtimelineDecoder library from armnn.

%package -n libtimelineDecoderJson%{version_lib}%{?package_suffix}
Summary:        libtimelineDecoderJson from armnn
Group:          Development/Libraries/C and C++
%if "%{target}" == "opencl"
Conflicts:      libtimelineDecoderJson%{version_lib}
%else
Conflicts:      libtimelineDecoderJson%{version_lib}-opencl
%endif

%description -n libtimelineDecoderJson%{version_lib}%{?package_suffix}
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow Lite, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains the libtimelineDecoder library from armnn.

%if %{with armnn_flatbuffers}
%package -n libarmnnSerializer%{version_lib}%{?package_suffix}
Summary:        libarmnnSerializer from armnn
Group:          Development/Libraries/C and C++
%if "%{target}" == "opencl"
Conflicts:      libarmnnSerializer%{version_lib}
%else
Conflicts:      libarmnnSerializer%{version_lib}-opencl
%endif

%description -n libarmnnSerializer%{version_lib}%{?package_suffix}
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow Lite, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains the libarmnnSerializer library from armnn.

%package -n libarmnnTfLiteParser%{version_lib_tfliteparser}%{?package_suffix}
Summary:        libarmnnTfLiteParser from armnn
Group:          Development/Libraries/C and C++
%if "%{target}" == "opencl"
Conflicts:      libarmnnTfLiteParser%{version_lib_tfliteparser}
%else
Conflicts:      libarmnnTfLiteParser%{version_lib_tfliteparser}-opencl
%endif

%description -n libarmnnTfLiteParser%{version_lib_tfliteparser}%{?package_suffix}
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow Lite, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains the libarmnnTfLiteParser library from armnn.
%endif

%if %{with armnn_onnx}
%package -n libarmnnOnnxParser%{version_lib_onnxparser}%{?package_suffix}
Summary:        libarmnnOnnxParser from armnn
Group:          Development/Libraries/C and C++
%if "%{target}" == "opencl"
Conflicts:      libarmnnOnnxParser%{version_lib_onnxparser}
%else
Conflicts:      libarmnnOnnxParser%{version_lib_onnxparser}-opencl
%endif

%description -n libarmnnOnnxParser%{version_lib_onnxparser}%{?package_suffix}
Arm NN is an inference engine for CPUs, GPUs and NPUs.
It bridges the gap between existing NN frameworks and the underlying IP.
It enables efficient translation of existing neural network frameworks,
such as TensorFlow Lite, allowing them to run efficiently – without
modification – across Arm Cortex CPUs and Arm Mali GPUs.

This package contains the libarmnnOnnxParser library from armnn.
%endif

%prep
%setup -q -n armnn-%{version}
%if %{with armnn_extra_tests}
%patch -P 200 -p1
%patch -P 201 -p1
%patch -P 202 -p1
%patch -P 203 -p1
%patch -P 204 -p1
%patch -P 205 -p1
# Add Boost log as downstream extra test requires it
sed -i 's/ find_package(Boost 1.59 REQUIRED COMPONENTS unit_test_framework)/find_package(Boost 1.59 REQUIRED COMPONENTS unit_test_framework filesystem system log program_options)/' ./cmake/GlobalConfig.cmake
%endif

%build
%if %{with armnn_onnx}
mkdir onnx_deps
PROTO=$(find %{_libdir} -name onnx.proto)
protoc $PROTO --proto_path=. --proto_path=%{_includedir} --proto_path=$(dirname $(find %{_libdir} -name onnx)) --cpp_out=./onnx_deps
%endif
%cmake \
  -DCMAKE_SKIP_RPATH=True \
  -DSHARED_BOOST=1 \
  -DCMAKE_CXX_FLAGS:STRING="%{optflags} -pthread -Wno-error=unused-result" \
  -DBOOST_LIBRARYDIR=%{_libdir} \
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
  -DBUILD_TF_LITE_PARSER=ON \
  -DTfLite_Schema_INCLUDE_PATH=%{_includedir}/tensorflow/lite/schema/ \
  -DTF_LITE_SCHEMA_INCLUDE_PATH=%{_includedir}/tensorflow/lite/schema/ \
%else
  -DBUILD_ARMNN_SERIALIZER=OFF \
  -DBUILD_TF_LITE_PARSER=OFF \
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
%if %{with PyArmnn}
  -DBUILD_PYTHON_WHL=ON \
  -DBUILD_PYTHON_SRC=ON \
%else
  -DBUILD_PYTHON_WHL=OFF \
  -DBUILD_PYTHON_SRC=OFF \
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
%endif
# Drop static libs - https://github.com/ARM-software/armnn/issues/514
rm -f  %{buildroot}%{_libdir}/*.a

# openCL UnitTests are failing in OBS due to the lack of openCL device
%if %{without compute_cl} && %{with armnn_tests}
%check
# Run tests
LD_LIBRARY_PATH="$(pwd)/build/" \
./build/UnitTests $UnitTestFlags
%endif

%post -n libarmnn%{version_lib}%{?package_suffix} -p /sbin/ldconfig
%postun -n libarmnn%{version_lib}%{?package_suffix} -p /sbin/ldconfig

%post -n libarmnnBasePipeServer%{version_lib}%{?package_suffix} -p /sbin/ldconfig
%postun -n libarmnnBasePipeServer%{version_lib}%{?package_suffix} -p /sbin/ldconfig

%post -n libarmnnTestUtils%{version_lib_testutils}%{?package_suffix} -p /sbin/ldconfig
%postun -n libarmnnTestUtils%{version_lib_testutils}%{?package_suffix} -p /sbin/ldconfig

%post -n libtimelineDecoderJson%{version_lib}%{?package_suffix} -p /sbin/ldconfig
%postun -n libtimelineDecoderJson%{version_lib}%{?package_suffix} -p /sbin/ldconfig

%post -n libtimelineDecoder%{version_lib}%{?package_suffix} -p /sbin/ldconfig
%postun -n libtimelineDecoder%{version_lib}%{?package_suffix} -p /sbin/ldconfig

%if %{with armnn_flatbuffers}
%post -n libarmnnSerializer%{version_lib}%{?package_suffix} -p /sbin/ldconfig
%postun -n libarmnnSerializer%{version_lib}%{?package_suffix} -p /sbin/ldconfig

%post -n libarmnnTfLiteParser%{version_lib_tfliteparser}%{?package_suffix} -p /sbin/ldconfig
%postun -n libarmnnTfLiteParser%{version_lib_tfliteparser}%{?package_suffix} -p /sbin/ldconfig
%endif

%if %{with armnn_onnx}
%post -n libarmnnOnnxParser%{version_lib_onnxparser}%{?package_suffix} -p /sbin/ldconfig
%postun -n libarmnnOnnxParser%{version_lib_onnxparser}%{?package_suffix} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%if %{with armnn_tests}
%{_bindir}/ExecuteNetwork
%if %{with armnn_flatbuffers}
%{_bindir}/ArmnnConverter
%{_bindir}/TfLite*-Armnn
%endif
%if %{with armnn_onnx}
%{_bindir}/Onnx*-Armnn
%endif
%if %{with armnn_flatbuffers}
%{_bindir}/SimpleSample
%endif
%endif

%if %{with armnn_extra_tests}
%files -n %{name}-extratests
%{_bindir}/ArmnnExamples
%endif

%files -n libarmnn%{version_lib}%{?package_suffix}
%{_libdir}/libarmnn.so.*

%files -n libarmnnBasePipeServer%{version_lib}%{?package_suffix}
%{_libdir}/libarmnnBasePipeServer.so.*

%files -n libarmnnTestUtils%{version_lib_testutils}%{?package_suffix}
%{_libdir}/libarmnnTestUtils.so.*

%files -n libtimelineDecoder%{version_lib}%{?package_suffix}
%{_libdir}/libtimelineDecoder.so.*

%files -n libtimelineDecoderJson%{version_lib}%{?package_suffix}
%{_libdir}/libtimelineDecoderJson.so.*

%if %{with armnn_flatbuffers}
%files -n libarmnnSerializer%{version_lib}%{?package_suffix}
%{_libdir}/libarmnnSerializer.so.*

%files -n libarmnnTfLiteParser%{version_lib_tfliteparser}%{?package_suffix}
%{_libdir}/libarmnnTfLiteParser.so.*
%endif

%if %{with armnn_onnx}
%files -n libarmnnOnnxParser%{version_lib_onnxparser}%{?package_suffix}
%{_libdir}/libarmnnOnnxParser.so.*
%endif

%files devel
%defattr(-,root,root)
%dir %{_includedir}/armnn/
%{_includedir}/armnn/*.hpp
%dir %{_includedir}/armnn/backends
%{_includedir}/armnn/backends/CMakeLists.txt
%{_includedir}/armnn/backends/*.hpp
%dir %{_includedir}/armnn/profiling
%{_includedir}/armnn/profiling/*.hpp
%dir %{_includedir}/armnn/profiling/client/
%dir %{_includedir}/armnn/profiling/client/include/
%{_includedir}/armnn/profiling/client/include/*.hpp
%dir %{_includedir}/armnn/profiling/client/include/backends/
%{_includedir}/armnn/profiling/client/include/backends/*.hpp
%dir %{_includedir}/armnn/profiling/common/
%dir %{_includedir}/armnn/profiling/common/include/
%{_includedir}/armnn/profiling/common/include/*.hpp
%dir %{_includedir}/armnn/utility
%{_includedir}/armnn/utility/*.hpp
%dir %{_includedir}/armnnUtils
%{_includedir}/armnnUtils/*.hpp
%dir %{_includedir}/armnnOnnxParser/
%{_includedir}/armnnOnnxParser/*.hpp
%dir %{_includedir}/armnnTfLiteParser/
%{_includedir}/armnnTfLiteParser/*.hpp
%dir %{_includedir}/armnnDeserializer/
%{_includedir}/armnnDeserializer/IDeserializer.hpp
%dir %{_includedir}/armnnSerializer/
%{_includedir}/armnnSerializer/ISerializer.hpp
%dir %{_includedir}/armnnTestUtils/
%{_includedir}/armnnTestUtils/*.hpp
%dir %{_libdir}/cmake/armnn
%{_libdir}/cmake/armnn/*
%{_libdir}/libarmnn.so
%{_libdir}/libarmnnBasePipeServer.so
%{_libdir}/libtimelineDecoder.so
%{_libdir}/libtimelineDecoderJson.so
%if %{with armnn_flatbuffers}
%{_libdir}/libarmnnSerializer.so
%{_libdir}/libarmnnTfLiteParser.so
%endif
%{_libdir}/libarmnnTestUtils.so
%if %{with armnn_onnx}
%{_libdir}/libarmnnOnnxParser.so
%endif

%changelog
