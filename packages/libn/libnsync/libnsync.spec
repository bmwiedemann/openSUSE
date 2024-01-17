#
# spec file for package libnsync
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


%define libmajor 1

Name:           libnsync
Version:        1.23.0
Release:        0
Summary:        Library that exports various synchronization primitives
License:        Apache-2.0
Group:          System/Libraries
URL:            https://github.com/google/nsync
Source:         nsync-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
C/C++ library that exports various synchronization primitives:
	locks
	condition variables
	run-once initialization
	waitable counter (useful for barriers)
	waitable bit (useful for cancellation, or other conditions)

%package -n libnsync%libmajor
Summary:        Library that exports various synchronization primitives
Group:          System/Libraries

%description -n libnsync%libmajor
Library for C that exports various synchronization primitives

%package -n libnsync_cpp%libmajor
Summary:        Library that exports various synchronization primitives
Group:          System/Libraries

%description -n libnsync_cpp%libmajor
Library for C++ that exports various synchronization primitives

%package devel
Summary:        Library that exports various synchronization primitives
Group:          Development/Libraries/C and C++
Requires:       libnsync%libmajor = %{version}
Requires:       libnsync_cpp%libmajor = %{version}

%description devel
C/C++ library that exports various synchronization primitives:
	locks
	condition variables
	run-once initialization
	waitable counter (useful for barriers)
	waitable bit (useful for cancellation, or other conditions)

%prep
%setup -q -n nsync-%{version}

%build
export CXXFLAGS="-pthread -std=c++11 -D_POSIX_C_SOURCE=200809L"
export CFLAGS="-pthread -std=c++11 -D_POSIX_C_SOURCE=200809L"
%cmake \
  -DBUILD_SHARED_LIBS=ON\
  -DNSYNC_ATOMIC_CPP11=ON\
  -DNSYNC_USE_CPP11_TIMEPOINT=ON\
  -DNSYNC_ENABLE_TESTS=0

%cmake_build

%install
%cmake_install

%check
%ctest

%post -n libnsync%{libmajor} -p /sbin/ldconfig
%postun -n libnsync%{libmajor} -p /sbin/ldconfig
%post -n libnsync_cpp%{libmajor} -p /sbin/ldconfig
%postun -n libnsync_cpp%{libmajor} -p /sbin/ldconfig

%files devel
%doc README 
%license LICENSE
%{_includedir}/nsync*.h
%{_libdir}/libnsync.so
%{_libdir}/libnsync_cpp.so

%files -n libnsync%{libmajor}
%{_libdir}/libnsync.so.*

%files -n libnsync_cpp%{libmajor}
%{_libdir}/libnsync_cpp.so.*

%changelog
