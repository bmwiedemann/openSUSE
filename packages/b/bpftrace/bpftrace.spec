#
# spec file for package bpftrace
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


Name:           bpftrace
Version:        0.11.2
Release:        0
Summary:        High-level tracing language for Linux eBPF
License:        Apache-2.0
Group:          Development/Tools/Debuggers
URL:            https://github.com/iovisor/bpftrace
Source:         https://github.com/iovisor/bpftrace/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  binutils
BuildRequires:  binutils-devel
BuildRequires:  bison
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  libbpf-devel
BuildRequires:  llvm-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(libbcc) >= 0.11
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(zlib)
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

# Correct the #!-line to avoid rpmlint warnings.
find tools -name '*.bt' -type f \
	-exec sed -i '1s|^#!%{_bindir}/env bpftrace|#!%{_bindir}/bpftrace|' '{}' ';'

%build
# Find libbfd.so and libopcodes.so. This is necessary because binutils gives
# these libraries very strange names which CMake cannot find. See boo#1162312.
LIBBFD="$(find "%{_libdir}" -type f -name 'libbfd*.so*')"
LIBOPCODES="$(find "%{_libdir}" -type f -name 'libopcodes*.so*')"

# We need to build with clang.
%define _lto_cflags %{nil}
export CC="clang"
export CXX="clang++"
%cmake \
	-DLIBBFD_LIBRARIES="${LIBBFD}" \
	-DLIBOPCODES_LIBRARIES="${LIBOPCODES}" \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DBUILD_STATIC_LIBS:BOOL=ON \
	-DBUILD_TESTING:BOOL=OFF
%cmake_build

%install
%cmake_install
# Set executable bit for tools.
chmod +x %{buildroot}%{_datadir}/bpftrace/tools/*.bt

%files
%{_bindir}/bpftrace
%{_mandir}/man8/bpftrace.8%{?ext_man}
%doc README.md docs/
%license LICENSE

%files tools
%dir %{_datadir}/bpftrace/
%dir %{_datadir}/bpftrace/tools
%{_datadir}/bpftrace/tools/*.bt
%dir %{_datadir}/bpftrace/tools/doc
%{_datadir}/bpftrace/tools/doc/*_example.txt
%{_mandir}/man8/*.8%{?ext_man}
%exclude %{_mandir}/man8/bpftrace.8%{ext_man}

%changelog
