#
# spec file for package shaderc
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


Name:           shaderc
%define lname libshaderc_shared1
Version:        2020.3
Release:        0
Summary:        A collection of tools, libraries and tests for shader compilation
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://github.com/google/shaderc

#Git-Clone:	https://github.com/google/shaderc
Source:         https://github.com/google/shaderc/archive/v%version.tar.gz
Patch1:         0001-Use-system-third-party-libs.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  glslang-devel >= 8.13.3727+git4
BuildRequires:  python-xml
BuildRequires:  spirv-headers >= 1.5.1.corrected+git24
BuildRequires:  spirv-tools-devel >= 2020.2

%description
A collection of tools, libraries and tests for shader compilation.
At the moment, included are:

* glslc, a command line compiler for GLSL/HLSL to SPIR-V, and
* libshaderc, a library API for doing the same.

Shaderc wraps around core functionality in glslang and SPIRV-Tools.

%package -n %lname
Summary:        SPIR-V shader compiler library
Group:          System/Libraries

%description -n %lname
A compiler library for GLSL/HLSL to SPIR-V.

Shaderc wraps around core functionality in glslang and SPIRV-Tools

%package devel
Summary:        Header files for the shaderc library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A compiler library for GLSL/HLSL to SPIR-V.

Shaderc wraps around core functionality in glslang and SPIRV-Tools

%prep
%autosetup -p1
echo "\"%version\"" >glslc/src/build-version.inc

%build
%cmake -DSHADERC_SKIP_TESTS=ON
%make_jobs

%install
%cmake_install
rm %buildroot/%_libdir/*.a

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%license LICENSE
%_bindir/glslc

%files -n %lname
%_libdir/libshaderc_shared.so.1*

%files devel
%_includedir/shaderc/
%_libdir/libshaderc_shared.so
%_libdir/pkgconfig/*.pc

%changelog
