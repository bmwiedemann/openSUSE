#
# spec file for package spirv-cross
#
# Copyright (c) 2023 SUSE LLC
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


%define _libpkg libspirv-cross-c-shared0
%define __builder ninja
Name:           spirv-cross
Version:        1.3.236.0
Release:        0
Summary:        Tool and library for SPIR-V reflection and disassembly
License:        Apache-2.0 OR MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/KhronosGroup/SPIRV-Cross
Source0:        https://github.com/KhronosGroup/SPIRV-Cross/archive/sdk-%version.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3
BuildRequires:  ninja
BuildRequires:  pkg-config

%description
SPIRV-Cross is a tool and library designed for parsing and
converting SPIR-V to other shader languages.

Features:
  * Conversion of SPIR-V to GLSL, MSL or HLSL
  * Conversion of SPIR-V to a JSON reflection format
  * Reflection API to simplify the creation of Vulkan pipeline
    layouts
  * Reflection API to modify and tweak OpDecorations
  * Support for "all" of vertex, fragment, tessellation, geometry
    and compute shaders.

%package -n %{_libpkg}
Summary:        Library for SPIR-V reflection and disassembly
Group:          System/Libraries

%description -n %{_libpkg}
SPIRV-Cross is a tool and library designed for parsing and
converting SPIR-V to other shader languages.

%package devel
Summary:        Development headers for the SPIRV-Cross library
Group:          Development/Libraries/C and C++
Requires:       %{_libpkg} = %{version}-%{release}
Obsoletes:      libspirv-cross-c-shared-devel < %{version}-%{release}
Provides:       libspirv-cross-c-shared-devel = %{version}-%{release}

%description devel
SPIRV-Cross is a tool and library designed for parsing and
converting SPIR-V to other shader languages.

%prep
%autosetup -p1 -n SPIRV-Cross-sdk-%{version}
sed -i 's,${CMAKE_INSTALL_PREFIX}/lib,%{_libdir},;s,/share/pkgconfig,/%{_lib}/pkgconfig,;s,DESTINATION lib,DESTINATION %{_lib},g' CMakeLists.txt

%build
%cmake \
    -DSPIRV_CROSS_SHARED=ON \
    -DSPIRV_CROSS_CLI=ON
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_libdir}/*.a
rm -r %{buildroot}%{_datadir}

%post -n %{_libpkg} -p /sbin/ldconfig
%postun -n %{_libpkg} -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_bindir}/spirv-cross

%files -n %{_libpkg}
%{_libdir}/libspirv-cross-c-shared.so.*

%files devel
%{_libdir}/libspirv-cross-c-shared.so
%{_libdir}/pkgconfig/spirv-cross-c-shared.pc
%{_includedir}/spirv_cross

%changelog
