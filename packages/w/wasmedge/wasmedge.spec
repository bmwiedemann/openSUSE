#
# spec file for package wasmedge
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


Name:           wasmedge
Version:        0.13.5
Release:        0
Summary:        High-performance and extensible WebAssembly runtime
License:        Apache-2.0 AND CC0-1.0
Group:          Development/Tools/Other
URL:            https://github.com/WasmEdge/WasmEdge
Source0:        https://github.com/WasmEdge/WasmEdge/releases/download/%{version}/%{name}-%{version}-src.tar.gz
BuildRequires:  boost-devel
BuildRequires:  cmake >= 3.15.0
BuildRequires:  gcc-c++ >= 9.4.0
BuildRequires:  spdlog-devel
# Supported platforms
ExclusiveArch:  x86_64 aarch64

%description
WasmEdge is a lightweight, high-performance, and extensible WebAssembly runtime
for cloud native, edge, and decentralized applications. It powers serverless
apps, embedded functions, microservices, smart contracts, and IoT devices.

%package -n libwasmedge0
Summary:        WasmEdge library
Group:          System/Libraries

%description -n libwasmedge0
Library for WasmEdge.

%package devel
Summary:        Development files for WasmEdge
Group:          Development/Libraries/C and C++
Requires:       libwasmedge0 = %{version}

%description devel
This package contains the header files and libraries needed for
compiling programs using WasmEdge.

%prep
%autosetup -n %{name}

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBUILD_SHARED_LIBS=OFF -DWASMEDGE_BUILD_TESTS=OFF -DWASMEDGE_BUILD_AOT_RUNTIME=OFF
%cmake_build

%install
%cmake_install

%post -n libwasmedge0 -p /sbin/ldconfig
%postun -n libwasmedge0 -p /sbin/ldconfig

%files
%license LICENSE LICENSE.spdx
%doc README.md SECURITY.md
%{_bindir}/wasmedge

%files -n libwasmedge0
%{_libdir}/libwasmedge.so.0*

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/libwasmedge.so

%changelog
