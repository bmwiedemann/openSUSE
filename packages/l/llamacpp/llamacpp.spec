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
%global upstream_build 10964
%global license_dir %{_datadir}/licenses

%global llama_sover        %{version}
%global llama_sover_suffix 0

%global mtmd_sover         %{llama_sover}
%global mtmd_sover_suffix  0

%global ggml_sover         0.24.0
%global ggml_sover_suffix  0

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

Name:           llamacpp
Version:        0.4.1
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
Patch1:         fix-negative-top-n.patch
BuildRequires:  cmake >= 3.14
%if 0%{?suse_version} == 1500
BuildRequires:  gcc13-c++
%else
%ifarch aarch64
%if 0%{?suse_version} >= 1610
BuildRequires:  gcc16-c++
%else
BuildRequires:  gcc-c++
%endif
%else
BuildRequires:  gcc-c++
%endif
%endif
BuildRequires:  git
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  shaderc
BuildRequires:  spirv-headers
%if %{with opencl}
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(OpenCL-CLHPP)
%endif
BuildRequires:  pkgconfig(libcurl)
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
Obsoletes:      libllama < 7266
Obsoletes:      libmtmd < 7266

%description devel
Development files for llama.cpp

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
Requires:       libggml-cpu
%if %{with opencl}
Recommends:     libggml-opencl
%endif
Recommends:     libggml-vulkan

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

%description -n libggml-cpu
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

This package includes the CPU backend for ggml.

%package -n libggml-vulkan
Summary:        A tensor library for C++ (Vulkan backend)

%description -n libggml-vulkan
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

This package includes the Vulkan backend for ggml.

%if %{with opencl}
%package -n libggml-opencl
Summary:        A tensor library for C++ (OpenCL backend)

%description -n libggml-opencl
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

This package includes the OpenCL backend for ggml.
%endif

%if %{with openvino}
%package -n libggml-openvino
Summary:        A tensor library for C++ (OpenVINO backend)

%description -n libggml-openvino
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

This package includes the OpenVINO backend for ggml.
%endif

%package -n ggml-devel
Summary:        Development files for ggml
Obsoletes:      libggml < 7266
Obsoletes:      libggml-base < 7266

%description -n ggml-devel
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

This package includes the development files necessary for building applications
that depend on ggml.

%package -n libmtmd%{mtmd_sover_suffix}
Summary:        Library to run multimodals inference models

%description -n libmtmd%{mtmd_sover_suffix}
As outlined in the history, libmtmd is the modern library designed to
replace the original llava.cpp implementation for handling multimodal inputs.

Built upon clip.cpp (similar to llava.cpp), libmtmd offers several advantages:
- Unified Interface: Aims to consolidate interaction for various multimodal models.
- Improved UX/DX: Features a more intuitive API, inspired by the Processor class
  in the Hugging Face transformers library.
- Flexibility: Designed to support multiple input types (text, audio, images) while
  respecting the wide variety of chat templates used by different models.

%package -n libllava
Summary:        Library to run multimodals inference models

%description -n libllava
Library to handle multimodal inputs for llama.cpp.

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

%if 0%{?suse_version} == 1500
export CC=gcc-13
export CXX=g++-13
%else
%ifarch aarch64
%if 0%{?suse_version} >= 1610
export CC=gcc-16
export CXX=g++-16
%endif
%endif
%endif

mkdir -p %{_libdir}

%cmake \
    -DCMAKE_SKIP_RPATH=ON \
    -DLLAMA_BUILD_TESTS=OFF \
    -DLLAMA_BUILD_EXAMPLES=OFF \
    -DLLAMA_BUILD_TOOLS=ON \
    -DLLAMA_CURL=ON \
    -DGGML_NATIVE=OFF \
    -DGGML_CPU=ON \
    -DGGML_CPU_ALL_VARIANTS=ON \
    -DGGML_VULKAN=ON \
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
    libggml-vulkan \
%if %{with opencl}
    libggml-opencl \
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
%{_libdir}/libllama.so.0
# libmtmd symlinks
%{_libdir}/libmtmd.so
%{_libdir}/libmtmd.so.0
# libllama-common symlinks
%{_libdir}/libllama-common.so
%{_libdir}/libllama-common.so.0

%files -n libllama%{llama_sover_suffix}
%dir %{license_dir}/libllama%{llama_sover_suffix}
%license %{license_dir}/libllama%{llama_sover_suffix}/LICENSE
%license %{license_dir}/libllama%{llama_sover_suffix}/THIRD_PARTY_NOTICES
%license %{license_dir}/libllama%{llama_sover_suffix}/LICENSE-Apache-2.0.txt
%license %{license_dir}/libllama%{llama_sover_suffix}/LICENSE-MPL-2.0.txt
%{_libdir}/libllama.so.%{llama_sover}

%files -n libllama-common%{llama_sover_suffix}
%dir %{license_dir}/libllama-common%{llama_sover_suffix}
%license %{license_dir}/libllama-common%{llama_sover_suffix}/LICENSE
%license %{license_dir}/libllama-common%{llama_sover_suffix}/THIRD_PARTY_NOTICES
%license %{license_dir}/libllama-common%{llama_sover_suffix}/LICENSE-Apache-2.0.txt
%license %{license_dir}/libllama-common%{llama_sover_suffix}/LICENSE-MPL-2.0.txt
%{_libdir}/libllama-common.so.%{llama_sover}

%files -n libggml%{ggml_sover_suffix}
%dir %{license_dir}/libggml%{ggml_sover_suffix}
%license %{license_dir}/libggml%{ggml_sover_suffix}/LICENSE
%license %{license_dir}/libggml%{ggml_sover_suffix}/THIRD_PARTY_NOTICES
%license %{license_dir}/libggml%{ggml_sover_suffix}/LICENSE-Apache-2.0.txt
%license %{license_dir}/libggml%{ggml_sover_suffix}/LICENSE-MPL-2.0.txt
%{_libdir}/libggml.so.%{ggml_sover}

%files -n libggml-base%{ggml_sover_suffix}
%dir %{license_dir}/libggml-base%{ggml_sover_suffix}
%license %{license_dir}/libggml-base%{ggml_sover_suffix}/LICENSE
%license %{license_dir}/libggml-base%{ggml_sover_suffix}/THIRD_PARTY_NOTICES
%license %{license_dir}/libggml-base%{ggml_sover_suffix}/LICENSE-Apache-2.0.txt
%license %{license_dir}/libggml-base%{ggml_sover_suffix}/LICENSE-MPL-2.0.txt
%{_libdir}/libggml-base.so.%{ggml_sover}

%files -n libggml-cpu
%dir %{license_dir}/libggml-cpu
%license %{license_dir}/libggml-cpu/LICENSE
%license %{license_dir}/libggml-cpu/THIRD_PARTY_NOTICES
%license %{license_dir}/libggml-cpu/LICENSE-Apache-2.0.txt
%license %{license_dir}/libggml-cpu/LICENSE-MPL-2.0.txt
%dir %{backend_dir}
%{backend_dir}/libggml-cpu-*.so

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
%{_libdir}/libggml.so.0
%{_libdir}/libggml-base.so
%{_libdir}/libggml-base.so.0

%files -n libmtmd%{mtmd_sover_suffix}
%dir %{license_dir}/libmtmd%{mtmd_sover_suffix}
%license %{license_dir}/libmtmd%{mtmd_sover_suffix}/LICENSE
%license %{license_dir}/libmtmd%{mtmd_sover_suffix}/THIRD_PARTY_NOTICES
%license %{license_dir}/libmtmd%{mtmd_sover_suffix}/LICENSE-Apache-2.0.txt
%license %{license_dir}/libmtmd%{mtmd_sover_suffix}/LICENSE-MPL-2.0.txt
%{_libdir}/libmtmd.so.%{mtmd_sover}

%changelog
