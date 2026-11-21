#
# spec file for package llamacpp
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2025 Eyad Issa <eyadlorenzo@gmail.com>
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


%global backend_dir %{_libdir}/ggml
%global upstream_build 12359
%global license_dir %{_datadir}/licenses

%global llama_sover        %{version}
%global llama_sover_suffix 1

%global mtmd_sover         %{llama_sover}
%global mtmd_sover_suffix  1

%global ggml_sover         1.0.0
%global ggml_sover_suffix  1
# PCI display controllers (class 03) from AMD and Intel, respectively.
# These broad matches do not guarantee backend support for every device.
%global amd_gpu_modalias   modalias(pci:v00001002d*sv*sd*bc03sc*i*)
%global intel_gpu_modalias modalias(pci:v00008086d*sv*sd*bc03sc*i*)

%if 0%{?suse_version} == 1500
%bcond_with opencl
%bcond_with openvino
%else
%bcond_without opencl
%ifarch x86_64 aarch64
%bcond_without openvino
%else
%bcond_with openvino
%endif
%endif

%if 0%{?suse_version} >= 1699
%ifarch x86_64
%bcond_without hip
%else
%bcond_with hip
%endif
%else
%bcond_with hip
%endif

%global gcc_version 0
%if 0%{?suse_version} == 1500
%global gcc_version 15
%else
%if 0%{?suse_version} >= 1600 && 0%{?suse_version} < 1699
%global gcc_version 16
%else
%ifarch aarch64
%if 0%{?suse_version} >= 1699
%global gcc_version 16
%endif
%endif
%endif
%endif

Name:           llamacpp
Version:        1.0.0
Release:        0
Summary:        Inference of Meta's LLaMA model (and others) in pure C/C++
License:        Apache-2.0 AND MIT AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MPL-2.0
URL:            https://github.com/ggml-org/llama.cpp
Source:         %{URL}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{URL}/releases/download/b%{upstream_build}/llama-b%{upstream_build}-ui.tar.gz
Source2:        llamacpp-third-party-licenses.txt
Source3:        LICENSE-Apache-2.0.txt
Source4:        LICENSE-MPL-2.0.txt
Patch0:         skip-sme-variants-when-unsupported.patch
%if %{with hip}
BuildRequires:  cmake >= 3.21
%else
BuildRequires:  cmake >= 3.19
%endif
%if %{gcc_version}
BuildRequires:  gcc%{gcc_version}-PIE
BuildRequires:  gcc%{gcc_version}-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  git
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  shaderc
BuildRequires:  spirv-headers
%if %{with opencl} || %{with openvino}
BuildRequires:  pkgconfig(OpenCL)
%endif
%if %{with opencl}
BuildRequires:  python3
BuildRequires:  pkgconfig(OpenCL-CLHPP)
%endif
%if %{with hip}
BuildRequires:  hipblas-devel
BuildRequires:  hipcc
BuildRequires:  rocblas-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
%endif
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libibverbs)
%if %{with openvino}
BuildRequires:  pkgconfig(openvino)
%endif
BuildRequires:  pkgconfig(vulkan)
# 32bit seems not to be supported anymore
ExcludeArch:    %{ix86} %{arm}

%description
The llama.cpp library provides a C++ interface for running inference
with large language models (LLMs). Initially designed to support Meta's
LLaMA model, it has since been extended to work with a variety of other models.

This package includes the llama-cli tool to run inference using the library.

%package devel
Summary:        Development files for llama.cpp
Requires:       ggml-devel = %{version}-%{release}
Requires:       libllama%{llama_sover_suffix} = %{version}-%{release}
Requires:       libllama-common%{llama_sover_suffix} = %{version}-%{release}
Requires:       libmtmd%{mtmd_sover_suffix} = %{version}-%{release}
Obsoletes:      libllama < 7266
Obsoletes:      libmtmd < 7266

%description devel
Headers, libraries and build configuration for developing
applications that use llama.cpp and its multimodal library.

%package -n libllama%{llama_sover_suffix}
Summary:        A C++ interface for running inference with large language models

%description -n libllama%{llama_sover_suffix}
The llama.cpp library provides a C++ interface for running inference
with large language models (LLMs). Initially designed to support Meta's
LLaMA model, it has since been extended to work with a variety of other models.

This package includes the shared libraries necessary for running applications
that depend on libllama.so.

%package -n libllama-common%{llama_sover_suffix}
Summary:        Common library for llama.cpp

%description -n libllama-common%{llama_sover_suffix}
The llama.cpp library provides a C++ interface for running inference
with large language models (LLMs). Initially designed to support Meta's
LLaMA model, it has since been extended to work with a variety of other models.

This package includes the shared libraries necessary for running applications
that depend on libllama-common.so.

%package -n libggml%{ggml_sover_suffix}
Summary:        A tensor library for C++
Requires:       libggml-cpu = %{version}-%{release}
%if %{with opencl}
Recommends:     libggml-opencl = %{version}-%{release}
%endif
Recommends:     libggml-vulkan = %{version}-%{release}

%description -n libggml%{ggml_sover_suffix}
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

%package -n libggml-base%{ggml_sover_suffix}
Summary:        A tensor library for C++ (base)

%description -n libggml-base%{ggml_sover_suffix}
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

This package includes the base shared library for ggml.

%package -n libggml-cpu
Summary:        A tensor library for C++ (CPU backend)
Requires:       libggml%{ggml_sover_suffix} = %{version}-%{release}
Requires:       libggml-base%{ggml_sover_suffix} = %{version}-%{release}

%description -n libggml-cpu
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

This package includes the CPU backend for ggml.

%package -n libggml-rpc
Summary:        RPC backend for ggml
Requires:       libggml%{ggml_sover_suffix} = %{version}-%{release}
Requires:       libggml-base%{ggml_sover_suffix} = %{version}-%{release}

%description -n libggml-rpc
The RPC backend for ggml provides access to remote compute devices
using TCP or RDMA.

%package -n ggml-rpc-server
Summary:        RPC server for ggml
Requires:       libggml-rpc = %{version}-%{release}

%description -n ggml-rpc-server
The ggml RPC server exposes local compute devices to remote ggml
clients over TCP or RDMA.

%package -n libggml-vulkan
Summary:        A tensor library for C++ (Vulkan backend)
Requires:       libggml%{ggml_sover_suffix} = %{version}-%{release}
Requires:       libggml-base%{ggml_sover_suffix} = %{version}-%{release}

%description -n libggml-vulkan
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

This package includes the Vulkan backend for ggml.

%if %{with opencl}
%package -n libggml-opencl
Summary:        A tensor library for C++ (OpenCL backend)
Requires:       libggml%{ggml_sover_suffix} = %{version}-%{release}
Requires:       libggml-base%{ggml_sover_suffix} = %{version}-%{release}

%description -n libggml-opencl
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

This package includes the OpenCL backend for ggml.
%endif

%if %{with hip}
%package -n libggml-hip
Summary:        A tensor library for C++ (HIP/ROCm backend)
Requires:       libggml%{ggml_sover_suffix} = %{version}-%{release}
Requires:       libggml-base%{ggml_sover_suffix} = %{version}-%{release}
Supplements:    (libggml%{ggml_sover_suffix} and %{amd_gpu_modalias})

%description -n libggml-hip
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

This package includes the HIP (AMD ROCm) backend for ggml.
%endif

%if %{with openvino}
%package -n libggml-openvino
Summary:        A tensor library for C++ (OpenVINO backend)
Requires:       libggml%{ggml_sover_suffix} = %{version}-%{release}
Requires:       libggml-base%{ggml_sover_suffix} = %{version}-%{release}
Supplements:    (libggml%{ggml_sover_suffix} and %{intel_gpu_modalias})

%description -n libggml-openvino
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

This package includes the OpenVINO backend for ggml.
%endif

%package -n ggml-devel
Summary:        Development files for ggml
Requires:       libggml%{ggml_sover_suffix} = %{version}-%{release}
Requires:       libggml-base%{ggml_sover_suffix} = %{version}-%{release}
Obsoletes:      libggml < 7266
Obsoletes:      libggml-base < 7266

%description -n ggml-devel
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

This package includes the development files necessary for building applications
that depend on ggml.

%package -n libmtmd%{mtmd_sover_suffix}
Summary:        Library to run multimodal inference models
Obsoletes:      libllava < 5402

%description -n libmtmd%{mtmd_sover_suffix}
As outlined in the history, libmtmd is the modern library designed to
replace the original llava.cpp implementation for handling multimodal inputs.

Built upon clip.cpp (similar to llava.cpp), libmtmd offers several advantages:
- Unified Interface: Aims to consolidate interaction for various multimodal models.
- Improved UX/DX: Features a more intuitive API, inspired by the Processor class
  in the Hugging Face transformers library.
- Flexibility: Designed to support multiple input types (text, audio, images) while
  respecting the wide variety of chat templates used by different models.

%ldconfig_scriptlets -n libllama%{llama_sover_suffix}
%ldconfig_scriptlets -n libllama-common%{llama_sover_suffix}
%ldconfig_scriptlets -n libggml%{ggml_sover_suffix}
%ldconfig_scriptlets -n libggml-base%{ggml_sover_suffix}
%ldconfig_scriptlets -n libmtmd%{mtmd_sover_suffix}

%prep
%autosetup -p1 -n llama.cpp-%{version}
mkdir -p tools/ui/dist
tar -xzf %{SOURCE1} --strip-components=1 -C tools/ui/dist
install -D -m 0644 %{SOURCE2} licenses/LICENSE-packaged-third-party
install -D -m 0644 %{SOURCE3} licenses/LICENSE-Apache-2.0.txt
install -D -m 0644 %{SOURCE4} licenses/LICENSE-MPL-2.0.txt

%build

%define _lto_cflags %{nil}
%define __builder ninja

%if %{gcc_version}
export CC=gcc-%{gcc_version}
export CXX=g++-%{gcc_version}
%endif

%cmake \
    -DCMAKE_SKIP_RPATH=ON \
    -DLLAMA_BUILD_TESTS=OFF \
    -DLLAMA_BUILD_EXAMPLES=OFF \
    -DLLAMA_BUILD_TOOLS=ON \
    -DLLAMA_CURL=ON \
    -DGGML_NATIVE=OFF \
    -DGGML_CPU=ON \
    -DGGML_CPU_ALL_VARIANTS=ON \
    -DGGML_RPC=ON \
    -DGGML_RPC_RDMA=ON \
    -DGGML_VULKAN=ON \
%if %{with hip}
    -DGGML_HIP=ON \
    -DAMDGPU_TARGETS=%{rocm_gpu_list_default} \
    -DCMAKE_HIP_FLAGS="--offload-compress" \
%else
    -DGGML_HIP=OFF \
%endif
%if %{with opencl}
    -DGGML_OPENCL=ON \
%else
    -DGGML_OPENCL=OFF \
%endif
%if %{with openvino}
    -DGGML_OPENVINO=ON \
%endif
    -DGGML_BACKEND_DL=ON \
    -DGGML_BACKEND_DIR="%{backend_dir}" \
    -DGGML_OPENCL_USE_ADRENO_KERNELS=OFF \
    -DLLAMA_BUILD_IS_DEV=OFF \
    -DLLAMA_BUILD_NUMBER=%{upstream_build} \
    -DLLAMA_VERSION="%{version}" \
    %{nil}

%cmake_build

%install
%cmake_install

for package in \
    %{name} \
    %{name}-devel \
    libllama%{llama_sover_suffix} \
    libllama-common%{llama_sover_suffix} \
    libggml%{ggml_sover_suffix} \
    libggml-base%{ggml_sover_suffix} \
    libggml-cpu \
    libggml-rpc \
    ggml-rpc-server \
    libggml-vulkan \
%if %{with opencl}
    libggml-opencl \
%endif
%if %{with hip}
    libggml-hip \
%endif
%if %{with openvino}
    libggml-openvino \
%endif
    ggml-devel \
    libmtmd%{mtmd_sover_suffix}
do
    install -D -m 0644 LICENSE \
        %{buildroot}%{license_dir}/$package/LICENSE
    install -D -m 0644 licenses/LICENSE-packaged-third-party \
        %{buildroot}%{license_dir}/$package/THIRD_PARTY_NOTICES
    install -D -m 0644 licenses/LICENSE-Apache-2.0.txt \
        %{buildroot}%{license_dir}/$package/LICENSE-Apache-2.0.txt
    install -D -m 0644 licenses/LICENSE-MPL-2.0.txt \
        %{buildroot}%{license_dir}/$package/LICENSE-MPL-2.0.txt
done

%files
%doc README.md
%dir %{license_dir}/%{name}
%license %{license_dir}/%{name}/LICENSE
%license %{license_dir}/%{name}/THIRD_PARTY_NOTICES
%license %{license_dir}/%{name}/LICENSE-Apache-2.0.txt
%license %{license_dir}/%{name}/LICENSE-MPL-2.0.txt
%{_bindir}/llama
%{_bindir}/llama-*
# private libraries
%{_libdir}/libllama-batched-bench-impl.so
%{_libdir}/libllama-bench-impl.so
%{_libdir}/libllama-cli-impl.so
%{_libdir}/libllama-completion-impl.so
%{_libdir}/libllama-fit-params-impl.so
%{_libdir}/libllama-perplexity-impl.so
%{_libdir}/libllama-quantize-impl.so
%{_libdir}/libllama-server-impl.so

%files devel
%dir %{license_dir}/%{name}-devel
%license %{license_dir}/%{name}-devel/LICENSE
%license %{license_dir}/%{name}-devel/THIRD_PARTY_NOTICES
%license %{license_dir}/%{name}-devel/LICENSE-Apache-2.0.txt
%license %{license_dir}/%{name}-devel/LICENSE-MPL-2.0.txt
%{_includedir}/llama*
%{_includedir}/mtmd*
%{_libdir}/cmake/llama
%{_libdir}/pkgconfig/llama.pc
# libllama symlinks
%{_libdir}/libllama.so
# libmtmd symlinks
%{_libdir}/libmtmd.so
# libllama-common symlinks
%{_libdir}/libllama-common.so

%files -n libllama%{llama_sover_suffix}
%dir %{license_dir}/libllama%{llama_sover_suffix}
%license %{license_dir}/libllama%{llama_sover_suffix}/LICENSE
%license %{license_dir}/libllama%{llama_sover_suffix}/THIRD_PARTY_NOTICES
%license %{license_dir}/libllama%{llama_sover_suffix}/LICENSE-Apache-2.0.txt
%license %{license_dir}/libllama%{llama_sover_suffix}/LICENSE-MPL-2.0.txt
%{_libdir}/libllama.so.%{llama_sover}
%{_libdir}/libllama.so.%{llama_sover_suffix}

%files -n libllama-common%{llama_sover_suffix}
%dir %{license_dir}/libllama-common%{llama_sover_suffix}
%license %{license_dir}/libllama-common%{llama_sover_suffix}/LICENSE
%license %{license_dir}/libllama-common%{llama_sover_suffix}/THIRD_PARTY_NOTICES
%license %{license_dir}/libllama-common%{llama_sover_suffix}/LICENSE-Apache-2.0.txt
%license %{license_dir}/libllama-common%{llama_sover_suffix}/LICENSE-MPL-2.0.txt
%{_libdir}/libllama-common.so.%{llama_sover}
%{_libdir}/libllama-common.so.%{llama_sover_suffix}

%files -n libggml%{ggml_sover_suffix}
%dir %{license_dir}/libggml%{ggml_sover_suffix}
%license %{license_dir}/libggml%{ggml_sover_suffix}/LICENSE
%license %{license_dir}/libggml%{ggml_sover_suffix}/THIRD_PARTY_NOTICES
%license %{license_dir}/libggml%{ggml_sover_suffix}/LICENSE-Apache-2.0.txt
%license %{license_dir}/libggml%{ggml_sover_suffix}/LICENSE-MPL-2.0.txt
%{_libdir}/libggml.so.%{ggml_sover}
%{_libdir}/libggml.so.%{ggml_sover_suffix}

%files -n libggml-base%{ggml_sover_suffix}
%dir %{license_dir}/libggml-base%{ggml_sover_suffix}
%license %{license_dir}/libggml-base%{ggml_sover_suffix}/LICENSE
%license %{license_dir}/libggml-base%{ggml_sover_suffix}/THIRD_PARTY_NOTICES
%license %{license_dir}/libggml-base%{ggml_sover_suffix}/LICENSE-Apache-2.0.txt
%license %{license_dir}/libggml-base%{ggml_sover_suffix}/LICENSE-MPL-2.0.txt
%{_libdir}/libggml-base.so.%{ggml_sover}
%{_libdir}/libggml-base.so.%{ggml_sover_suffix}

%files -n libggml-cpu
%dir %{license_dir}/libggml-cpu
%license %{license_dir}/libggml-cpu/LICENSE
%license %{license_dir}/libggml-cpu/THIRD_PARTY_NOTICES
%license %{license_dir}/libggml-cpu/LICENSE-Apache-2.0.txt
%license %{license_dir}/libggml-cpu/LICENSE-MPL-2.0.txt
%dir %{backend_dir}
%{backend_dir}/libggml-cpu-*.so

%files -n libggml-rpc
%dir %{license_dir}/libggml-rpc
%license %{license_dir}/libggml-rpc/LICENSE
%license %{license_dir}/libggml-rpc/THIRD_PARTY_NOTICES
%license %{license_dir}/libggml-rpc/LICENSE-Apache-2.0.txt
%license %{license_dir}/libggml-rpc/LICENSE-MPL-2.0.txt
%dir %{backend_dir}
%{backend_dir}/libggml-rpc.so

%files -n ggml-rpc-server
%dir %{license_dir}/ggml-rpc-server
%license %{license_dir}/ggml-rpc-server/LICENSE
%license %{license_dir}/ggml-rpc-server/THIRD_PARTY_NOTICES
%license %{license_dir}/ggml-rpc-server/LICENSE-Apache-2.0.txt
%license %{license_dir}/ggml-rpc-server/LICENSE-MPL-2.0.txt
%{_bindir}/ggml-rpc-server

%files -n libggml-vulkan
%dir %{license_dir}/libggml-vulkan
%license %{license_dir}/libggml-vulkan/LICENSE
%license %{license_dir}/libggml-vulkan/THIRD_PARTY_NOTICES
%license %{license_dir}/libggml-vulkan/LICENSE-Apache-2.0.txt
%license %{license_dir}/libggml-vulkan/LICENSE-MPL-2.0.txt
%dir %{backend_dir}
%{backend_dir}/libggml-vulkan.so

%if %{with opencl}
%files -n libggml-opencl
%dir %{license_dir}/libggml-opencl
%license %{license_dir}/libggml-opencl/LICENSE
%license %{license_dir}/libggml-opencl/THIRD_PARTY_NOTICES
%license %{license_dir}/libggml-opencl/LICENSE-Apache-2.0.txt
%license %{license_dir}/libggml-opencl/LICENSE-MPL-2.0.txt
%dir %{backend_dir}
%{backend_dir}/libggml-opencl.so
%endif

%if %{with hip}
%files -n libggml-hip
%dir %{license_dir}/libggml-hip
%license %{license_dir}/libggml-hip/LICENSE
%license %{license_dir}/libggml-hip/THIRD_PARTY_NOTICES
%license %{license_dir}/libggml-hip/LICENSE-Apache-2.0.txt
%license %{license_dir}/libggml-hip/LICENSE-MPL-2.0.txt
%dir %{backend_dir}
%{backend_dir}/libggml-hip.so
%endif

%if %{with openvino}
%files -n libggml-openvino
%dir %{license_dir}/libggml-openvino
%license %{license_dir}/libggml-openvino/LICENSE
%license %{license_dir}/libggml-openvino/THIRD_PARTY_NOTICES
%license %{license_dir}/libggml-openvino/LICENSE-Apache-2.0.txt
%license %{license_dir}/libggml-openvino/LICENSE-MPL-2.0.txt
%dir %{backend_dir}
%{backend_dir}/libggml-openvino.so
%endif

%files -n ggml-devel
%dir %{license_dir}/ggml-devel
%license %{license_dir}/ggml-devel/LICENSE
%license %{license_dir}/ggml-devel/THIRD_PARTY_NOTICES
%license %{license_dir}/ggml-devel/LICENSE-Apache-2.0.txt
%license %{license_dir}/ggml-devel/LICENSE-MPL-2.0.txt
%{_includedir}/ggml*.h
%{_includedir}/gguf.h
%{_libdir}/cmake/ggml
%{_libdir}/libggml.so
%{_libdir}/libggml-base.so

%files -n libmtmd%{mtmd_sover_suffix}
%dir %{license_dir}/libmtmd%{mtmd_sover_suffix}
%license %{license_dir}/libmtmd%{mtmd_sover_suffix}/LICENSE
%license %{license_dir}/libmtmd%{mtmd_sover_suffix}/THIRD_PARTY_NOTICES
%license %{license_dir}/libmtmd%{mtmd_sover_suffix}/LICENSE-Apache-2.0.txt
%license %{license_dir}/libmtmd%{mtmd_sover_suffix}/LICENSE-MPL-2.0.txt
%{_libdir}/libmtmd.so.%{mtmd_sover}
%{_libdir}/libmtmd.so.%{mtmd_sover_suffix}

%changelog
