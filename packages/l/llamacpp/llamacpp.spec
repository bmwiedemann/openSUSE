#
# spec file for package llamacpp
#
# Copyright (c) 2025 SUSE LLC
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


Name:           llamacpp
Version:        4501
Release:        0
Summary:        llama-cli tool to run inference using the llama.cpp library
License:        MIT
URL:            https://github.com/ggerganov/llama.cpp
Source:         %{name}-%{version}.tar.gz
Patch0:         0001-dl-load-path.patch
Patch1:         0002-build-main-cli.patch
BuildRequires:  cmake >= 3.14
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  shaderc
BuildRequires:  pkgconfig(OpenCL)
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
Requires:       ggml-rt

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
Provides:       ggml-rt

%description -n libggml-cpu
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

This package includes the CPU backend for ggml.

%package -n libggml-vulkan
Summary:        A tensor library for C++ (Vulkan backend)
Provides:       ggml-rt

%description -n libggml-vulkan
A tensor library for C++. It was created originally to support llama.cpp
and WhisperCpp projects.

This package includes the Vulkan backend for ggml.

%package -n libggml-opencl
Summary:        A tensor library for C++ (OpenCL backend)
Provides:       ggml-rt

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

%prep
%autosetup -p1

%build
%define _lto_cflags %{nil}
%define __builder ninja

%cmake \
    -DCMAKE_SKIP_RPATH=ON \
    -DLLAMA_BUILD_TESTS=OFF \
    -DGGML_CPU=ON \
    -DGGML_VULKAN=ON \
    -DGGML_OPENCL=ON \
    -DGGML_OPENCL_USE_ADRENO_KERNELS=OFF \

%cmake_build

%install
%cmake_install

# used for shader compilation only
rm %{buildroot}%{_bindir}/vulkan-shaders-gen

# fix .pc file paths
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
mv %{buildroot}%{_prefix}/lib/pkgconfig/* %{buildroot}/%{_libdir}/pkgconfig/

# remove .py extension
mv %{buildroot}%{_bindir}/convert_hf_to_gguf.py %{buildroot}%{_bindir}/convert_hf_to_gguf

%files
%doc README.md
%license LICENSE

%{_bindir}/convert_hf_to_gguf

%{_bindir}/llama-cli
%{_bindir}/llama-server
%{_bindir}/llama-bench

%files -n libllama
%{_libdir}/libllama.so

%files -n libggml
%{_libdir}/libggml.so

%files -n libggml-base
%{_libdir}/libggml-base.so

%files -n libggml-cpu
%{_libdir}/libggml-cpu.so

%files -n libggml-vulkan
%{_libdir}/libggml-vulkan.so

%files -n libggml-opencl
%{_libdir}/libggml-opencl.so

%files devel
%{_includedir}/llama*
%{_libdir}/cmake/llama
%{_libdir}/pkgconfig/llama.pc

%files -n ggml-devel
%{_includedir}/ggml*.h
%{_includedir}/gguf.h

%changelog
