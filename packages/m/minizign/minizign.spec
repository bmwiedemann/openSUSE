#
# spec file for package minizign
#
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           minizign
Version:        0.1.7
Release:        0
Summary:        Minisign reimplemented in Zig
License:        ISC
URL:            https://github.com/jedisct1/zig-minisign
Source:         https://github.com/jedisct1/zig-minisign/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  zig >= 0.15
BuildRequires:  zig-rpm-macros
# this is supposed to be %%zig_arches from zig-rpm-macros but it is not pulled in by OBS scheduler
# ExclusiveArch: %%zig_arches
ExclusiveArch: x86_64 aarch64 riscv64 %{mips64}

%description
A Zig implementation of Minisign. minizign supports signature verification,
signing, and key generation.

%prep
%autosetup -p1 -n zig-minisign-%{version}

%build
%zig_build

%install
%zig_install

%check
%zig_test

%files
%license LICENSE
%doc README.md
%{_bindir}/minizign

%changelog
