#
# spec file for package adaptivecpp
#
# Copyright (c) 2024 SUSE LLC
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
Version:        24.06.0~0
Release:        0
Summary:        Open implementation of SYCL for CPUs and GPUs
License:        BSD-2-Clause
URL:            https://adaptivecpp.github.io
Source:         %{name}-%{version}.tar.gz
Patch1:         0001-Use-bin-env-python3-instead-of-python3-in-scripts.patch
Patch2:         0002-CMake-acpp-clang-to-MODULE.patch
Patch3:         0003-Remove-realpath-in-acpp.patch
BuildRequires:  boost-devel
BuildRequires:  clang18
BuildRequires:  clang18-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libboost_context-devel
BuildRequires:  libboost_fiber-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libedit-devel
BuildRequires:  libomp18-devel
# todo: remove version specifier on next v.
BuildRequires:  llvm18
BuildRequires:  llvm18-devel
BuildRequires:  make
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  terminfo
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
Requires:       clang18
Requires:       libadaptivecpp = %{version}
ExcludeArch:    i586

%description
A C++ compiler that supports the SYCL standard and C++ standard parallelism for CPUs and
GPUs from all vendors.

%package -n libadaptivecpp
Summary:        Library for AdaptiveCpp
Requires:       libadaptivecpp-omp
Requires:       libadaptivecpp-rt

%description -n libadaptivecpp
Implementation of SYCL and C++ standard parallelism for CPUs and GPUs from all vendors.

%package -n libadaptivecpp-omp
Summary:        OpenMP runtime for AdaptiveCpp
Requires:       libadaptivecpp = %{version}
Provides:       libadaptivecpp-rt

%description -n libadaptivecpp-omp
Implementation of SYCL and C++ standard parallelism for CPUs and GPUs from all vendors.
This package contains the OpenMP runtime for AdaptiveCpp.

%package -n libadaptivecpp-devel
Summary:        Development files for libadaptivecpp

%description -n libadaptivecpp-devel
Development files for libadaptivecpp

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
%dir %{_prefix}%{_sysconfdir}/AdaptiveCpp
%{_prefix}%{_sysconfdir}/AdaptiveCpp/acpp-core.json

# Leap <= 15.6
%if 0%{?sle_version} <= 150600 && 0%{?is_opensuse}
%dir %{_prefix}%{_sysconfdir}/
%endif

%files -n libadaptivecpp
%{_prefix}/lib/libacpp-clang.so
%{_prefix}/lib/libacpp-common.so
%{_prefix}/lib/libacpp-rt.so
%dir %{_prefix}/lib/hipSYCL
%{_prefix}/lib/hipSYCL/bitcode/
%{_prefix}/lib/hipSYCL/llvm-to-backend/

%files -n libadaptivecpp-omp
%{_prefix}/lib/hipSYCL/librt-backend-omp.so

%files -n libadaptivecpp-devel
%{_includedir}/AdaptiveCpp/
%dir %{_prefix}/lib/cmake/
%{_prefix}/lib/cmake/AdaptiveCpp/
%{_prefix}/lib/cmake/OpenSYCL/
%{_prefix}/lib/cmake/hipSYCL/

%changelog
