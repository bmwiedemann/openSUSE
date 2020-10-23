#
# spec file for package librpma
#
# Copyright (c) 2020 SUSE LLC
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


Name:           rpma
%define lname   librpma0
Version:        0.9.0
Release:        0
Summary:        Remote Persistent Memory Access
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://pmem.io/pmdk/
Source:         https://github.com/pmem/rpma/archive/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkg-config
BuildRequires:  libibverbs-devel
BuildRequires:  pkgconfig(libpmem) >= 1.6
ExclusiveArch:  x86_64 ppc64le

%description
librpma is a C library for accessing persistent memory (PMem) devices on
remote hosts over Remote Direct Memory Access (RDMA).

%package -n %{lname}
Summary:        Remote Persistent Memory Access
Group:          System/Libraries

%description -n %{lname}
librpma is a C library for accessing persistent memory (PMem) devices on
remote hosts over Remote Direct Memory Access (RDMA).

The librpma library provides two possible schemes of operation:
Remote Memory Access and Messaging. Both of them are available over a connection
established between two peers. Both of these schemes can make use of PMem as
well as DRAM for the sake of building
Remote Persistent Memory Accessing (RPMA) applications.

%package devel
Summary:        Development files for librpma
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Development files for librpma

%prep
%autosetup -p1

%build
%cmake -DBUILD_TESTS=OFF
%cmake_build

%install
%cmake_install
# Fix install dir for cmake files
mkdir -p %{buildroot}/%{_libdir}/cmake/librpma
mv  %{buildroot}/%{_libdir}/librpma/cmake/*.cmake %{buildroot}/%{_libdir}/cmake/librpma

%post -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/librpma.so.*
%license LICENSE

%files devel
%doc CHANGELOG.md
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/cmake/librpma
%{_libdir}/pkgconfig/*.pc

%changelog
