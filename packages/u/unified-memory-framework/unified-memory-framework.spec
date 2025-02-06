#
# spec file for package unified-memory-framework
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


%define libname libumf0
Name:           unified-memory-framework
Version:        0.10.1
Release:        0
Summary:        oneAPI Unified Memory Framework (UMF)
License:        Apache-2.0
URL:            https://github.com/oneapi-src/unified-memory-framework
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hwloc-devel
BuildRequires:  level-zero-devel
BuildRequires:  libnuma-devel
BuildRequires:  ninja
BuildRequires:  tbb-devel

%description
The Unified Memory Framework (UMF) is a library for constructing allocators
and memory pools. It also contains broadly useful abstractions and utilities
for memory management. UMF allows users to manage multiple memory pools characterized
by different attributes, allowing certain allocation types to be isolated
from others and allocated using different hardware resources as required.

%package -n %{libname}
Summary:        oneAPI Unified Memory Framework (UMF)

%description -n %{libname}
The Unified Memory Framework (UMF) is a library for constructing allocators
and memory pools. UMF allows users to manage multiple memory pools characterized
by different attributes, allowing certain allocation types to be isolated
from others and allocated using different hardware resources as required.

%package devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}
Requires:       level-zero-devel
Recommends:     %{name}-doc

%description devel
The Unified Memory Framework (UMF) is a library for constructing allocators
and memory pools.

This package contains the development files for UMF.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
The Unified Memory Framework (UMF) is a library for constructing allocators
and memory pools.

This package contains the documentation for UMF.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake \
    -DUMF_BUILD_TESTS=OFF \
    -DUMF_BUILD_SHARED_LIBRARY=ON \
    -DUMF_LEVEL_ZERO_INCLUDE_DIR=%{_includedir}/level_zero \
    -DUMF_BUILD_CUDA_PROVIDER=OFF
%cmake_build

%install
%cmake_install

rm %{buildroot}%{_datadir}/doc/umf/licensing/third-party-programs.txt
rm %{buildroot}%{_datadir}/doc/umf/LICENSE.TXT

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
# licenses
%license LICENSE.TXT
%doc README.md
%doc licensing/third-party-programs.txt

%{_libdir}/libumf.so.0
%{_libdir}/libumf.so.0.0.0
%{_libdir}/libumf_proxy.so.0

%files devel
%{_libdir}/libumf.so
%{_libdir}/libumf_proxy.so
%{_includedir}/umf.h
%{_includedir}/umf/
%{_libdir}/cmake/umf/

%files doc
%if 0%{?sle_version} == 150500
%{_datadir}/doc/umf/
%else
%{_docdir}/unified-memory-framework/
%endif

%changelog
