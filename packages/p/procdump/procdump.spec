#
# spec file for package procdump
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


Name:           procdump
Version:        3.5.3
Release:        0
Summary:        Process coredump emitter using performance triggers
License:        BSD-2-Clause AND MIT AND BSD-3-Clause
URL:            https://github.com/Microsoft/ProcDump-for-Linux
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
# Newer clang lowers the eBPF zeroing loop into an extern memset()
# without BTF info, failing the skeleton link; fixed upstream-bound.
Patch0:         %{name}-ebpf-no-builtin-memset.patch
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(zlib)
Requires:       gdb
# eBPF/restrack backend builds only for x86_64 and aarch64
ExclusiveArch:  %{rust_tier1_arches}

%description
A Linux version of the eponymous ProcDump tool from the Windows Sysinternals
suite. It can create core dumps of processes based on performance triggers.

%prep
%autosetup -p1 -a1 -n ProcDump-for-Linux-%{version}

%build
%{cargo_build} --bin procdump

# No %%check: the integration suite needs passwordless sudo and a .NET
# SDK/runtime, neither available in the build root (see BUILD.md).

%install
%cargo_install -p crates/procdump-cli
install -D -m 0644 procdump.1 %{buildroot}%{_mandir}/man1/procdump.1

%files
%license LICENSE
%doc README.md
%{_bindir}/procdump
%{_mandir}/man1/procdump.1%{?ext_man}

%changelog
