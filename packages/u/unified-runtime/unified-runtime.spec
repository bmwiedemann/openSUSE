#
# spec file for package unified-runtime
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


%if 0%{?suse_version} > 1600
%bcond_without opencl_adapter
%else
%bcond_with opencl_adapter
%endif
Name:           unified-runtime
Version:        0.11.4
Release:        0
Summary:        oneAPI Unified Runtime (UR)
License:        Apache-2.0
URL:            https://github.com/oneapi-src/unified-runtime
Source0:        %{name}-%{version}.tar.gz
Patch1:         remove-link.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  unified-memory-framework-devel
%if %{with opencl_adapter}
BuildRequires:  pkgconfig(OpenCL)
%endif

%description
oneAPI Unified Runtime (UR) provides a unified interface to device
agnostic runtimes such as DPC++.
UR provides extensibility where new backends can be developed to
support new software platforms and devices.

%package devel
Summary:        Development files for the oneAPI Unified Runtime
Requires:       pkgconfig
Requires:       unified-memory-framework-devel

%description devel
oneAPI Unified Runtime (UR) provides a unified interface to device
agnostic runtimes such as DPC++.

This package contains the development files for the oneAPI Unified Runtime.

%package -n libur_loader0
Summary:        oneAPI Unified Runtime loader

%description -n libur_loader0
oneAPI Unified Runtime (UR) provides a unified interface to device
agnostic runtimes such as DPC++.

This package contains the oneAPI Unified Runtime loader.

%package -n libur_adapter_native_cpu0
Summary:        oneAPI Unified Runtime native CPU adapter

%description -n libur_adapter_native_cpu0
oneAPI Unified Runtime (UR) provides a unified interface to device
agnostic runtimes such as DPC++.

This package contains the oneAPI Unified Runtime native CPU adapter.

%package -n libur_adapter_opencl0
Summary:        oneAPI Unified Runtime OpenCL adapter

%description -n libur_adapter_opencl0
oneAPI Unified Runtime (UR) provides a unified interface to device
agnostic runtimes such as DPC++.

This package contains the oneAPI Unified Runtime OpenCL adapter.

%prep
%autosetup -p1

%build
%define __builder ninja
# the static library is needed by the produced cmake files
# otherwise, when using find_package, CMake throws an error
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
%cmake \
    -DUR_USE_EXTERNAL_UMF=ON \
    -DUR_BUILD_TESTS=OFF \
    -DUR_BUILD_ADAPTER_NATIVE_CPU=ON \
%if %{with opencl_adapter}
    -DUR_BUILD_ADAPTER_OPENCL=ON \
    -DUR_OPENCL_INCLUDE_DIR=%{_includedir} \
%endif
    -DCMAKE_SKIP_RPATH=ON
%cmake_build
%cmake_build urinfo

%install
%cmake_install

install -Dm 755 build/bin/urinfo %{buildroot}%{_bindir}/urinfo

rm %{buildroot}%{_includedir}/.clang-format

%ldconfig_scriptlets -n libur_loader0
%ldconfig_scriptlets -n libur_adapter_native_cpu0

%if %{with opencl_adapter}
%ldconfig_scriptlets -n libur_adapter_opencl0
%endif

%files
%license LICENSE.TXT
%doc README.md
%{_bindir}/urinfo

%files devel
%{_includedir}/ur_api.h
%{_includedir}/ur_api_funcs.def
%{_includedir}/ur_ddi.h
%{_includedir}/ur_print.h
%{_includedir}/ur_print.hpp
%{_libdir}/pkgconfig/libur_loader.pc

%dir %{_prefix}/lib/cmake/
%{_prefix}/lib/cmake/unified-runtime/
%{_libdir}/libur_loader.so
%{_libdir}/libur_adapter_native_cpu.so
# The cmake file looks for .a unconditionally, so splitting to -devel-static seems to have no benefit presently
%{_libdir}/libur_common.a

%if %{with opencl_adapter}
%{_libdir}/libur_adapter_opencl.so
%endif

%files -n libur_loader0
%{_libdir}/libur_loader.so.0*

%files -n libur_adapter_native_cpu0
%{_libdir}/libur_adapter_native_cpu.so.0*

%if %{with opencl_adapter}
%files -n libur_adapter_opencl0
%{_libdir}/libur_adapter_opencl.so.0*
%endif

%changelog
