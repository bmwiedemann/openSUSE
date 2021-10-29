#
# spec file for package intel-graphics-compiler
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


%global llvm_commit llvmorg-11.1.0
%global opencl_clang_commit fd68f64b33e67d58f6c36b9e25c31c1178a1962a
%global spirv_llvm_translator_commit c67e6f26a7285aa753598ef792593ac4a545adf9
%global vc_intrinsics_commit e5ad7e02aa4aa21a3cd7b3e5d1f3ec9b95f58872
Name:           intel-graphics-compiler
Version:        1.0.8744
Release:        1%{?dist}
Summary:        Intel Graphics Compiler for OpenCL
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/intel/intel-graphics-compile
Source0:        https://github.com/intel/intel-graphics-compiler/archive/igc-%{version}.tar.gz
Source1:        https://github.com/intel/opencl-clang/archive/%{opencl_clang_commit}/intel-opencl-clang.tar.gz
Source2:        https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/%{spirv_llvm_translator_commit}/spirv-llvm-translator.tar.gz
Source3:        https://github.com/llvm/llvm-project/archive/%{llvm_commit}/llvm-project.tar.gz
Source4:        https://github.com/intel/vc-intrinsics/archive/%{vc_intrinsics_commit}/vc-intrinsics.zip
BuildRequires:  memory-constraints
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  unzip
ExclusiveArch:  x86_64

%description
Intel Graphics Compiler for OpenCL.

%package -n libigc1
Summary:        Library for Intel Graphics Compiler
Group:          System/Libraries

%description -n libigc1
An LLVM based compiler for OpenCL targeting Intel Gen graphics hardware architecture.

%package -n libigc-devel
Summary:        Headers for the Intel Graphics Compiler library
Requires:       libigc1 = %{version}-%{release}

%description -n libigc-devel
This package contains development files for libigc.

%package -n iga
Summary:        Intel Graphics Assembler
Group:          Development/Tools/Building

%description -n iga
Assembler and disassembler for OpenCL kernels.

%package -n libiga64-1
Summary:        Library for Intel Graphics Assembler
Group:          System/Libraries

%description -n libiga64-1
Library files for Intel Graphics Assembler.

%package -n libiga-devel
Summary:        Headers for the Intel Graphics Assembler library
Requires:       libiga64-1 = %{version}-%{release}

%description -n libiga-devel
This package contains development files for libiga

%package -n libigdfcl1
Summary:        Intel Graphics Frontend Compiler library
Group:          System/Libraries

%description -n libigdfcl1
Library files for the Intel Graphics Frontend Compiler.

%package -n libigdfcl-devel
Summary:        Headers for the Intel Graphics Frontend Compiler library
Requires:       libigdfcl1 = %{version}-%{release}

%description -n libigdfcl-devel
This package contains development files for libigdfcl.

%package -n libopencl-clang11
Summary:        A wrapper library around clang
Group:          System/Libraries

%description -n libopencl-clang11
A wrapper library around clang.

%prep
mkdir llvm-project
tar -xzf %{_sourcedir}/llvm-project.tar.gz -C llvm-project --strip-components=1
mv llvm-project/clang llvm-project/llvm/tools/

unzip %{_sourcedir}/vc-intrinsics.zip
mv vc-intrinsics* vc-intrinsics

pushd llvm-project/llvm/projects
mkdir opencl-clang llvm-spirv
tar -xzf %{_sourcedir}/intel-opencl-clang.tar.gz -C opencl-clang --strip-components=1
tar -xzf %{_sourcedir}/spirv-llvm-translator.tar.gz -C llvm-spirv --strip-components=1
popd

mkdir igc
tar -xzf %{_sourcedir}/igc-%{version}.tar.gz -C igc --strip-components=1

%build
%limit_build -m 900

mkdir build
pushd build

# FIXME: you should use %%cmake macros
export CXXFLAGS="-Wno-nonnull -Wno-dev -fPIE"
export LDFLAGS="-pie"
cmake ../igc \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DINSTALL_SPIRVDLL=0

%make_build
popd

%install
cd build
%make_install

rm -fv %{buildroot}%{_bindir}/GenX_IR \
	%{buildroot}%{_bindir}/clang-11 \
	%{buildroot}%{_bindir}/lld \
	%{buildroot}%{_includedir}/opencl-c.h \
	%{buildroot}%{_includedir}/opencl-c-base.h \
	%{buildroot}%{_prefix}/lib/debug
chmod +x %{buildroot}%{_libdir}/libopencl-clang.so.11

%post -n libigc1 -p /sbin/ldconfig
%postun -n libigc1 -p /sbin/ldconfig
%post -n libiga64-1 -p /sbin/ldconfig
%postun -n libiga64-1 -p /sbin/ldconfig
%post -n libigdfcl1 -p /sbin/ldconfig
%postun -n libigdfcl1 -p /sbin/ldconfig
%post -n libopencl-clang11 -p /sbin/ldconfig
%postun -n libopencl-clang11 -p /sbin/ldconfig

%files -n iga
%{_bindir}/iga64

%files -n libiga64-1
%{_libdir}/libiga64.so.*

%files -n libiga-devel
%{_libdir}/libiga64.so
%{_includedir}/iga

%files -n libigc1
%{_libdir}/libigc.so.*
%dir %{_libdir}/igc
%license %{_libdir}/igc/NOTICES.txt

%files -n libigc-devel
%{_libdir}/libigc.so
%{_includedir}/igc

%files -n libigdfcl1
%{_libdir}/libigdfcl.so.*

%files -n libigdfcl-devel
%{_libdir}/libigdfcl.so
%{_includedir}/visa
%{_libdir}/pkgconfig/igc-opencl.pc

%files -n libopencl-clang11
%{_libdir}/libopencl-clang.so.11

%changelog
