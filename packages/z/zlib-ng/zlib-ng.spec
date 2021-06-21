#
# spec file for package zlib-ng
#
# Copyright (c) 2021 SUSE LLC
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

%define soversion 2

Name:           zlib-ng
Version:        2.0.4
Release:        0
Summary:        Zlib replacement with SIMD optimizations
License:        Zlib
Url:            https://github.com/zlib-ng/zlib-ng
Source0:        https://github.com/zlib-ng/zlib-ng/archive/refs/tags/%{version}.tar.gz#/zlib-ng-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  systemtap-sdt-devel
 
%description
zlib-ng is a zlib replacement with support for CPU intrinsics (SSSE3,
AVX2, NEON, VSX) when available.
 
%package -n     libz-ng%{soversion}
Summary:        Zlib replacement with SIMD optimizations
 
%description -n libz-ng%{soversion}
zlib-ng is a zlib replacement with support for CPU intrinsics (SSSE3,
AVX2, NEON, VSX) when available.

%package        devel
Summary:        Development files for %{name}
Requires:       libz-ng%{soversion} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains header files for
developing application that use %{name}.
 
%prep
%autosetup -p1
 
%build
# zlib-ng uses a different macro for library directory.
# 32-bit Arm requires to set soft/hard float
%cmake \
%ifarch %{arm}
  -DCMAKE_C_FLAGS=-mfloat-abi=hard \
%endif
  -DWITH_SANITIZERS=ON \
  -DINSTALL_LIB_DIR=%{_libdir}
%cmake_build

%install
%cmake_install

%check
# Tests fail when run in parallel.
# %%define _smp_mflags -j1
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
%ctest

%post -n libz-ng%{soversion} -p /sbin/ldconfig
%postun -n libz-ng%{soversion} -p /sbin/ldconfig

%files -n libz-ng%{soversion}
%{_libdir}/libz-ng.so.%{soversion}*
%license LICENSE.md
%doc README.md
 
%files devel
%{_includedir}/zconf-ng.h
%{_includedir}/zlib-ng.h
%{_libdir}/libz-ng.so
%{_libdir}/pkgconfig/%{name}.pc
 
%changelog
