#
# spec file for package spirv-cross
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


%define _ver 2020-05-19
%define _libver 0.33.0
%define _sover 0
%define _libname libspirv-cross-c-shared
%define _libpkg %{_libname}%{_sover}
%define __builder ninja
Name:           spirv-cross
Version:        20200403
Release:        0
Summary:        Tool and library for SPIR-V reflection and disassembly
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/KhronosGroup/SPIRV-Cross
Source0:        https://github.com/KhronosGroup/SPIRV-Cross/archive/%{_ver}.tar.gz#/%{name}-%{_ver}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig

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
Version:        %{_libver}
Release:        0
Summary:        Library for SPIR-V reflection and disassembly
Group:          System/Libraries

%description -n %{_libpkg}
SPIRV-Cross is a tool and library designed for parsing and
converting SPIR-V to other shader languages.

%package -n %{_libname}-devel
Version:        %{_libver}
Release:        0
Summary:        Development headers for the SPIRV-Cross library
Group:          Development/Libraries/C and C++
Requires:       %{_libpkg} = %{_libver}

%description -n %{_libname}-devel
SPIRV-Cross is a tool and library designed for parsing and
converting SPIR-V to other shader languages.

%prep
%setup -q -n SPIRV-Cross-%{_ver}
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
%{_libdir}/libspirv-cross-c-shared.so.%{_sover}
%{_libdir}/libspirv-cross-c-shared.so.%{_libver}

%files -n %{_libname}-devel
%{_libdir}/libspirv-cross-c-shared.so
%{_libdir}/pkgconfig/spirv-cross-c-shared.pc
%{_includedir}/spirv_cross

%changelog
