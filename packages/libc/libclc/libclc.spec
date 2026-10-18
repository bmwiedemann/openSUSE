#
# spec file for package libclc
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


%global _libclc_llvm 23
%global _libclc_llvm_ver %{_libclc_llvm}.1.0
%global _version %_libclc_llvm_ver%{?_rc:rc%_rc}
%global _tagver %_libclc_llvm_ver%{?_rc:-rc%_rc}

%global _libclc_targets spirv{32,64}-unknown-unknown

Name:           libclc
Version:        0.2.0+llvm%{_libclc_llvm_ver}%{?_rc:~rc%_rc}
Release:        0
Summary:        OpenCL C programming language library
License:        Apache-2.0 WITH LLVM-exception AND (BSD-3-Clause OR MIT)
Group:          Development/Libraries/C and C++
URL:            https://libclc.llvm.org/
# Built manually via "git archive --prefix=%{name}-%{_version}.src/ llvmorg-%{_tagver} .
# | xz -T0 >../%{name}-%{_version}.src.tar.xz" until upstream provides tarballs again.
Source0:        %{name}-%{_version}.src.tar.xz
Patch1:         cmake-use-imported-targets.patch
BuildRequires:  clang%{_libclc_llvm}-devel
BuildRequires:  cmake
BuildRequires:  llvm%{_libclc_llvm}-devel
BuildRequires:  python3-base
BuildRequires:  pkgconfig(LLVMSPIRVLib)
BuildArch:      noarch

%description
Library requirements of the OpenCL C programming language.

%prep
%setup -q -n libclc-%{_version}.src
%autopatch -p2

%build
%define __builddir build-${target}
for target in %{_libclc_targets}
do
  pushd .
  %cmake \
    -DCMAKE_C_COMPILER=clang-%{_libclc_llvm} \
    -DCMAKE_CXX_COMPILER=clang++-%{_libclc_llvm} \
    -DLLVM_DEFAULT_TARGET_TRIPLE=${target}
  %cmake_build
  popd
done

%install
for target in %{_libclc_targets}
do
  %cmake_install
  # We don't need the static library.
  rm %{buildroot}%{_datadir}/clc/${target}/libclc.a
done

%files
%license LICENSE.TXT
%{_datadir}/clc

%changelog
