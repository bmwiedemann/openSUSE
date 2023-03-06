#
# spec file for package bpftrace
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
# nodebuginfo


# Disable binary stripping because bpftrace depends on debug symbols in its
# implementation of the BEGIN trigger. See bsc#1178928.
%undefine _build_create_debug
%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

# Use the latest supported LLVM version, but Leap only has a slightly older one
# so just use whatever version is available.
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150500
%define llvm_major_version 15
%else
%define llvm_major_version %{nil}
%endif

Name:           bpftrace
Version:        0.17.0
Release:        0
Summary:        High-level tracing language for Linux eBPF
License:        Apache-2.0
Group:          Development/Tools/Debuggers
URL:            https://github.com/iovisor/bpftrace
Source:         https://github.com/iovisor/bpftrace/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         Vendor-BPF_F_KPROBE_MULTI_RETURN-definition.patch
BuildRequires:  binutils
BuildRequires:  binutils-devel
BuildRequires:  bison
BuildRequires:  clang%{llvm_major_version}
BuildRequires:  clang%{llvm_major_version}-devel
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  libbpf-devel
BuildRequires:  libxml2-devel
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
# We need to build with clang.
%define _lto_cflags %{nil}
export CC="clang"
export CXX="clang++"
%cmake \
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
