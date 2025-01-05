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


Name:           unified-runtime
Version:        0.11.2
Release:        0
Summary:        oneAPI Unified Runtime (UR)
License:        Apache-2.0
URL:            https://github.com/oneapi-src/unified-runtime
Source0:        %{name}-%{version}.tar.gz
Patch1:         remove-link.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
BuildRequires:  unified-memory-framework-devel

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
%cmake \
    -DUR_USE_EXTERNAL_UMF=ON \
    -DUR_BUILD_TESTS=OFF \
    -DUR_BUILD_ADAPTER_NATIVE_CPU=ON \
    -DUR_BUILD_ADAPTER_OPENCL=ON \
    -DUR_OPENCL_INCLUDE_DIR=%{_includedir} \
    -DCMAKE_SKIP_RPATH=ON
%cmake_build
%cmake_build urinfo

%install
%cmake_install

install -Dm 755 build/bin/urinfo %{buildroot}%{_bindir}/urinfo

rm %{buildroot}%{_includedir}/.clang-format
rm %{buildroot}%{_libdir}/libur_common.a

%ldconfig_scriptlets -n libur_loader0
%ldconfig_scriptlets -n libur_adapter_native_cpu0
%ldconfig_scriptlets -n libur_adapter_opencl0

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
%{_libdir}/libur_adapter_opencl.so

%files -n libur_loader0
%{_libdir}/libur_loader.so.0
%{_libdir}/libur_loader.so.0.11.2

%files -n libur_adapter_native_cpu0
%{_libdir}/libur_adapter_native_cpu.so.0
%{_libdir}/libur_adapter_native_cpu.so.0.11.2

%files -n libur_adapter_opencl0
%{_libdir}/libur_adapter_opencl.so.0
%{_libdir}/libur_adapter_opencl.so.0.11.2

%changelog
