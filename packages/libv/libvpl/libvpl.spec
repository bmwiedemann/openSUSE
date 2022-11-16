#
# spec file for package libvpl
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


%if 0%{?suse_version} < 1550
  %define _distconfdir %{_prefix}%{_sysconfdir}
%endif

%if 0%{?suse_version} >= 1550
# Legacy tools use x86 asm, https://github.com/oneapi-src/oneVPL/issues/69
%ifarch x86_64 %{ix86}
%bcond_without tools
%else
%bcond_with tools
%endif
%endif

%global sover 2
Name:           libvpl
%define lname   libvpl%{sover}
Version:        2023.0.0
Release:        0
Summary:        oneAPI Video Processing Library (oneVPL) dispatcher, tools, and examples
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://github.com/oneapi-src/oneVPL
Source0:        https://github.com/oneapi-src/oneVPL/archive/refs/tags/v%{version}.tar.gz#/oneVPL-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
# https://github.com/oneapi-src/oneVPL/pull/73
Patch0:         https://patch-diff.githubusercontent.com/raw/oneapi-src/oneVPL/pull/73.patch#/remove_x86_64_check.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wayland-client)
%if 0%{?suse_version} < 1550
ExclusiveArch:  x86_64
%endif

%description
The oneAPI Video Processing Library (oneVPL) provides a single video processing
API for encode, decode, and video processing that works across a wide range of
accelerators.

%package -n %lname
Summary:        oneAPI Video Processing Library (oneVPL) dispatcher
Group:          System/Libraries

%description -n %lname
The oneAPI Video Processing Library (oneVPL) provides a single video processing
API for encode, decode, and video processing that works across a wide range of
accelerators.

%package devel
Summary:        Development files for oneAPI Video Processing Library (oneVPL) dispatcher
Group:          Development/Languages/C and C++
Requires:       %lname = %version

%description devel
This package contains the development headers and pkgconfig files for
the oneAPI Video Processing Library (oneVPL) dispatcher

%package samples
Summary:        Examples for the oneAPI Video Processing Library (oneVPL) dispatcher
Group:          Development/Languages/C and C++

%description samples
This package contains example applications for the oneAPI Video Processing Library (oneVPL) dispatcher.

%prep
%autosetup -p1 -n oneVPL-%{version}

%build
%cmake \
  -DBUILD_TOOLS:BOOL=%{?with_tools:ON}%{!?with_tools:OFF} \
  %{nil}
%cmake_build

%install
%cmake_install

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files
%doc README.md third-party-programs.txt

%files -n %lname
%license LICENSE
%dir %{_distconfdir}
%dir %{_distconfdir}/modulefiles
%dir %{_distconfdir}/vpl
%{_distconfdir}/modulefiles/vpl
%{_distconfdir}/vpl/vars.sh
%{_libdir}/libvpl.so.%{sover}
%{_libdir}/libvpl.so.%{sover}.*

%if %{with tools}
%files samples
%{_bindir}/*
%endif

%files devel
%doc
%{_includedir}/vpl/
%{_libdir}/libvpl.so
%{_libdir}/pkgconfig/vpl.pc
%{_libdir}/cmake/vpl/
%{_datadir}/vpl/

%changelog
