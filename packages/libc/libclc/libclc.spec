#
# spec file for package libclc
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


%define _libclc_llvm_ver 11.0.0

Name:           libclc
Version:        0.2.0+llvm%{_libclc_llvm_ver}
Release:        0
Summary:        OpenCL C programming language library
License:        (BSD-3-Clause OR MIT) AND Apache-2.0 WITH LLVM-exception
Group:          Development/Libraries/C and C++
URL:            https://libclc.llvm.org/
Source0:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{_libclc_llvm_ver}/%{name}-%{_libclc_llvm_ver}.src.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  clang-devel >= 4.0
BuildRequires:  cmake
BuildRequires:  llvm >= 4.0
BuildRequires:  python3-base
Provides:       libclc(llvm%{_llvm_sonum})
BuildArch:      noarch

%description
Library requirements of the OpenCL C programming language.

%prep
%setup -q -n libclc-%{_libclc_llvm_ver}.src

%build
# The libraries are bitcode files, so LTO is neither supported nor does it help.
%define _lto_cflags %{nil}

sed -i "s|python|python3|g" CMakeLists.txt
%cmake \
  -DCMAKE_C_COMPILER=clang \
  -DCMAKE_CXX_COMPILER=clang++ \
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
