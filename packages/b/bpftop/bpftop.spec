#
# spec file for package bpftop
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           bpftop
Version:        0.7.1
Release:        0
Summary:        Dynamic real-time view of running eBPF programs
License:        Apache-2.0
URL:            https://github.com/Netflix/bpftop
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.78
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(zlib)
ExclusiveArch:  %{rust_tier1_arches}

%description
bpftop provides a dynamic real-time view of running eBPF programs. It displays
the average runtime, events per second, and estimated total CPU % for each
program.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
%cargo_install

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
