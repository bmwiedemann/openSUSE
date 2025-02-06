#
# spec file for package intel-graphics-compiler
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


%global llvm_commit llvmorg-14.0.5
%global opencl_clang_commit 470cf0018e1ef6fc92eda1356f5f31f7da452abc
%global spirv_llvm_translator_commit efbedd32b700c01a15d44121fca862625c2594ac
%global vc_intrinsics_commit v0.21.0
%global so_version 2.5.0
Name:           intel-graphics-compiler
Version:        2.5.6
Release:        1%{?dist}
Summary:        Intel Graphics Compiler for OpenCL
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://github.com/intel/intel-graphics-compile
Source0:        https://github.com/intel/intel-graphics-compiler/archive/v%{version}.tar.gz
Source1:        https://github.com/intel/opencl-clang/archive/%{opencl_clang_commit}/intel-opencl-clang.tar.gz
Source2:        https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/%{spirv_llvm_translator_commit}/spirv-llvm-translator.tar.gz
Source3:        https://github.com/llvm/llvm-project/archive/%{llvm_commit}/llvm-project.tar.gz
Source4:        https://github.com/intel/vc-intrinsics/archive/%{vc_intrinsics_commit}/vc-intrinsics.zip
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
BuildRequires:  spirv-tools-devel
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

%package -n libopencl-clang14
Summary:        A wrapper library around clang
Group:          System/Libraries

%description -n libopencl-clang14
A wrapper library around clang.

%prep
mkdir llvm-project
tar -xzf %{_sourcedir}/llvm-project.tar.gz -C llvm-project --strip-components=1
pushd llvm-project
popd

unzip %{_sourcedir}/vc-intrinsics.zip
mv vc-intrinsics* vc-intrinsics

pushd llvm-project/llvm/projects
mkdir opencl-clang llvm-spirv
tar -xzf %{_sourcedir}/intel-opencl-clang.tar.gz -C opencl-clang --strip-components=1
tar -xzf %{_sourcedir}/spirv-llvm-translator.tar.gz -C llvm-spirv --strip-components=1
popd

mkdir igc
tar -xzf %{_sourcedir}/v%{version}.tar.gz -C igc --strip-components=1
pushd igc
popd

%build
%limit_build -m 900

mkdir build
pushd build

# FIXME: you should use %%cmake macros
export CXXFLAGS="-Wno-nonnull -fPIE  -Wno-error=free-nonheap-object"
export LDFLAGS="-pie"
cmake ../igc \
  -DCMAKE_BUILD_TYPE=Release \
  -DIGC_OPTION__ARCHITECTURE_TARGET='Linux64' \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DINSTALL_SPIRVDLL=0 \
  -DIGC_OPTION__SPIRV_TOOLS_MODE=Prebuilds \
  -DIGC_OPTION__USE_PREINSTALLED_SPRIV_HEADERS=ON \
  -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR=%{_includedir}/spirv

%make_build
popd

%install
cd build
%make_install

rm -fv %{buildroot}%{_bindir}/GenX_IR \
	%{buildroot}%{_bindir}/clang-14 \
	%{buildroot}%{_bindir}/lld \
	%{buildroot}%{_includedir}/opencl-c.h \
	%{buildroot}%{_includedir}/opencl-c-base.h \
	%{buildroot}%{_prefix}/lib/debug
chmod +x %{buildroot}%{_libdir}/libopencl-clang.so.14
ln -s %{_libdir}/libiga64.so.%{so_version} %{buildroot}%{_libdir}/libiga64.so
ln -s %{_libdir}/libigc.so.%{so_version} %{buildroot}%{_libdir}/libigc.so
ln -s %{_libdir}/libigdfcl.so.%{so_version} %{buildroot}%{_libdir}/libigdfcl.so

%post -n libigc2 -p /sbin/ldconfig
%postun -n libigc2 -p /sbin/ldconfig
%post -n libiga64-2 -p /sbin/ldconfig
%postun -n libiga64-2 -p /sbin/ldconfig
%post -n libigdfcl2 -p /sbin/ldconfig
%postun -n libigdfcl2 -p /sbin/ldconfig
%post -n libopencl-clang14 -p /sbin/ldconfig
%postun -n libopencl-clang14 -p /sbin/ldconfig

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

%files -n libopencl-clang14
%{_libdir}/libopencl-clang.so.14

%changelog
