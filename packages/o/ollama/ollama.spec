#
# spec file for package ollama
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?is_opensuse}
%{bcond_with cuda}
%else
%{bcond_without cuda}
%endif
%{bcond_with rocm}

%if 0%{?sle_version} && 0%{?sle_version} >= 150600
%global force_gcc_version 12
%endif
%if 0%{?suse_version} >= 1699
%global force_gcc_version 14
%endif

%define cuda_version_major 13
%define cuda_version_minor 0
%define cuda_version %{cuda_version_major}-%{cuda_version_minor}

Name:           ollama
Version:        0.12.10
Release:        0
Summary:        Tool for running AI models on-premise
License:        MIT
URL:            https://ollama.com
Source:         https://github.com/ollama/ollama/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zstd
Source2:        %{name}.service
Source3:        %{name}-user.conf
Source4:        sysconfig.%{name}
BuildRequires:  cmake >= 3.24
BuildRequires:  git-core
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  shaderc
BuildRequires:  sysuser-tools
BuildRequires:  zstd
BuildRequires:  golang(API) >= 1.24
BuildRequires:  group(render)
BuildRequires:  group(video)
BuildRequires:  pkgconfig(vulkan)
Requires:       group(render)
Requires:       group(video)
Recommends:     ( %{name}-vulkan or %{name}-cuda or %{name}-rocm )
%if %{with cuda}
# requires cuda-toolkit*-config-common, cuda-cudart, cuda-cccl
BuildRequires:  cuda-cudart-devel-%{cuda_version}
BuildRequires:  cuda-driver-devel-%{cuda_version}
# requires cuda-crt, cuda-nvvm
BuildRequires:  cuda-nvcc-%{cuda_version}
# requires libcublas
BuildRequires:  libcublas-devel-%{cuda_version}
%endif
%if %{with rocm}
BuildRequires:  hipblas-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocminfo
%endif

Requires(pre):  %fillup_prereq
# 32bit seems not to be supported anymore while riscv isn't yet.
ExcludeArch:    %{ix86} %{arm} riscv64
%sysusers_requires
%if 0%{?force_gcc_version}
BuildRequires:  gcc%{force_gcc_version}-c++
%endif
%if 0%{suse_version} >= 1600
BuildRequires:  gcc-c++ >= 11.4.0
%else
BuildRequires:  gcc14-c++
%endif

%description
Ollama is a tool for running AI models on one's own hardware.
It offers a command-line interface and a RESTful API.
New models can be created or existing ones modified in the
Ollama library using the Modelfile syntax.
Source model weights found on Hugging Face and similar sites
can be imported.

%package vulkan
Summary:        Ollama Module using Vulkan

%description vulkan
Ollama plugin module using Vulkan.

%package cuda
Summary:        Ollama Module using CUDA

%description cuda
Ollama plugin module using NVIDIA CUDA.

%package rocm
Summary:        Ollama Module using AMD ROCm

%description rocm
Ollama plugin module for ROCm.

%prep
%autosetup -a1 -p1 -n %{name}-%{version}

%build
%define __builder ninja

%sysusers_generate_pre %{SOURCE3} %{name} %{name}-user.conf

export GOFLAGS="-buildmode=pie -mod=vendor"
export CXX="g++%{?force_gcc_version:-%force_gcc_version}"
export CC="gcc%{?force_gcc_version:-%force_gcc_version}"
export GOFLAGS="-mod=vendor -v"

%if %{with cuda}
export PATH=/usr/local/cuda-%{cuda_version_major}.%{cuda_version_minor}/bin:$PATH
export LIBRARY_PATH=/usr/local/cuda/lib64/stubs
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/cuda/lib64
export LDFLAGS=-s
export GOFLAGS="${GOFLAGS} '-ldflags=-w -s -X=github.com/ollama/ollama/version.Version=%{version} -X=github.com/ollama/ollama/server.mode=release\'"
export CGO_ENABLED=1
# NOTE: NVIDIA compiler (nvcc) will look for the default g++ so we
# have to set it to g++12 explicitly
export CUDAHOSTCXX=/usr/bin/g++%{?force_gcc_version:-%{force_gcc_version}}
%endif

# fix CMAKE_BINARY_DIR / OLLAMA_INSTALL_DIR location
sed -i -e 's@\(${CMAKE_BINARY_DIR}\)/lib/ollama@\1/%{_lib}/ollama@' CMakeLists.txt
sed -i -e 's@\(${CMAKE_INSTALL_PREFIX}\)/lib/ollama@\1/%{_lib}/ollama@' CMakeLists.txt
# overwrite ml/path.go so LibOllamaPath is set to our path
echo -e 'package ml\nvar LibOllamaPath string = "/usr/%{_lib}/ollama"' > ml/path.go
# for dlopens
sed -i -e 's@"lib"@"%{_lib}"@' \
    -e 's@"lib/ollama"@"%{_lib}/ollama"@' \
    ml/backend/ggml/ggml/src/ggml.go

%cmake \
    -UOLLAMA_INSTALL_DIR -DOLLAMA_INSTALL_DIR=%{_libdir}/ollama \
    -UCMAKE_INSTALL_BINDIR -DCMAKE_INSTALL_BINDIR=%{_libdir}/ollama \
    -DGGML_BACKEND_DIR=%{_libdir}/ollama \
    %{?with_cuda:-DCMAKE_CUDA_COMPILER=/usr/local/cuda-%{cuda_version_major}.%{cuda_version_minor}/bin/nvcc} \
    %{?with_rocm:-DCMAKE_HIP_COMPILER=%rocmllvm_bindir/clang++ \
       -DAMDGPU_TARGETS=%{rocm_gpu_list_default}} \
    %{nil}
%cmake_build

cd ..
go build -trimpath -o %{name} .

%install
%cmake_install
install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}-user.conf
install -D -m 0644 %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -d %{buildroot}%{_localstatedir}/lib/%{name}
mkdir -p %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}

mkdir -p "%{buildroot}/%{_docdir}/%{name}"
cp -Ra docs/* "%{buildroot}/%{_docdir}/%{name}"
# remove copies of system libraries
shopt -s nullglob
rm -rf %{buildroot}%{_libdir}/%{name}/lib{vulkan,drm,amd,hip,cu,hsa,roc,numa,elf}*

%check
%if 0%{?force_gcc_version}
export CXX="g++-%{?force_gcc_version}"
export CC="gcc-%{?force_gcc_version}"
# pie doesn't work with gcc12 on leap
export GOFLAGS="-mod=vendor"
%endif
go test -v ./...

%pre -f %{name}.pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%fillup_only

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README.md
%license LICENSE
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}-user.conf
%exclude %{_libdir}/ollama/libggml-cuda.so
%exclude %{_libdir}/ollama/libggml-hip.so
%exclude %{_libdir}/ollama/libggml-vulkan.so
%{_fillupdir}/sysconfig.%{name}
%attr(-, ollama, ollama) %{_localstatedir}/lib/%{name}

%files vulkan
%{_libdir}/ollama/libggml-vulkan.so

%if %{with cuda}
%files cuda
%{_libdir}/ollama/libggml-cuda.so
%endif

%if %{with rocm}
%files rocm
%{_libdir}/ollama/libggml-hip.so
%endif

%changelog
