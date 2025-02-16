#
# spec file for package zlib-ng
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


%define target @BUILD_FLAVOR@%{nil}
%if "%{target}" == "compat"
%bcond_without zlib_compat
%else
%bcond_with zlib_compat
%endif
%bcond_with     systemtap
%if %{with zlib_compat}
%define soversion 1
%define compat_suffix -compat
%else
%define soversion 2
%endif
Name:           zlib-ng%{?compat_suffix}
Version:        2.2.3
Release:        0
Summary:        Zlib replacement with SIMD optimizations
License:        Zlib
URL:            https://github.com/zlib-ng/zlib-ng
Source0:        https://github.com/zlib-ng/zlib-ng/archive/refs/tags/%{version}.tar.gz#/zlib-ng-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libabigail-tools
BuildRequires:  cmake(GTest)
%if %{with systemtap}
BuildRequires:  systemtap-sdt-devel
%endif

%description
zlib-ng is a zlib replacement with support for CPU intrinsics (SSSE3,
AVX2, NEON, VSX) when available.

%package -n     libz-ng%{?compat_suffix}%{soversion}
Summary:        Zlib replacement with SIMD optimizations

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
export CC=gcc
%cmake \
%ifarch %{arm32}
  -DCMAKE_C_FLAGS="%{optflags} -mfloat-abi=hard" \
%endif
%ifnarch armv6l armv6hl
  -DWITH_ARMV6:BOOL=OFF \
%endif
%if %{with zlib_compat}
  -DZLIB_COMPAT=ON -DWITH_NEW_STRATEGIES=OFF \
%endif
  -DINSTALL_LIB_DIR=%{_libdir} \
  -DWITH_RVV=OFF \
  -DWITH_GTEST=OFF
%cmake_build

%install
%cmake_install
%if %{with zlib_compat}
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
mkdir -p %{buildroot}%{_libdir}/zlib-ng-compat
(cat > %{buildroot}%{_sysconfdir}/ld.so.conf.d/zlib-ng-compat-%{_arch}.conf) <<-EOF
	%{_libdir}/zlib-ng-compat
	EOF
pushd %{buildroot}%{_libdir}/
	mv libz.so.* zlib-ng-compat/
	ln -sf zlib-ng-compat/libz.so.1 libz.so
popd
%endif

%check
# Tests fail when run in parallel.
# %%define _smp_mflags -j1
%if %{with zlib_compat}
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}/zlib-ng-compat
%else
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
%endif
%ctest

%ifarch ppc64le
%global target_cpu powerpc64le
%else
%global target_cpu %{_target_cpu}
%endif
%ifarch x86_64
%global cpu_vendor pc
%else
%global cpu_vendor unknown
%endif

%ifarch aarch64 ppc64le x86_64
%global __cmake_builddir %{_vpath_builddir}
export CC=gcc
export CFLAGS="%{optflags} -fPIC"
%if %{with zlib_compat}
CHOST=%{target_cpu}-%{cpu_vendor}-linux-gnu sh test/abicheck.sh --zlib-compat
%else
CHOST=%{target_cpu}-%{cpu_vendor}-linux-gnu sh test/abicheck.sh
%endif
%endif

%post -n libz-ng%{?compat_suffix}%{soversion} -p /sbin/ldconfig
%postun -n libz-ng%{?compat_suffix}%{soversion} -p /sbin/ldconfig

%files -n libz-ng%{?compat_suffix}%{soversion}
%if %{with zlib_compat}
%config %{_sysconfdir}/ld.so.conf.d/zlib-ng-compat-%{_arch}.conf
%dir %{_libdir}/zlib-ng-compat/
%{_libdir}/zlib-ng-compat/libz.so.%{soversion}*
%else
%{_libdir}/libz-ng.so.%{soversion}*
%endif
%license LICENSE.md
%doc README.md

%files devel
%if %{with zlib_compat}
%{_includedir}/zconf.h
%{_includedir}/zlib.h
%{_includedir}/zlib_name_mangling.h
%{_libdir}/libz.so
%{_libdir}/pkgconfig/zlib.pc
%{_libdir}/cmake/ZLIB
%else
%{_includedir}/zconf-ng.h
%{_includedir}/zlib-ng.h
%{_includedir}/zlib_name_mangling-ng.h
%{_libdir}/libz-ng.so
%{_libdir}/pkgconfig/zlib-ng.pc
%{_libdir}/cmake/zlib-ng
%endif

%changelog
