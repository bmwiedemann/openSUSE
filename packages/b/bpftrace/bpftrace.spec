#
# spec file for package bpftrace
#
# Copyright (c) 2024 SUSE LLC
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


# Use default LLVM unless it is not yet supported
%if 0%{?suse_version} >= 1600
 %if 0%{?product_libs_llvm_ver} > 18
 %define llvm_major_version 18
 %else
 %define llvm_major_version %{nil}
 %endif
 %define gcc_package gcc-c++
 %define gcc_binary gcc
 %define gxx_binary g++
%else
 # Hard-code latest LLVM for SLES, the default version is too old
 %if 0%{?sle_version} == 150600
  %define llvm_major_version 17
 %else
 %if 0%{?sle_version} == 150500
  %define llvm_major_version 15
 %else
 %if 0%{?sle_version} == 150400
  %define llvm_major_version 11
 %endif
 %endif
 %endif
 %define gcc_package gcc13-c++
 %define gcc_binary gcc-13
 %define gxx_binary g++-13
%endif

Name:           bpftrace
Version:        0.21.2
Release:        0
Summary:        High-level tracing language for Linux eBPF
License:        Apache-2.0
Group:          Development/Tools/Debuggers
URL:            https://github.com/iovisor/bpftrace
Source:         https://github.com/iovisor/bpftrace/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 0001-tools-bashreadline-fix-probe-for-dynamically-linked-.patch bsc#1232536
Patch0:         0001-tools-bashreadline-fix-probe-for-dynamically-linked-.patch
BuildRequires:  %gcc_package
BuildRequires:  binutils
BuildRequires:  binutils-devel
BuildRequires:  bison
BuildRequires:  clang%{llvm_major_version}-devel
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  libbpf-devel
BuildRequires:  libxml2-devel
BuildRequires:  lldb%{llvm_major_version}-devel
BuildRequires:  llvm%{llvm_major_version}-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  cmake(cereal)
BuildRequires:  pkgconfig(libbcc) >= 0.11
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rubygem(asciidoctor)
ExcludeArch:    %arm %ix86

%description
High-level tracing language for Linux, allowing for instrumentation of
in-kernel and userspace state. It makes use of only upstream features such as
eBPF tracing (which builds on kprobes, uprobes, and a variety of other kernel
technologies). BPFtrace's language is inspired by awk and C, as well as other
tracers such as DTrace and SystemTap.

%package tools
Summary:        Example bpftrace scripts and other useful snippets
Group:          Development/Tools/Debuggers
Requires:       %{name} = %{version}
BuildArch:      noarch

%description tools
Collection of tools for quick instrumentation and inspection of a running
system. These are all BPFtrace scripts within %{_datadir}/bpftrace, and can be
easily modified to allow for different types of debugging.

%prep
%setup -q
%autopatch -p1

# Correct the #!-line to avoid rpmlint warnings.
find tools -name '*.bt' -type f \
	-exec sed -i '1s|^#!%{_bindir}/env bpftrace|#!%{_bindir}/bpftrace|' '{}' ';'

%build
# We need to build with clang, enable LTO via CMake instead.
%define _lto_cflags %{nil}
export CC="%gcc_binary"
export CXX="%gxx_binary"
%cmake \
	-DCMAKE_INTERPROCEDURAL_OPTIMIZATION:BOOL=TRUE \
	-DLLVM_REQUESTED_VERSION="${LLVM_VERSION}" \
	-DLIBBFD_LIBRARIES="${LIBBFD}" \
	-DLIBOPCODES_LIBRARIES="${LIBOPCODES}" \
	-DUSE_SYSTEM_BPF_BCC:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DBUILD_STATIC_LIBS:BOOL=ON \
	-DBUILD_TESTING:BOOL=OFF
%cmake_build

%install
%cmake_install
# Set executable bit for tools.
chmod +x %{buildroot}%{_datadir}/bpftrace/tools/*.bt
chmod +x %{buildroot}%{_datadir}/bpftrace/tools/old/*.bt

%files
%{_bindir}/bpftrace
%{_bindir}/bpftrace-aotrt
%{_mandir}/man8/bpftrace.8%{?ext_man}
%doc README.md docs/
%license LICENSE

%files tools
%dir %{_datadir}/bpftrace/
%dir %{_datadir}/bpftrace/tools
%{_datadir}/bpftrace/tools/*.bt
%dir %{_datadir}/bpftrace/tools/old
%{_datadir}/bpftrace/tools/old/*.bt
%dir %{_datadir}/bpftrace/tools/doc
%{_datadir}/bpftrace/tools/doc/*_example.txt
%{_mandir}/man8/*.8%{?ext_man}
%exclude %{_mandir}/man8/bpftrace.8%{ext_man}

%changelog
