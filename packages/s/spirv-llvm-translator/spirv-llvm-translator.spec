#
# spec file for package spirv-llvm-translator
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2023, Martin Hauke <mardnh@gmx.de>
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


%define sover   18
Name:           spirv-llvm-translator
Version:        18.1.2
Release:        0
Summary:        LLVM/SPIR-V Bi-Directional Translator library
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://github.com/KhronosGroup/SPIRV-LLVM-Translator
Source:         https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/refs/tags/v%{version}.tar.gz#/SPIRV-LLVM-Translator-%{version}.tar.gz
Source101:      %{name}.rpmlintrc
BuildRequires:  cmake >= 3.3
BuildRequires:  gcc-c++
BuildRequires:  llvm%{sover}-devel
BuildRequires:  pkgconfig
BuildRequires:  spirv-headers
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)

%description
The LLVM/SPIR-V Bi-Directional Translator, a library and tool for translation
between LLVM IR and SPIR-V.

%package -n libLLVMSPIRVLib%{sover}
Summary:        LLVM/SPIR-V Bi-Directional Translator library
Group:          System/Libraries

%description -n libLLVMSPIRVLib%{sover}
The LLVM/SPIR-V Bi-Directional Translator, a library and tool for translation
between LLVM IR and SPIR-V.

%package -n libLLVMSPIRVLib-devel
Summary:        Development files for LLVM/SPIR-V Bi-Directional Translator library
Group:          Development/Languages/C and C++
Requires:       libLLVMSPIRVLib%{sover} = %{version}

%description -n libLLVMSPIRVLib-devel
The LLVM/SPIR-V Bi-Directional Translator, a library and tool for translation
between LLVM IR and SPIR-V.

This package provides headers and libraries required for building software using
the LLVM/SPIR-V Bi-Directional Translator library.

%prep
%setup -q -n SPIRV-LLVM-Translator-%{version}

%build
%cmake \
 -DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR=%{_prefix} \
 -DLLVM_SPIRV_BUILD_EXTERNAL=YES
%cmake_build

%install
%cmake_install

%post   -n libLLVMSPIRVLib%{sover} -p /sbin/ldconfig
%postun -n libLLVMSPIRVLib%{sover} -p /sbin/ldconfig

%files -n libLLVMSPIRVLib%{sover}
%license LICENSE.TXT
%doc README.md
%{_libdir}/libLLVMSPIRVLib.so.%{sover}*

%files -n libLLVMSPIRVLib-devel
%{_bindir}/llvm-spirv
%{_includedir}/LLVMSPIRVLib
%{_libdir}/libLLVMSPIRVLib.so
%{_libdir}/pkgconfig/LLVMSPIRVLib.pc

%changelog
