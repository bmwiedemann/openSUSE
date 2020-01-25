#
# spec file for package klee
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


%define llvm_version_major 9
%define llvm_version_minor 0
%define llvm_version %{llvm_version_major}

%define version_unconverted 2.0+20200119

%ifarch %{ix86} x86_64
%define with_uclibc 1
%else
%define with_uclibc 0
%endif

Name:           klee
Summary:        LLVM Execution Engine
License:        NCSA
Group:          Development/Languages/Other
Version:        2.0+20200119
Release:        0
URL:            http://klee.github.io/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
Source2:        https://raw.githubusercontent.com/llvm-mirror/llvm/release_%{llvm_version_major}%{llvm_version_minor}/utils/not/not.cpp
Source3:        https://raw.githubusercontent.com/llvm-mirror/llvm/release_%{llvm_version_major}%{llvm_version_minor}/utils/FileCheck/FileCheck.cpp

BuildRequires:  clang%{llvm_version}
BuildRequires:  cmake
BuildRequires:  gperftools-devel
%if %{with_uclibc}
BuildRequires:  klee-uclibc-devel-static(llvm%{llvm_version})
%endif
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  libselinux-devel
BuildRequires:  llvm%{llvm_version}-devel
BuildRequires:  ninja
# tests need sqlite3
BuildRequires:  python3
BuildRequires:  python3-lit
BuildRequires:  python3-setuptools
BuildRequires:  python3-tabulate
BuildRequires:  sqlite3-devel
BuildRequires:  stp-devel
BuildRequires:  xz
BuildRequires:  zlib-devel

%description
KLEE is a symbolic virtual machine built on top of the LLVM compiler
infrastructure, and available under the UIUC open source license. For more
information on what KLEE is and what it can do, see the OSDI 2008 paper. 

%prep
%setup -q
%autopatch -p1

mkdir -p build/test/
cp %{SOURCE2} build/test/
cp %{SOURCE3} build/test/

sed -i '1s@/usr/bin/env python3*@/usr/bin/python3@' \
	test/Concrete/ConcreteTest.py \
	tools/klee-stats/klee-stats \
	tools/ktest-tool/ktest-tool

%build
# Make _lto_cflags compatible with Clang. On some arches, it doesn't work.
%ifarch x86_64 %{ix86} ppc64le s390x
%define _lto_cflags "-flto=thin"
%else
%define _lto_cflags %{nil}
%endif
%define __builder ninja
# they use -DNDEBUG, but we cannot, hence setting CMAKE_C*_FLAGS
# SHARED libs do not work at all yet
%cmake \
	-DCMAKE_C_COMPILER=clang \
	-DCMAKE_CXX_COMPILER=clang++ \
	-DCMAKE_AR=%{_bindir}/llvm-ar \
	-DCMAKE_RANLIB=%{_bindir}/llvm-ranlib \
	-DENABLE_DOXYGEN=OFF \
	-DENABLE_SOLVER_STP=ON \
	-DENABLE_TCMALLOC=ON \
	-DENABLE_UNIT_TESTS=OFF \
	-DENABLE_SYSTEM_TESTS=ON \
	-DCMAKE_C_FLAGS="%optflags" \
	-DCMAKE_CXX_FLAGS="%optflags" \
%if %{with_uclibc}
	-DENABLE_POSIX_RUNTIME=ON \
	-DENABLE_KLEE_UCLIBC=ON \
	-DKLEE_UCLIBC_PATH=%{_libdir}/klee-uclibc/ \
%endif
	-DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build

%check
%ifarch x86_64
cd build
ninja check
%endif

%install
%cmake_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc NEWS README.md
%license LICENSE.TXT
%{_bindir}/gen-bout
%{_bindir}/gen-random-bout
%{_bindir}/kleaver
%{_bindir}/klee
%{_bindir}/klee-replay
%{_bindir}/klee-stats
%{_bindir}/ktest-tool
%{_includedir}/klee/
%{_libdir}/libkleeRuntest.so*
%dir %{_libdir}/klee/
%dir %{_libdir}/klee/runtime/
%{_libdir}/klee/runtime/libklee-libc.bca
%{_libdir}/klee/runtime/libkleeRuntimeFreeStanding.bca
%{_libdir}/klee/runtime/libkleeRuntimeIntrinsic.bca
%if %{with_uclibc}
%{_libdir}/klee/runtime/klee-uclibc.bca
%{_libdir}/klee/runtime/libkleeRuntimePOSIX.bca
%endif

%changelog
