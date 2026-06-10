#
# spec file for package ollama
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{bcond_with rocm}
%{bcond_with cuda}
%if 0%{?suse_version} >= 1610
%{bcond_without vulkan}
%else
%{bcond_with vulkan}
%endif

%global flavor @BUILD_FLAVOR@%{nil}
%global preset_flavor %flavor

%if "%{flavor}" == "cuda"
%global preset_flavor cuda-v13
%if %{with cuda}
ExclusiveArch:  x86_64
%else
ExclusiveArch:  SKIP_IT
%endif
%endif

%if "%{flavor}" == "rocm"
%global preset_flavor rocm_v7_2_linux
%if %{with rocm}
ExclusiveArch:  x86_64
%else
ExclusiveArch:  SKIP_IT
%endif
%endif

%ifarch aarch64
%if 0%{?suse_version} <= 1600
# the compiler is too old for aarch64 here
ExclusiveArch:  SKIP_IT
%endif
%endif

%if 0%{?sle_version} && 0%{?sle_version} >= 150600
%global force_gcc_version 12
%endif

%if 0%{?suse_version} >= 1601
%global force_gcc_version 15
%endif

%define cuda_version_major 13
%define cuda_version_minor 0
%define cuda_version %{cuda_version_major}-%{cuda_version_minor}

Name:           ollama
Version:        0.30.6
Release:        0
Summary:        Tool for running AI models on-premise
License:        MIT
URL:            https://ollama.com
Source:         https://github.com/ollama/ollama/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zstd
Source2:        %{name}.service
Source3:        %{name}-user.conf
Source4:        sysconfig.%{name}
Source5:        %{name}-rpmlintrc
Source10:       llama.cpp-main.tar.xz
Source11:       mlx-main.tar.xz
Source12:       mlx-c-main.tar.xz
Patch0:         fix-mlxrunner-tests.diff
Patch1:         disable-llama.cpp-ui.patch
BuildRequires:  ccache
BuildRequires:  cmake >= 3.24
BuildRequires:  git-core
BuildRequires:  ninja
BuildRequires:  patchelf
BuildRequires:  pkgconfig
BuildRequires:  shaderc
BuildRequires:  sysuser-tools
BuildRequires:  zstd
BuildRequires:  golang(API) >= 1.26
BuildRequires:  group(render)
BuildRequires:  group(video)
Requires:       group(render)
Requires:       group(video)
Recommends:     ( %{name}-vulkan or %{name}-cuda or %{name}-rocm )

%if "%{flavor}" == "test"
%global debug_package %{nil}
BuildRequires:  ollama
%if %{with vulkan}
BuildRequires:  ollama-vulkan
%endif
%if %{with rocm}
BuildRequires:  ollama-rocm
%endif
%if %{with cuda}
BuildRequires:  ollama-cuda
%endif
%endif

%if "%{flavor}" == "vulkan"
BuildRequires:  glslang-devel
BuildRequires:  spirv-headers
BuildRequires:  pkgconfig(vulkan)
%endif

%if "%{flavor}" == "cuda" || "%{flavor}" == "mlx_cuda"
# requires cuda-toolkit*-config-common, cuda-cudart, cuda-cccl
BuildRequires:  cuda-cudart-devel-%{cuda_version}
BuildRequires:  cuda-driver-devel-%{cuda_version}
# requires cuda-crt, cuda-nvvm
BuildRequires:  cuda-nvcc-%{cuda_version}
# requires libcublas
BuildRequires:  libcublas-devel-%{cuda_version}
%endif

%if "%{flavor}" == "rocm"
BuildRequires:  hipblas-common-devel
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
Requires:       %{name} = %{version}-%{release}

%description vulkan
Ollama plugin module using Vulkan.

%package cuda
Summary:        Ollama Module using CUDA
Requires:       %{name} = %{version}-%{release}

%description cuda
Ollama plugin module using NVIDIA CUDA.

%package rocm
Summary:        Ollama Module using AMD ROCm
Requires:       %{name} = %{version}-%{release}

%description rocm
Ollama plugin module for ROCm.

%prep
%autosetup -a1 -p1 -n %{name}-%{version}

%build
%if "%{?flavor}" == "test"
exit 0
%endif

%define __builder ninja

%sysusers_generate_pre %{SOURCE3} %{name} %{name}-user.conf

# fix install dir
sed -i -e 's@OLLAMA_BUILD_DIR .*lib/ollama@OLLAMA_BUILD_DIR ${CMAKE_BINARY_DIR}/%{_lib}/ollama@' CMakeLists.txt
sed -i -e 's@OLLAMA_LIB_DIR "lib/ollama"@OLLAMA_LIB_DIR "%{_lib}/ollama"@' CMakeLists.txt
sed -i -e 's@ "lib/ollama"@ "%{_lib}/ollama"@' llama/server/CMakeLists.txt

# fix rpath
find . -name CMakeLists.txt -type f -exec sed -i 's/@loader_path/\/usr\/%_lib\/ollama/g' {} +
find . -name CMakeLists.txt -type f -exec sed -i '/PROPERTIES INSTALL_RPATH/d' {} +

# overwrite ml/path.go so LibOllamaPath is set to our path
echo -e 'package ml\nvar LibOllamaPath string = "/usr/%{_lib}/ollama"' > ml/path.go
export GOFLAGS="-buildmode=pie -mod=vendor"
#export GOFLAGS="-mod=vendor -v"
export CXX="g++%{?force_gcc_version:-%force_gcc_version}"
export CC="gcc%{?force_gcc_version:-%force_gcc_version}"

%if "%{flavor}" == "cuda"
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
sed -i -e 's@CMAKE_LIB_DIR "lib/ollama"@CMAKE_LIB_DIR "%{_lib}/ollama"@' CMakeLists.txt
# overwrite ml/path.go so LibOllamaPath is set to our path
echo -e 'package ml\nvar LibOllamaPath string = "/usr/%{_lib}/ollama"' > ml/path.go

# and also the local copy of MLX sources
export OLLAMA_MLX_SOURCE=%_sourcedir/mlx-main
export OLLAMA_MLX_C_SOURCE=%_sourcedir/mlx-c-main

%cmake \
    -UOLLAMA_INSTALL_DIR -DOLLAMA_INSTALL_DIR=%{_libdir}/ollama \
    -UCMAKE_INSTALL_BINDIR -DCMAKE_INSTALL_BINDIR=%{_libdir}/ollama \
    -DGGML_BACKEND_DIR=%{_libdir}/ollama \
    -DCMAKE_SKIP_BUILD_RPATH=ON \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
    -DCMAKE_INSTALL_RPATH='$ORIGIN' \
    -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=OFF \
    -DFETCHCONTENT_SOURCE_DIR_LLAMA_CPP=%_sourcedir/llama.cpp-main \
%if "%{?flavor}" == "cuda"
    -DCMAKE_CUDA_COMPILER=/usr/local/cuda-%{cuda_version_major}.%{cuda_version_minor}/bin/nvcc \
%endif
%if "%{?flavor}" == "rocm"
    -DCMAKE_HIP_COMPILER=%rocmllvm_bindir/clang++ \
    -DAMDGPU_TARGETS=%{rocm_gpu_list_default} \
    -DCMAKE_HIP_FLAGS=--offload-compress \
%endif
%if "%{?flavor}" != ""
    -DARG_RUNNER_DIR=%preset_flavor \
%endif
    %{nil}

#
# MLX Flavor
#
%if "%{?flavor}" == "mlx_cuda"
cd ..
export OLLAMA_SKIP_CPU_GENERATE="1"
cmake -S llama/server --preset 'llama_cuda_v13_linux' \
    -DOLLAMA_MLX_BACKENDS=cuda_v13 \
    -DBLAS_INCLUDE_DIRS=/usr/include/openblas \
    -DLAPACK_INCLUDE_DIRS=/usr/include/openblas \
    -DCMAKE_SKIP_BUILD_RPATH=ON \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
    -DCMAKE_INSTALL_RPATH='$ORIGIN' \
    -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=OFF \
    -DFETCHCONTENT_SOURCE_DIR_LLAMA_CPP=%_sourcedir/llama.cpp-main \

cmake --build build/mlx_cuda_v13 -- -l %{jobs}
exit 0
%endif

#
# Flavor package (vulkan/cuda/rocm)
#
%if "%{?flavor}" != ""
cd ..
export OLLAMA_SKIP_CPU_GENERATE="1"
cmake -S llama/server --preset %preset_flavor \
    -DCMAKE_SKIP_BUILD_RPATH=ON \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
    -DCMAKE_INSTALL_RPATH='$ORIGIN' \
    -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=OFF \
    -DFETCHCONTENT_SOURCE_DIR_LLAMA_CPP=%_sourcedir/llama.cpp-main \

local_directory=build/llama-server-%preset_flavor
cmake --build ${local_directory%_linux} -- -l %{jobs}
exit 0
%endif

#
# Main package
#
%cmake_build

cd ..
go build -trimpath -o %{name} .

%install
%if "%{?flavor}" == "test"
exit 0
%endif
export DESTDIR=%buildroot

%if "%{?flavor}" != ""
#
# Flavor package
#
local_directory=%preset_flavor
local_directory=${local_directory%_linux}
%if "%{?flavor}" == "mlx_cuda"
cmake --install build/mlx_cuda_v13 --component MLX --prefix %{_prefix}
cmake --install build/mlx_cuda_v13 --component MLX_VENDOR --prefix %{_prefix}
%else
cmake --install build/llama-server-${local_directory} --component llama-server --prefix %{_prefix}
%endif
mv %buildroot/usr/%_lib/ollama/${local_directory}/* %buildroot/usr/%_lib/ollama/
rmdir %buildroot/usr/%_lib/ollama/${local_directory}
%else
#
# Main package
#
cmake --install build/llama-server-local --component llama-server --prefix %{_prefix}

install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}-user.conf
install -D -m 0644 %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -d %{buildroot}%{_localstatedir}/lib/%{name}
mkdir -p %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}

mkdir -p "%{buildroot}/%{_docdir}/%{name}"
cp -Ra docs/* "%{buildroot}/%{_docdir}/%{name}"
%endif

# remove copies of system libraries
shopt -s nullglob
rm -rf %{buildroot}%{_libdir}/%{name}/lib{vulkan,drm,amd,hip,cu,hsa,roc,numa,elf}*

# fixup the rpath
for lib in %{buildroot}%{_libdir}/ollama/*.so; do
    patchelf --set-rpath '$ORIGIN' "$lib" || true
done

patchelf --set-rpath '%{_libdir}/ollama' "%{buildroot}%{_bindir}/%{name}" || true

%check
%if "%{?flavor}" == "test"
  export LD_LIBRARY_PATH=%_libdir/ollama
  for f in \
%ifarch aarch64
     cpu-armv8.0_1 \
     cpu-armv8.2_1 \
     cpu-armv8.2_2 \
     cpu-armv8.2_3 \
     cpu-armv8.6_1 \
     cpu-armv8.6_2 \
     cpu-armv9.2_1 \
     cpu-armv9.2_2 \
%endif
%ifarch x86_64
     cpu-alderlake \
     cpu-haswell \
     cpu-icelake \
     cpu-sandybridge \
     cpu-skylakex \
     cpu-sse42 \
     cpu-x64 \
%endif
%if %{with vulkan}
    vulkan \
%endif
%if %{with rocm}
    hip \
%endif
%if %{with cuda}
    cuda \
%endif
  ; do
    file=%_libdir/ollama/libggml-${f}.so
    test -e "$file" || exit 1
    ldd -r "$file" | grep "undefined symbol:" && exit 1
  done
  exit 0
%endif

%if 0%{?force_gcc_version}
export CXX="g++-%{?force_gcc_version}"
export CC="gcc-%{?force_gcc_version}"
# pie doesn't work with gcc12 on leap
export GOFLAGS="-mod=vendor"
%endif
go test -v ./... || exit 0

%pre -f %{name}.pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%fillup_only

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%if "%{flavor}" == "cuda"
%files cuda
%dir %{_libdir}/ollama
%{_libdir}/ollama/libggml-cuda.so
%endif

%if "%{flavor}" == "vulkan"
%files vulkan
%dir %{_libdir}/ollama
%{_libdir}/ollama/libggml-vulkan.so
%endif

%if "%{flavor}" == "rocm"
%files rocm
%dir %{_libdir}/ollama
%{_libdir}/ollama/rocblas
%{_libdir}/ollama/libggml-hip.so
%endif

%if "%{flavor}" == "" && "%{flavor}" != "test"
%files
%doc README.md
%license LICENSE
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}-user.conf
%{_fillupdir}/sysconfig.%{name}
%attr(-, ollama, ollama) %{_localstatedir}/lib/%{name}
%endif

%changelog
