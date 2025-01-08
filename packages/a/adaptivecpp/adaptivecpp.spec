#
# spec file for package adaptivecpp
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


Name:           adaptivecpp
Version:        24.10.0~0
Release:        0
Summary:        Open implementation of SYCL for CPUs and GPUs
License:        BSD-2-Clause
URL:            https://adaptivecpp.github.io
Source:         %{name}-%{version}.tar.gz
Patch1:         0001-Use-bin-env-python3-instead-of-python3-in-scripts.patch
Patch2:         0002-Remove-realpath-in-acpp.patch
BuildRequires:  boost-devel
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libboost_context-devel
BuildRequires:  libboost_fiber-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libedit-devel
BuildRequires:  llvm
BuildRequires:  llvm-devel
BuildRequires:  make
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  terminfo
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
ExcludeArch:    i586

%description
AdaptiveCpp is an open implementation of SYCL and C++ standard parallelism
for CPUs and GPUs from all vendors.

%package -n libacpp-common
Summary:        Common library for AdaptiveCpp
Obsoletes:      libadaptivecpp <= %{version}-%{release}

%description -n libacpp-common
AdaptiveCpp is an open implementation of SYCL and C++ standard parallelism
for CPUs and GPUs from all vendors.

This package contains the common library for AdaptiveCpp.

%package -n libacpp-clang
Summary:        Clang plugin for AdaptiveCpp
Requires:       libacpp-bitcode
Provides:       libacpp-clang = %{version}
Obsoletes:      libadaptivecpp <= %{version}-%{release}

%description -n libacpp-clang
AdaptiveCpp is an open implementation of SYCL and C++ standard parallelism
for CPUs and GPUs from all vendors.

This package contains the Clang plugin for AdaptiveCpp.

%package -n libacpp-rt
Summary:        Runtime library for AdaptiveCpp
Requires:       adaptivecpp-rt
Provides:       libacpp
Provides:       libadaptivecpp = %{version}-%{release}
Obsoletes:      libadaptivecpp <= %{version}-%{release}

%description -n libacpp-rt
AdaptiveCpp is an open implementation of SYCL and C++ standard parallelism
for CPUs and GPUs from all vendors.

This package contains the runtime library for AdaptiveCpp.

%package -n libacpp-rt-omp
Summary:        OpenMP runtime for AdaptiveCpp
Provides:       adaptivecpp-rt
Obsoletes:      libadaptivecpp-omp <= %{version}-%{release}

%description -n libacpp-rt-omp
AdaptiveCpp is an open implementation of SYCL and C++ standard parallelism
for CPUs and GPUs from all vendors.

This package contains the OpenMP runtime for AdaptiveCpp.

%package -n libacpp-bitcode
Summary:        Bitcode for AdaptiveCpp
Obsoletes:      libadaptivecpp <= %{version}-%{release}
BuildArch:      noarch

%description -n libacpp-bitcode
AdaptiveCpp is an open implementation of SYCL and C++ standard parallelism
for CPUs and GPUs from all vendors.

This package contains the bitcode for AdaptiveCpp JIT compilation.

%package -n libacpp-llvm-to-backend
Summary:        LLVM to backend for AdaptiveCpp
Requires:       libacpp-bitcode
Obsoletes:      libadaptivecpp <= %{version}-%{release}

%description -n libacpp-llvm-to-backend
LLVM to backend for AdaptiveCpp

%package devel
Summary:        Development files for libadaptivecpp
Requires:       adaptivecpp = %{version}
Requires:       libacpp-clang = %{version}
Obsoletes:      libadaptivecpp-devel <= %{version}-%{release}

%description devel
Development files for AdaptiveCpp

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake

%cmake_build

%install
%cmake_install
%fdupes -s %{buildroot}%{_prefix}/lib/
%fdupes -s %{buildroot}%{_includedir}/
%fdupes -s %{buildroot}%{_bindir}/

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_bindir}/acpp
%{_bindir}/acpp-hcf-tool
%{_bindir}/acpp-appdb-tool
%{_bindir}/acpp-info
%{_bindir}/syclcc
%{_bindir}/syclcc-clang

# Leap <= 15.6
%if 0%{?sle_version} <= 150600 && 0%{?is_opensuse}
%dir %{_prefix}%{_sysconfdir}/
%endif

%files devel
%{_includedir}/AdaptiveCpp/
%dir %{_prefix}/lib/cmake/
%{_prefix}/lib/cmake/AdaptiveCpp/
%{_prefix}/lib/cmake/OpenSYCL/
%{_prefix}/lib/cmake/hipSYCL/
%dir %{_prefix}%{_sysconfdir}/AdaptiveCpp
%{_prefix}%{_sysconfdir}/AdaptiveCpp/acpp-core.json

%files -n libacpp-common
%{_prefix}/lib/libacpp-common.so

%files -n libacpp-clang
%{_prefix}/lib/libacpp-clang.so

%files -n libacpp-rt
%{_prefix}/lib/libacpp-rt.so

%files -n libacpp-bitcode
%dir %{_prefix}/lib/hipSYCL/
%{_prefix}/lib/hipSYCL/bitcode/

%files -n libacpp-rt-omp
%{_prefix}/lib/hipSYCL/librt-backend-omp.so

%files -n libacpp-llvm-to-backend
%dir %{_prefix}/lib/hipSYCL/
%{_prefix}/lib/hipSYCL/llvm-to-backend/

%changelog
