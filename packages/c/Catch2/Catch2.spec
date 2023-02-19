#
# spec file for package Catch2
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


Name:           Catch2
Version:        3.3.1
Release:        0
Summary:        A modern, C++-native, header-only, test framework for unit-tests, TDD and BDD
License:        BSL-1.0
URL:            https://github.com/catchorg/%{name}/
Source:         https://github.com/catchorg/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.10
BuildRequires:  gcc-c++ >= 6
BuildRequires:  pkgconfig

%description
Catch2 stands for C++ Automated Test Cases in a Header and is a multi-paradigm
test framework for modern C++14 and newer.
It also provides basic micro-benchmarking features, and simple BDD macros.

%package devel
Summary:        A modern, C++-native, header-only, test framework for unit-tests, TDD and BDD

%description devel
Catch2 stands for C++ Automated Test Cases in a Header and is a multi-paradigm
test framework for modern C++14 and newer.
It also provides basic micro-benchmarking features, and simple BDD macros.

%prep
%autosetup -p1

%build
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DBUILD_SHARED_LIBS=OFF \
       -DCMAKE_INSTALL_DOCDIR=%{_defaultdocdir}/%{name} \
       -DPKGCONFIG_INSTALL_DIR=%{_libdir}/pkgconfig
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE.txt
%doc README.md CODE_OF_CONDUCT.md
%doc %{_defaultdocdir}/%{name}
%{_datadir}/%{name}
%{_includedir}/catch2
%{_libdir}/lib%{name}*.a
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/catch2.pc
%{_libdir}/pkgconfig/catch2-with-main.pc

%changelog
