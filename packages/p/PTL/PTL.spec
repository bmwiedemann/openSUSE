#
# spec file for package PTL
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


%define sover 2
%define libname libptl%{sover}
Name:           PTL
Version:        2.3.3
Release:        0
Summary:        C++11 mutilthreading tasking system
License:        MIT
URL:            https://github.com/jrmadsen/PTL
Source:         https://github.com/jrmadsen/PTL/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  tbb-devel

%description
Parallel Tasking Library (PTL) is a C++11 multithreading tasking
system on top of std::thread featuring thread pools, task groups,
and lock-free task queues.

%package -n %{libname}
Summary:        Parallel Tasking Library

%description -n %{libname}
Parallel Tasking Library (PTL) is a C++11 multithreading tasking
system on top of std::thread featuring thread pools, task groups,
and lock-free task queues.

This package provides the shared library for %{name}.

%package -n ptl-devel
Summary:        Headers for building with PTL
Requires:       %{libname} = %{version}
Requires:       tbb-devel

%description -n ptl-devel
Parallel Tasking Library (PTL) is a C++11 multithreading tasking
system on top of std::thread featuring thread pools, task groups,
and lock-free task queues.

This package provides the headers and sources for developing against %{name}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n ptl-devel
%license LICENSE
%doc README.md
%{_includedir}/PTL/
%{_libdir}/*.so
%{_libdir}/cmake/
%{_libdir}/pkgconfig/*.pc

%files -n %{libname}
%license LICENSE
%{_libdir}/*.so.*

%changelog
