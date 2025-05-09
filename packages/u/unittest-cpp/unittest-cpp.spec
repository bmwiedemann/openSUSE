#
# spec file for package unittest-cpp
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


%define lname	libUnitTest++-2_0_0
Name:           unittest-cpp
Version:        2.0.0
Release:        0
Summary:        A unit testing framework for C++
License:        MIT
URL:            https://github.com/unittest-cpp
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM correct lib64 install pathes
Patch1:         fix-install.patch
Patch2:         shared.patch
# PATCH-FIX-UPSTREAM unittest-cpp-2.0.0-gcc12.patch -- Fix build with GCC 12 (https://github.com/unittest-cpp/unittest-cpp/pull/185)
Patch3:         unittest-cpp-2.0.0-gcc12.patch
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
UnitTest++ is a unit testing framework for C++. It was designed
to do test-driven development on a wide variety of platforms.
UnitTest++ is mostly standard C++ and makes minimal use of
advanced library and language features.

%package -n %{lname}
Summary:        A unit testing framework for C++

%description -n %{lname}
UnitTest++ is a unit testing framework for C++. It was designed
to do test-driven development on a wide variety of platforms.
UnitTest++ is mostly standard C++ and makes minimal use of
advanced library and language features.

%package devel
Summary:        Development files for unittest-cpp
Requires:       %{lname} = %{version}

%description devel
A lightweight unit testing framework for C++.

This package contains header files and libraries needed to develop
application that use %{name}.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5

%install
export LD_LIBRARY_PATH=. # tests want this
%cmake_install
# add missing devel symlink
ln -s libUnitTest++-%{version}.so "%{buildroot}/%{_libdir}/libUnitTest++.so"
# replace broken .pc file
perl -i -lpe 's{^Version:\s*$}{Version: %{version}}' "%{buildroot}/%{_libdir}/pkgconfig"/*.pc

%check
%ctest

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/libUnitTest++-2*.so

%files devel
%license LICENSE
%doc AUTHORS README.md
%{_includedir}/UnitTest++
%{_libdir}/pkgconfig/UnitTest++.pc
%{_libdir}/cmake/
%{_libdir}/libUnitTest++.so

%changelog
