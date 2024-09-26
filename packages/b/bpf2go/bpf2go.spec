#
# spec file for package bpf2go
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


Name:           bpf2go
Version:        0.16.0
Release:        0
Summary:        CLI tool to read, modify, load and hook eBPF programs
License:        MIT
Group:          Productivity/Networking/System
URL:            https://github.com/cilium/ebpf
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.22

%description
bpf2go is a CLI tool to read, modify and load eBPF programs and attach them to
various hooks in the Linux kernel.

https://ebpf-go.dev

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build ./cmd/%{name}

%check
# execute the binary as a basic check
./%{name} --help

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
