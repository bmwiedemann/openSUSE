#
# spec file for package rz-ghidra
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


Name:           rz-ghidra
Version:        0.7.0
Release:        0
Summary:        Deep ghidra decompiler integration for rizin and rz-cutter
URL:            https://github.com/rizinorg/rz-ghidra
Source0:        https://github.com/rizinorg/rz-ghidra/releases/download/v%{version}/%{name}-src-v%{version}.tar.gz
License:        LGPL-3.0-only
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Cutter)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Rizin)

%description
rz-ghidra is an integration of the Ghidra decompiler and Sleigh Disassembler for Rizin.
It is solely based on the decompiler part of Ghidra, which is written entirely in C++,
so Ghidra itself is not required at all and the plugin can be built self-contained

%package devel
Summary:        Development files for the rz-ghidra package
Requires:       %{name} = %{version}

%description devel
Development files for the rz-ghidra package. See rz-ghidra package for more
information.

%prep
%setup -q -n %{name}

%build
%cmake \
    -DCUTTER_INSTALL_PLUGDIR=%{_datadir}/rizin/cutter/plugins/native \
    -DBUILD_CUTTER_PLUGIN=ON \
    -DBUILD_SLASPECS=ON

%cmake_build

%install
%cmake_install

%check

%files
%{_libdir}/rizin/
%{_datadir}/rizin/

%files devel
%{_includedir}/rz_ghidra.h
%{_libdir}/pkgconfig/rz_ghidra.pc

%changelog
