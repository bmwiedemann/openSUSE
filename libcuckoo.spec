#
# spec file for package libcuckoo
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
Name:           libcuckoo
Version:        0.3.1
Release:        0
Summary:        A high-performance, concurrent hash table
License:        Apache-2.0
URL:            https://github.com/efficient/%{name}
Source:         https://github.com/efficient/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Libcuckoo is a high-performance, concurrent hash table.

%package devel
Summary:        Files for Developing with libcuckoo

%description devel
Libcuckoo is a high-performance, concurrent hash table.
This package contains the libcuckoo development files.

%prep
%autosetup -p1

%build
%cmake \
     -DBUILD_EXAMPLES=OFF \
     -DBUILD_TESTS=ON \
     -DBUILD_STRESS_TESTS=OFF \
     -DBUILD_UNIT_TESTS=ON \
     -DBUILD_UNIVERSAL_BENCHMARK=OFF
%make_build

%install
%cmake_install

%check
%ctest

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.hh
%dir %{_includedir}/%{name}-c
%{_includedir}/%{name}-c/cuckoo_table_template.cc
%{_includedir}/%{name}-c/cuckoo_table_template.h
%dir %{_datadir}/cmake/%{name}
%{_datadir}/cmake/%{name}/*.cmake

%changelog
