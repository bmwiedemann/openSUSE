#
# spec file for package sleef
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2023 Fabio Pesari
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


%define v_major 3
%define v_minor 9
%define v_patch 0

Name:           sleef
Version:        %{v_major}.%{v_minor}.%{v_patch}
Release:        0
Summary:        SIMD Library for Evaluating Elementary Functions, vectorized libm and DFT
License:        BSL-1.0
Group:          Productivity/Scientific/Math
URL:            https://sleef.org/
Source:         https://github.com/shibatch/sleef/archive/refs/tags/%{v_major}.%{v_minor}.%{v_patch}.tar.gz#/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  fftw3-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  gmp-devel
BuildRequires:  ninja

%description
SLEEF is a library that implements vectorized versions of C standard math
functions. This library also includes DFT subroutines.

%package -n libsleef%{v_major}
Summary:        SIMD Library for Evaluating Elementary Functions, vectorized libm and DFT
License:        BSL-1.0
Group:          System/Libraries

%description -n libsleef%{v_major}
SLEEF is a library that implements vectorized versions of C standard math
functions. This library also includes DFT subroutines.

%package devel
Summary:        Development files for SLEEF
License:        BSL-1.0
Group:          Development/Languages/C and C++
Requires:       libsleef%{v_major} = %{version}

%description devel
SLEEF is a library that implements vectorized versions of C standard math
functions. This library also includes DFT subroutines.

These are the development files for SLEEF.

%prep
%autosetup

%build
%define __builder ninja
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
%ifarch aarch64
    -DCOMPILER_SUPPORTS_SVE=OFF \
%endif
    -DSLEEF_ENABLE_TLFLOAT=OFF
%cmake_build

%install
%cmake_install

%post -n libsleef%{v_major} -p /sbin/ldconfig
%postun -n libsleef%{v_major} -p /sbin/ldconfig

%files -n libsleef%{v_major}
%license LICENSE.txt
%{_libdir}/libsleef*.so.*

%files devel
%doc README.adoc
%license LICENSE.txt
%{_libdir}/libsleef*.so
%{_includedir}/sleef.h
%dir %{_libdir}/cmake/sleef/
%{_libdir}/cmake/sleef/*.cmake
%{_libdir}/pkgconfig/sleef.pc

%changelog
