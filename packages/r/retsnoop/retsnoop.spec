#
# spec file for package retsnoop
#
# Copyright (c) 2025 SUSE LLC
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


Name:           retsnoop
Version:        0.11
Release:        0
Summary:        Investigate kernel error call stacks
License:        BSD-2-Clause
URL:            https://github.com/anakryiko/retsnoop/
Source:         %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  clang >= 12
BuildRequires:  libelf-devel
BuildRequires:  linux-glibc-devel >= 4.5
BuildRequires:  llvm >= 12
BuildRequires:  zlib-devel

%description
Retsnoop is a BPF-based tool for non-intrusive mass-tracing of Linux kernel
internals. Retsnoop's main goal is to provide a flexible and ergonomic way
to extract the exact information from the kernel that is useful to the user.
Retsnoop achieves its goal by low-overhead non-intrusive tracing of a
of kernel functions, intercepting their entries and exits. Retsnoop's central
concept is a user-specified set of kernel functions of interest. This allows
retsnoop to capture high-relevance data by letting the user flexibly control
a relevant subset of kernel functions. All other kernel functions are ignored
and don't pollute captured data with irrelevant information.

%prep
%autosetup -p1 -a1

%build
cd %{_builddir}/%{name}-%{version}/src
%make_build

%install
install -D -m0755 -s src/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
