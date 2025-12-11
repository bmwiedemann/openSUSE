#
# spec file for package spirv-tools
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define _lto_cflags %nil
%define lname libSPIRV-Tools-2025_5_rc1

# Leap 15 and SLES 15 defaults to GCC 7, which does not have stable C++17 ABI.
# See https://bugzilla.suse.com/show_bug.cgi?id=1235697
%if 0%{?suse_version} < 1600
%define gcc_version 13
%endif

Name:           spirv-tools
Version:        2025.5~rc1
Release:        0
Summary:        API and commands for processing SPIR-V modules
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/KhronosGroup/SPIRV-Tools
Source:         https://github.com/KhronosGroup/SPIRV-Tools/archive/refs/tags/v2025.5.rc1.tar.gz
Source9:        baselibs.conf
Patch1:         ver.diff
BuildRequires:  bison
BuildRequires:  cmake >= 3.17.2
BuildRequires:  gcc%{?gcc_version} >= 9
BuildRequires:  gcc%{?gcc_version}-c++ >= 9
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  python3-xml
BuildRequires:  spirv-headers >= 1.6.4+sdk335

%description
The package includes an assembler, binary module parser,
disassembler, and validator for SPIR-V.

%package -n %lname
Summary:        SPIR-V tool component library
Group:          System/Libraries

%description -n %lname
The SPIR-V Tool library contains all of the implementation details
driving the SPIR-V assembler, binary module parser, disassembler and
validator, and is used in the standalone tools whilst also enabling
integration into other code bases directly.

%package devel
Summary:        Development headers for the SPIR-V tool library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
The SPIR-V Tool library contains all of the implementation details
driving the SPIR-V assembler, binary module parser, disassembler and
validator, and is used in the standalone tools whilst also enabling
integration into other code bases directly.

%prep
%autosetup -p1 -n SPIRV-Tools-2025.5.rc1
find . -type f -name CMakeLists.txt -exec \
	perl -i -pe 's{\@PACKAGE_VERSION\@}{%version}' CMakeLists.txt {} +

%build
%cmake -DSPIRV-Headers_SOURCE_DIR="%_prefix" \
	-DCMAKE_C_COMPILER="gcc%{?gcc_version:-%{gcc_version}}" \
	-DCMAKE_CXX_COMPILER="g++%{?gcc_version:-%{gcc_version}}" \
	-DSPIRV_TOOLS_BUILD_STATIC:BOOL=OFF -DBUILD_SHARED_LIBS:BOOL=ON
%cmake_build

%install
%cmake_install
perl -i -lpe 's{^#!/usr/bin/env sh$}{#!/bin/sh}' "%buildroot/%_bindir/spirv-lesspipe.sh"
for i in "" "-diff" "-link" "-lint" "-opt" "-reduce" "-shared"; do
	ln -s "libSPIRV-Tools$i-%version.so" "%buildroot/%_libdir/libSPIRV-Tools$i.so"
done

%ldconfig_scriptlets -n %lname

%files
%_bindir/spirv-*
%doc LICENSE

%files -n %lname
%_libdir/libSPIRV-Tools-*2*.so

%files devel
%_libdir/cmake/
%_libdir/libSPIRV-Tools.so
%_libdir/libSPIRV-Tools-diff.so
%_libdir/libSPIRV-Tools-link.so
%_libdir/libSPIRV-Tools-lint.so
%_libdir/libSPIRV-Tools-opt.so
%_libdir/libSPIRV-Tools-reduce.so
%_libdir/libSPIRV-Tools-shared.so
%_libdir/pkgconfig/SPIRV-Tools.pc
%_libdir/pkgconfig/SPIRV-Tools-shared.pc
%_includedir/spirv-tools/

%changelog
