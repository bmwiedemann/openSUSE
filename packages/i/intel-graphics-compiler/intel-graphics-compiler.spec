#
# spec file for package intel-graphics-compiler
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


%global llvm_ref llvmorg-16.0.6
%global opencl_clang_ref 7161d7c6
%global spirv_llvm_translator_ref de396f26
%global vc_intrinsics_ref v0.25.0

%global llvm_version 16.0.6
%global llvm_major %gsub %{llvm_version} %{quote:%..+} %{quote: }

Name:           intel-graphics-compiler
Version:        2.30.1
Release:        0%{?dist}
Summary:        Intel Graphics Compiler for OpenCL
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://github.com/intel/intel-graphics-compiler
Source0:        https://github.com/intel/intel-graphics-compiler/archive/v%{version}.tar.gz
Source1:        https://github.com/intel/opencl-clang/archive/%{opencl_clang_ref}/opencl-clang.tar.gz
Source2:        https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/%{spirv_llvm_translator_ref}/spirv-llvm-translator.tar.gz
Source3:        https://github.com/llvm/llvm-project/archive/%{llvm_ref}/llvm-project.tar.gz
Source4:        https://github.com/intel/vc-intrinsics/archive/%{vc_intrinsics_ref}/vc-intrinsics.tar.gz
Patch0:         0001-Replace-ciso646-with-version.patch
Patch1:         0003-Empty-check-before-vector-use.patch
Patch2:         0001-Remove-rpath.patch
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  make
BuildRequires:  memory-constraints
BuildRequires:  patch
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-Mako
BuildRequires:  python3-PyYAML
BuildRequires:  spirv-headers
BuildRequires:  spirv-tools-devel > 2025.1
BuildRequires:  unzip
ExclusiveArch:  x86_64

%description
Intel Graphics Compiler for OpenCL.

%package -n libigc2
Summary:        Library for Intel Graphics Compiler
Group:          System/Libraries

%description -n libigc2
An LLVM based compiler for OpenCL targeting Intel Gen graphics hardware architecture.

%package -n libigc-devel
Summary:        Headers for the Intel Graphics Compiler library
Requires:       libigc2 = %{version}-%{release}

%description -n libigc-devel
This package contains development files for libigc.

%package -n iga
Summary:        Intel Graphics Assembler
Group:          Development/Tools/Building

%description -n iga
Assembler and disassembler for OpenCL kernels.

%package -n libiga64-2
Summary:        Library for Intel Graphics Assembler
Group:          System/Libraries

%description -n libiga64-2
Library files for Intel Graphics Assembler.

%package -n libiga-devel
Summary:        Headers for the Intel Graphics Assembler library
Requires:       libiga64-2 = %{version}-%{release}

%description -n libiga-devel
This package contains development files for libiga

%package -n libigdfcl2
Summary:        Intel Graphics Frontend Compiler library
Group:          System/Libraries

%description -n libigdfcl2
Library files for the Intel Graphics Frontend Compiler.

%package -n libigdfcl-devel
Summary:        Headers for the Intel Graphics Frontend Compiler library
Requires:       libigdfcl2 = %{version}-%{release}

%description -n libigdfcl-devel
This package contains development files for libigdfcl.

%package -n libopencl-clang%{llvm_major}
Summary:        A wrapper library around clang
Group:          System/Libraries

%description -n libopencl-clang%{llvm_major}
A wrapper library around clang.

%prep
mkdir llvm-project
tar -xzf %{_sourcedir}/llvm-project.tar.gz -C llvm-project --strip-components=1
pushd llvm-project
%patch -P 0 -p1
%patch -P 2 -p1
popd

mkdir vc-intrinsics
tar -xzf %{_sourcedir}/vc-intrinsics.tar.gz -C vc-intrinsics --strip-components=1

pushd llvm-project/llvm/projects
mkdir opencl-clang llvm-spirv
tar -xzf %{_sourcedir}/opencl-clang.tar.gz -C opencl-clang --strip-components=1
tar -xzf %{_sourcedir}/spirv-llvm-translator.tar.gz -C llvm-spirv --strip-components=1
popd

mkdir igc
tar -xzf %{_sourcedir}/v%{version}.tar.gz -C igc --strip-components=1
pushd igc
%patch -P 1 -p1
popd

%build
# Remove cmake4 error due to not setting
# min cmake version - sflees.de
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%limit_build -m 900

mkdir build
pushd build

# FIXME: you should use %%cmake macros
export CXXFLAGS="-Wno-nonnull -fPIE  -Wno-error=free-nonheap-object"
# FIXME: Disable linker pie as this seems to break when linking static libraries
#export LDFLAGS="-pie"
cmake ../igc \
  -DCMAKE_BUILD_TYPE=Release \
  -DIGC_OPTION__ARCHITECTURE_TARGET='Linux64' \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DINSTALL_SPIRVDLL=0 \
  -DIGC_OPTION__SPIRV_TOOLS_MODE=Prebuilds \
  -DIGC_OPTION__USE_PREINSTALLED_SPRIV_HEADERS=ON \
  -DIGC_OPTION__LLVM_PREFERRED_VERSION=%{llvm_version} \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR=%{_includedir}/spirv
#  -DLLVM_LOCAL_RPATH=""

%make_build
popd

%install
cd build
%make_install

rm -fv %{buildroot}%{_bindir}/GenX_IR \
    %{buildroot}%{_bindir}/clang-%{llvm_major} \
    %{buildroot}%{_bindir}/lld \
    %{buildroot}%{_includedir}/opencl-c.h \
    %{buildroot}%{_includedir}/opencl-c-base.h \
    %{buildroot}%{_prefix}/lib/debug \
    %{buildroot}%{_prefix}/lib/NewPMPlugin*
chmod +x %{buildroot}%{_libdir}/libopencl-clang.so.%{llvm_major}

%post -n libigc2 -p /sbin/ldconfig
%postun -n libigc2 -p /sbin/ldconfig
%post -n libiga64-2 -p /sbin/ldconfig
%postun -n libiga64-2 -p /sbin/ldconfig
%post -n libigdfcl2 -p /sbin/ldconfig
%postun -n libigdfcl2 -p /sbin/ldconfig
%post -n libopencl-clang%{llvm_major} -p /sbin/ldconfig
%postun -n libopencl-clang%{llvm_major} -p /sbin/ldconfig

%files -n iga
%{_bindir}/iga64

%files -n libiga64-2
%{_libdir}/libiga64.so.*

%files -n libiga-devel
%{_libdir}/libiga64.so
%{_includedir}/iga

%files -n libigc2
%{_libdir}/libigc.so.*
%dir %{_libdir}/igc2
%license %{_libdir}/igc2/NOTICES.txt

%files -n libigc-devel
%{_libdir}/libigc.so
%{_includedir}/igc

%files -n libigdfcl2
%{_libdir}/libigdfcl.so.*

%files -n libigdfcl-devel
%{_libdir}/libigdfcl.so
%{_includedir}/visa
%{_libdir}/pkgconfig/igc-opencl.pc

%files -n libopencl-clang%{llvm_major}
%{_libdir}/libopencl-clang.so.%{llvm_major}

%changelog
