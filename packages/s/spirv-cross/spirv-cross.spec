#
# spec file for package spirv-cross
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


%define lname libspirv-cross-c-shared0
%define __builder ninja
%if 0%{?suse_version} < 1600
%define gcc_version 13
%endif

Name:           spirv-cross
Version:        1.4.313.0
Release:        0
Summary:        Tool and library for SPIR-V reflection and disassembly
License:        Apache-2.0 OR MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/KhronosGroup/SPIRV-Cross
Source0:        https://github.com/KhronosGroup/SPIRV-Cross/archive/vulkan-sdk-%version.tar.gz
BuildRequires:  cmake >= 3
BuildRequires:  gcc%{?gcc_version} >= 9
BuildRequires:  gcc%{?gcc_version}-c++ >= 9
BuildRequires:  ninja
BuildRequires:  pkg-config

%description
SPIRV-Cross is a tool and library designed for parsing and
converting SPIR-V to other shader languages.

Features:

* Conversion of SPIR-V to GLSL, MSL or HLSL
* Conversion of SPIR-V to a JSON reflection format
* Reflection API to simplify the creation of Vulkan pipeline layouts
* Reflection API to modify and tweak OpDecorations
* Support for "all" of vertex, fragment, tessellation, geometry and
  compute shaders.

%package -n %lname
Summary:        Library for SPIR-V reflection and disassembly
Group:          System/Libraries

%description -n %lname
SPIRV-Cross is a tool and library designed for parsing and
converting SPIR-V to other shader languages.

%package devel
Summary:        Development headers for the SPIRV-Cross library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version-%release
Obsoletes:      libspirv-cross-c-shared-devel < %version-%release
Provides:       libspirv-cross-c-shared-devel = %version-%release

%description devel
SPIRV-Cross is a tool and library designed for parsing and
converting SPIR-V to other shader languages.

%prep
%autosetup -p1 -n SPIRV-Cross-vulkan-sdk-%version
sed -i 's,$CMAKE_INSTALL_PREFIX/lib,%_libdir,;s,/share/pkgconfig,/%_lib/pkgconfig,;s,DESTINATION lib,DESTINATION %_lib,g' CMakeLists.txt

%build
%cmake \
	-DCMAKE_C_COMPILER="gcc%{?gcc_version:-%{gcc_version}}" \
	-DCMAKE_CXX_COMPILER="g++%{?gcc_version:-%{gcc_version}}" \
	-DSPIRV_CROSS_SHARED=ON -DSPIRV_CROSS_CLI=ON
%cmake_build

%install
%cmake_install
rm -fv %buildroot/%_libdir/*.a
# When static/shared library names aren't thought through...
for i in c core cpp glsl hlsl msl reflect util; do
	ln -s "libspirv-cross-c-shared.so" "%buildroot/%_libdir/libspirv-cross-$i.so"
done

%ldconfig_scriptlets -n %lname

%files
%license LICENSE
%doc README.md
%_bindir/spirv-cross

%files -n %lname
%_libdir/libspirv-cross-c-shared.so.*

%files devel
%_libdir/libspirv-cross-*.so
%_libdir/pkgconfig/*.pc
%_includedir/spirv_cross
%dir %_datadir/spirv*
%_datadir/spirv*/cmake/

%changelog
