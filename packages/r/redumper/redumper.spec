#
# spec file for package redumper
#
# Copyright (c) 2024-2025, Martin Hauke <mardnh@gmx.de>
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


Name:           redumper
Version:        532
Release:        0
Summary:        Low level CD dumper utility
License:        GPL-3.0-only
Group:          Productivity/Multimedia/CD/Grabbers
URL:            https://github.com/superg/redumper/
Source:         https://github.com/superg/redumper/archive/refs/tags/build_%{version}.tar.gz#/%{name}-build_%{version}.tar.gz
BuildRequires:  clang19
BuildRequires:  cmake
BuildRequires:  libstdc++6-devel-gcc15
BuildRequires:  lld19
BuildRequires:  llvm19-devel
BuildRequires:  ninja
ExclusiveArch:  x86_64

%description
redumper is a low-level byte perfect CD disc dumper.

It supports incremental dumps, advanced SCSI/C2 repair,
intelligent audio CD offset detection and a lot of other features.
redumper also is a general purpose DVD/HD-DVD/Blu-ray disc dumper.

%prep
%autosetup -p1 -n redumper-build_%{version}

%build
%define _lto_cflags %{nil}
%define __builder ninja
%cmake \
  -DCMAKE_CXX_COMPILER="clang++-19" \
  -DCMAKE_C_COMPILER="clang-19" \
  -DCMAKE_CXX_FLAGS="-I/usr/lib64/clang/19/include/"
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/redumper

%changelog
