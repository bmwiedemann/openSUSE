#
# spec file for package spirv-tools
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


%define lname libSPIRV-Tools-suse18

Name:           spirv-tools
Version:        2020.3
Release:        0
Summary:        API and commands for processing SPIR-V modules
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/KhronosGroup/SPIRV-Tools

Source:         https://github.com/KhronosGroup/SPIRV-Tools/archive/v%version.tar.gz
Source9:        baselibs.conf
Patch1:         ver.diff
Patch2:         gcc48.diff
BuildRequires:  bison
BuildRequires:  cmake >= 2.8.12
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  python3-xml
BuildRequires:  spirv-headers >= 1.5.1.corrected+git24

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
%setup -qn SPIRV-Tools-%version
%autopatch -p1

%build
%cmake -D"SPIRV-Headers_SOURCE_DIR=%_prefix"
make %{?_smp_mflags}

%install
%cmake_install

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_bindir/spirv-*
%doc LICENSE

%files -n %lname
%_libdir/libSPIRV-Tools.so.*
%_libdir/libSPIRV-Tools-link.so.*
%_libdir/libSPIRV-Tools-opt.so.*
%_libdir/libSPIRV-Tools-reduce.so.*
%_libdir/libSPIRV-Tools-shared.so.*

%files devel
%_libdir/cmake/
%_libdir/libSPIRV-Tools.so
%_libdir/libSPIRV-Tools-link.so
%_libdir/libSPIRV-Tools-opt.so
%_libdir/libSPIRV-Tools-reduce.so
%_libdir/libSPIRV-Tools-shared.so
%_libdir/pkgconfig/SPIRV-Tools.pc
%_libdir/pkgconfig/SPIRV-Tools-shared.pc
%_includedir/spirv-tools/

%changelog
