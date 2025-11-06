#
# spec file for package llamacpp
#
# Copyright (c) 2025 SUSE LLC and contributors
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

Name:           llamacpp
Version:        6937
Release:        0
Summary:        Inference of Meta's LLaMA model (and others) in pure C/C++
License:        MIT
URL:            https://github.com/ggml-org/llama.cpp
Source:         %{URL}/archive/b%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.14
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  shaderc
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(libcurl)
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

%description devel
Development files for llama.cpp

%package -n libllama
Summary:        A C++ interface for running inference with large language models

%description -n libllama
The llama.cpp library provides a C++ interface for running inference
with large language models (LLMs). Initially designed to support Meta's
LLaMA model, it has since been extended to work with a variety of other models.

This package includes the shared libraries necessary for running applications
that depend on libllama.so.

%package -n libggml
Summary:        A tensor library for C++
Requires:       libggml-cpu
Recommends:     libggml-opencl
Recommends:     libggml-vulkan

%description -n libggml
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

%package -n libggml-base
Summary:        A tensor library for C++ (base)

%description -n libggml-base
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

%package -n libggml-opencl
Summary:        A tensor library for C++ (OpenCL backend)

%description -n libggml-opencl
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

This package includes the OpenCL backend for ggml.

%package -n ggml-devel
Summary:        Development files for ggml

%description -n ggml-devel
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

This package includes the development files necessary for building applications
that depend on ggml.

%package -n libmtmd
Summary:        Library to run multimodals inference models

%description -n libmtmd
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

%prep
%autosetup -p1 -n llama.cpp-b%{version}

%build

%define _lto_cflags %{nil}
%define __builder ninja

mkdir -p %{_libdir}

%cmake \
    -DCMAKE_SKIP_RPATH=ON \
    -DLLAMA_BUILD_TESTS=OFF \
    -DLLAMA_BUILD_EXAMPLES=OFF \
    -DLLAMA_BUILD_TOOLS=ON \
    -DLLAMA_CURL=ON \
    -DGGML_NATIVE=OFF \
    -DGGML_CPU=ON \
    -DGGML_VULKAN=ON \
    -DGGML_OPENCL=ON \
    -DGGML_BACKEND_DL=ON \
    -DGGML_BACKEND_DIR="%{backend_dir}" \
    -DGGML_OPENCL_USE_ADRENO_KERNELS=OFF \
    -DLLAMA_BUILD_NUMBER=%{version} \
    -DLLAMA_VERSION="0.0.%{version}" \
    %{nil}

%cmake_build

%install
%cmake_install

# dev scripts
rm %{buildroot}%{_bindir}/convert_hf_to_gguf.py

%files
%doc README.md
%license LICENSE
%{_bindir}/llama-*

%files devel
%license LICENSE
%{_includedir}/llama*
%{_includedir}/mtmd*
%{_libdir}/cmake/llama
%{_libdir}/pkgconfig/llama.pc

%files -n libllama
%license LICENSE
%{_libdir}/libllama.so

%files -n libggml
%license LICENSE
%{_libdir}/libggml.so

%files -n libggml-base
%license LICENSE
%{_libdir}/libggml-base.so

%files -n libggml-cpu
%license LICENSE
%dir %{backend_dir}
%{backend_dir}/libggml-cpu.so

%files -n libggml-vulkan
%license LICENSE
%dir %{backend_dir}
%{backend_dir}/libggml-vulkan.so

%files -n libggml-opencl
%license LICENSE
%dir %{backend_dir}
%{backend_dir}/libggml-opencl.so

%files -n ggml-devel
%license LICENSE
%{_includedir}/ggml*.h
%{_includedir}/gguf.h
%{_libdir}/cmake/ggml

%files -n libmtmd
%license LICENSE
%{_libdir}/libmtmd.so

%changelog
