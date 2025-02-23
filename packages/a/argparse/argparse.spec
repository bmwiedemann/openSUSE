#
# spec file for package argparse
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


%define __builder ninja
%if 0%{suse_version} < 1600
%define gcc_ver 9
%endif
Name:           argparse
Version:        3.2
Release:        0
Summary:        Argument Parser for Modern C++
License:        MIT
URL:            https://github.com/p-ranav/argparse
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc%{?gcc_ver}-c++
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig

%description
%{name} is a header-only command-line argument parser for modern C++.

%package devel
Summary:        Header file for argparse, an argument parser for C++

%description devel
%{name} is a header-only command-line argument parser for modern C++.

This package provides the header file for %{name}.

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_CXX_COMPILER=g++%{?gcc_ver:-%{gcc_ver}} \
  -DARGPARSE_BUILD_SAMPLES:BOOL=ON
%cmake_build

%install
%cmake_install

%check
pushd %{__builddir}
./test/tests
popd

%files devel
%license LICENSE
%doc README.md
%{_includedir}/argparse/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
