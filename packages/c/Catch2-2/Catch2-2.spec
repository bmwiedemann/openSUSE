#
# spec file for package Catch2-2
#
# Copyright (c) 2023 SUSE LLC
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


%define srcname Catch2
Name:           Catch2-2
Version:        2.13.10
Release:        0
Summary:        A modern, C++-native, header-only, test framework for unit-tests, TDD and BDD
License:        BSL-1.0
URL:            https://github.com/catchorg/Catch2/
Source:         https://github.com/catchorg/%{srcname}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
#PATCH-FIX-OPENSUSE fix-pragmas-old-gcc.patch -- Fix usage of gcc pragmas for old gcc version on Leap gh#catchorg/Catch2#2416
Patch0:         fix-pragmas-old-gcc.patch
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++ >= 6
BuildRequires:  pkgconfig

%description
Catch2 stands for C++ Automated Test Cases in a Header and is a multi-paradigm
test framework for C++. which also supports Objective-C (and maybe C).
It is primarily distributed as a single header file, although certain
extensions may require additional headers.

This package provides version 2.x of Catch2.

%package devel
Summary:        A modern, C++-native, header-only, test framework for unit-tests, TDD and BDD
Conflicts:      Catch2-devel >= 3
Provides:       Catch2-devel = %{version}

%description devel
Catch2 stands for C++ Automated Test Cases in a Header and is a multi-paradigm
test framework for C++. which also supports Objective-C (and maybe C).
It is primarily distributed as a single header file, although certain
extensions may require additional headers.

This package provides version 2.x of Catch2.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%cmake \
       -DCMAKE_INSTALL_DOCDIR:PATH=%{_defaultdocdir}/%{name} \
       -DPKGCONFIG_INSTALL_DIR:PATH=%{_libdir}/pkgconfig \
       -DCATCH_BUILD_EXAMPLES:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE.txt
%doc README.md CODE_OF_CONDUCT.md
%doc %{_defaultdocdir}/%{name}
%{_datadir}/%{srcname}/
%{_includedir}/catch2/
%{_libdir}/cmake/%{srcname}/
%{_libdir}/pkgconfig/catch2.pc

%changelog
