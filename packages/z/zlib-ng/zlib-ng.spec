#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%define target @BUILD_FLAVOR@%{nil}
%if "%target" == "compat"
%bcond_without zlib_compat
%else
%bcond_with zlib_compat
%endif

%if %{with zlib_compat}
%define soversion 1
%define compat_suffix -compat
%else
%define soversion 2
%endif

%bcond_with     systemtap

Name:           zlib-ng%{?compat_suffix}
Version:        2.0.6
Release:        0
Summary:        Zlib replacement with SIMD optimizations
License:        Zlib
URL:            https://github.com/zlib-ng/zlib-ng
Source0:        https://github.com/zlib-ng/zlib-ng/archive/refs/tags/%{version}.tar.gz#/zlib-ng-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM - Backport https://github.com/zlib-ng/zlib-ng/pull/1297 to fix boo#1200578
Patch0:         1297.patch
BuildRequires:  cmake
BuildRequires:  gcc
%if %{with systemtap}
BuildRequires:  systemtap-sdt-devel
%endif

%description
zlib-ng is a zlib replacement with support for CPU intrinsics (SSSE3,
AVX2, NEON, VSX) when available.

%package -n     libz-ng%{?compat_suffix}%{soversion}
Summary:        Zlib replacement with SIMD optimizations
%if %{with zlib_compat}
Conflicts:      libz%{soversion}
%endif

%description -n libz-ng%{?compat_suffix}%{soversion}
zlib-ng is a zlib replacement with support for CPU intrinsics (SSSE3,
AVX2, NEON, VSX) when available.

%package        devel
Summary:        Development files for %{name}
Requires:       libz-ng%{?compat_suffix}%{soversion} = %{version}-%{release}
%if %{with zlib_compat}
Conflicts:      zlib-devel
Provides:       zlib-devel
%endif

%description    devel
The %{name}-devel package contains header files for
developing application that use %{name}.

%prep
%autosetup -p1 -n zlib-ng-%{version}

%build
# zlib-ng uses a different macro for library directory.
# 32-bit Arm requires to set soft/hard float
%cmake \
%ifarch %{arm}
  -DCMAKE_C_FLAGS=-mfloat-abi=hard \
%endif
%if %{with zlib_compat}
  -DZLIB_COMPAT=ON \
%endif
  -DINSTALL_LIB_DIR=%{_libdir}
%cmake_build

%install
%cmake_install

%check
# Tests fail when run in parallel.
# %%define _smp_mflags -j1
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
%ctest

%post -n libz-ng%{?compat_suffix}%{soversion} -p /sbin/ldconfig
%postun -n libz-ng%{?compat_suffix}%{soversion} -p /sbin/ldconfig

%files -n libz-ng%{?compat_suffix}%{soversion}
%if %{with zlib_compat}
%{_libdir}/libz.so.%{soversion}*
%else
%{_libdir}/libz-ng.so.%{soversion}*
%endif
%license LICENSE.md
%doc README.md

%files devel
%if %{with zlib_compat}
%{_includedir}/zconf.h
%{_includedir}/zlib.h
%{_libdir}/libz.so
%{_libdir}/pkgconfig/zlib.pc
%else
%{_includedir}/zconf-ng.h
%{_includedir}/zlib-ng.h
%{_libdir}/libz-ng.so
%{_libdir}/pkgconfig/zlib-ng.pc
%endif

%changelog
