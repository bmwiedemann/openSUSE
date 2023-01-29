#
# spec file for package libclc
#
# Copyright (c) 2023 SUSE LLC
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


%define _libclc_llvm_ver 15.0.0
%define _version %_libclc_llvm_ver%{?_rc:rc%_rc}
%define _tagver %_libclc_llvm_ver%{?_rc:-rc%_rc}

Name:           libclc
Version:        0.2.0+llvm%{_libclc_llvm_ver}%{?_rc:~rc%_rc}
Release:        0
Summary:        OpenCL C programming language library
License:        Apache-2.0 WITH LLVM-exception AND (BSD-3-Clause OR MIT)
Group:          Development/Libraries/C and C++
URL:            https://libclc.llvm.org/
Source0:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_tagver}/%{name}-%{_version}.src.tar.xz
Source1:        %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM: CMAKE_<LANG>_FLAGS is a string and not a list.
Patch0:         cmake-flags-concat.patch
BuildRequires:  cmake
%if 0%{?suse_version} >= 1550
BuildRequires:  clang-devel
BuildRequires:  llvm-devel
BuildRequires:  pkgconfig(LLVMSPIRVLib)
%else
 %if 0%{?sle_version} >= 150500
BuildRequires:  clang15-devel
BuildRequires:  llvm15-devel
 %else
  %if 0%{?sle_version} >= 150400
BuildRequires:  clang13-devel
BuildRequires:  llvm13-devel
  %else
   %if 0%{?sle_version} >= 150300
BuildRequires:  clang11-devel
BuildRequires:  llvm11-devel
   %else
BuildRequires:  clang9-devel
BuildRequires:  llvm9-devel
   %endif
  %endif
 %endif
%endif
BuildRequires:  python3-base
Provides:       libclc(llvm%{_llvm_sonum})
BuildArch:      noarch

%description
Library requirements of the OpenCL C programming language.

%prep
%setup -q -n libclc-%{_version}.src
%patch0 -p1

%build
# The libraries are bitcode files, so LTO is neither supported nor does it help.
%define _lto_cflags %{nil}

# For now we turn off opaque pointers - Clang uses them by default, but Mesa doesn't support them yet.
%cmake \
  -DCMAKE_C_COMPILER=clang \
  -DCMAKE_CXX_COMPILER=clang++ \
%if %{_llvm_sonum} >= 15
  -DCMAKE_CLC_FLAGS="-Xclang -no-opaque-pointers" \
  -DCMAKE_LLAsm_FLAGS="-Xclang -no-opaque-pointers" \
%endif
%if 0%{?suse_version} < 1550
  -DLIBCLC_TARGETS_TO_BUILD="amdgcn--;amdgcn--amdhsa;amdgcn-mesa-mesa3d;r600--;nvptx--;nvptx64--;nvptx--nvidiacl;nvptx64--nvidiacl" \
%endif
  -DENABLE_RUNTIME_SUBNORMAL:BOOL=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE.TXT
%{_includedir}/clc
%{_datadir}/clc
%{_datadir}/pkgconfig/libclc.pc

%changelog
